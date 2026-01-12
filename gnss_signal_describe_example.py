"""
File: gnss_signal_describe_example.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates the use of Pandas describe() function
on sample GNSS signal-related data for exploratory data analysis (EDA).
"""

import pandas as pd

# --------------------------------------------------
# 1. Create Sample GNSS / Signal Dataset
# --------------------------------------------------
data = {
    "Satellite_ID": ["G01", "G02", "G03", "G04", "G05"],
    "SNR_dB": [45.2, 38.5, 42.0, 30.8, 47.1],
    "Pseudorange_m": [20200000, 20185000, 20215000, 20150000, 20230000],
    "Doppler_Hz": [-1200.5, -1150.3, -1180.0, -1305.7, -1100.2],
    "Elevation_deg": [60, 45, 55, 30, 70]
}

df = pd.DataFrame(data)

print("GNSS Signal Dataset:")
print(df)

print("-" * 70)

# --------------------------------------------------
# 2. describe() on Numerical GNSS Parameters
# --------------------------------------------------
print("Statistical Summary of GNSS Signal Parameters:")
print(df.describe())

print("-" * 70)

# --------------------------------------------------
# 3. describe() on Categorical Data (Satellite ID)
# --------------------------------------------------
print("Summary of Satellite IDs:")
print(df.describe(include="object"))

print("-" * 70)

# --------------------------------------------------
# 4. Parameter-wise describe()
# --------------------------------------------------
print("SNR Statistics:")
print(df["SNR_dB"].describe())

print("-" * 70)

print("Pseudorange Statistics:")
print(df["Pseudorange_m"].describe())

print("-" * 70)

# --------------------------------------------------
# 5. Practical GNSS Insights from describe()
# --------------------------------------------------
print("GNSS Insights:")
print("• Average SNR (dB):", df["SNR_dB"].mean())
print("• Minimum Elevation (deg):", df["Elevation_deg"].min())
print("• Maximum Elevation (deg):", df["Elevation_deg"].max())
print("• Doppler Range (Hz):",
      df["Doppler_Hz"].min(), "to", df["Doppler_Hz"].max())
