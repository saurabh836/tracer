import tweepy  # https://github.com/tweepy/tweepy
import pprint

# Twitter API credentials
consumer_key = "6THoh0ixs5BqEBHQfaKiwDK8x"
consumer_secret = "SfFyDbTKG2ohjVSHdbmR9zMJL6Pj4wUpyRvTBEUZA5tL5duVPS"
access_key = "713252801351131136-saQqIIzfImXd2ftTDIKYlrpraHG31VP"
access_secret = "rlTNNf1thJVpy1wC6juv3ZM2fGYvha32kXQNtZ62ebqO8"


def uni(lis):
    new = []
    for n in lis:
        tem = {}
        for i, k in n.iteritems():
            temp = ['screen_name', 'profile_image_url', 'name']
            if i in temp:
                if i == 'screen_name':
                    i = 'profile_url'
                    tid = k
                    k = 'https://twitter.com/' + k
                    tem.update({'id': '@' + tid})
                if i == 'profile_image_url':
                    k = k.replace("normal", "bigger")
                tem.update({i: k})
        new.append(tem)
    return new


def get_twitter(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    a = api.search_users(screen_name)
    x = [j._json for j in a]
    return uni(x)

# pprint.pprint(get_twitter("Abhiram Bhise"))
