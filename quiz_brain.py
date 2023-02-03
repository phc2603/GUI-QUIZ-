import html


class QuizBrain:

    def __init__(self, q_list):
        self.numero_questoes = 0
        self.score = 0
        self.lista_quest = q_list
        self.questao_atual = None

    def ainda_tem_questoes(self):
        return self.numero_questoes < len(self.lista_quest)

    def proxima_questao(self):
        self.questao_atual = self.lista_quest[self.numero_questoes]
        q_txt = html.unescape(self.questao_atual.text)
        self.numero_questoes += 1
        texto_final = f"Q.{self.numero_questoes}: {q_txt} (True/False): "
        return texto_final

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.questao_atual.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

