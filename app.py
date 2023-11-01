from flask import Flask, render_template, request,redirect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment
from datetime import datetime
import face_recognition,os
import os.path
import os 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
db = SQLAlchemy(app)

class person(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(300),nullable=False)
    photo_path = db.Column(db.String(500))
    date=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

def check_file_exists(path):
    return os.path.exists(path) 

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/database', methods=['GET','POST'])
def database():
    matching_people= None
    if request.method == 'POST':
        search_name = request.form['search_name']
        matching_people = person.query.filter(person.name.ilike(f"%{search_name}%")).all()
        # return render_template('database.html', matching_people=matching_people)


    all_records = person.query.all()
    return render_template('database.html', matching_people=matching_people, all_records=all_records,check_file_exists=check_file_exists)

@app.route('/face_comparison', methods=['POST', 'GET'])
def face_comparison():
    if request.method == 'POST':

        name = request.form['name']
        uploaded_image = request.files['image']

        # Load and encode the uploaded image
        uploaded_image_data = face_recognition.load_image_file(uploaded_image)
        uploaded_face_encoding = face_recognition.face_encodings(uploaded_image_data)

        if uploaded_face_encoding:
            matching_people = []
            for person_record in person.query.filter_by(name=name).all():
                stored_image_data = face_recognition.load_image_file(person_record.photo_path)
                stored_face_encoding = face_recognition.face_encodings(stored_image_data)
                
                if face_recognition.compare_faces([uploaded_face_encoding[0]], stored_face_encoding[0])[0]:
                    matching_people.append(person_record.name)

        if matching_people:
            result = f"Matching persons: {', '.join(matching_people)}"
        else:
            result = "No match found"
    else:
        result = "None"

    return render_template('face_comparison.html', result=result)



@app.route('/face_upload', methods=['GET', 'POST'])
def face_upload():
    if request.method == 'POST':
        name = request.form['name']
        photo = request.files['photo']
        
        # Save the uploaded photo to a location
        if photo:
            photo_filename = secure_filename(photo.filename)  # Make sure to import `secure_filename`
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
            photo.save(photo_path)
            
            # Store the photo path and name in the database
            new_person = person(name=name, photo_path=photo_path)
            db.session.add(new_person)
            db.session.commit()
            
    return render_template('face_upload.html')


if __name__ == '__main__':
    app.run(debug=True)
