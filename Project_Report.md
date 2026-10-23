# Online Course and Learning Platform Analysis

## 1. Abstract
This project demonstrates how data analysis can be used to study online courses by examining enrolment, ratings, pricing, course categories, difficulty levels, and completion rates. Python, Pandas, and Matplotlib are used for data preparation and visualization, with an optional Streamlit dashboard for interactive exploration.

## 2. Problem Statement
Online learning platforms offer courses across many subjects and difficulty levels. Learners and course providers may benefit from understanding which courses attract enrolments, how courses are rated, and whether completion patterns differ across course difficulty levels. This project provides a simple data-analysis workflow to explore these questions.

## 3. Objectives
- Explore course and platform information.
- Check and clean missing, duplicate, or invalid records.
- Compare enrolment across courses and platforms.
- Study ratings by course category.
- Compare completion rates by difficulty level.
- Visualize the findings and present them in a dashboard.

## 4. Dataset Description
The included dataset contains 300 illustrative course records with fields for course ID, course name, category, platform, difficulty level, duration, price, enrolments, rating, and completion rate. The dataset is synthetic and was generated for project practice; it is not real data from a commercial learning platform.

## 5. Tools and Technologies
- Python
- Pandas for data manipulation
- Matplotlib for charts
- Jupyter Notebook / Google Colab for analysis
- Streamlit for an optional interactive dashboard
- GitHub for version control and sharing

## 6. Methodology
1. Load the CSV dataset.
2. Inspect rows, columns, data types, and descriptive statistics.
3. Check missing values and duplicate rows.
4. Validate rating, completion, and enrolment ranges.
5. Aggregate and visualize course enrolments, category ratings, completion by difficulty, platform enrolments, and price versus rating.
6. Present results in a dashboard and summarize limitations.

## 7. Visualizations
- Top 10 courses by total enrolment
- Average course rating by category
- Average completion rate by difficulty level
- Total enrolments by platform
- Course price versus rating scatter plot

## 8. Findings
Run the notebook or dashboard to calculate the results from the included sample dataset. Findings must be described as observations from this synthetic sample only. Do not claim that they represent real-world platform performance.

## 9. Limitations
The sample dataset is artificially generated and cannot establish actual learner behavior or real platform rankings. Completion rate and enrolment values are illustrative. A real-world study should use a trustworthy public dataset, document its source, and consider the date range and sampling limitations.

## 10. Future Enhancements
- Replace the sample data with a verified public dataset.
- Add time-based analysis if dates are available.
- Add course recommendation features.
- Include filters and downloadable results in the dashboard.
- Compare results across a larger and more representative dataset.

## 11. Conclusion
This project demonstrates a basic end-to-end workflow for online course analysis, including dataset exploration, cleaning, visualization, and dashboard presentation. The workflow can be adapted to a real dataset for a stronger academic project.
