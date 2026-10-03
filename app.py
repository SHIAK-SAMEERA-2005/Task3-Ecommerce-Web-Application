from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "task3"

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Smart Watch", "price": 2500},
    {"id": 3, "name": "Headphones", "price": 1500},
    {"id": 4, "name": "Keyboard", "price": 1000}
]

@app.route("/", methods=["GET", "POST"])
def home():

    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        product_id = int(request.form["product_id"])
        session["cart"].append(product_id)
        session.modified = True

    cart = []

    for product in products:
        if product["id"] in session["cart"]:
            cart.append(product)

    total = sum(product["price"] for product in cart)

    return render_template(
        "index.html",
        products=products,
        cart=cart,
        total=total
    )


@app.route("/checkout")
def checkout():

    session["cart"] = []

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)