from data import Dados
from uistart import UiStart
from question_model import Question


class CriaLista:
    def __init__(self):
        inicio = UiStart()
        banco_dados = Dados(inicio.nq, inicio.parametro_cat)

        self.banco_quest = []

        for questao in banco_dados.dados_questao:
            q_texto = questao["question"]
            q_resp = questao["correct_answer"]
            nova_quest = Question(q_texto, q_resp)
            self.banco_quest.append(nova_quest)

