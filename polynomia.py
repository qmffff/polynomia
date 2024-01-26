class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, value):
        return value


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, value):
        return self.i


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Mul):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)

        if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, Div):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)

        return left + " / " + right

    def evaluate(self, value):
        denominator = self.p2.evaluate(value)
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return self.p1.evaluate(value) / denominator


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Mul):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)

        if isinstance(self.p2, Add) or isinstance(self.p2, Mul):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)

        return left + " - " + right

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Div)):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Div)):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)

        return left + " * " + right

    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)


poly = Add(
    Sub(
        Mul(
            Int(3),
            Div(X(), X())
        ),
        Int(5)
    ),
    Mul(
        Int(4),
        Add(
            X(),
            Div(
                Mul(X(), X()),
                Int(3)
            )
        )
    )
)

print(poly)

for x_value in [-1, 0, 1, 2]:
    try:
        result = poly.evaluate(x_value)
        print(f"poly.evaluate({x_value}) = {result}")
    except ZeroDivisionError as e:
        print(f"Error evaluating poly at X = {x_value}: {e}")
