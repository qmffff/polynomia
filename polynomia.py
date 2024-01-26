class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


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


poly = Add(
    Sub(
        Mul(
            Int(3),
            Div(X(), Int(2))
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
