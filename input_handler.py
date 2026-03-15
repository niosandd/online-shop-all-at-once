def get_user_input():
    """
    Функция для ввода данных о товаре от пользователя.
    Возвращает словарь с данными или None при ошибке.
    """
    try:
        name = input("Введите имя товара (строка): ").strip()
        if not name:
            raise ValueError("Имя товара не может быть пустым.")

        price_str = input("Введите цену товара (вещественное число, например 10.99): ").strip()
        price = float(price_str)
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")

        quantity_str = input("Введите количество (целое число): ").strip()
        quantity = int(quantity_str)
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")

        description = input("Введите описание (строка, опционально): ").strip()

        return {
            "name": name,
            "price": price,
            "quantity": quantity,
            "description": description
        }
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return None


def process_data(data):
    """
    Обработка данных: расчет общей стоимости.
    """
    if data:
        total_cost = data["price"] * data["quantity"]
        print(f"Товар: {data['name']}, Описание: {data['description']}")
        print(f"Общая стоимость: {total_cost:.2f}")
    else:
        print("Данные не введены.")


# Пример использования
if __name__ == "__main__":
    data = get_user_input()
    process_data(data)
