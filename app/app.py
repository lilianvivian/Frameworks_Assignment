import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import os

# Set Seaborn style
sns.set(style="whitegrid")

# -------------------------------
# Load cleaned dataset
# -------------------------------
cleaned_file = os.path.join("..", "outputs", "metadata_cleaned.csv")
df = pd.read_csv(cleaned_file)

# -------------------------------
# Streamlit App Title
# -------------------------------
st.title("CORD-19 Data Explorer")
st.write("""
Explore COVID-19 research papers from the CORD-19 dataset. 
Filter by year, view top journals, and see a word cloud of paper titles.
""")

# -------------------------------
# Sidebar filters
# -------------------------------
year_min = int(df['year'].min())
year_max = int(df['year'].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    year_min,
    year_max,
    (2020, 2021)
)

# Filter dataset by selected year range
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -------------------------------
# Show sample data
# -------------------------------
st.subheader("Sample Papers")
st.dataframe(df_filtered[['title', 'journal', 'year']].head(10))

# -------------------------------
# Publications by Year
# -------------------------------
st.subheader("Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# Top Journals
# -------------------------------
st.subheader("Top 10 Journals")
top_journals = df_filtered['journal'].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="magma", ax=ax2)
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# -------------------------------
# Word Cloud of Titles
# -------------------------------
st.subheader("Word Cloud of Paper Titles")
text = " ".join(title for title in df_filtered['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

fig3, ax3 = plt.subplots(figsize=(12,6))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# -------------------------------
# Paper Counts by Source
# -------------------------------
st.subheader("Top 10 Sources of Papers")
source_counts = df_filtered['source_x'].value_counts().head(10)

fig4, ax4 = plt.subplots(figsize=(8,4))
sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm", ax=ax4)
ax4.set_xlabel("Number of Papers")
ax4.set_ylabel("Source")
st.pyplot(fig4)
