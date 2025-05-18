time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

time_values = time_string.split(',')

for value in time_values:
    value = value.replace('s', '')
    
    if 'h' in value:
        hours = int(value.split('h')[0])
        total_minutes += hours * 60
        value = value.split('h')[1]

    if 'm' in value:
        minutes = int(value.split('m')[0])
        total_minutes += minutes

print(total_minutes)