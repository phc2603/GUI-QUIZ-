import tkinter
from tkinter import ttk
from tkinter import messagebox


class UiStart:
    def __init__(self):
        self.parametro_cat = 0
        self.nq = 0
        self.tela = tkinter.Tk()
        self.tela.geometry("600x400")
        self.tela.config(padx=5, pady=5, bg="#375362")
        self.tela.title("Setup")
        self.titulo_quest = tkinter.Label(text='Numero de questões', font=('Arial', 10, 'bold'))
        self.numero_quest = ttk.Combobox(values=['10', '15', '20', '25', '30'])
        self.titulo_quest.grid(row=0, column=0)
        self.numero_quest.grid(row=1, column=0, padx=40, pady=10)

        self.categoria = ttk.Combobox(values=['Conhecimentos Gerais(General Knowledge)', 'Filmes (Films)',
                                              'Computação(Computers)', 'Video Games(Games)', 'Geografia(Geography)',
                                              'Musica(Music)', 'Qualquer Categoria(Any Category)', ], width=40)
        self.categoria.grid(row=1, column=1)
        self.titulo_categoria = tkinter.Label(text="Categoria", font=('Arial', 10, 'bold'))
        self.titulo_categoria.grid(row=0, column=1)

        self.botao_start = tkinter.Button(text='Start', font=('Arial', 20, 'bold'), fg='#0000FF', bg='#CCFFFF',
                                          width=15, command=self.preencheutudo)
        self.botao_start.grid(row=2, column=1, columnspan=2, pady=250)

        self.tela.mainloop()

    def preencheutudo(self):
        if len(self.categoria.get()) == 0 or len(self.numero_quest.get()) == 0:
            messagebox.showerror(title='Erro', message='Favor, escolher todos os valores')
        else:
            self.nq = int(self.numero_quest.get())
            if self.categoria.get() == 'Conhecimentos Gerais(General Knowledge)':
                self.parametro_cat = 9
            elif self.categoria.get() == 'Filmes (Films)':
                self.parametro_cat = 11
            elif self.categoria.get() == 'Computação(Computers)':
                self.parametro_cat = 18
            elif self.categoria.get() == 'Video Games(Games)':
                self.parametro_cat = 15
            elif self.categoria.get() == 'Qualquer Categoria(Any Category)':
                self.parametro_cat = 0
            elif self.categoria.get() == 'Musica(Music)':
                self.parametro_cat = 12
            else:
                self.parametro_cat = 22
            self.tela.destroy()