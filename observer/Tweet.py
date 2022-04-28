from datetime import datetime
class Tweet:
    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id
        self.created_at = str(datetime.now().strftime("%H:%M")) + " - " + str(datetime.now().strftime("%d/%m/%Y"))

    # Returns the text of the tweet
    def get_text(self):
        return self.text
    # Returns the user_id of the tweet
    def get_user_id(self):
        return self.user_id
    # Returns the created_at of the tweet
    def get_created_at(self):
        return self.created_at
    