from controllers import _Controller

from flask import render_template


class MainPageController(_Controller):
    def _get(self):
        return render_template("main.html")

    def _post(self):
        pass