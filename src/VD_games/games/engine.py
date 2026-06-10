"""Движок для запуска игр."""
from VD_games.cli import welcome_user

ROUNDS_TO_WIN = 3

def run_game(get_question_and_answer, game_description: str) -> None:
    """Запускает игру.
    
    Args:
        get_question_and_answer: функция, возвращающая (question, correct_answer)
        game_description: описание правил игры
    """
    print("Welcome to the VD-games!")
    name = welcome_user()
    print(game_description)
    
    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = get_question_and_answer()
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
