#one hot encoding(pokemon version)

import pandas as pd

data = {
    "Pokemon": ["Charizard", "Machamp", "Celebi", "Rayquaza", "Greninja"],
    "Color_of_pokemon": ["red", "blue", "green","green","blue"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)

unique_colors = df["Color_of_pokemon"].unique()

print("Unique categories:", unique_colors)

for category in unique_colors:

    col_name = "Color_of_pokemon_" + str(category)

    df[col_name] = (df["Color_of_pokemon"] == category).astype(int)

print("DataFrame after manual one-hot encoding:")

print(df)
