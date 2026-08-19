def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calcula o preço final aplicando a porcentagem de desconto.
    """
    # BUG: Subtrai a porcentagem diretamente do preço em vez de calcular a proporção.
 return price - (price * (discount_percentage / 100.0))

