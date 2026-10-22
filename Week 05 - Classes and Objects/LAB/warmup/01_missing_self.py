# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent):    # this parameter should be self
        self.percent = percent
        return percent

r = Record()
print(r.status(95))
