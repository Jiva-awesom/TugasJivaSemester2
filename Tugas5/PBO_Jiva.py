class segitilu:
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def gL(self):
        return 0.5 * self.a * self.t

segitilu1 = segitilu(8, 66)
segitilu2 = segitilu(8967, 8)

print(f"luas dsefgititiga: {segitilu1.gL()}")
print(f"luas dsefgititiga: {segitilu2.gL()}")