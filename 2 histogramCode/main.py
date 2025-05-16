import pandas as pd
import matplotlib.pyplot as plt

data = {
    "year": [2019, 2020, 2022, 2022, 2022, 2022, 2023, 2023, 2024, 2024],  # 示例年份
    "method": [
        "Theory & survey", "Modeling", "Evaluation", "Theory & survey", "Modeling",
        "Evaluation", "Theory & survey", "Theory & survey", "Modeling", "Theory & survey"
    ]
}
df = pd.DataFrame(data)

count_table = df.pivot_table(index="year", columns="method", aggfunc="size", fill_value=0)

ax = count_table.plot.bar(
    stacked=True,
    figsize=(8, 4)
)
ax.set_xlabel("Publication Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Papers by Year and Evaluation Method")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
