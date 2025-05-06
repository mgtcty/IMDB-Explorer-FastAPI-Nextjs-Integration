import pandas as pd

# Load the TSV file
df = pd.read_csv('tsv/title.basics.tsv', sep='\t', encoding='utf-8')

# Save to CSV
df.drop('endYear', axis=1, inplace=True)
df.to_csv('csv/title.basics.normalized.csv', index=False, encoding='utf-8')

print("Successfully normalized title.basics.tsv: one genre per row.")

print(df.head())