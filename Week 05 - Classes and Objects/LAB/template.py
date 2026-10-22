"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
            """stores the label,value,limit using self"""
            self.label = label
            self.value = value
            self.limit = limit
    
    def status(self):
        """Return OVER LIMIT, WARNING or OK based on percent()."""
        p = (self.value/self.limit)*100
        if p >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"
# ==================================================================== RECORDS
with open("record.txt","w") as f:
    f.write(f"R-001, 87.0, 100.0\nR-002, 120.0, 100.0\n")
def load_records(path):
        """Read label,value,limit lines and return a list of dictionaries."""
        records = []
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append(Record(label, float(value), float(limit)))
        return records

records = load_records("record.txt")
# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"value        : {record.value:>10.2f}")
    print(f"limit        : {record.limit:>10.2f}")
    print(f"Status       : {record.status():>10}")
    print("=" * 34)

print(f"Total OVER LIMIT records are: {Record.over_limit_count}")
# ==========================================================================

