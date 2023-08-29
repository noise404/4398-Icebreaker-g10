from winotify import Notification
import requests
import datetime

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
# example of math with dates 
current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(days=1)
#print(current_date)

headers = {
    "Authorization": "Bearer 3sSgKx00ZdDvrU7QYkiy0SKek4uUjz1HkrFZPP84",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
user_request = requests.get("https://courses.ianapplebaum.com/api/syllabus/4", headers=headers)

data = user_request.json()
events = data.get('events', [])

#Iterate through syllabus and build string of assignment and date

MessageString = ""
counter = 0
for event in events:
    event_name = event.get('event_name')
    event_date = event.get('event_date')
    event_date_obj = datetime.datetime.strptime(event_date, "%Y-%m-%d")
    if(event_date_obj < current_date):
        continue
    MessageString += event_name + " " + event_date + "\n"
    counter += 1
    if(counter >= 3):
        break

#Send notification

toast = Notification(app_id="CIS 4398 Due Dates Reminder",
                     title="Next Three Assignments",
                     msg= MessageString)
toast.show()