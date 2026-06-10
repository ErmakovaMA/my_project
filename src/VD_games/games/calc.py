"""Игра «Калькулятор»."""
import random
from VD_games.games.engine import run_game

def generate_question() -> tuple[str, str]:
    """Генерирует случайное выражение и правильный ответ."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    else:  # operation == '*'
        result = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    return question, str(result)

def main():
    game_description = "What is the result of the expression?"
    run_game(generate_question, game_description)

if __name__ == "__main__":
    main()
