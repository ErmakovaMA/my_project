"""Игра «Арифметическая прогрессия»."""
import random
from VD_games.games.engine import run_game

def generate_progression() -> tuple[str, str]:
    """Генерирует арифметическую прогрессию с пропущенным элементом."""
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    
    # Генерируем полную прогрессию
    progression = [str(start + i * step) for i in range(length)]
    
    # Выбираем случайный индекс для пропуска
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    # Заменяем выбранный элемент на ".."
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    return question, correct_answer

def main():
    game_description = "What number is missing in the progression?"
    run_game(generate_progression, game_description)

if __name__ == "__main__":
    main()
