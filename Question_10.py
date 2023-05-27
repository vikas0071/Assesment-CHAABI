# Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

################################################# WithOut Optimization ###############################

# from datetime import datetime, timedelta

# def get_previous_date(date, n):
#     # Convert the date string to a datetime object
#     date = datetime.strptime(date, '%y-%m-%d')
    
#     # Calculate the timedelta for n days
#     delta = timedelta(days=n)
    
#     # Subtract the timedelta from the given date to get the previous date
#     previous_date = date - delta
    
#     # Convert the previous date back to a string representation
#     previous_date_str = previous_date.strftime('%y-%m-%d')
    
#     return previous_date_str


################################################# With Optimization ###############################



from datetime import datetime, timedelta

def get_previous_date(date, n):
    return (datetime.strptime(date, '%y-%m-%d') - timedelta(days=n)).strftime('%y-%m-%d')

date = '16-12-10'
n = 11

result = get_previous_date(date, n)
print(result)
