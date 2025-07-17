import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r' \d+\.\d+ | \d+ '
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match.strip())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

if __name__ == "__main__":
    text = ("Загальний дохід працівника складається з декількох частин: "
            " 1000.01 як основний дохід, доповнений додатковими надходженнями "
            " 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  

