# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, Welcome to KodeCamp DevOps Bookcamp!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('MESSAGE', 'Hello, Welcome to KodeCamp DevOps Bootcamp!')
    password = os.getenv('PASSWORD', 'default_password')
    return f"{message} - Password: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
