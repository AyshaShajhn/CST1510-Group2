"""
RECORD CHECK  -  my version
===========================

Name  :  Aysha Shajahan
Lane  :  AI
Date  :  11/05/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
df = pd.DataFrame({
    "label": ["srv-01", "srv-02", "srv-03", "srv-04", "srv-05"],
    "value": [80, 95, 120, 70, 110],
    "limit": [100, 100, 100, 100, 100]  
})   

# ================================================================= PROCESS

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")


# ================================================================== OUTPUT
print(df)
print(df[df["status"] != "OK"])
grouped = df.groupby("status").size()
print(grouped)
df.to_csv("records_output.csv", index=False)

import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind='bar', title='Count per Status')
plt.savefig("status_counts.png")
plt.show()

