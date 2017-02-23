from flask import Flask

app = Flask(__name__)
""" usually we can add main fuction like def hellowolrd(): return "hello world" below and with app.run(...) then we can
run the applicatio,but in this example, we put main function to views.py and app.run to the run.py """
app.config.from_object('config')
from app import views
