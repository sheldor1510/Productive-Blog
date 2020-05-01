import os

class Config:
    SECRET_KEY =  '8c95ca907af41d125536253accdf36b4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_USERNAME = 'example@gmail.com'
    MAIL_PASSWORD = 'examplepassword'

