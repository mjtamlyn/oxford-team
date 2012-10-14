import os

from flask import Flask, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.threaded = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db')
db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = Email(email=request.post('email'))
        db.session.add(email)
        db.session.commit()
        return 'ok'
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
