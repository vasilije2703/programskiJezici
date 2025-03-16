import json
from pprint import pprint


with open('log.json' , 'r', encoding='utf-8') as f:
    events = json.load(f)
    pprint(events)

with open('employees.txt' , 'r') as t:
    employees = t.readlines()

count  = {}
for event in events:
    if event["type"] in count:
        count[event["type"]] += 1
    else:
        count[event["type"]] = 1

#pprint(count)

employees = {emp.strip().lower() for emp in  employees}
filtered_events = [
    event for event in events if event["actor"]["login"].strip().lower() in employees
]


#print("Employee events: " , len(filtered_events))










