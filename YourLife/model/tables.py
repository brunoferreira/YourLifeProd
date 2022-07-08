from YourLife import db

class User(db.Model):
    __tablename__="users"
    
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    name=db.Column(db.String)
    surname=db.Column(db.String)
    email=db.Column(db.String, unique=True)
    summary=db.Column(db.String)

    def __init__(self,username,password,name,surname,email):
        self.username=username
        self.password=password
        self.name=name
        self.surname=surname
        self.email=email
        self.summary = ''

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__="posts"
    
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.Text)
    username=db.Column(db.Text)

    def __init__(self, content, username):
        self.content=content
        self.username = username

    def __repr__(self) -> str:
        return "<Post %r>" % self.id

class Photo(db.Model):
    __tablename__="photos"
    
    id=db.Column(db.Integer, primary_key=True)
    filepath=db.Column(db.Text)
    username=db.Column(db.Text)
    type=db.Column(db.Integer)

    def __init__(self, filepath, username, type):
        self.filepath=filepath
        self.username=username
        self.type = type

    def __repr__(self) -> str:
        return "<Post %r>" % self.id