# generate_data.py

import pandas as pd
import numpy as np

# Simulate school connectivity data
np.random.seed(42)
data = pd.DataFrame({
    "latitude": np.random.uniform(0, 90, 500),
    "longitude": np.random.uniform(0, 180, 500),
    "bandwidth_mbps": np.random.uniform(0.1, 10, 500),
    "is_urban": np.random.choice([0, 1], size=500),
    "connectivity_label": np.random.choice(["Low", "Medium", "High"], size=500, p=[0.4, 0.4, 0.2])
})

data.to_csv("school_data.csv", index=False)
print("✅ Data generated and saved to school_data.csv")
