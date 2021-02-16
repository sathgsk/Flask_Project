from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sathishgofficial@gmail.com'
app.config['MAIL_PASSWORD'] = 'Pass@123'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/",methods=['GET'])
def index():
   msg = Message('Hello', sender = 'sathishgofficial@gmail.com', recipients = ['mr.sathishkumargsk@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)