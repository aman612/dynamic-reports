import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
date_range = pd.date_range(start='2024-01-01', end='2024-01-10')
print(f"date_range {date_range}")
df = pd.DataFrame({
    'Date': date_range,
    'Open': np.random.uniform(100, 200, len(date_range)),
    'High': np.random.uniform(200, 300, len(date_range)),
    'Low': np.random.uniform(50, 100, len(date_range)),
    'Close': np.random.uniform(150, 250, len(date_range))
})
print(f"df {df}")
# Save DataFrame to CSV
df.to_csv('candlestick_data.csv', index=False)
