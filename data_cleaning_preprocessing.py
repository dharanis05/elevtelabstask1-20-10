import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("marketing_campaign_dirty.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# Replace '######' with NaN for easier handling
df = df.replace("######", np.nan)

# Detect and convert date columns
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            if df[col].notna().sum() > 0:
                df[col] = df[col].dt.strftime('%d-%m-%Y')
        except:
            pass

# Capitalize names (for columns likely containing names)
for col in df.columns:
    if "name" in col.lower():
        df[col] = df[col].astype(str).apply(lambda x: x.strip().title() if isinstance(x, str) else x)

# Fill NaN (numeric) with column mean
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill NaN (non-numeric) with mode or 'Unknown'
for col in df.select_dtypes(exclude=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')

# Save the cleaned file
df.to_csv("marketing_campaign_cleaned.csv", index=False)

print("✅ Cleaning complete! File saved as 'marketing_campaign_cleaned.csv'")
