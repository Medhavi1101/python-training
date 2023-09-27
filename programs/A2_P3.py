

def date_to_day_name(date,month,year):
    diff=date_to_week_day(date,month,year)
    return day_name(diff)

def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff

def days_in_month(month , year):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30
    

def day_name(index):
    day_names=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    return day_names[index]

def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def date_value(day ,month, year):
    value=0
    y=year-1
    # total days elapsed till the end of previous year
    value = y * 365 + y//4  - y//100 + y//400

    # add total days passed till previous month of this year
    m=1
    while m<month:
        #print(f'Adding {days_in_month(m,year)} for {m}/{year}')
        value+= days_in_month(m,year)
        m+=1

    #add days of this month
    value+=day
    return value

def print_calendar(month,year):
    for i in range(7):
        print( day_name(i).upper()[0:3], end="\t")
    print()
    
    position = date_to_week_day(1,month,year)
    print("\t"*position, end="")

    for day in range(1, days_in_month(month,year)+1):
        print(day,end="\t")
        position+=1
        if position %7 ==0:
            print()
            
print_calendar(9,2023)



