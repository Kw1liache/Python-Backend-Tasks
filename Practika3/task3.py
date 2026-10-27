class Product:
    def __init__(
        self, name: str, price: float, stock: int, category: str) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        if stock < 0:
            raise ValueError("Количество на складе не может быть отрицательным.")
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.order_history: list[Order] = []


class Order:
    def __init__(
        self,
        products: dict[Product, int],
        discount_percent: float = 0,
        tax_percent: float = 0,
    ) -> None:
        if not products:
            raise ValueError("Нельзя оформить пустой заказ.")
        if not 0 <= discount_percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100 процентов.")
        if tax_percent < 0:
            raise ValueError("Налог не может быть отрицательным.")

        self.products = products.copy()
        self.discount_percent = discount_percent
        self.tax_percent = tax_percent
        self.total: float | None = None

    def process(self, customer: Customer) -> float:
        if self.total is not None:
            raise ValueError("Заказ уже оформлен.")
        for product, quantity in self.products.items():
            if quantity <= 0:
                raise ValueError("Количество товара должно быть положительным.")
            if product.stock < quantity:
                raise ValueError(f"Недостаточно товара «{product.name}» на складе.")

        subtotal = sum(
            product.price * quantity
            for product, quantity in self.products.items()
        )
        discounted_total = subtotal * (1 - self.discount_percent / 100)
        self.total = round(discounted_total * (1 + self.tax_percent / 100), 2)

        for product, quantity in self.products.items():
            product.stock -= quantity
        customer.order_history.append(self)
        return self.total


class ShoppingCart:
    def __init__(self) -> None:
        self.products: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")
        new_quantity = self.products.get(product, 0) + quantity
        if new_quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе.")
        self.products[product] = new_quantity

    def remove_product(self, product: Product) -> None:
        if product not in self.products:
            raise KeyError(f"Товара «{product.name}» нет в корзине.")
        del self.products[product]

    def update_quantity(self, product: Product, quantity: int) -> None:
        if product not in self.products:
            raise KeyError(f"Товара «{product.name}» нет в корзине.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")
        if quantity == 0:
            self.remove_product(product)
            return
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе.")
        self.products[product] = quantity

    def checkout(
        self,
        customer: Customer,
        discount_percent: float = 0,
        tax_percent: float = 0,
    ) -> float:
        order = Order(self.products, discount_percent, tax_percent)
        total = order.process(customer)
        self.products.clear()
        return total


if __name__ == "__main__":
    laptop = Product("Ноутбук", 80000, 5, "Электроника")
    mouse = Product("Мышь", 2500, 10, "Аксессуары")
    customer = Customer("Алексей", "alex@example.com")
    cart = ShoppingCart()

    cart.add_product(laptop)
    cart.add_product(mouse, 2)
    cart.update_quantity(mouse, 1)
    total = cart.checkout(customer, discount_percent=10, tax_percent=20)

    print(f"Заказ покупателя {customer.name}: {total:.2f} руб.")
    print(f"Заказов в истории: {len(customer.order_history)}")
    print(f"Ноутбуков осталось на складе: {laptop.stock}")
