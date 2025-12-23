import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. SIMPLE DATA ENTRY
# Format: [Category, Task, Start Date (YYYY-MM-DD), End Date (YYYY-MM-DD)]
RAW_JOURNEY_DATA = [
    ["Foundations", "Systems Mastery (HCL/Intaglio)", "2013-06-01", "2020-01-01"],
    ["Foundations", "Infrastructure Stability", "2013-06-01", "2020-01-01"],
    ["Rigor", "MS Business Analytics (Marist)", "2020-01-01", "2022-05-01"],
    ["Rigor", "Research Modeling / NLP", "2020-06-01", "2022-05-01"],
    ["Strategy", "Sr. Data Analyst (Bayer)", "2022-05-01", "2025-12-01"],
    ["Strategy", "BI Strategy Lead (Function)", "2022-10-01", "2025-12-01"],
    ["Strategy", "Statistical Integrity (LMM)", "2023-01-01", "2025-12-01"],
]

# 2. AUTOMATIC COLOR MAPPING
# Define your colors by category once here
CATEGORY_COLORS = {
    "Foundations": "#94a3b8", # Slate 400
    "Rigor": "#64748b",       # Slate 500
    "Strategy": "#2563eb"     # Blue 600
}

# 3. DATA PROCESSING
df = pd.DataFrame(RAW_JOURNEY_DATA, columns=["Category", "Task", "Start", "End"])
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Color'] = df['Category'].map(CATEGORY_COLORS)

# 4. PLOTTING
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f8fafc')
ax.set_facecolor('#f8fafc')

# Draw bars
for i, row in df.iterrows():
    duration = (row['End'] - row['Start']).days
    ax.barh(row['Task'], duration, left=row['Start'], color=row['Color'], height=0.6, alpha=0.9)
    
    # Add labels inside or next to the bars
    label_x_pos = row['Start'] + pd.Timedelta(days=100)
    ax.text(label_x_pos, i, row['Task'], va='center', color='white', fontweight='bold', fontsize=10)

# 5. STYLING & FORMATTING
plt.title('The 12-Year Evolution: Systems Stability to Strategic Impact', 
          fontsize=18, fontweight='bold', pad=30, color='#1e293b')

# Clean up the chart area
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#cbd5e1')

# X-Axis Grid and Labels
ax.grid(axis='x', linestyle='--', alpha=0.4, color='#cbd5e1')
ax.tick_params(axis='x', colors='#64748b', labelsize=10)
ax.tick_params(axis='y', left=False) # Hide y-axis ticks since labels are on bars

plt.tight_layout()

# 6. SAVE
output_path = 'assets/images/journey.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Visual Story successfully generated at: {output_path}")