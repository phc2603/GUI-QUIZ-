from quiz_brain import QuizBrain
from ui import QuizUI
from crialista import CriaLista


cria = CriaLista()
quiz = QuizBrain(cria.banco_quest)
QuizUI(quiz)

