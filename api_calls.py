# 3sSgKx00ZdDvrU7QYkiy0SKek4uUjz1HkrFZPP84
import requests
import datetime

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
# example of math with dates 
current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(days=1)
print(current_date)

headers = {
    "Authorization": "Bearer 3sSgKx00ZdDvrU7QYkiy0SKek4uUjz1HkrFZPP84",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
user_request = requests.get("https://courses.ianapplebaum.com/api/syllabus/2", headers=headers)

print(user_request.json())

data = user_request.json()
events = data.get('events', [])

for event in events:
    event_name = event.get('event_name')
    event_date = event.get('event_date')
    print(event_name + " ---- " + event_date)



