# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt","w") as f:
    f.write("srv-01,87,100\n")
    f.write("srv-02,120,100\n")
    f.write("srv-03,67,100\n")
with open("records.txt") as f:
    print(f.read())
