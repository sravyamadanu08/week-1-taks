#2.4 Company Holidays Using Tuples

company_holidays = ("2026-01-26", "2026-03-08", "2026-08-15", "2026-10-02", "2026-12-25")#Create a tuple of company holiday dates.
print(company_holidays)

company_holidays[1] = "2026-04-01" #tuples are immutable,Once a tuple is created, you cannot modify its elements,will cause a TypeError: 'tuple' object does not support item assignment
print(company_holidays)
