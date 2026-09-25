"""
RECORD CHECK  -  my version
===========================

Name  : Aysha Shajahan
Lane  :  AI       (delete two)
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
Label = input("Enter Label: ")
Used = float(input("Enter Used: "))
Total = float(input("Enter Total: "))
Free = Total - Used
percent = (Used / Total) * 100


print("=" * 34)
print(" "*3, f" RECORD CHECK  -  {Label}")
print("=" * 34)    
print("Used:"," "*15, Used, "GB")   
print("Total:"," "*13, Total, "GB")
print(f"Free: {Free:>+20.2f} GB")
print(f"percent: {percent:>17.2f} %")
print("=" * 34)
print(f"This month, you used {Used:.2f} GB of your {Total:.2f} GB limit, leaving {Free:.2f} GB free.") # : the final concluding statement
print("=" * 34)


# ==================================================================== OUTPUT

 
