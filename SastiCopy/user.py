from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('user',__name__, url_prefix='/user')

@bp.route('/confirmation')
def confirmation():
    return render_template('user/confirmation.html')

@bp.route('/tracking')
def tracking():
    return render_template('user/tracking.html')
