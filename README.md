# Online Course and Learning Platform Analysis

## Project overview
This project analyzes online course data to explore enrolment patterns, course ratings, course prices, categories, and completion rates.

## Dataset notice
`dataset/online_courses.csv` is a **synthetic, artificially generated sample dataset** created for demonstration and academic practice. It is not official data from Coursera, Udemy, edX, or any other platform. If your faculty requires a real dataset, replace it with a suitable public dataset and update the column names in the notebook/dashboard.

## Project structure
- `dataset/online_courses.csv` — sample dataset
- `notebook/Online_Course_Learning_Analysis.ipynb` — analysis notebook
- `dashboard/app.py` — Streamlit dashboard
- `visualizations/` — location for exported charts
- `report/Project_Report.md` — editable project report

## Tools
Python, Pandas, Matplotlib, Jupyter Notebook / Google Colab, Streamlit, GitHub.

## Run the notebook
1. Open Google Colab or Jupyter Notebook.
2. Upload the notebook and dataset.
3. In Colab, upload `online_courses.csv` and change the path to `/content/online_courses.csv`, or run the notebook in the extracted project folder so the relative path works.

## Run the dashboard locally
Install Python, then run:
```bash
pip install pandas matplotlib streamlit
streamlit run dashboard/app.py
```
Keep the project folder structure unchanged so the dashboard can find the dataset.

## Suggested analysis questions
1. Which courses have the highest enrolment?
2. Which categories have the highest average rating?
3. Does average completion rate vary by difficulty?
4. How do course prices and ratings vary?
5. Which platforms have the largest total enrolments in this sample?

## Important
Treat findings as results from the synthetic demonstration dataset only. Do not present them as actual market statistics.
