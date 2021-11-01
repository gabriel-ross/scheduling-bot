

class PersonModel(object):

    def __init__(self, discord_username: str, name: str, phone_num: str, email: str) -> None:
        self.discord_username = discord_username
        self.name = name
        self.phone_num = phone_num
        self.email = email