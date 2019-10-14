from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('land', __name__)

@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
    'SELECT * FROM product'
    ).fetchall()
    print(products)
    return render_template('land/index.html', products = products)

@bp.route('/contact')
def contact():
    return render_template('land/contact.html')
