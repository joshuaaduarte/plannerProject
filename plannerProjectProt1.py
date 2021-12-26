from dateutil import tz
from datetime import datetime
from ics import Calendar, Event

date_format = '%Y-%m-%d %H:%M:%S' # Format the ics module expects the dates to be in
due = '2021-12-26 12:00:00'       # Sample date that needs to be converted to UTC (Currently in Canada/Pacific time zone)

# First let's convert this to a datetime object in the Canada/Pacific Time zone

# Original 
# due_dt = datetime.strptime(due,date_format).replace(tzinfo=tz.gettz('Canada/Pacific'))

# Updated
due_dt = datetime.strptime(due,date_format).replace(tzinfo=tz.gettz('UTC/Central'))

# # Then let's convert the date to UTC so ics can handle it correctly
due_dt = due_dt.astimezone(tz.tzutc())

c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = due_dt.strftime(date_format) # Updated this to use date_format
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
        my_file.writelines(c)
