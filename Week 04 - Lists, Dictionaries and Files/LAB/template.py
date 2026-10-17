"""
RECORD CHECK  -  my version
===========================

Name  : Aysha Shajahan
Lane  :  AI 
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check(value, limit):
    '''returns the difference and percent after calculation'''
    difference = value - limit
    percent = (value/limit)*100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    '''returns the whole report when called'''
    print()
    print("=" * 34) 
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Used       :  {value:>10.2f}")
    print(f"Total      :  {limit:>10.2f}")
    print(f"Free       :  {difference:>10.2f}")
    print(f"Percent    :  {percent:>10.2f} %")
    print(f"Status     :  {status:>10}")
    print("=" * 34)

with open("records.txt","w") as f:
    f.write('srv-01,87,100\n srv-02,120,100\n srv-03,67,100\n')
def load_records(path):
    """Read label,value,limit lines and return a list of dictionaries."""
    records = [] 
    with open(path) as f:
        for line in f:
            label,value,limit = line.strip().split(",")
            value = float(value)
            limit = float(limit)
            records.append({"label": label, "value": value, "limit": limit})
    return records

records = load_records("records.txt")
total = 0
with open("results.txt","w") as f:
    for record in records:
        value = record['value']
        limit = record['limit']
        difference,percent = check(value,limit)
        if percent >= 100:
            status = "OVER LIMIT"
            total += 1
        elif percent >= 90:
            status = "WARNING"
        else:
            status = "OK"

        print_report(record["label"], value, limit, difference, percent, status)
        f.write(f'{record["label"]},{status}\n')

print(f"Total OVER LIMIT records are: {total}")

with open("results.txt") as f:
    print(f.read())

  





