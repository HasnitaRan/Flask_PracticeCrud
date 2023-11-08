from flask import Flask, render_template, request, url_for, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return "halo selamat datang bidadari"

# http://127.0.0.1:5000
@app.route('/') #decorator
def index():
    return f'''
    <a href="{url_for('home')}">Go to Home!</a>
    <br>
    <a href="{url_for('user', username='Hasnita')}">Go to My Page!</a>
    <br>
    <img src="{ url_for('static', filename='apel.png') }" />
    '''


# http://127.0.0.1:5000/home
@app.route("/home")
def home():
    return "<h1>This is my home!</h1>"

# http://127.0.0.1:5000/user/yourname
@app.route('/user/<username>')
def user(username):
    return f'My name is {username}'
    #return 'My name is '+username

with app.test_request_context():
    print(url_for('index'))
    print(url_for('home'))
    print(url_for('user', username='Hasnita'))



@app.get('/mydata')
def mydata():
    name = request.args.get('nama')
    kelas = request.args.get('kelas')
    
    return jsonify({'Nama' : name, 'Kelas' : kelas,'Result' : 'Sukses'})

if __name__ == '__main__':
    app.run(debug=True)


#####
#class Base(DeclarativeBase):

# db = SQLAlchemy(model_class=Base)
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myflask.db"
# db.init_app(app)

# class User(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     email: Mapped[str] = mapped_column(String)

# with app.app_context():
#     db.create_all()

#     @app.route("/users")
#     def user_list():
#         users = db.session.execute(db.select(User).order_by(User.username)).scalars()
#         return render_template("user/list.html", users=users)

# @app.route("/users/create", methods=["GET", "POST"])
# def user_create():
#     if request.method == "POST":
#         user = User(
#             username=request.form["username"],
#             email=request.form["email"],
#         )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("user_detail", id=user.id))

#     return render_template("user/create.html")

# @app.route("/user/<int:id>")
# def user_detail(id):
#     user = db.get_or_404(User, id)
#     return render_template("user/detail.html", user=user)

# @app.route("/user/<int:id>/delete", methods=["GET", "POST"])
# def user_delete(id):
#     user = db.get_or_404(User, id)

#     if request.method == "POST":
#         db.session.delete(user)
#         db.session.commit()
#         return redirect(url_for("user_list"))

#     return render_template("user/delete.html", user=user)