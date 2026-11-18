
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "shopping-cart-secret-key"

products = [
    {
        "id": 1,
        "name": "Simsiz quloqchin",
        "category": "Elektronika",
        "price": 249000,
        "rating": 4.8,
        "reviews": 124,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600",
        "description": "Yuqori sifatli simsiz quloqchin."
    },
    {
        "id": 2,
        "name": "Aqlli soat",
        "category": "Elektronika",
        "price": 399000,
        "rating": 4.6,
        "reviews": 89,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600",
        "description": "Zamonaviy va qulay aqlli soat."
    },
    {
        "id": 3,
        "name": "Kundalik ryukzak",
        "category": "Moda",
        "price": 189000,
        "rating": 4.7,
        "reviews": 65,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600",
        "description": "Har kun foydalanish uchun qulay ryukzak."
    },
    {
        "id": 4,
        "name": "Yugurish oyoq kiyimi",
        "category": "Moda",
        "price": 329000,
        "rating": 4.9,
        "reviews": 210,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600",
        "description": "Yengil va qulay sport oyoq kiyimi."
    },
    {
        "id": 5,
        "name": "Raqamli fotoapparat",
        "category": "Elektronika",
        "price": 899000,
        "rating": 4.8,
        "reviews": 76,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600",
        "description": "Yuqori sifatli suratlar uchun fotoapparat."
    },
    {
        "id": 6,
        "name": "Qahva tayyorlagich",
        "category": "Uy uchun",
        "price": 459000,
        "rating": 4.5,
        "reviews": 52,
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600",
        "description": "Mazali qahva tayyorlash uchun avtomatik qurilma."
    },
    {
        "id": 7,
        "name": "Quyosh ko‘zoynagi",
        "category": "Moda",
        "price": 159000,
        "rating": 4.4,
        "reviews": 43,
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600",
        "description": "Zamonaviy va chiroyli ko‘zoynak."
    },
    {
        "id": 8,
        "name": "Stol chirog‘i",
        "category": "Uy uchun",
        "price": 119000,
        "rating": 4.6,
        "reviews": 38,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600",
        "description": "Ish stoli uchun zamonaviy chiroq."
    }
]


def get_cart():
    return session.get("cart", {})


def get_cart_details():
    cart = get_cart()
    cart_items = []
    total = 0
    total_quantity = 0

    for product in products:
        product_id = str(product["id"])
        quantity = cart.get(product_id, 0)

        if quantity > 0:
            item = product.copy()
            item["quantity"] = quantity
            item["subtotal"] = product["price"] * quantity

            cart_items.append(item)
            total += item["subtotal"]
            total_quantity += quantity

    return cart_items, total, total_quantity


@app.route("/")
def index():
    cart_items, total, total_quantity = get_cart_details()

    return render_template(
        "index.html",
        products=products,
        cart_items=cart_items,
        total=total,
        total_quantity=total_quantity
    )


@app.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = get_cart()
    product_id = str(product_id)

    if any(str(p["id"]) == product_id for p in products):
        cart[product_id] = cart.get(product_id, 0) + 1

    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/update/<int:product_id>", methods=["POST"])
def update_cart(product_id):
    cart = get_cart()
    product_id = str(product_id)

    try:
        quantity = int(request.form.get("quantity", 1))
    except (ValueError, TypeError):
        quantity = 1

    if quantity <= 0:
        cart.pop(product_id, None)
    elif any(str(p["id"]) == product_id for p in products):
        cart[product_id] = quantity

    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/remove/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)

    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear_cart():
    session["cart"] = {}
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
