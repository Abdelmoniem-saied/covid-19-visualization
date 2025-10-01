from numpy.random import randn 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd


df=pd.read_csv("d:\data science\worldometer_coronavirus_summary_data.csv")


# 1 line plot

plt.figure(figsize=(10,6))

plt.plot(df.groupby("continent")["total_confirmed"].sum(), label="Confirmed", marker="o")
plt.plot(df.groupby("continent")["total_deaths"].sum(), label="Deaths", marker="o")
plt.plot(df.groupby("continent")["total_recovered"].sum(), label="Recovered", marker="o")

plt.title("COVID-19 Global Cases by Continent")
plt.ylabel("Cases")
plt.legend()
plt.show()



#2  Figures & Subplots




df_grouped = df.groupby("continent").sum(numeric_only=True)

#figure مع 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(15,5))

# Subplot 1
axes[0].plot(df_grouped.index, df_grouped["total_confirmed"], 'b-o')
axes[0].set_title("Confirmed Cases")

# Subplot 2
axes[1].plot(df_grouped.index, df_grouped["total_deaths"], 'r-o')
axes[1].set_title("Deaths")

# Subplot 3
axes[2].plot(df_grouped.index, df_grouped["total_recovered"], 'g-o')
axes[2].set_title("Recovered")

plt.suptitle("COVID-19 by Continent")
plt.show()




# 3️⃣ Histogram

plt.figure(figsize=(8,5))
plt.hist(df["total_cases_per_1m_population"].dropna(), bins=50, color='skyblue', edgecolor='black')
plt.title("Distribution of COVID-19 cases per 1M population")
plt.xlabel("Cases per 1M population")
plt.ylabel("Number of countries")
plt.show()



#4️⃣ Scatter Plot


plt.figure(figsize=(8,5))
plt.scatter(df["total_tests"], df["total_confirmed"], alpha=0.5, c="purple")
plt.title("Tests vs Confirmed Cases")
plt.xlabel("Total Tests")
plt.ylabel("Total Confirmed Cases")
plt.xscale("log")   # علشان الأرقام كبيرة جدًا
plt.yscale("log")
plt.show()



# 5️⃣ Adjusting subplot spacing

fig, axes = plt.subplots(2, 2, figsize=(12,8))

axes[0,0].bar(df_grouped.index, df_grouped["total_confirmed"], color="blue")
axes[0,0].set_title("Confirmed Cases")

axes[0,1].bar(df_grouped.index, df_grouped["total_deaths"], color="red")
axes[0,1].set_title("Deaths")

axes[1,0].bar(df_grouped.index, df_grouped["total_recovered"], color="green")
axes[1,0].set_title("Recovered")

axes[1,1].bar(df_grouped.index, df_grouped["active_cases"], color="orange")
axes[1,1].set_title("Active Cases")

plt.suptitle("COVID-19 by Continent (Grouped Bar Charts)", fontsize=14)
plt.subplots_adjust(wspace=0.3, hspace=0.4)  # مسافات بين الرسومات
plt.show()



# Ticks & Labels


fig, ax = plt.subplots(figsize=(10,6))

top10 = df.sort_values("total_confirmed", ascending=False).head(10)
ax.bar(top10["country"], top10["total_confirmed"], color="purple")

ax.set_title("Top 10 Countries by Confirmed Cases")
ax.set_xlabel("Country")
ax.set_ylabel("Confirmed Cases")

# تعديل الـ ticks
ax.set_xticklabels(top10["country"], rotation=45, fontsize="small")
plt.show()


# 7️⃣ Legends

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(df_grouped.index, df_grouped["total_confirmed"], 'b-o', label="Confirmed")
ax.plot(df_grouped.index, df_grouped["total_deaths"], 'r--', label="Deaths")
ax.plot(df_grouped.index, df_grouped["total_recovered"], 'g-.', label="Recovered")

ax.set_title("COVID-19 Cases by Continent")
ax.legend(loc="best")
plt.show()


