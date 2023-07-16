from question_model import Question
from data import question_data, question_data2
from quiz_brain import QuizBrain


question_bank = []


for question in question_data2:
    # question_text = question['text']
    # question_answer = question['answer']
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations for complete our quiz!!!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

