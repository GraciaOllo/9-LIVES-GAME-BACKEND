import sqlite3
from models.quiz import QuizModel


class QuizController:
    @staticmethod
    def get_all_quizzes():
        return QuizModel().read()

    @staticmethod
    def get_quiz_with_id(quiz_id):
        return QuizModel().readById(quiz_id)

    @staticmethod
    def save_quiz(id_category, question, option1, option2, option3, option4, correct_answer, quiz_id=None):
        if quiz_id is not None:
            quiz = QuizController.get_quiz_with_id(quiz_id)
            quiz.id_category = id_category
            quiz.question = question
            quiz.option1 = option1
            quiz.option2 = option2
            quiz.option3 = option3
            quiz.option4 = option4
            quiz.correct_answer = correct_answer
        else:
            quiz = QuizModel(id_category=id_category, question=question, option1=option1, option2=option2, option3=option3, option4=option4, correct_answer=correct_answer)

        quiz.create()
        return quiz

    @staticmethod
    def delete_quiz(quiz_id):
        QuizModel().deleteById(quiz_id)
        return "Quiz deleted successfully."