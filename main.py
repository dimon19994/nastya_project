from flask import Flask, request
from controllers.login import LoginController
from controllers.main_page import MainPageController

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return LoginController(request).call()


@app.route("/main", methods=['GET', 'POST'])
def main():
    return MainPageController(request).call()


if __name__ == '__main__':
    app.run()