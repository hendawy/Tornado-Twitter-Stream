from config import config
from twython import Twython, exceptions, TwythonStreamer
from twython.exceptions import TwythonError, TwythonAuthError
import requests

class TwitterStreamer(TwythonStreamer):
	def on_success(self, data):
		global http_response
		global iterator
		if 'text' in data:
			request_data = {
				'body' : data['text'].encode('utf-8'),
				'screen_name': data['user']['screen_name']
			}
			requests.post(config['send_to'] ,data = request_data)
	def on_error(self, status_code, data):
		print status_code

def main():
	stream = TwitterStreamer(
		config['api_key'], 
		config['api_secret'], 
		config['access_token'], 
		config['access_token_secret']
	)
	stream.statuses.filter( track=config['keyword'].encode('utf-8') )

if __name__ == '__main__':
	main()

{u'contributors': None, u'truncated': False, u'text': u'Omg! Grabe lang happenings kanina. Hahahaha. #G2BLast3Nights', u'in_reply_to_status_id': None, u'id': 441224554854088704, u'favorite_count': 0, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [45, 60], u'text': u'G2BLast3Nights'}], u'urls': []}, u'in_reply_to_screen_name': None, u'id_str': u'441224554854088704', u'retweet_count': 0, u'in_reply_to_user_id': None, u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 81801887, u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/378800000180567800/zCPiAxX4.jpeg', u'verified': False, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/415874967515844608/h3sb0h-r_normal.jpeg', u'profile_sidebar_fill_color': u'F5F3F0', u'profile_text_color': u'050105', u'followers_count': 332, u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'81801887', u'profile_background_color': u'FADCBB', u'listed_count': 2, u'is_translation_enabled': False, u'utc_offset': 28800, u'statuses_count': 16640, u'description': u'I tweet to express not to impress \u221e 18\u2551 Dentistry \u2551 Escolarian', u'friends_count': 319, u'location': u'Dasmarinas City, Cavite PH', u'profile_link_color': u'020003', u'profile_image_url': u'http://pbs.twimg.com/profile_images/415874967515844608/h3sb0h-r_normal.jpeg', u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/81801887/1393686778', u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/378800000180567800/zCPiAxX4.jpeg', u'name': u'Kristine Mojica \u30c4', u'lang': u'en', u'profile_background_tile': True, u'favourites_count': 3216, u'screen_name': u'krstnmojica', u'notifications': None, u'url': None, u'created_at': u'Mon Oct 12 09:16:48 +0000 2009', u'contributors_enabled': False, u'time_zone': u'Hong Kong', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'lang': u'en', u'created_at': u'Wed Mar 05 14:51:46 +0000 2014', u'filter_level': u'medium', u'in_reply_to_status_id_str': None, u'place': None}
