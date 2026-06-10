"""Игра «Наибольший общий делитель (НОД)»."""
import random
import math
from VD_games.games.engine import run_game

def generate_question() -> tuple[str, str]:
    """Генерирует два случайных числа и правильный ответ (НОД)."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = math.gcd(num1, num2)
    
    question = f"{num1} {num2}"
    return question, str(result)

def main():
    game_description = "Find the greatest common divisor of given numbers."
    run_game(generate_question, game_description)

if __name__ == "__main__":
    main()
