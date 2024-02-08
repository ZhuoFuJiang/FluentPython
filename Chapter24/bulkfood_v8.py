import model_v8 as model


class LineItem(model.Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    walnuts = LineItem('walnuts', 1, 10)
    # print(vars(walnuts))
    # print(dir(walnuts))
    print(getattr(walnuts, 'weight'))
    print(LineItem.weight)
    print(vars(walnuts))
    for name in LineItem.field_names():
        print(name)