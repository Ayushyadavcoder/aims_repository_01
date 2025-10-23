#Imputation(Pokemon Version)

import pandas as pd
import numpy as np
from collections import Counter

data = {
    "Pokwmon_ID": [1, 2, 3, 4, 5, 6],
    #age
    "Level": [29, np.nan, 52, 40, np.nan, 36], 
    #Salary       
    "CP": [50000, 60000, np.nan, 80000, 75000, np.nan],
    #department
    "Pokemon_types": ["Fire", "Water", "Gound", np.nan, "Flying", "Dragon"]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values:")
print(df)

# Mean imputation for 'Level'
Level_mean = df["Level"].mean(skipna=True)
print("Mean of Level (ignoring NaNs):", Level_mean)
df["Level_mean_imputed"] = df["Level"].fillna(Level_mean)
print("Level after mean imputation:")
print(df[["Level", "Level_mean_imputed"]])

# Median imputation for 'CP'
CP_median = df["CP"].median(skipna=True)
print("Median of CP:", CP_median)
df["CP_median_imputed"] = df["CP"].fillna(CP_median) 
print("CP after median imputation:")
print(df[["CP", "CP_median_imputed"]])

# Mode
Pokemon_types_values = df["Pokemon_types"].dropna().tolist()  
counter = Counter(Pokemon_types_values)
mode_Pokemon_types, count = counter.most_common(1)[0]
print("Mode of Pokemon_types:", mode_Pokemon_types, "count:", count)
df["Pokemon_types_mode_imputed"] = df["Pokemon_types"].fillna(mode_Pokemon_types)
print("Pokemon_types after mode imputation:")
print(df[["Pokemon_types", "Pokemon_types_mode_imputed"]])

# Forward fill 
df_ffill = df.copy()
df_ffill["Pokemon_types_ffill"] = df_ffill["Pokemon_types"].ffill()
print("Pokemon_types after forward fill:")
print(df_ffill[["Pokemon_types", "Pokemon_types"]])

# Backward fill
df_bfill = df.copy()
df_bfill["Pokemon_types_bfill"] = df_bfill["Pokemon_types"].bfill()
print("Pokemon_types after backward fill:")
print(df_bfill[["Pokemon_types", "Pokemon_types_bfill"]])