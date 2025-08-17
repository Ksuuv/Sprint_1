string = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

for i in string.split(','):
    minutes = 0
    for element in i.split():
        if 'h' in element:
            hours = int(element.replace('h', ''))
            minutes += hours * 60
        elif 'm' in element:
            mins = int(element.replace('m', ''))
            minutes += mins
        elif 's' in element:
            seconds = int(element.replace('s', ''))
            minutes += seconds / 60
    
    total_minutes += minutes

print(f"Общее количество минут: {total_minutes}")
