from flask import Flask
from flask.ext.gravatar import Gravatar

website = Flask(__name__)
from website import views

gravatar = Gravatar(website,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)
