def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товара с учётом налога.
    Args:
        price: Цена товара.
        tax_rate: Налоговый процент.

    Returns:
        Стоимость товара с учетом налога.
    """

    #если налоговая ставка меньше 0
    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    #благаемые налогом цены
    taxed_prices = []
    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)
    return taxed_prices


def calculate_tax(price: float, tax_rate: float) -> float:

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    result = price * tax_rate / 100
    return result + price