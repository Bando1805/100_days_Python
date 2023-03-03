from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'],question_data[i]['correct_answer']))
        
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('\n')
print('You have completed the quiz!')
print(f'Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}')

