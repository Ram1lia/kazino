from envparse import env
import os
env.read_envfile('settings.env')
many = int(os.environ.get('MY_MONEY'))
