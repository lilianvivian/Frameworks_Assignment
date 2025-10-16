# CORD-19 Data Explorer

A professional-grade project exploring the CORD-19 dataset of COVID-19 research papers.  
This project demonstrates data cleaning, analysis, visualization, and an interactive Streamlit web application.

---

## **Project Overview**

- **Dataset:** `metadata.csv` from CORD-19 containing titles, abstracts, publication dates, journals, authors, and sources.  
- **Objectives:**  
  - Clean and prepare the data for analysis  
  - Generate visualizations to reveal trends in COVID-19 research  
  - Build an interactive Streamlit app to explore the dataset  

---

## **Folder Structure**
CORD19_Data_Explorer/
├── data/ # Raw dataset
├── notebooks/ # Analysis and cleaning notebooks
├── app/ # Streamlit app
├── outputs/ # Figures and cleaned data
├── requirements.txt # Python dependencies
└── README.md

To run the Streamlit app:
```
python -m streamlit run app/app.py
```

Visualizations

Publications by Year – Yearly publication trends

Top Journals – Top 10 journals publishing COVID-19 research

Word Cloud of Titles – Frequent words in paper titles

Paper Counts by Source – Distribution of papers by source

All figures are saved in outputs/figures/.


~~~

Author

Lily – Data Science & ML Engineer
