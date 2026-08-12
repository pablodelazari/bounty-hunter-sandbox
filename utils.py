def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calcula o preço final aplicando a porcentagem de desconto.
    """
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount
