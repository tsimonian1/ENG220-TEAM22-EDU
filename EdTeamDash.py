import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Education Data Dashboard", layout="wide")

st.title("Education Data Dashboard")

st.subheader("This is an analysis of Cuba school data, this dashboard is hoping to highlight the strengths and areas "
        "for improvement of Cuba's school district by utilizing"
        "resources, accessibility, tutoring, funding, and more.")
st.space("large")

#ELA SCORES

DISTRICT_NAME = "Cuba Independent School District Score"

st.header("ELA Proficiency %(State vs. District)")
st.subheader("NM Standardized English Language Arts Test Scores ")

df1 = pd.DataFrame({ "year": [2010,2011,2012,2013,2014,2015,2016,2017,
                       2018, 2019, 2020, 2021, 2022,2023, 2024, 2025], 
        "district_score": [32.4,37.5,34.3,33.5,30.8,18.9,28.6,28,
                           16.83,19,19,19,8,11,15.82,18.04],
        "state_score": [57.4,49.8,50.8,50.6,49,33.3,37,37,
                        31.1,34,34,34,34,22,19.04,31.6]
        })

series = {      DISTRICT_NAME:
        ("district_score", "#1f77b4"),
        "New Mexico Average Score":("state_score", "#ff7f0e")}

fig1 = go.Figure()

#Shaded COVID section
fig1.add_vrect(
    x0=min([2020, 2021]) - 0.5,
    x1=max([2020, 2021]) + 0.5,
    fillcolor="gray",
    opacity=0.15,
    line_width=0,
    annotation_text="N/A",
    annotation_position="top left",
)

for name, (col, color) in series.items():
    #Add colored lines.
    fig1.add_trace(go.Scatter(
        x=df1["year"], y=df1[col],
        mode="lines+markers",
        name=name,
        line=dict(color=color),
    ))

fig1.update_layout(
    xaxis=dict(dtick=1, title="Year"),
    yaxis=dict(title="ELA Score")
)

st.plotly_chart(fig1, use_container_width=True)
st.caption(
    "Gray shaded years: standardized testing was not administered due to COVID-19. "
)

with st.expander("View data"):
    st.dataframe(df1)
st.text("The Engligh Language Art scores for Cuba have never reached the proficiency level " \
"as the state average. There are many complex reasons for why this could be the case.")
#MATH SCORES

st.header("MATH Proficiency %(State vs. District)")
st.subheader("NM Standardized Mathematics Test Scores")

df2 = pd.DataFrame({ "year": [2010,2011,2012,2013,2014,2015,2016,2017,
                              2018,2019,2020,2021,2022,2023, 2024, 2025], 
        "district_score": [43.2,31.1,30.6,25.1,25.4,5,9.3,7,
                           4,4,4,4,5,11,15.82,18.04],
        "state_score": [58.2,41.8,42.9,42,40.7,17.6,20.2,20,
                        21.6,20,20,20,25,22,19.04,31.6]
        })

fig2 = go.Figure()

fig2.add_vrect(
    x0=min([2020, 2021]) - 0.5,
    x1=max([2020, 2021]) + 0.5,
    fillcolor="gray",
    opacity=0.15,
    line_width=0,
    annotation_text="N/A",
    annotation_position="top left",
)

for name, (col, color) in series.items():
    fig2.add_trace(go.Scatter(
        x=df2["year"], y=df2[col],
        mode="lines+markers",
        name=name,
        line=dict(color=color),
    ))

fig2.update_layout(
    xaxis=dict(dtick=1, title="Year"),
    yaxis=dict(title="MATH Score")
)

st.plotly_chart(fig2, use_container_width=True)
st.caption(
    "Gray shaded years: standardized testing was not administered due to COVID-19. "
)

with st.expander("View data"):
    st.dataframe(df2)

st.text("The Mathematics Scores for the Cuba School District follow a similar pattern" \
" to the ELA score comparison. The level of proficiency dipped as low as 4%.")

#GRAD RATES
st.header("Graduation Rates (State Average vs. District)")

df3 = pd.DataFrame({ "year": [2018,2019,2020,2021,2022,2023,2024,2025], 
        "district_rate": [70.4,83.8,88.8,94,91,84.8,86.37,86],
        "state_rate": [73.9,75,76.9,76.8,76,76.7,78.2,80.6]
        })

long_df3 = df3.melt(id_vars="year",
        value_vars=["district_rate","state_rate"],
        var_name="Series",
        value_name="%"
        )

long_df3["Series"] = long_df3["Series"].map({
        "district_rate": "Sandoval County Graduation Rate",
        "state_rate": "NM Average Graduation Rate"
})

fig3 = px.line( long_df3, x="year",
              y="%", color= "Series",
              markers=True
              )

fig3.update_xaxes(dtick=1)
st.plotly_chart(fig3, use_container_width=True)

with st.expander("View data"):
    st.dataframe(df3)

st.text("Despite the below average scores, the graduation rate of Cuba, NM" \
" is higher than the state average. High graduation rates can be closely related" \
" to community factors and school enviornment.")
#ATTENDANCE

st.header("Chronic Absenteeism(State vs.District)(%)")

df4 = pd.DataFrame({ "year": [2018,2019,2020,2021,2022,
                              2023, 2024, 2025], 
        "district_per": [25.41,71.16,40.67,60.37,92.48,
                         60,68.61,54.29],
        "state_per": [16.4,17.87,16.03,29.76,40.73,
                        39.22,29.77,33.08]
        })

long_df4 = df4.melt(id_vars="year",
        value_vars=["district_per","state_per"],
        var_name="Series",
        value_name="%"
        )

long_df4["Series"] = long_df4["Series"].map({
        "district_per": "Cuba Independent School Dist Average",
        "state_per": "NM Average"
})

fig4 = px.line( long_df4, x="year",
              y="%", color= "Series",
              markers=True
              )

fig4.update_xaxes(dtick=1)
st.plotly_chart(fig4, use_container_width=True)

with st.expander("View data"):
    st.dataframe(df4)
st.text("This graph displays the number of students that are absent from school " \
"at an unacceptable rate.")
