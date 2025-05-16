import pandas as pd
import matplotlib.pyplot as plt

# 1. 构造数据：用字典或直接读入你的 10 篇论文的年份和类别
data = {
    "year": [2019, 2020, 2022, 2022, 2022, 2022, 2023, 2023, 2024, 2024],  # 示例年份
    "method": [
        "Theory & survey", "Modeling", "Evaluation", "Theory & survey", "Modeling",
        "Evaluation", "Theory & survey", "Theory & survey", "Modeling", "Theory & survey"
    ]
}
df = pd.DataFrame(data)

# 2. 统计每个年份、每种评估方法的论文数
count_table = df.pivot_table(index="year", columns="method", aggfunc="size", fill_value=0)

# 3. 绘制堆叠柱状图
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
