year=int(input("Enter year to be checked:"))
if(year%4==0and year%100!=0 or yeat%400==0):
  print ("the year is a leap year!")
else:
  print ("the year isn't a leap year!")