'''
event handler for scheduler bot
'''

import discord
import re
from typing import List


class DiscordClient(discord.Client):
    '''
    client for discord containing event handlers
    '''

    def __init__(self, event_service, db_profile):

        self._event_service = event_service
        self._db_profile = db_profile

    async def on_message(self, message):

        '''
        event-creation message format:
        /createevent dateTime user1, user2, user3...
        ''' 
        if message.content.startswith("/createevent"):

            # digest message
            msg_contents = re.split('\s|,')
            date_time = msg_contents[1]
            invitees = self.clean_usernames(msg_contents[2:])
            
            # pass to event service, tell it we've recieved an event creation request
            # should event service be abstract? 
            self.event_service.create_event(date_time, invitees)

    @classmethod
    def clean_usernames(cls, usernames: List[List[str]]) -> List[List[str]]:
        
        cleaned_usernames = []

        for username in usernames:
            if username:
                cleaned_usernames.append(re.sub('[!@#^,; ]', '', username))

        return cleaned_usernames