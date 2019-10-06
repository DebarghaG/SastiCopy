from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('shop',__name__, url_prefix='/shop')

@bp.route('/about')
def index():
    return render_template('shop/about.html')

@bp.route('/category')
def contact():
    return render_template('shop/category.html')
# Replicate this for each category when adding

@bp.route('/singleproduct')
def singleprod():
    return render_template('shop/single-product.html')
