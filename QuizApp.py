# quiz_app.py

class Quiz:
    def __init__(self):
        # List of questions, each with options and the correct answer index
        self.questions = [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) H2O", "B) O2", "C) CO2", "D) NaCl"],
                "answer": "A"
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Nikola Tesla"],
                "answer": "B"
            },
            {
                "question": "Which planet is closest to the sun?",
                "options": ["A) Earth", "B) Venus", "C) Mercury", "D) Mars"],
                "answer": "C"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark"],
                "answer": "B"
            },
            {
                "question": "How many continents are there on Earth?",
                "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
                "answer": "C"
            }
        ]

        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz App!")
        print("Answer the following questions by typing the correct option (A, B, C, or D).")

        # Loop through each question
        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question['question']}")
            for option in question["options"]:
                print(option)

            # Get the user's answer
            user_answer = input("Your answer (A, B, C, D): ").strip().upper()

            # Check if the answer is correct
            if user_answer == question["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer was {question['answer']}")

        # Display the final score
        self.show_score()

    def show_score(self):
        print(f"\nQuiz Over! Your final score is: {self.score}/{len(self.questions)}")


# Run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
