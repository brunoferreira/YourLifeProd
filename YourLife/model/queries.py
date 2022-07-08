from YourLife import db
from YourLife.model.tables import User, Post, Photo

def username_available(username):
    query = User.query.filter_by(username=username).first()
    if query == None:
        return True
    return False

def email_available(email):
    query = User.query.filter_by(email=email).first()
    if query == None:
        return True
    return False

def login(username, password):
    query = User.query.filter_by(username=username, password=password).first()
    if query == None:
        return False
    return True

def change_profile_photo(username, filepath):
    db.session.query(Photo).filter(Photo.username == username and Photo.type == 0).update({"filepath": filepath}, synchronize_session="fetch")
    db.session.commit()

def get_profile_photo(username):
    query = db.session.query(Photo).filter(Photo.username == username and Photo.type == 0)
    return query.first().filepath

def change_summary(username, summary):
    db.session.query(User).filter(User.username == username).update({"summary": summary}, synchronize_session="fetch")
    db.session.commit()

def get_summary(username):
    query = db.session.query(User).filter(User.username == username)
    return query.first().summary

def add_album_photo(username, filepath):
    db.session.add(Photo(filepath, username, 1))
    db.session.commit()

def get_album_photos(username):
    query = db.session.query(Photo).filter(Photo.username == username, Photo.type == 1)
    res = []
    for r in query.all():
        res.append(r.filepath)
    return res

def get_posts(username):
    query = db.session.query(Post).filter(Post.username == username)
    res = []
    for r in query.all():
        res.append(r.content)
    return res

def add_post(username, content):
    db.session.add(Post(content, username))
    db.session.commit()

def get_full_name(username):
    query = db.session.query(User).filter(User.username == username)
    return query.first().name + ' ' + query.first().surname