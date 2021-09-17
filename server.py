from flask import Flask, render_template, redirect, request
from users import User 
app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users")

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("read_all.html", all_users = users)

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create',methods=['POST'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)