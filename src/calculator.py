class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> int:
        return a / b if b != 0 else 0

    @staticmethod
    def modulus(a: int, b: int) -> int:
        return a % b

    @staticmethod
    def exponentiate(base: int, exponent: int) -> int:
        return base ** exponent
