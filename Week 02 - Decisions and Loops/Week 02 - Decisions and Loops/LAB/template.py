"""
RECORD CHECK  -  my version
===========================

Name  : Aysha Shajahan
Lane  :  AI 
Date  : 02/10/2026

Run it:   python template.py
"""
total = 0
while True:
    # ==================================================================== INPUT
    label = input("Label: ")
    if label == "quit":
        break
    value = float(input("Value: "))
    limit = float(input("Limit: "))

    # ================================================================== PROCESS
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    if status == "OVER LIMIT":
        total += 1
    # ================================================================== OUTPUT
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"value        : {value:>10.2f}")
    print(f"limit        : {limit:>10.2f}")
    print(f"difference   : {difference:>+10.2f}")
    print(f"of limit     : {percent:>9.2f} %")
    print(f"status       : {status:>10}")
    print("=" * 34)
print(f"Total OVER LIMIT records: {total}")

