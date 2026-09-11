def apply_discount(price, discount_percent=10):
    discounted_percent = price - (price * discount_percent / 100)
    return round(discounted_percent, 2)