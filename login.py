# Arquivo login.py
# Contém a interface e função de validação de Login
# --------------------------------------------------

# [Importações] ------------------------------------
import tkinter as tk
from tkinter import *
from crud import Crud
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
# ---------------------------------------------------

# [Classe referente a interface Login e função de validação]
class Login:
    def __init__(self):
        # Janela principal
        self.janela_login = Tk()
        self.janela_login.title('CRUD - JORGE STÉFANO')
        self.janela_login.geometry('1200x700+160+40')
        self.janela_login.configure(bg='#002A43')
        self.janela_login.minsize(width = 1200, height = 700)
        self.janela_login.maxsize(width = 1200, height =700)
        self.janela_login.resizable(width=False, height=False)
        self.icone = PhotoImage(file ='imagens\engrenagem.png')
        self.janela_login.iconphoto(False, self.icone)
        

        # Frame Geral
        self.frame_geral = Frame(self.janela_login, width=900, height=550, bg='white')
        self.frame_geral.place(x=150, y=80)
        self.frame_login = Frame(self.frame_geral, width=470, height=550, bg='#012136')
        self.frame_login.place(x=450, y=0)


        # Imagem
        imagem_login = PhotoImage(file =r"D:\Projetos\Novo CRUD\imagens\imagem.png")
        self.label_login = Label(self.frame_login, image = imagem_login)
        self.label_login.place(x=-20, y=0)
        imagem_login_2 = PhotoImage(file =r"D:\Projetos\Novo CRUD\imagens\fundo login.png")
        self.label_login2 = Label(self.frame_geral, image = imagem_login_2)
        self.label_login2.place(x=25, y=30)


        # Entr
        self.entry_usuario = Entry(self.frame_login, width = 25, font=('Helvetica', 15))
        self.entry_usuario.insert(0, "Usuário")
        self.entry_usuario.place(x=75, y=280)

        self.entry_senha = Entry(self.frame_login, width = 25, font=('Helvetica', 15))
        self.entry_senha.insert(0, "Senha")
        self.entry_senha.place(x=75, y=340)


        # Função de Validação do Login
        def validacao(event=None):
            '''Recebe usuario e senha das entries, valida o login e acessa o Crud'''
            user = self.entry_usuario.get()
            password = self.entry_senha.get()
            conexao = mysql.connector.connect(host='localhost', user='root', password='', database='crud')
            cursor = conexao.cursor()
            sql = "SELECT * FROM user where usuario = %s;"
            cursor.execute(sql,(user,))
            resultado = cursor.fetchall()
            for _, usuario, senha in resultado: 
                usuario = usuario
                senha = senha
            if (usuario == user) and (senha == password):
                self.janela_login.destroy()
                janela_crud = Crud()
            elif (usuario != user) or (senha != password):
                messagebox.showerror('Erro Login', "Usuário ou Senha incorretos")   
           
            
        # Ativa a tecla ENTER para confirmar login
        self.janela_login.bind('<Return>', validacao)
        

        # Botão ENTRAR
        self.botao_entrar = Button(self.frame_login, width =30, bg='#FFFFFF', text='Entrar', font=('Helvetica',12), fg='#012136', command=validacao)
        self.botao_entrar.place(x=75, y=420)


        def novo_usuario():
            '''Cadastra novo usuário'''
            #self.frame_login.destroy()
            self.frame_novo_usuario = Frame(self.janela_login, width=450, height=550, bg='#012136')
            self.frame_novo_usuario.place(x=600, y=80)

            self.label_cadastro_usuario = Label(self.frame_novo_usuario, text='Cadastro Novo Usuário', width=32, font=('Helvetica',14))
            self.label_cadastro_usuario.place(x=45, y=60)

            self.label_nome = Label(self.frame_novo_usuario, text='Nome:', font=('Helvetica',13), bg='#012136', fg='white')
            self.label_nome.place(x=30, y=160)
            self.entry_nome = Entry(self.frame_novo_usuario, width=32, font=('Helvetica',12))
            self.entry_nome.place(x=100, y=160)

            self.label_usuario_novoUser = Label(self.frame_novo_usuario, text='Usuário:', font=('Helvetica',13), bg='#012136', fg='white')
            self.label_usuario_novoUser.place(x=30, y=210)
            self.entry_usuario_novoUser = Entry(self.frame_novo_usuario, width=32, font=('Helvetica',12))
            self.entry_usuario_novoUser.place(x=100, y=210)

            self.label_senha_novoUser = Label(self.frame_novo_usuario, text='Senha:', font=('Helvetica',13), bg='#012136', fg='white')
            self.label_senha_novoUser.place(x=30, y=260)
            self.entry_senha_novoUser = Entry(self.frame_novo_usuario, width=32, font=('Helvetica',12))
            self.entry_senha_novoUser.place(x=100, y=260)


            def cadastro_novo(nome, usuario, senha):
                ''' Cria novo usuario no Banco de dados'''

                # [Faz conexão com o bando de dados]
                conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'crud')

                # Envia novo usuario pra o Banco de dados. Se algo der errado na operação é avisado
                try:
                    cursor = conexao.cursor()
                    sql = "INSERT INTO user (nome, usuario, senha) VALUES (%s, %s, %s);"
                    cursor.execute(sql, (nome, usuario, senha))
                    conexao.commit()
                except mysql.connector.Error as erro:
                    print("Erro na operação: ", erro)
                    conexao.rollback()
                conexao.close()


            # [Faz o envio dos dados recolhidos para a função cadastro_novo para ser enviado para o Banco de dados]
            def cadastro():
                '''Faz o envio dos dados recolhidos para a função cadastro_novo no arquivo regras_de_negocio para ser enviado para o Banco de dados'''
                nome = self.entry_nome.get()
                user = self.entry_usuario_novoUser.get()
                senha = self.entry_senha_novoUser.get()
                cadastro_novo(nome, user, senha)
                self.entry_nome.delete(0, 'end')
                self.entry_usuario_novoUser.delete(0, 'end')
                self.entry_senha_novoUser.delete(0, 'end')


            def voltar():
                '''destroi frame novo usuario'''
                # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar]   
                #for widget in self.frame_novo_usuario.winfo_children():
                   # widget.destroy()

                self.frame_novo_usuario.destroy()
                
               
                
            # [Botão Cadastrar usuário - após inserir todos os dados nas entries, confirma no botão que enviará os dados para o Banco de Dados]
            self.botao_cadastrar_usuario = Button(self.frame_novo_usuario, width=15, bg='white', fg='#012136', text='Cadastrar', font=('Helvetica',12), command=cadastro)
            self.botao_cadastrar_usuario.place(x=84, y=360)

            # [Botão Voltar a tela de login]
            self.botao_voltar = Button(self.frame_novo_usuario, width=15, bg='white', fg='#012136', text='Voltar', font=('Helvetica',12), command=voltar)
            self.botao_voltar.place(x=250, y=360)


        # [Botão que da acesso ao Frame onde contém o formulário(entries) para cadastro de novo usuário] 
        self.novo_usuario = Button(self.frame_geral, width =40, bg='#002A43', text='Criar novo usuário', font=('Helvetica',12), fg='white', command=novo_usuario)
        self.novo_usuario.place(x=43, y=422)


        self.janela_login.mainloop()


if __name__ == '__main__':
    app = Login()
        


      



