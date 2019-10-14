from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('shop',__name__, url_prefix='/shop')

#A well written company description goes here.
@bp.route('/about')
def index():
    return render_template('shop/about.html')

@bp.route('/cart')
def cart():
    return render_template('shop/cart.html')

@bp.route('/checkout')
def checkout():
    return render_template('shop/checkout.html')

#Hardcode the category page in HTML
@bp.route('/category')
def contact():
    db = get_db()
    products = db.execute(
    'SELECT * FROM product'
    ).fetchall()
    print(products)
    return render_template('shop/category.html', products = products)

#Method should return product information
def get_product(identity):
    product = get_db().execute(
    'SELECT * FROM product WHERE id=identity'
    ).fetchone()
    return product

#Render product detailed view, photo, description etc.
@bp.route('/singleproduct/<int:id>')
def singleprod(id):
    product = get_product(id)
    return render_template('shop/single-product.html', products = product)

#To add a product to the cart

@bp.route('/add', methods=['POST'])
def add_product_to_cart():
    cursor = None
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        #Validating the recieved values.
        if _quantity and _code and request.method == 'POST':
            row = db.get_db().execute(
            'SELECT * FROM product where code =%s', _code).fetchone()

            itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}

            all_total_price=0
            all_total_quantity=0

            session.modified=True
            if 'cart_item' in session:
                if row['code'] in session['cart_item']:
                    for key,value in session['cart_item'].items():
                        if row['code'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                    session['cart_item'] = itemArray
                    all_total_quantity = all_total_quantity + _quantity
                    all_total_price = all_total_price + _quantity * row['price']

            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(url_for('.products'))

        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)

@bp.route('/empty')
def empty_cart():
    try:
        session.clear()
        #Feel free to change this to whatever you feel is necessary
        #As a design feature to when the cart is emptied.
        return redirect(url_for('.category'))
    except Exception as e:
        print(e)

def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array+second_array
    elif isinstance(first_array, dict) and isinstance(second_array, list):
        return dict(list(first_array.items())+list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False

"""

@Prajwal : As a reference to how the functions work and how to end up
templating the products objects that are being passed to :

https://www.roytuts.com/simple-shopping-cart-using-python-flask-mysql/


"""
