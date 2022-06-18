from controllers import _Controller

from flask import render_template, redirect, url_for


class LoginController(_Controller):
    def _get(self):
        return render_template("login.html")

    def _post(self):
        if self.request.form.get("login", "") != "" and self.request.form.get("password", "") != "":
            if self.request.form["login"] == "test" and self.request.form["password"] == "test":
                return redirect(url_for('main'))
            else:
                return render_template("login.html", error="incorrect login or password")
        else:
            return render_template("login.html", error="Fill all fields")
