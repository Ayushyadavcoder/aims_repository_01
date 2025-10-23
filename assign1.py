#Ordinal Encoding (Pokemon version) 
import pandas as pd

data = {
    "Pokemon": ["Pikachu", "Greninja","magikarp","Gliscor","Charizard", "Diglett", "jinx","Rotom","Bidoof"],
    "Category":  ["Beast", "Beast", "God", "Good", "Beast", "Noob", "Gay", "Good","God"]
}
df = pd.DataFrame(data)
print("Og DataFrame:")
print(df)

ordered_categories = ["Gay","Noob","Good","Beast","God"]

mapping = {category: index for index, category in enumerate(ordered_categories)}
print("Mapping dictionary:", mapping)
print()

df["Category_order"] = df["Category"].map(mapping)

unmapped = df[df["Category_order"].isna()]["Category"].unique()
if len(unmapped) > 0:
    print("These categories were not available and are now NaN:", unmapped)
print("DataFrame after ordinal encoding:")
print(df)

