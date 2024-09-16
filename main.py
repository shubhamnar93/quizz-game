from data import question_data
from question_model import Question
from quiz_brain import Quizz


question_bank=[]
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))
m= Quizz(question_bank)
while m.still_have_question():
    m.asking_question()

print("you have completed the quizz")
print(f"your final score was: {m.score}/{m.question_number}")