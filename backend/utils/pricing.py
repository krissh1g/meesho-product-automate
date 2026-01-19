import random

def apply_pricing(base_price, shipping=50, min_margin=100, max_margin=150):
    cost = base_price + shipping
    margin = random.randint(min_margin, max_margin)
    selling = cost + margin
    return cost, selling
