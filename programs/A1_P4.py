def week_day_name(index):
    names = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    return names[index]

print(week_day_name(5))

def is_leap_year(year):
    if(year%100 !=0 and year%4 ==0) or year%400 ==0:
        return 29
    

def days_in_month(month,year):
    if month == 2:
        return 28 + int(is_leap_year(year))
    elif (month<8 and month%2 !=0) or (month>8 and month%2 ==0):
        return 31
    else:
        return 30
        
m=1
while m<=12:
    print(days_in_month(n),ends = "\t")
    m+=1
    
    print("\nleap ")
    
def date_value(day,month,year):
    value = 0
    y = year - 1
    value = y*365 + y//4 - y//100 + y//400
    return value
    
    m = 1
    while m<month:
        print(f'adding(days_in_month(m,year))')
        value += days_in_month(m,year)
        m+=1
        
    value += day
    return value
 
def week_Day_name(date,month,year):
    ref_date = data_value(1,1,2004)
    input_date = date_value(date,month,year)
    diff = (Ref_data_input_Data) % 7
    return get_Week_Day_name(diff)

date_to_week_day(21,9,2023)