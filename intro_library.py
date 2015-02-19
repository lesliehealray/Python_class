from datetime import datetime    
    
print datetime.now()
now = datetime.now()            
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.hour
current_minutes = now.minute
current_seconds = now.second
now = datetime.now()
print current_year
print current_month
print current_day
print '%s:%s:%s ' % (current_hour, current_minutes, current_seconds)
