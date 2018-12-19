from etsy import EtsyEnvProduction
from requests_oauthlib import OAuth1Session


class EtsyOAuthClient(OAuth1Session):
    def __init__(self, oauth_consumer_key,
                 oauth_consumer_secret, etsy_env=EtsyEnvProduction(), **kwargs):
        super(EtsyOAuthClient, self).__init__(
            oauth_consumer_key, oauth_consumer_secret, **kwargs)
        self.request_token_url = etsy_env.request_token_url
        self.access_token_url = etsy_env.access_token_url
        self.signin_url = etsy_env.signin_url

    def get_signin_url(self, **kwargs):
        self.fetch_request_token(self.request_token_url)
        return self.authorization_url(self.signin_url)

    def set_oauth_verifier(self, oauth_verifier):
        token = self.fetch_access_token(
            self.access_token_url, verifier=str(oauth_verifier))
        self.resource_owner_key = token['oauth_token']
        self.resource_owner_secret = token['oauth_token_secret']

    def do_oauth_request(self, url, http_method, content_type, body):
        headers = {}
        if content_type:
            headers = {'Content-Type': content_type}
        return self.request(http_method, url, headers=headers, data=body).text
