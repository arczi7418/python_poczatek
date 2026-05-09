products = {
    "chleb": {
        "quantity": 100,
        "price": 8
    },
    "jajka": {
        "quantity": 200,
        "price": 1.5
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity