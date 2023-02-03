import tkinter
from quiz_brain import QuizBrain
from crialista import CriaLista

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.qb = quiz_brain
        self.tela = tkinter.Tk()
        self.tela.config(padx=20, pady=20, bg=THEME_COLOR)
        self.tela.title("Quiz")
        #label pontuacao
        self.pontuacao = tkinter.Label(text='Score: 0', font=('Arial', 15, 'bold'), fg='white', bg=THEME_COLOR, highlightthickness=0)
        self.pontuacao.grid(row=0, column=1)
        #criando o canvas central
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.texto_questao = self.canvas.create_text(150, 125, text='teste', font=('Arial', 20, 'italic'), fill=THEME_COLOR, width=280)#width é para caber a questao na tela, para que ela se realinha com base no width do canvas
        self.canvas.grid(row=1, column=0, columnspan=2)
        #botao V
        imagem_v = tkinter.PhotoImage(file='images/true.png')
        self.botaoV = tkinter.Button(image=imagem_v, highlightthickness=0, command=lambda: self.checka_resposta(1))
        self.botaoV.grid(row=2, column=0, pady=50)
        #botao X
        imagem_x = tkinter.PhotoImage(file='images/false.png')
        self.botaoX = tkinter.Button(image=imagem_x, highlightthickness=0, command=lambda: self.checka_resposta(2))
        self.botaoX.grid(row=2, column=1)

        self.pega_proxima_questao()

        self.tela.mainloop()

    def pega_proxima_questao(self):
        self.canvas.config(bg='white')
        if self.qb.ainda_tem_questoes():
            txt_questao = self.qb.proxima_questao()
            self.canvas.itemconfig(self.texto_questao, text=txt_questao)
        else:
            self.canvas.itemconfig(self.texto_questao, text=f'Fim do Quiz!\nPontuacao Final: {self.qb.score}')
            self.botaoX['state'] = 'disabled'
            self.botaoV['state'] = 'disabled'
            botao_reset = tkinter.Button(text="Reset", highlightthickness=0, width=30, bg='green', command=self.reset)
            botao_reset.grid(row=3, column=0, columnspan=2)

    def checka_resposta(self, bt):
        if bt == 1:
            self.feedback(self.qb.check_answer('true'))
        else:
            self.feedback(self.qb.check_answer('false'))

    def feedback(self, resp):
        if resp:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.texto_questao, text=f'Score: {self.qb.score}')
            self.pontuacao.config(text=f'Score: {self.qb.score}')
        else:
            self.canvas.config(bg='red')
        self.tela.after(1000, self.pega_proxima_questao)

    def reset(self):
        self.tela.destroy()
        x = CriaLista()
        quiz = QuizBrain(x.banco_quest)
        self.__init__(quiz)
