"""
RECORD CHECK  -  my version
===========================

Name  : Aysha Shajahan
Lane  :  AI      
Date  : 12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
    return {"hostname": hostname, "rating": fields["rating"], "age": fields["age"]}

def status_of(rating, age):
    """Return OVER LIMIT, WARNING or OK for an age,rating."""
    if age >= 21 or rating<3:
        return "FLAGGED"
    else:
        return "OK"

# ====================================================================== INPUT
with open("raw_records.txt","w") as f:
    f.write("  Survey-2026 , rating=4 , age=18  \n   SURVEY-2025 , rating=2 , age=45  \n        SuRveY-2023,rating=5,age=6       \n    SurveY-2027,rating=1,   age=78\n    survey-2021  ,rating=4.5, age=19  \n")

# =============================================================== PROCESS + OUTPUT
total = 0
flagged = 0
with open("raw_records.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)   
        status = status_of(record["rating"], record["age"])
        print(record, "Status:", status)
        total += 1

        if status == "FLAGGED":
            flagged += 1

print("Total No. Records:",total, "\nTotal Flagged Records:",flagged)

# ==========================================================================

