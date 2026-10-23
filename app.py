import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Online Learning Analysis", page_icon="📚", layout="wide")
st.title("📚 Online Course and Learning Platform Analysis")
st.caption("Explore course popularity, ratings, prices, and completion rates.")

DATA_PATH = Path(__file__).resolve().parents[1] / "dataset" / "online_courses.csv"
df = pd.read_csv(DATA_PATH)

with st.sidebar:
    st.header("Filters")
    platforms = st.multiselect("Platform", sorted(df["Platform"].unique()), default=sorted(df["Platform"].unique()))
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    difficulties = st.multiselect("Difficulty", sorted(df["Difficulty_Level"].unique()), default=sorted(df["Difficulty_Level"].unique()))

filtered = df[df["Platform"].isin(platforms) & df["Category"].isin(categories) & df["Difficulty_Level"].isin(difficulties)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Courses in view", f"{filtered['Course_ID'].nunique():,}")
c2.metric("Total enrolments", f"{filtered['Students_Enrolled'].sum():,}")
c3.metric("Average rating", f"{filtered['Course_Rating'].mean():.2f} / 5" if len(filtered) else "N/A")
c4.metric("Average completion", f"{filtered['Completion_Rate_Percent'].mean():.1f}%" if len(filtered) else "N/A")

if filtered.empty:
    st.warning("No rows match the selected filters. Please change the filters.")
else:
    left, right = st.columns(2)
    with left:
        st.subheader("Top courses by enrolment")
        top = filtered.groupby("Course_Name")["Students_Enrolled"].sum().nlargest(10).sort_values()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(top.index, top.values)
        ax.set_xlabel("Students enrolled")
        st.pyplot(fig)
    with right:
        st.subheader("Average rating by category")
        avg = filtered.groupby("Category")["Course_Rating"].mean().sort_values()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(avg.index, avg.values)
        ax.set_xlim(0, 5)
        ax.set_xlabel("Average rating / 5")
        st.pyplot(fig)

    left, right = st.columns(2)
    with left:
        st.subheader("Completion rate by difficulty")
        comp = filtered.groupby("Difficulty_Level")["Completion_Rate_Percent"].mean().reindex(["Beginner","Intermediate","Advanced"]).dropna()
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(comp.index, comp.values)
        ax.set_ylim(0, 100)
        ax.set_ylabel("Completion rate (%)")
        st.pyplot(fig)
    with right:
        st.subheader("Course price vs rating")
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(filtered["Course_Price_USD"], filtered["Course_Rating"], alpha=0.6)
        ax.set_xlabel("Price (USD)")
        ax.set_ylabel("Rating")
        st.pyplot(fig)

    st.subheader("Filtered course data")
    st.dataframe(filtered, use_container_width=True)
    st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_courses.csv", "text/csv")

st.info("Dataset note: This project uses an artificially generated sample dataset for demonstration, not real data from any platform.")
