import pandas as pd
import os

# --- Define file paths ---
original_path = "data/metadata.csv"              # Big file (local only)
output_path = "outputs/sample_metadata_cleaned.csv"  # Small version for GitHub/demo

# --- Ensure output folder exists ---
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("📥 Loading data (this may take a few seconds)...")
df = pd.read_csv(original_path, low_memory=False)

# --- Select relevant columns ---
columns_needed = ['cord_uid', 'title', 'abstract', 'publish_time', 'journal', 'authors', 'source_x']
df = df[columns_needed]

# --- Clean data ---
df = df.dropna(subset=['title', 'abstract', 'publish_time'])
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['publish_time'])
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))

# --- Create sample subset (first 500 rows) ---
df_sample = df.head(500)

# --- Save sample dataset ---
df_sample.to_csv(output_path, index=False)

print(f"✅ Sample data created successfully at: {output_path}")
print(f"Sample shape: {df_sample.shape}")
