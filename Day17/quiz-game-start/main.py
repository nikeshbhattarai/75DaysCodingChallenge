from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data["results"]:
    que = Question(q_data["question"], q_data["correct_answer"])
    question_bank.append(que)

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")
