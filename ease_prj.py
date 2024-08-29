import pandas as pd
from datetime import time

# Load the Excel file
file_path = r'C:\Users\urite\OneDrive\Desktop\prj\Match Dump-DE Take home assignment.xlsx'
df_matches = pd.read_excel(file_path, sheet_name='Match Dump Sheet')

# Convert the 'Time (IST)' column to datetime.time format
df_matches['Time (IST)'] = pd.to_datetime(df_matches['Time (IST)'], format='%H:%M:%S', errors='coerce').dt.time

# Define the time range mappings based on priority
time_range_mappings = [
    ((time(17, 0), time(20, 30)), 1),
    ((time(12, 0), time(17, 0)), 2),
    ((time(20, 30), time(23, 0)), 3),
    ((time(9, 0), time(12, 0)), 4),
    ((time(23, 0), time(1, 0)), 5),
    ((time(1, 0), time(6, 0)), 6),
    ((time(6, 0), time(9, 0)), 7)
]

# Function to determine the time priority
def determine_time_priority(match_time):
    return next((priority for (start, end), priority in time_range_mappings if start <= match_time < end), 7)

# Priority mappings for all parameters
priority_mappings = {
    'Series Type': {'World Cup': 1, 'other': 2},
    'Rivalry': {'India vs Pakistan': 1, 'Ashes': 2, 'other': 3},
    'Teams': {'India': 1, 'England': 2, 'Australia': 3, 'South Africa': 4, 'Pakistan': 5, 'New Zealand': 6, 'Sri Lanka': 7, 'West Indies': 8, 'Afghanistan': 9},
    'Match Category': {'International': 1, 'Domestic': 2},
    'Format': {'T20I': 1, 'ODI': 2, 'Test': 3},
    'Is League': {'Yes': 1, 'No': 2},
    'Gender': {'Men': 1, 'Women': 2},
    'No. of Teams': {12: 1, 10: 2, 9: 3, 8: 4, 6: 5, 4: 6, 3: 7, 2: 8}
}

# Apply priority mappings
for column, mapping in priority_mappings.items():
    if column == 'Teams':
        df_matches['Teams Priority'] = df_matches.apply(lambda row: min(mapping.get(row['Team A'], 10), mapping.get(row['Team B'], 10)), axis=1)
    elif column == 'Is League':
        df_matches['Is League Priority'] = df_matches['League/Event'].map(lambda x: 1 if 'League' in str(x) else 2)
    elif column == 'Format':
        df_matches['Format Priority'] = df_matches['Match Type'].map(mapping).fillna(3)
    elif column in df_matches.columns:  # Check if the column exists in the DataFrame
        df_matches[f'{column} Priority'] = df_matches[column].map(mapping).fillna(max(mapping.values()))

# Apply time priority
df_matches['Time Priority'] = df_matches['Time (IST)'].apply(determine_time_priority)

# Calculate total priority
priority_columns = [col for col in df_matches.columns if col.endswith('Priority')]
df_matches['Total Priority'] = df_matches[priority_columns].sum(axis=1)

# Sort the matches based on the total priority
df_matches_sorted = df_matches.sort_values(by='Total Priority', ascending=True)

print(df_matches_sorted.head(10))