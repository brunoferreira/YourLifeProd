from flask import render_template, session, request, send_file
from YourLife import app
from YourLife.model import queries

@app.route("/album/<username>", methods=['GET'])
def album(username):
    if len(username) > 4 and (username[-4:] in ['.png', '.jpg'] or username[-5:] == '.jpeg'):
        return send_file('photos/' + username, mimetype='image/jpg')

    album = queries.get_album_photos(username)
    full_name = queries.get_full_name(username)

    return render_template('albumPage.html', album=album, full_name=full_name)