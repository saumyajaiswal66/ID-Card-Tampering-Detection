from flask import Flask

import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
from app import views

# if app.config["ENV"] == "production":
#     app.config.from_object("config.DevelopmentConfig")
# elif app.config["ENV"] == "testing":
#     app.config.from_object("config.TestingConfig")
# else:
#     app.config.from_object("config.ProductionConfig")

