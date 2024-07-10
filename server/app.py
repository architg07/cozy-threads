import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import stripe
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#Product Catalog
items = [
    {
        'id': 1,
        'price': 20,
        'priceId': 'price_1PZpfD2MxxPYBwdYCHvAenyZ',
        'name': 'Cozy Shirt',
        'image': '../products/cozy-shirt.jpeg',
        'shortDescription': "Warm and comfortable",
        'longDescription': "This cozy sweater is made from the finest materials and will keep you warm during the coldest days.",
    },
    {
        'id': 2,
        'price': 70,
        'priceId': 'price_1PZpgC2MxxPYBwdYlMiDpyXX',
        'name': 'Cozy Sweater',
        'image': '../products/cozy-sweater.jpeg',
        'shortDescription': "Warm and stylish",
        'longDescription': "Our cozy sweater is perfect for a night out on the town or a casual day at the office.",
    },
    {
        'id': 3,
        'price': 50,
        'name': 'Cozy Jacket',
        'priceId': 'price_1PZyN82MxxPYBwdYD4mtMA8e',
        'image': '../products/cozy-jacket.jpeg',
        'shortDescription': "Stylish and trendy",
        'longDescription': "Our cozy jacket is perfect for a night out on the town or a casual day at the office.",
    },
    {
        'id': 4,
        'price': 30,
        'priceId': 'price_1PZpfj2MxxPYBwdYimtQrzLf',
        'name': 'Cozy Pants',
        'image': '../products/cozy-pants.jpeg',
        'shortDescription': "Perfect for lounging",
        'longDescription': "Our comfy pants are perfect for lounging around the house or running errands in style.",
            
    },
    {
        'id': 5,
        'price': 100,
        'priceId': 'price_1PZphN2MxxPYBwdYyUQYUBxK',
        'name': 'Cozy Shoes',
        'image': '../products/cozy-shoes.jpeg',
        'shortDescription': "Stylish and comfortable",
        'longDescription': "Our cozy shoes are perfect for a night out on the town or a casual day at the office.",
    }

]

#env Variables to be used for Stripe session and Redirect to frontend
stripe_publishable_key = os.environ.get('STRIPE_PUBLISHABLE_KEY', 'false')
stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY', 'false')
vue_client_hostname = os.environ.get('VUE_CLIENT_HOSTNAME', 'http://localhost:8080')

logger.info(vue_client_hostname)
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

stripe_keys = {
    'publishable_key': stripe_publishable_key,
    'secret_key': stripe_secret_key,
}

stripe.api_key = stripe_keys['secret_key']

@app.route('/items', methods=['GET'])
def all_items():
    return jsonify({
        'status': 'success',
        'items': items
    })

@app.route('/config')
def get_publishable_key():
    stripe_config = {'publicKey': stripe_keys['publishable_key']}
    return jsonify(stripe_config)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    domain_url = f'{vue_client_hostname}'

    try:
        data = json.loads(request.data)
        cart_items = data['cartItems']
        items_dict = {item['id']: item for item in items}
        finalItems = [items_dict[item_id] for item_id in cart_items if item_id in items_dict]
        
        # create line items for the Stripe session
        line_items = []
        for item in finalItems:
            line_items.append({
                'price': item['priceId'],
                'quantity': 1,
            })

        # create new checkout session
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/cancelled',
            payment_method_types=['card'],
            mode='payment',
            line_items=line_items
        )

        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run()