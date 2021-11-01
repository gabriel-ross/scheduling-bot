

class EventService(object):
    
    def __init__(self):
        # initialize db connection
        pass

    def create_event(self, date_time, invitees):

        pass
        
        # validate event
        #   * query db for events with similar datetimes
        #   * see if any event overlap or invitee overlap
        #   * if overlap:
        #       * send message via discord service that there is overlap
        #   * if no overlap:
        #       * create event in db, add event to each person's events in db
        #       * send message via discord service that event was successfully created
        #       * use notifier service(s) to notify attendees






