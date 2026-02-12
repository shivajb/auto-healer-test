def calculate_total(price, tax):
    # Intentional Bug: forgot to convert input to float
    return price + (price * tax)

print(calculate_total("100", 0.05))
