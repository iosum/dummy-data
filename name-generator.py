import names
import xlsxwriter
import random

outWorkbook = xlsxwriter.Workbook("data-set.xlsx")
outSheet = outWorkbook.add_worksheet()

for i in range(0,1000):
    DOB = (random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", 
    "10", "11", "12"]) + "-" + random.choice(["01", "02", "03", "04", "05", "06", 
    "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
    "20", "21", "22", "23", "24", "25", "26", "27", "28"]) + "-" + 
    random.choice(["1980", "1981", "1982", "1983", "1984", "1985", "1986", 
    "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1996", 
    "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"
  , "2008", "2009", "2010"]))
    isPoliceCheck = (random.choice(["True","False"]))
    isTraining = (random.choice(["True","False"]))
    outSheet.write(i+1, 0, names.get_first_name())
    outSheet.write(i+1, 1, names.get_last_name())
    outSheet.write(i+1, 2, DOB)
    outSheet.write(i+1, 3, isPoliceCheck)
    outSheet.write(i+1, 4, isTraining)

print('done')

outWorkbook.close()
