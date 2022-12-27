#[ Arquivo crud.py]
# Aqui contem a aplicação e suas funcionalidades como (inserir, excluir, alterar e buscar)
# ----------------------------------------------------------------------------------------

#[Importações]-------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
#---------------------------------------------------------------

#[Classe onde contém a interface da aplicação e algumas funcionalidades]
class Crud:
    def __init__(self):
        # Janela principal do Crud ----------------------------------
        self.janela_crud = Tk()
        self.janela_crud.title('CRUD - JORGE STÉFANO')
        self.janela_crud.geometry('1200x700+160+40')
        self.janela_crud.configure(bg='#002A43')
        self.janela_crud.minsize(width = 1200, height = 700)
        self.janela_crud.maxsize(width = 1200, height =700)
        self.janela_crud.resizable(width=False, height=False)
        self.icone = PhotoImage(file ='imagens\engrenagem.png')
        self.janela_crud.iconphoto(False, self.icone)

        # Frame Lateral(onde ficam os botões das funcionalidades do crud) -----------------------------------------------------------------
        self.frame_lateral = Frame(self.janela_crud, width=250, height=700, bg='#CFCFCF')
        self.frame_lateral.place(x=0, y=0)

        self.frame_principal = Frame(self.janela_crud, width=910, height=660, bg='white')     


        # Imagem Logo ---------------------------------------------------
        imagem = PhotoImage(file=r"D:\Projetos\Novo CRUD\imagens\engrenagem.png")
        self.label_logo = Label(self.janela_crud, image=imagem, bg='#CFCFCF')
        self.label_logo.place(x=50, y=10)

            

        # [funcões do CRUD] ------------
        
        # Inserir ----------------------
        def inserir_cliente():
            "Contém Labels, Entries e funções para Cadastro de novo cliente"

            # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar]   
            for widget in self.frame_principal.winfo_children():
                widget.destroy()

            #[monta o frame principal]
            self.frame_principal.place(x=270, y=20)

            # [Labels e Entrys do Frame Inserir] ---------------------
            label_titulo = Label(self.frame_principal, text='CADASTRO DE CLIENTE', font=('Helvetica', 17), bg='#002A43', fg='white', width=50, height=2)
            label_titulo.place(x=130, y=70)

            label_cpf = Label(self.frame_principal, text='CPF:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_cpf.place(x=250, y=210)
            entry_cpf = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_cpf.place(x=330, y=210)

            label_nome = Label(self.frame_principal, text='Nome:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_nome.place(x=250, y=260)
            entry_nome = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_nome.place(x=330, y=260)

            label_email = Label(self.frame_principal, text='Email:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_email.place(x=250, y=310)
            entry_email = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_email.place(x=330, y=310)

            label_telefone = Label(self.frame_principal, text='Telefone:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_telefone.place(x=250, y=360)
            entry_telefone = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_telefone.place(x=330, y=360)

            #[Captura todos os dados digitados no formulário(Entry) e limpa após clicar no botão cadastrar]
            def insere_bd():
                '''Cria um novo cliente no Banco de Dados'''
                cpf = entry_cpf.get()
                nome = entry_nome.get()
                email = entry_email.get()
                telefone = entry_telefone.get()
                #inserir(cpf, nome, email, telefone)

                # [Faz a conexão com o Banco de dados] 
                conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'crud')

                # [Cria um novo cliente no Banco de Dados. Se der algum erro, mostra, desfaz as alterações feitas no bd e fecha conexao]
                try:    
                    cursor = conexao.cursor()
                    sql = "INSERT INTO cliente (cpf, nome, email, telefone) VALUES (%s,%s,%s,%s); "
                    cursor.execute(sql, (cpf, nome, email, telefone))
                    conexao.commit()
                    messagebox.showinfo(title='Banco de Dados', message='Cliente inserido com sucesso!')
                except mysql.connector.Error as erro:
                    messagebox.showerror(title='Banco de Dados', message='Erro ao inserir cliente')
                    conexao.rollback()
                conexao.close()     
                limpar()

            #[Limpar o formulário(Entry), após clicar no botão limpar]
            def limpar():
                entry_cpf.delete(0, 'end')
                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')

        

            #[Botões] ---------------------------------------------------
            botao_cadastrar = Button(self.frame_principal, text='Cadastrar', bg='#002A43', fg='white', font=('Helvetica', 12), width=17, command=insere_bd)
            botao_cadastrar.place(x=255, y=470)

            botao_limpar = Button(self.frame_principal, text='Limpar', bg='#002A43', fg='white', font=('Helvetica', 12), width=17, command=limpar)
            botao_limpar.place(x=500, y=470)

         # Alterar ----------------------
        def alterar_cliente():         
            '''Monta novo frame com labels, entries e função de captura de dados para a função Alterar dados de cliente'''

             # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar e monta o frame principal]            
            for widget in self.frame_principal.winfo_children():
                widget.destroy()

            #[monta o frame principal]
            self.frame_principal.place(x=270, y=20)

            # [Labels e Entrys do Frame alterar] ---------------------
            label_titulo = Label(self.frame_principal, text='ALTERAR DADOS DO CLIENTE', font=('Helvetica', 17), bg='#002A43', fg='white', width=50, height=2)
            label_titulo.place(x=130, y=70)

            label_cpf = Label(self.frame_principal, text='CPF:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_cpf.place(x=250, y=210)
            entry_cpf = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_cpf.place(x=330, y=210)

            label_nome = Label(self.frame_principal, text='Nome:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_nome.place(x=250, y=260)
            entry_nome = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_nome.place(x=330, y=260)

            label_email = Label(self.frame_principal, text='Email:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_email.place(x=250, y=310)
            entry_email = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_email.place(x=330, y=310)

            label_telefone = Label(self.frame_principal, text='Telefone:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_telefone.place(x=250, y=360)
            entry_telefone = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_telefone.place(x=330, y=360)


            #[Limpar o formulário(Entry), após clicar no botão limpar]
            def limpar():
                entry_cpf.delete(0, 'end')
                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')

            #[Captura todos os dados digitados no formulário(Entry) e limpa após clicar no botão cadastrar]
            def alterar_bd():
                ''' Atualiza dados do cliente do Banco de Dados '''
                cpf = entry_cpf.get()
                nome = entry_nome.get()
                email = entry_email.get()
                telefone = entry_telefone.get()
                
                #[Faz a conexão com o banco de dados]
                conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'crud')

                #[Faz a listagem de todos os clientes. Caso algo de errado, mostra o erro]
                try:
                    cursor = conexao.cursor()
                    sql = 'UPDATE cliente set nome = %s, email = %s, telefone = %s WHERE cpf = %s;'
                    cursor.execute(sql, (nome, email, telefone, cpf))
                    conexao.commit()
                    messagebox.showinfo(title='Banco de Dados', message='Dados alterados com sucesso!')
                except mysql.connector.Error as erro:
                    messagebox.showerror(title='Banco de Dados', message='Erro: Não foi possível alterar os dados!')
                    conexao.rollback()
                conexao.close()
                limpar()

        
            #[Botões] ---------------------------------------------------
            botao_alterar = Button(self.frame_principal, text='Alterar', bg='#002A43', fg='white', font=('Helvetica', 12), width=17, command=alterar_bd)
            botao_alterar.place(x=255, y=470)

            botao_limpar = Button(self.frame_principal, text='Limpar', bg='#002A43', fg='white', font=('Helvetica', 12), width=17, command=limpar)
            botao_limpar.place(x=500, y=470)

        # Buscar ----------------------
        def buscar_cliente():            
            '''Monta novo frame com labels, entrie e função de captura de dados para a função Buscar cliente''' 

            # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar e monta o frame principal]   
            for widget in self.frame_principal.winfo_children():
                widget.destroy()

            #[monta o frame principal]
            self.frame_principal.place(x=270, y=20)

            # [Labels e Entrys do Frame Inserir] ---------------------
            label_titulo = Label(self.frame_principal, text='BUSCAR CLIENTE', font=('Helvetica', 17), bg='#002A43', fg='white', width=50, height=2)
            label_titulo.place(x=130, y=100)

            label_cpf = Label(self.frame_principal, text='CPF:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_cpf.place(x=180, y=240)
            entry_cpf = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_cpf.place(x=230, y=240)


            def buscar_bd():
                '''Conecta ao Banco de Dados e traz resultados para inserir na Treeview'''
                cpf = entry_cpf.get()

                # Labes que mostrarão os resultados da busca pelo cpf do cliente
                global label_resultado_cpf, label_resultado_nome, label_resultado_email, label_resultado_telefone
                label_resultado_cpf = Label(self.frame_principal, font=('Helvetica', 12), bg='white', fg='#002A43', text='')
                label_resultado_cpf.place(x=230, y=320)
                label_resultado_nome = Label(self.frame_principal, font=('Helvetica', 12), bg='white', fg='#002A43', text='')
                label_resultado_nome.place(x=230, y=360)
                label_resultado_email = Label(self.frame_principal, font=('Helvetica', 12), bg='white', fg='#002A43', text='')
                label_resultado_email.place(x=230, y=400)
                label_resultado_telefone = Label(self.frame_principal, font=('Helvetica', 12), bg='white', fg='#002A43', text='')
                label_resultado_telefone.place(x=230, y=440)
                
               
                # Conecta ao Banco de dados e traz o resultado referente ao cpf digitado
                conexao = mysql.connector.connect(host = 'localhost', user='root', password = '', database='crud')
                cursor = conexao.cursor()
                sql = 'SELECT * FROM cliente WHERE cpf = %s;'
                cursor.execute(sql,(cpf,))
                resultado = cursor.fetchall()
                for resp in resultado:
                    recebido = (resp[0], resp[1], resp[2], resp[3])
                    label_resultado_cpf['text']=(f'CPF: {recebido[0]}')
                    label_resultado_nome['text']=(f'Nome: {recebido[1]}')
                    label_resultado_email['text']=(f'Email: {recebido[2]}')
                    label_resultado_telefone['text']=(f'Telefone: {recebido[3]}')

                
                #[Limpar o formulário(Entry), após clicar no botão buscar]
                entry_cpf.delete(0, 'end')

            def limpar_busca():
                label_resultado_cpf['text']=''
                label_resultado_nome['text']=''
                label_resultado_email['text']=''
                label_resultado_telefone['text']=''

                

            #[Botão Bucar] ---------------------------------------------------
            botao_buscar = Button(self.frame_principal, text='Buscar', bg='#002A43', fg='white', font=('Helvetica', 11), width=10, command=buscar_bd)
            botao_buscar.place(x=580, y=237)

            #[Botão Limpar] ---------------------------------------------------
            botao_limpar_busca = Button(self.frame_principal, text='Limpar', bg='#8B0000', fg='white', font=('Helvetica', 11), width=10, command=limpar_busca)
            botao_limpar_busca.place(x=685, y=237)
  
        # Listar ----------------------
        def listar_clientes():
            '''Monta novo frame com label e treeview para mostrar todos os clientes cadastrados'''

            # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar e monta o frame principal]   
            for widget in self.frame_principal.winfo_children():
                widget.destroy()

            #[monta o frame principal]
            self.frame_principal.place(x=270, y=20)

            # [Labels e Entrys do Frame Inserir] ---------------------
            label_titulo = Label(self.frame_principal, text='LISTAR CLIENTES', font=('Helvetica', 17), bg='#002A43', fg='white', width=50, height=2)
            label_titulo.place(x=130, y=50)
            
            # [Treeview] ------------------------------
            estilo = ttk.Style()
            #estilo.configure('Treeview.Heading', font=('Helvetica, 11'), height=11)

            # [Configurações da Treeview] -------------
            estilo.configure('Treeview',
            background = 'white',
            foreground = 'black',
            rowheight = 25,
            fieldbackground = 'white',
            font=('Helvetica', 11))

            # [Colunas Treeview]-------------------------
            columns = ('cpf', 'nome', 'email', 'telefone')

            tree = ttk.Treeview(self.frame_principal, columns = columns, show = 'headings', height = 11)

            # [Configuração de cor linhas treeview]
            tree.tag_configure('impar', background='white')
            tree.tag_configure('par', background='#B0C4DE')

            # [Nomes e tamanho das colunas]
            tree.column("cpf", width=150)
            tree.column("nome", width=290)
            tree.column("email", width=190)
            tree.column("telefone", width=145)
            
            # Cabeçalhos Treeview ----------------------------------------------------
            tree.heading('cpf', text='CPF')
            tree.heading('nome', text='Nome do Cliente')
            tree.heading('email', text='Email')
            tree.heading('telefone', text='Telefone')
            
            # Posicão Treeview ----------------------------------------------------------
            tree.place(x=75, y=180)
            
            # Inserindo Scrollbar ----------------------------------------------------
            scroll_bar = Scrollbar(self.janela_crud)
            scroll_bar.pack(side = 'right', fill = 'y')
            tree.config(yscrollcommand = scroll_bar.set)
            scroll_bar.config(command = tree.yview)

            
            # [Conecta ao Banco de Dados e traz os dados do cliente relacionado ao cpf digitado]
            conexao = mysql.connector.connect(host = 'localhost', user='root', password = '', database='crud')
            cursor = conexao.cursor()
            sql = 'SELECT * FROM cliente;'
            cursor.execute(sql)
            resultado = cursor.fetchall()
            count = 0
            for resp in resultado:
                if count % 2 == 0:
                    tree.insert('', tk.END, values=(resp[0], resp[1], resp[2], resp[3]), tags=('par'))
                else:
                    tree.insert('', tk.END, values=(resp[0], resp[1], resp[2], resp[3]), tags=('impar'))
                count += 1

        # Excluir ----------------------
        def excluir_cliente():           
            '''Monta novo frame com labes, entries e função de captura dos dados para função excluir'''

            # [Procura por widgets no frame, caso tenha, limpa o frame logo ao entrar e monta o frame principal]   
            for widget in self.frame_principal.winfo_children():
                widget.destroy()

            #[monta o frame principal]
            self.frame_principal.place(x=270, y=20)

            # [Labels e Entrys do Frame Inserir] ---------------------
            label_titulo = Label(self.frame_principal, text='EXCLUSÃO DE CLIENTE', font=('Helvetica', 17), bg='#002A43', fg='white', width=50, height=2)
            label_titulo.place(x=130, y=200)

            label_cpf = Label(self.frame_principal, text='CPF:', font=('Helvetica', 12), bg='white', fg='#002A43')
            label_cpf.place(x=180, y=350)
            entry_cpf = Entry(self.frame_principal, width=36, font=('Helvetica', 12), border=2)
            entry_cpf.place(x=230, y=350)

            def excluir_bd():
                ''' Excluir cliente do Banco de Dados a partir do CPF'''
                # captura cpf digitado na entry
                cpf = entry_cpf.get()
                
                #[Conexão com o Banco de Dados]
                conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'crud')
                #[Tenta excluir o cliente caso der erro, mostra]
                try:     
                    cursor = conexao.cursor()
                    sql = "DELETE FROM cliente WHERE cpf = %s;"
                    cursor.execute(sql, (cpf,))
                    conexao.commit()
                    messagebox.showinfo(title='Banco de Dados', message='Cliente excluído com sucesso!')
                except mysql.connector.Error as erro:
                    messagebox.showerror(title='Banco de Dados', message='Erro: Não foi possível excluir o cliente!')
                    conexao.rollback()
                conexao.close()    
                
                #[Limpar o formulário(Entry), após clicar no botão limpar]
                entry_cpf.delete(0, 'end')

               
            #[Botão] ---------------------------------------------------
            botao_excluir = Button(self.frame_principal, text='Excluir', bg='#8B0000', fg='white', font=('Helvetica', 11), width=17, command=excluir_bd)
            botao_excluir.place(x=590, y=346)

 
        # Botões do CRUD ------------------------------------------------------------------
        self.botao_inserir = Button(self.frame_lateral, width=20, height=2, bg='#002A43', fg='white', text='Inserir', font=('Helvetica', 15), command=inserir_cliente)
        self.botao_inserir.place(x=10, y=180)

        self.botao_alterar = Button(self.frame_lateral, width=20, height=2, bg='#002A43', fg='white', text='Alterar', font=('Helvetica', 15), command=alterar_cliente)
        self.botao_alterar.place(x=10, y=260)

        self.botao_buscar = Button(self.frame_lateral, width=20, height=2, bg='#002A43', fg='white', text='Buscar', font=('Helvetica', 15), command=buscar_cliente)
        self.botao_buscar.place(x=10, y=340)

        self.botao_listar = Button(self.frame_lateral, width=20, height=2, bg='#002A43', fg='white', text='Listar', font=('Helvetica', 15), command=listar_clientes)
        self.botao_listar.place(x=10, y=420)

        self.botao_excluir = Button(self.frame_lateral, width=20, height=2, bg='#8B0000', fg='white', text='Excluir', font=('Helvetica', 15), command=excluir_cliente)
        self.botao_excluir.place(x=10, y=500)

       
        self.janela_crud.mainloop()

if __name__ == '__main__':
    app = Crud()