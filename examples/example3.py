def identify_product_by_name(name):
    if name == "авокадо":
        return "Это фрукт"
    elif name == "чай":
        return "Это напиток"
    else:
        return "Неизвестный продукт"

product_description = identify_product_by_name('авокадо')
print(product_description)