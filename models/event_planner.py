from models.event import Event

event_1 = Event("10/03/2022", "Music Concert", "200", "Usher Hall", "Classical Music")
event_2 = Event("12/03/2022", "Play", "80", "Kings Theatre", "Theatre")
event_3 = Event("05/06/2022", "Comedy Gig", "50", "Pub", "A funny show")

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)