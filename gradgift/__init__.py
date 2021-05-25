import os
from flask import Flask

from local_settings import Config
# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

import gradgift.routes
