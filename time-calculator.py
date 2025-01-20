import re

def add_time(start, duration, optional=None):
    # components
    time = re.findall(r'\d+', start)
    hour = int(time[0])
    minute = int(time[1])
    duration_time = re.findall(r'\d+', duration)
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    
    # AM/PM
    meridiem = re.search(r'\b(AM|PM)\b', start).group()
    
    # Convert to 24-hour format
    if meridiem == 'PM' and hour != 12:
        hour += 12
    elif meridiem == 'AM' and hour == 12:
        hour = 0
    
    # duration
    total_minutes = minute + duration_minute
    total_hours = hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60
    
    # new day
    days_later = total_hours // 24
    total_hours %= 24
    
    # 12-hour format
    new_meridiem = 'AM' if total_hours < 12 else 'PM'
    new_hour = total_hours % 12
    if new_hour == 0:
        new_hour = 12  # midnight and noon

    # format
    new_time = f"{new_hour}:{total_minutes:02d} {new_meridiem}"
    
    # optional
    if optional:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        optional = optional.capitalize()
        if optional in days_of_week:
            day_index = days_of_week.index(optional)
            new_day = days_of_week[(day_index + days_later) % 7]
            new_time += f", {new_day}"
    
    # days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time


if __name__ == '__main__':
    print(add_time('3:30 PM', '2:12'))
