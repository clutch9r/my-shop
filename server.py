from flask import Flask, jsonify
from database import get_products, get_categories
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/categories')
def categories():
    cats = get_categories()
    return jsonify([{'id': c[0], 'name': c[1]} for c in cats])

@app.route('/products')
def products():
    prods = get_products()
    return jsonify([{
        'id': p[0], 'name': p[1], 'price': p[2],
        'description': p[3], 'photo_id': p[4], 'category_id': p[5]
    } for p in prods])

@app.route('/products/<int:cat_id>')
def products_by_category(cat_id):
    prods = get_products(cat_id)
    return jsonify([{
        'id': p[0], 'name': p[1], 'price': p[2],
        'description': p[3], 'photo_id': p[4], 'category_id': p[5]
    } for p in prods])
import httpx

@app.route('/photo/<photo_id>')
async def get_photo(photo_id):
    TOKEN = "твой_токен"
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={photo_id}")
        file_path = r.json()['result']['file_path']
        img = await client.get(f"https://api.telegram.org/file/bot{TOKEN}/{file_path}")
        return img.content, 200, {'Content-Type': 'image/jpeg'}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)