import random
import time

class Quiz:
    def __init__(self) -> None:
        self.questions = [
            "What is the most common activation function used in neural networks?",
            "Which algorithm is often used for training deep learning models on large datasets?",
            "What is the primary goal of natural language processing (NLP)?",
            "What is the term used to describe a type of AI that can understand, interpret, and generate human-like text?",
            "What is the process of adjusting the weights and biases of a neural network during training to minimize errors?"
        ]

        self.answers = [
            ["ReLU (Rectified Linear Unit)", "Sigmoid", "Tanh", "Linear"],  # Correct: ReLU (Rectified Linear Unit)
            ["Backpropagation", "Gradient Descent", "Random Forest", "K-Means"],  # Correct: Backpropagation
            ["To enable computers to understand and process human language", "To design intelligent agents that mimic human behavior", "To generate random text for creative writing", "To classify images in computer vision tasks"],  # Correct: To enable computers to understand and process human language
            ["Natural Language Generation (NLG)", "Chatbot", "Transformer", "GPT (Generative Pre-trained Transformer)"],  # Correct: GPT (Generative Pre-trained Transformer)
            ["Gradient Descent", "Backpropagation", "Stochastic Gradient Descent (SGD)", "Adam Optimizer"],  # Correct: Backpropagation
        ]

        self.correct_choice = [0, 0, 0, 3, 1]
        self.total_time = 0  # To store the total time spent

    def exam_question(self, question, choices, time_limit=10):
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        start_time = time.time()
        try:
            user_choice = int(input("Your Time is 10 sec for each Question\nEnter your choice between 1 and 4. If you want to exit, press 5: "))

            # For Count Total Time
            elapsed_time = time.time() - start_time
            self.total_time += elapsed_time 

            if elapsed_time > time_limit:
                print(f"Time's up!. \nYou took {elapsed_time:.2f} seconds to answer the question.")
                return None
            
            # if user want to exit
            if user_choice == 5:
                print("Thanks for playing!")
                exit()
                
            elif user_choice < 1 or user_choice > len(choices):
                raise ValueError("Please enter a number between 1 and 4.")
            return user_choice - 1
        except ValueError as e:
            print(e)
            return self.exam_question(question, choices)

    def lets_play_the_game(self):
        print("Welcome to the interview board! ")
        score = 0
        for i in range(len(self.questions)):
            print(f"\nQuestion {i+1}:")
            user_choice = self.exam_question(self.questions[i], self.answers[i])
            if user_choice == self.correct_choice[i]:
                print("Correct!")
                print(f"The correct answer is: {self.answers[i][self.correct_choice[i]]}")
                score += 1
            else:
                print("Oops! That's incorrect. Better Luck next time")
        print(f"\nYou got {score} out of {len(self.questions)} questions correct.")
        print(f"Total time spent: {self.total_time:.2f} seconds.")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.lets_play_the_game()
