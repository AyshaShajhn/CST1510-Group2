"""
RECORD CHECK  -  my version
===========================

Name  : Aysha Shajahan
Lane  :  AI    
Date  : 10/08/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
def check(value, limit):
    '''returns the difference and percent after calculation'''
    difference = value - limit
    percent = (value/limit)*100
    return difference, percent

def status_of(percent):
    '''returns the status according to the percent calculated'''
    percent = check(value,limit)
    for number in percent:
        if number >= 100:
             status = "OVER LIMIT" 
        elif number >= 90:
            status = "WARNING"
        else:
            status = "OK"
    return status 
     

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
# ==================================================================== INPUT
total = 0
while True:
    label = input("Label:")
    if label == "quit":
            break
    value = float(input("Value:"))
    limit = float(input("Limit:"))

#================================================================== PROCESS
    difference,percent = check(value, limit)        
    status = status_of(percent)  
    if status == "OVER LIMIT":
            total += 1      
# =================================================================== OUTPUT
    print_report(label, value, limit, difference, percent, status)
if label == "quit":
        print("Total OVERLIMIT records:", total)
    
    