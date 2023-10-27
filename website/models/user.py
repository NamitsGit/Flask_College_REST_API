from website.utils.constants import db
# from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        u =  "\"id\" : \"{}\",\"uname\" : \"{}\",\"email\" : \"{}\",\"password\" : \"{}\"".format(self.id, self.username, self.email, self.password)
        u = "{ "+ u +" }"
        return u


