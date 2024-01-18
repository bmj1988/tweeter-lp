# !!START
import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"
    # define any other secret environment variables here

# !!END
