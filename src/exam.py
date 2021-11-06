from enum import IntEnum
from random import choice
from random import randint
from sys import maxsize

from calculator import Calculator

MIN_INT: int = -maxsize - 1
MAX_INT: int = maxsize


class SimpleOperations:
    MIN: int = 2
    MAX: int = 9
    DESCRIPTION: str = "simple operations with numbers 2-9"


class IntegralSquares:
    MIN: int = 11
    MAX: int = 29
    EXPONENT: int = 2
    DESCRIPTION: str = "integral squares with numbers 11-29"


class Level(IntEnum):
    SIMPLE_OPERATIONS = 1
    INTEGRAL_SQUARES = 2


class ArithmeticExam:
    OPERATIONS = {
        "+": Calculator.add,
        "-": Calculator.subtract,
        "*": Calculator.multiply,
        # "/": Calculator.divide,
        # "%": Calculator.modulus,
        # "**": Calculator.exponentiate,
    }
    LEVEL_MESSAGE = ("Which level do you want? Enter a number:\n"
                     "1 - simple operations with numbers 2-9\n"
                     "2 - integral squared of 11-29\n")
    MAX_TASKS = 5

    def __init__(self) -> None:
        self.marks = 0

    @staticmethod
    def get_random_number(min_: int, max_: int) -> int:
        return randint(min_, max_)

    @staticmethod
    def get_user_answer(min_: int = MIN_INT, max_: int = MAX_INT, message: str = "") -> int:
        while True:
            try:
                answer = int(input(message))
                if not min_ <= answer <= max_:
                    raise ValueError
                return answer
            except ValueError:
                print("Incorrect format.")

    def generate_expression(self) -> tuple[str, int]:
        operation = choice(list(self.OPERATIONS.keys()))
        left_operand = self.get_random_number(min_=SimpleOperations.MIN,
                                              max_=SimpleOperations.MAX)
        right_operand = self.get_random_number(min_=SimpleOperations.MIN,
                                               max_=SimpleOperations.MAX)
        result = self.OPERATIONS[operation](left_operand, right_operand)
        return f"{left_operand} {operation} {right_operand}", result

    def simple_operations(self) -> None:
        for _ in range(self.MAX_TASKS):
            expression, result = self.generate_expression()
            print(expression)
            answer = self.get_user_answer()
            self.evaluate_answer(answer, result)

    def integral_squares(self) -> None:
        for _ in range(self.MAX_TASKS):
            random_base = self.get_random_number(min_=IntegralSquares.MIN,
                                                 max_=IntegralSquares.MAX)
            print(random_base)
            result = Calculator.exponentiate(base=random_base,
                                             exponent=IntegralSquares.EXPONENT)
            answer = self.get_user_answer()
            self.evaluate_answer(answer, result)

    def evaluate_answer(self, answer: int, result: int) -> None:
        if answer == result:
            self.marks += 1
            print("Right!")
        else:
            print("Wrong!")

    def select_level(self, level: int) -> None:
        if level == Level.SIMPLE_OPERATIONS:
            self.simple_operations()
        elif level == Level.INTEGRAL_SQUARES:
            self.integral_squares()

    def display_results(self, level: int) -> None:
        result = f"{self.marks}/{self.MAX_TASKS}"
        print(f"Your mark is {result}. Would you like to save the result? Enter yes or no.")
        if input().lower() in ["yes", "y"]:
            self.save_result_to_file(result, level, self.get_level_description(level))

    @staticmethod
    def get_level_description(level: int) -> str:
        return SimpleOperations.DESCRIPTION if level == 1 else IntegralSquares.DESCRIPTION

    @staticmethod
    def save_result_to_file(result: str, level: int, description: str) -> None:
        name = input("What is your name?\n")
        filename = "results.txt"

        with open(filename, "a", encoding="utf-8") as file_out:
            file_out.write(f"{name}: {result} in level {level} ({description})\n")

        print(f'The results are saved in "{filename}".')

    def run(self) -> None:
        level = self.get_user_answer(min_=1, max_=2, message=self.LEVEL_MESSAGE)
        self.select_level(level)
        self.display_results(level)
