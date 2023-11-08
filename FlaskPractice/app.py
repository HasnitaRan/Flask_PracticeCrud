from flask import Flask, request, redirect, url_for, render_template, jsonify
from models import db,WasteBankModel
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wastebank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()
    
@app.route('/create', methods = ['GET', 'POST'])    
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        nama = request.form['nama']
        jenis = request.form['jenis']
        harga = request.form['harga']
        
    wastebank = WasteBankModel(
        nama = nama,
        jenis = jenis,
        harga = harga
    )    
    db.session.add(wastebank)
    db.session.commit()
    return redirect('/home')

@app.route('/home', methods = ['GET'])    
def RetrieveList():
    wastebank =WasteBankModel.query.all()
    return render_template ('index.html', wastebank = wastebank)


@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    waste = WasteBankModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if waste:
            db.session.delete(waste)
            db.session.commit()
        nama = request.form['nama']
        jenis = request.form['jenis']
        harga = request.form['harga']


        waste = WasteBankModel(
            nama=nama,
            jenis=jenis,
            harga=harga,
        )
        db.session.add(waste)
        db.session.commit()
        return redirect('/')
        return f"Waste with id = {id} Does not exist"
 
    return render_template('update.html', waste = waste)



@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    wastebank = WasteBankModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if wastebank:
            db.session.delete(wastebank)
            db.session.commit()
            return redirect('/')
        abort(404)
     #return redirect('/')
    return render_template('delete.html')

    
app.run(host='localhost', port=5000, use_reloader=False) 
















#######tryyyyy
# from flask import Flask, redirect, url_for, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", content="Testing")

# if __name__ == "__main__":
#     app.run(debug=True)



#########################capstone postman################################################

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/mwd_flask'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# class Sampah(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String(50))
#     jenis = db.Column(db.String(50))
#     harga = db.Column(db.Float)

# # Rute untuk menampilkan semua data sampah (GET)
# @app.route('/sampah', methods=['GET'])
# def data_sampah():
#     sampah_list = Sampah.query.all()
#     result = []
#     for sampah in sampah_list:
#         result.append({
#             'id': sampah.id,
#             'nama': sampah.nama,
#             'jenis': sampah.jenis,
#             'harga': sampah.harga
#         })
#     return jsonify(result)

# # Rute untuk menambahkan data sampah (POST)
# @app.route('/sampah', methods=['POST'])
# def add_sampah():
#     data = request.json
#     new_sampah = Sampah(nama=data['nama'], jenis=data['jenis'], harga=data['harga'])
#     db.session.add(new_sampah)
#     db.session.commit()
#     return jsonify({'message': 'Data sampah berhasil ditambahkan'}), 201

# # Rute untuk mengambil data sampah berdasarkan ID (GET)
# @app.route('/sampah/<int:id>', methods=['GET'])
# def sampah_id(id):
#     sampah = Sampah.query.get(id)
#     if not sampah:
#         return jsonify({'message': 'Data sampah tidak ditemukan'}), 404
#     result = {
#         'id': sampah.id,
#         'nama': sampah.nama,
#         'jenis': sampah.jenis,
#         'harga': sampah.harga
#     }
#     return jsonify(result)

# # Rute untuk mengedit data sampah berdasarkan ID (PUT)
# @app.route('/sampah/<int:id>', methods=['GET','PUT'])
# def edit_sampah(id):
#     sampah = Sampah.query.get(id)
#     if not sampah:
#         return jsonify({'message': 'Data sampah tidak ditemukan'}), 404
#     data = request.json
#     sampah.nama = data['nama']
#     sampah.jenis = data['jenis']
#     sampah.harga = data['harga']
#     db.session.commit()
#     return jsonify({'message': 'Data sampah berhasil diupdate'})

# # Rute untuk menghapus data sampah berdasarkan ID (DELETE)
# @app.route('/sampah/<int:id>', methods=['DELETE'])
# def delete_sampah(id):
#     sampah = Sampah.query.get(id)
#     if not sampah:
#         return jsonify({'message': 'Data sampah tidak ditemukan'}), 404
#     db.session.delete(sampah)
#     db.session.commit()
#     return jsonify({'message': 'Data sampah berhasil dihapus'})
# with app.app_context():
#     db.create_all()

# if __name__ == '_main_':
#     app.run(debug=True)







#####################################Latihan mandiri#########################################

# from flask import Flask,jsonify, request

# app = Flask(__name__)

# # Sample data (can be replaced with a database)
# books = [
#     {"id": 1, "title": "Book 1", "author": "Author 1"},
#     {"id": 2, "title": "Book 2", "author": "Author 2"},
#     {"id": 3, "title": "Book 3", "author": "Author 3"}
# ]

# @app.route('/books', methods=['GET'])
# def get_books():
#     return books

# # Get a specific book by ID
# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     for book in books:
#         if book['id']==book_id:
#             return book
        
#     return {'error':'Book not Found'}

# # Create a book
# @app.route('/books', methods=['POST'])
# def create_book():
#     new_book={'id':len(books)+1,'title':request.json['title'],'author':request.json['author']}
#     books.append(new_book)
#     return new_book

# # Update a book
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     for book in books:
#         if book['id']==book_id:
#             book['title']=request.json['title']
#             book['author']=request.json['author']
#             return book
#     return {'error':'Book not found'}

# # Delete a book
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     for book in books:
#         if book['id']==book_id:
#             books.remove(book)
#             return {"data":"Book Deleted Successfully"}
        
#     return {'error':'Book not Found'}

# # Run the flask run
# if __name__ == '__main__':
#     app.run(debug=True)