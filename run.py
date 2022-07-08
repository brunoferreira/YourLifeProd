from YourLife import app, db
from YourLife.model import tables

if __name__ =="__main__":
    db.create_all()
    app.run()