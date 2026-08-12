def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calcula o preço final aplicando a porcentagem de desconto.
    
    Args:
        price: The original price
        discount_percentage: The discount percentage (e.g., 10 for 10%)
    
    Returns:
        The price after applying the discount
    
    Examples:
        >>> calculate_discount(50.0, 10)
        45.0
        >>> calculate_discount(100.0, 20)
        80.0
    """
    # Apply discount percentage correctly: price * (1 - discount/100)
    return price * (1 - discount_percentage / 100)
