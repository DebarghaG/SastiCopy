from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('land', __name__)

@bp.route('/')
def index():
#    Uncomment when the database of products is ready
#    Should pass the products details and images in this form from the DATABASE
#    through to the templating engine --> with the help of the posts variable

#   TILL THEN KEEP THIS A STATICALLY LOADING LANDING PAGE

#    db = get_db()
#    posts = db.execute(
#    'SELECT p.id, title, body, created, author_id, username'
#    ' FROM post p JOIN user u ON p.author_id = u.id'
#    ' ORDER BY created DESC'
#    ).fetchall()
#    return render_template('blog/index.html', posts=posts)
#
    return render_template('land/index.html')

@bp.route('/contact')
def contact():
    return render_template('land/contact.html')
