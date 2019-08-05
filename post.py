from twitter import Twitter, OAuth
import access

def lambda_handler(event, context):
	access_token = "1057214897946165248-xqkpkQIQQTi7AQRHjeOXrne4P9QPGk"
	access_token_secret = "4VqE1WQxWpr7ysfiFgCxEplV6Ky5hMJpdVLTjs47oST0u"
	api_key = "xTjNpPAMLpjNQgHUaIJcuLVQJ"
	api_secret = "o8Dziw80QpOck4ThmOaO7kQbYJQgYLKb7JeGxsKpWC0q6nksKD"

	t = Twitter(auth = OAuth(access_token, access_token_secret, api_key, api_secret))

	text = access.pick_text()
	statusUpdate = t.statuses.update(status=text)
	print(statusUpdate)

	# data
	print(statusUpdate['user']['screen_name'])
	print(statusUpdate['user']['name'])
	print(statusUpdate['text'])

