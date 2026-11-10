# Census Reporter: Cuba, NM https://censusreporter.org/profiles/16000US3519150-cuba-nm/
# NM-PED Tribal Education Status Report https://web.ped.nm.gov/wp-content/uploads/2025/11/FINAL_v2_2024.25_Statewide_TESR_PED_Released11.15.2025.pdf

import tkinter # GUI toolkit
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def submit_post(): # defines the logic for posting a submission to the forum
	submission = text_box.get("1.0", tkinter.END).strip() # capture entry into textbox
	if not submission:
		return

	text_box.delete("1.0", tkinter.END) # clear textbox after post for new entries
	
	global first_post # If this is the first post, hide the "no one has posted" message
	if first_post:
		empty_label.pack_forget()
		first_post = False
	
	post_frame = tkinter.Frame( # entry box to type in
			scrollable_frame, bg="white", bd=1, relief=tkinter.SOLID, padx=12, pady=12
	)
	post_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X, pady=6)

	# Add the text inside the box
	post_label = tkinter.Label(
			post_frame,
			text=submission,
			bg="white",
			anchor="w",
			justify=tkinter.LEFT,
			wraplength=500,
			font=("Tahoma", 11),
	)
	post_label.pack(fill=tkinter.X)

	
# SURVEY QUESTIONS
questions = [
    "Do you think students have access to enough educational resources?",
    "Would additional tutoring programs benefit students?",
    "Do you think more community programs would help students succeed?"
]

# Store the number of Yes and No responses
responses = {
    question: {"Yes": 0, "No": 0}
    for question in questions
}

current_question = 0


# RECORD AN ANSWER
def answer_question(answer):
    global current_question

    question = questions[current_question]

    # Record the response
    responses[question][answer] += 1

    # Move to the next question
    current_question += 1

    # Update question display
    if current_question < len(questions):
        question_label.config(
            text=questions[current_question]
        )
    else:
        question_label.config(
            text="Thank you for completing the survey!"
        )

        yes_button.config(state=tkinter.DISABLED)
        no_button.config(state=tkinter.DISABLED)

    update_graph()


# UPDATE THE GRAPH
def update_graph():
    ax.clear()

    question_names = [
        f"Q{i+1}" for i in range(len(questions))
    ]

    yes_values = [
        responses[q]["Yes"] for q in questions
    ]

    no_values = [
        responses[q]["No"] for q in questions
    ]

    x = range(len(questions))
    width = 0.35

    ax.bar(
        [i - width/2 for i in x],
        yes_values,
        width,
        label="Yes"
    )

    ax.bar(
        [i + width/2 for i in x],
        no_values,
        width,
        label="No"
    )

    ax.set_title("Survey Results")
    ax.set_ylabel("Number of Responses")
    ax.set_xlabel("Questions")
    ax.set_xticks(list(x))
    ax.set_xticklabels(question_names)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    graph_canvas.draw()

root = tkinter.Tk() # desktop window
root.title("Application with Forum")
root.geometry("640x800")
root.config(bg="#ADD8E6")


# SCROLLING LOGIC
container = tkinter.Frame(root, bg="#ADD8E6")
container.pack(fill=tkinter.BOTH, expand=True, padx=0, pady=0)

canvas = tkinter.Canvas(container, bg="#ADD8E6", highlightthickness=0)
scrollbar = tkinter.Scrollbar(container, orient="vertical", command=canvas.yview)

