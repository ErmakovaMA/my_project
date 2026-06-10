"""Игра «Простое ли число?»."""
import random
import math
from VD_games.games.engine import run_game

def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_question() -> tuple[str, str]:
    """Генерирует случайное число и правильный ответ (yes/no)."""
    number = random.randint(1, 100)
    answer = "yes" if is_prime(number) else "no"
    return str(number), answer

def main():
    game_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_question, game_description)

if __name__ == "__main__":
    main()
