class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("What is 2 + 2? ", "4"),
    Question("What is the largest mammal? ", "Blue whale"),
    Question("Which planet is known as the Red Planet? ", "Mars")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question.answer}.")
    
    print(f"You got {score} out of {len(questions)} questions correct!")

if __name__ == "__main__":
    run_quiz(questions)
