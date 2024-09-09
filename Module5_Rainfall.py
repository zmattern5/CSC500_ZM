import calendar

from numpy.ma.core import append
from numpy.ma.extras import average

number_of_years = int(input('Enter the Number of Years:\n',))
total_rainfall = 0
total_months = 0
lst_total_rainfall = []
for year in range(number_of_years):
    for month in range(12):
        input_prompt = 'Enter the inches of rainfall for ' + calendar.month_name[month+1] + ' year ' + str(year+1) +':\n'
        current_rainfall = int(input(input_prompt))
        #total_rainfall = current_rainfall + total_rainfall
        lst_total_rainfall.append(current_rainfall)
        total_months = total_months + 1
print('Total Rainfall:\n',sum(lst_total_rainfall))
print('Average Rainfall per month:\n',average(lst_total_rainfall))
print('Total Months:\n',total_months)