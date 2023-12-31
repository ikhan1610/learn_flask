from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #Flask constructor / instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
with app.app_context():
    db = SQLAlchemy(app) 
    class Todo(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        content = db.Column(db.String(200), nullable = False )
        date_created = db.Column(db.DateTime, default = datetime.utcnow)

        def __repr__(self):
            return '<Task %r>' % self.id
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