scrollable_frame = tkinter.Frame(canvas, bg="#ADD8E6")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.bind( # make inner frame resize with the canvas width so text wrapping works
    "<Configure>",
    lambda e: canvas.itemconfig(canvas_window, width=e.width)
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
scrollbar.pack(side="right", fill=tkinter.Y)

canvas.bind_all(
    "<MouseWheel>",
    lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
)


# intro with blurb about why we are doing this project
header = tkinter.Label(
		scrollable_frame,
		text="MOTIVATION",
		font=("Tahoma", 16, "bold"),
        bg="#ADD8E6",
)
header.pack(pady=15)

subheader = tkinter.Label(
    scrollable_frame,
    text=(
        "Census data for 2024-2025 showed that 34% of children under 18 in Cuba, New Mexico are living below the poverty line. According to the Tribal Education Status Report by NM-PED, economically disadvantaged students performed 6 to 10% below district averages. This project visualizes and analyzes student data to identify real-world solutions that can empower young people and improve their access to opportunities and success."
    ),
    font=("Tahoma", 11),
    bg="#ADD8E6",
    fg="#555555",
    wraplength=550,
    justify=tkinter.LEFT,
)
subheader.pack(anchor="w", padx=20, pady=(10, 5))



# dummy section 2
header = tkinter.Label(
		scrollable_frame,
		text="SECTION 2",
		font=("Tahoma", 16, "bold"),
        bg="#ADD8E6",
)
header.pack(pady=15)

subheader = tkinter.Label(
    scrollable_frame,
    text=(
        "   A blurb about section 2."
    ),
    font=("Tahoma", 11),
    bg="#ADD8E6",
    fg="#555555",
    wraplength=550,
    justify=tkinter.LEFT,
)
subheader.pack(anchor="w", padx=20, pady=(10, 5))

# START OF SURVEY SECTION

header = tkinter.Label(
    scrollable_frame,
    text="Student Survey",
    font=("Tahoma", 16, "bold"),
    bg="#ADD8E6",
)
header.pack(pady=15)

subheader = tkinter.Label(
    scrollable_frame,
    text="Answer the following questions to help us understand "
         "the needs of students and families in our community.",
    font=("Tahoma", 11),
    bg="#ADD8E6",
    fg="#555555",
    wraplength=550,
    justify=tkinter.LEFT,
)
subheader.pack(anchor="w", padx=20, pady=(10, 5))


# Question display
survey_frame = tkinter.Frame(
    scrollable_frame,
    bg="white",
    padx=15,
    pady=15
)
survey_frame.pack(fill=tkinter.X, padx=20, pady=10)

question_label = tkinter.Label(
    survey_frame,
    text=questions[0],
    font=("Tahoma", 12, "bold"),
    bg="white",
    fg="#333333",
    wraplength=500,
    justify=tkinter.CENTER,
)
question_label.pack(pady=15)


# Yes and No buttons
button_frame = tkinter.Frame(
    survey_frame,
    bg="white"
)
button_frame.pack(pady=10)

yes_button = tkinter.Button(
    button_frame,
    text="YES",
    bg="#6495ED",
    fg="white",
    font=("Tahoma", 11, "bold"),
    width=12,
    command=lambda: answer_question("Yes")
)
yes_button.pack(side=tkinter.LEFT, padx=10)

no_button = tkinter.Button(
    button_frame,
    text="NO",
    bg="#CD5C5C",
    fg="white",
    font=("Tahoma", 11, "bold"),
    width=12,
    command=lambda: answer_question("No")
)
no_button.pack(side=tkinter.LEFT, padx=10)


# GRAPH SECTION
graph_frame = tkinter.Frame(
    scrollable_frame,
    bg="white",
    padx=10,
    pady=10
)
graph_frame.pack(fill=tkinter.X, padx=20, pady=10)

# Create Matplotlib graph
fig, ax = plt.subplots(figsize=(6, 4))

graph_canvas = FigureCanvasTkAgg(
    fig,
    master=graph_frame
)

graph_canvas.draw()

graph_canvas.get_tk_widget().pack(
    fill=tkinter.BOTH,
    expand=True
)

# Display initial graph
update_graph()

# END OF SURVEY SECTION


# START OF FORUM GUI
header = tkinter.Label(
		scrollable_frame,
		text="Share your submissions!",
		font=("Tahoma", 16, "bold"),
		bg="#ADD8E6",
		fg="#333333",
)
header.pack(pady=15)

subheader = tkinter.Label(
    scrollable_frame,
    text=(
        "How can we can empower students and their families in Cuba?"
    ),
    font=("Tahoma", 11),
    bg="#ADD8E6",
    fg="#555555",
    wraplength=550,
    justify=tkinter.LEFT,
)
subheader.pack(anchor="w", padx=20, pady=(10, 5))

# text input box
form_frame = tkinter.Frame(scrollable_frame, bg="white", padx=15, pady=15)
form_frame.pack(fill=tkinter.X, padx=20, pady=10)

text_box = tkinter.Text(form_frame, height=5, font=("Tahoma", 11))
text_box.pack(fill=tkinter.X, pady=(5, 10))

submit_btn = tkinter.Button(
		form_frame,
		text="PUBLISH",
		bg="#6495ED",
		fg="white",
		font=("Tahoma", 11, "bold"),
		command=submit_post,
)
submit_btn.pack(anchor="w")

# Posts will be listed here
subheader = tkinter.Label(
		scrollable_frame,
		text="Recent Posts",
		font=("Tahoma", 13, "bold"),
		bg="#ADD8E6",
		fg="#555555",
)
subheader.pack(anchor="w", padx=20, pady=(20, 5))



first_post = True
empty_label = tkinter.Label(
		scrollable_frame,
		text="No one has posted here yet!",
		font=("Tahoma", 11, "italic"),		
        bg="#ffffff",
)
empty_label.pack(side=tkinter.BOTTOM, anchor="w", pady=5)

# Start the application loop
root.mainloop()