from social_core.backends.twitter import TwitterOAuth as auth

# Monkey Patch for social_core.backends.twitter.TwitterOAuth
# https://dev.twitter.com/rest/reference/get/account/verify_credentials
class TwitterOAuth(auth):
    def get_user_details(self, response):
        """Return user details from Twitter account"""
        fullname, first_name, last_name = self.get_user_names(response['name'])
        return {'username': response['screen_name'],
                'email': response.get('email', ''),
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'icon_url': response.get('profile_image_url', '')}

