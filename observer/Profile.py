from Tweet import Tweet

class Profile:
    
    def __init__(self, username):
        self.username = username
        self.Tweets = []
        self.Followers = []
    
    # Returns the username of the profile
    def get_username(self):
        return self.username

    # Adds new tweet to the profile
    def add_tweet(self):
        tweetContent = str(input("Enter tweet: "))
        tweet = Tweet(tweetContent, self.username)
        self.Tweets.append(tweet)
        self.notify_followers(tweet)

    # Notifies its followers of a new tweet
    def notify_followers(self, tweet):
        for follower in self.Followers:
            follower.update(self, tweet)

    # Returns the tweets of the profile
    def follow(self, Profile):
        Profile.Followers.append(self)

    # Update message of new tweet
    def update(self, Profile, tweet):
        print(f'''New tweet from {Profile.get_username()}! - "{tweet.get_text()}" : {tweet.get_created_at()}''')

    # Returns followers of the profile
    def get_followers(self):
        return self.Followers
