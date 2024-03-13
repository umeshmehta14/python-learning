import requests


def get_products():
    url = "https://techbayum14.onrender.com/api/v1/products/filter"
    res = requests.get(url)
    data = res.json()
    if data["success"] and "data" in data:
        return data["data"]
    else:
        raise Exception("Failed to get product")

def main():
    try:
        products_data = get_products()
        products = products_data["products"]
        for product in products:
            print(product["title"])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()