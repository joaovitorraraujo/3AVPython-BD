# tkinter e ctk
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# para os valores decimais funcionarem
from decimal import Decimal  # Importar a classe Decimal para lidar com valores decimais

# tkcalendar 
from tkcalendar import Calendar, DateEntry
from datetime import date

#imagem
from PIL import ImageTk,Image
from tkinter import messagebox

#matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# criptografar senhas
from cryptography.fernet import Fernet

#locale
import locale

# sair do programa
import sys

#regex
import re

# funçoes auxiliares
from functions import email_exists,user_exists,is_valid_email,format_cpf,check_cpf_format,check_real_brl,cryptography_password,decrypt_password

#funcoes do crud
from CRUD import bar_values,pie_valores,update_data_user,check_user_password_recover, delete_category,view_category_search,porcentagem_value, view_category,view_expense,view_revenue,insert_category,insert_expense,insert_revenue,insert_usuario,check_user_password,check_cpf_register,check_email_register,check_user_register,table,check_category,delete_expense,delete_revenue



class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window = self 
        self.window .title("")
        self.window .geometry("900x650")
        self.window.resizable(False, False)
        ctk.set_appearance_mode("dark")

        
        self.images = {} # Dicionário para armazenar as imagens

        self.load_images()
        self.login_screen()
    
    def load_images(self):
        # ----------------------------------------
        img_pattern = ImageTk.PhotoImage(Image.open("imagens/pattern.png"))
        self.images['pattern'] = img_pattern
        # ----------------------------------------
        img_logo = Image.open("imagens/logo.png")
        img_logo = img_logo.resize((35,35))
        img_logo = ImageTk.PhotoImage(img_logo)
        self.images['logo'] = img_logo
        # ----------------------------------------
        img_logo = Image.open("imagens/logo.png")
        img_logo = img_logo.resize((45,45))
        img_logo = ImageTk.PhotoImage(img_logo)
        self.images['logo principal'] = img_logo
        # logo welcome----------------------------
        img_logo_welcomw = Image.open("imagens/logo.png")
        img_logo_welcomw = img_logo_welcomw.resize((210,210))
        img_logo_welcomw = ImageTk.PhotoImage(img_logo_welcomw)
        self.images['logo welcome'] = img_logo_welcomw
        # ----------------------------------------
        img_home = Image.open("imagens/home.png")
        img_home = img_home.resize((45,45))
        img_home = ImageTk.PhotoImage(img_home)
        self.images['home'] = img_home
        # ----------------------------------------
        img_config = Image.open("imagens/configuracoes.png")
        img_config = img_config.resize((45,45))
        img_config = ImageTk.PhotoImage(img_config)
        self.images['config'] = img_config
        # ----------------------------------------
        img_logout = Image.open("imagens/logout.png")
        img_logout = img_logout.resize((45,45))
        img_logout = ImageTk.PhotoImage(img_logout)
        self.images['logout'] = img_logout
        # renda-----------------------------------
        img_renda = Image.open("imagens/renda.png")
        img_renda = img_renda.resize((30,30))
        img_renda = ImageTk.PhotoImage(img_renda)
        self.images['renda'] = img_renda
        # despesa-----------------------------------
        img_despesa = Image.open("imagens/despesa.png")
        img_despesa = img_despesa.resize((30,30))
        img_despesa = ImageTk.PhotoImage(img_despesa)
        self.images['despesa'] = img_despesa
        # saldo-----------------------------------
        img_saldo = Image.open("imagens/saldo.png")
        img_saldo = img_saldo.resize((30,30))
        img_saldo = ImageTk.PhotoImage(img_saldo)
        self.images['saldo'] = img_saldo
        # tabela-----------------------------------
        img_tabela = Image.open("imagens/tabela.png")
        img_tabela = img_tabela.resize((30,30))
        img_tabela = ImageTk.PhotoImage(img_tabela)
        self.images['tabela'] = img_tabela
        # adicionar-----------------------------------
        img_adicionar = Image.open("imagens/adicionar.png")
        img_adicionar = img_adicionar.resize((30,30))
        img_adicionar = ImageTk.PhotoImage(img_adicionar)
        self.images['adicionar'] = img_adicionar
        # lixeira-----------------------------------
        img_lixeira = Image.open("imagens/lixeira.png")
        img_lixeira = img_lixeira.resize((30,30))
        img_lixeira = ImageTk.PhotoImage(img_lixeira)
        self.images['lixeira'] = img_lixeira
        # user-----------------------------------
        img_user = Image.open("imagens/user.png")
        img_user = img_user.resize((30,30))
        img_user = ImageTk.PhotoImage(img_user)
        self.images['user'] = img_user
        # cpf-----------------------------------
        img_cpf = Image.open("imagens/cpf.png")
        img_cpf = img_cpf.resize((30,30))
        img_cpf = ImageTk.PhotoImage(img_cpf)
        self.images['cpf'] = img_cpf
        # password-----------------------------------
        img_password = Image.open("imagens/password.png")
        img_password = img_password.resize((30,30))
        img_password = ImageTk.PhotoImage(img_password)
        self.images['password'] = img_password
    #TELA DE LOGIN =============================================================================
    def login_screen(self):
        def move_frames_out(x, frame, final_x):
            if x < final_x:
                frame.place(x=x, rely=0.5, anchor=ctk.CENTER)
                x += 5  
                l_pattern.after(1, move_frames_out, x, frame, final_x)
            

        def move_frame_in(x, frame, final_x):
            if x > final_x:
                frame.place(x=x, rely=0.5, anchor=ctk.CENTER)
                x -= 5  
                l_pattern.after(1, move_frame_in, x, frame, final_x)
        # Utilizando a imagem 'pattern'
        l_pattern = ctk.CTkLabel(
            master=self.window, 
            image=self.images['pattern'])
        l_pattern.pack()
        
        #creating custom frame
        frame_login=ctk.CTkFrame(
            master=l_pattern, 
            width=320, 
            height=360, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_login.place(x=455, rely=0.5, anchor=ctk.CENTER)
        
        # create logo 
        app_logo = ctk.CTkLabel(
            master=frame_login,
            image=self.images['logo'],
            width=300,
            compound="left",
            text="PYMYMONEY",
            font=('Impact',20, "underline"))
        app_logo.place(x=10, y=20)
        
        l_login=ctk.CTkLabel(
            master=frame_login, 
            width=300, 
            text="FAÇA LOGIN",
            font=('Century Gothic',20))
        l_login.place(x=10, y=70)
        
        def on_enter_pressed(event):
            event.widget.tk_focusNext().focus()
            
        entry_user=ctk.CTkEntry(
            master=frame_login,
            width=220, 
            placeholder_text='E-mail',
            corner_radius=15,
            border_color="white",
            border_width=2)
        entry_user.place(x=50, y=120)
        
        entry_password=ctk.CTkEntry(
            master=frame_login, 
            width=220, 
            placeholder_text='Senha',
            show="*",
            corner_radius=15,
            border_color="white",
            border_width=2,
            )
        entry_password.place(x=50, y=165)
        
        entry_user.bind("<Return>", on_enter_pressed)
        
        view_password = ctk.BooleanVar()
        
        checkbox_view_password = ctk.CTkCheckBox(
            master=frame_login,
            width=100, 
            variable=view_password,
            text="Mostrar senha", 
            corner_radius=15,
            checkmark_color="black",
            hover_color="#302c2c",
            fg_color="white",
            border_color="white",
            border_width=2
        )
        checkbox_view_password.place(x=50,y=210)
        
        def toggle_password_visibility(*args):
            if view_password.get():
                entry_password.configure(show="")
            else:
                entry_password.configure(show="*")

        view_password.trace("w", toggle_password_visibility)
        
        def scren_forgot_password():
            global frame_forgot_password
            
            move_frames_out(455, frame_login, 1100)
            frame_login.pack_forget()
            
            frame_forgot_password = ctk.CTkFrame(
                master=l_pattern, 
                width=320, 
                height=360, 
                corner_radius=20,
                bg_color="transparent",
                border_color="black",
                border_width=2
            )
            frame_forgot_password.place(x=-320, rely=0.5, anchor=ctk.CENTER)  
            
            move_frames_out(-320, frame_forgot_password, 455)
            
            app_logo = ctk.CTkLabel(
                master=frame_forgot_password,
                image=self.images['logo'],
                width=300,
                compound="left",
                text="PYMYMONEY",
                font=('Impact',20, "underline"))
            app_logo.place(x=10, y=20)
            
            l_forgot_password=ctk.CTkLabel(
                master=frame_forgot_password, 
                width=300, 
                text="PERDEU SUA SENHA?\nNÃO SE PREOCUPE!",
                font=('Century Gothic',20))
            l_forgot_password.place(x=10, y=70)
            
            e_user_recover = ctk.CTkEntry(
                master=frame_forgot_password,
                width=220, 
                placeholder_text='Nome Completo(Registrado)',
                corner_radius=15,
                border_color="white",
                border_width=2)
            e_user_recover.place(x=50, y=130)
            
            e_cpf_recover = ctk.CTkEntry(
                master=frame_forgot_password, 
                width=220, 
                placeholder_text='CPF(Registrado)',
                corner_radius=15,
                border_color="white",
                border_width=2)
            e_cpf_recover.place(x=50, y=165)
            e_cpf_recover.bind("<FocusOut>", format_cpf)
            
            e_email_recover = ctk.CTkEntry(
                master=frame_forgot_password, 
                width=220, 
                placeholder_text='E-mail(Registrado)',
                corner_radius=15,
                border_color="white",
                border_width=2)
            e_email_recover.place(x=50, y=200)
            
            
            e_user_recover.bind("<Return>", on_enter_pressed)
            e_cpf_recover.bind("<Return>", on_enter_pressed)
            e_email_recover.bind("<Return>", on_enter_pressed)
            
            l_password=ctk.CTkLabel(
                master=frame_forgot_password, 
                width=1, 
                height=1,
                text="Sua senha: *****",
                font=('Arial 20',17))
            
            l_password.place(x=50, y=310)
            
            def back_login():
                    move_frame_in(455, frame_forgot_password, -320)                                        
                    move_frame_in(1100, frame_login, 450)      
                    def time_to_destroy():
                        frame_forgot_password.destroy()
                    frame_forgot_password.after(1000,time_to_destroy)                                 
            
            def recover():
                recover_name = e_user_recover.get()
                recover_cpf = e_cpf_recover.get()
                recover_email = e_email_recover.get()
                
                e_check_recover = check_user_password_recover(recover_name,recover_cpf,recover_email)
                
                if e_check_recover:
                    password_recover = e_check_recover[4]
                                       
                    l_password.configure(text=f"Sua senha:{password_recover}")
                    
                    CTkMessagebox(title="Info", icon="check", message="Senha recuperada com sucesso!", sound=1)
                                                              
                else:
                    CTkMessagebox(title="Info", icon="cancel", message="Usuário não encontrado!", sound=1)
                

            button_recover = ctk.CTkButton(
                master=frame_forgot_password, 
                width=220,
                text="Recuperar",
                text_color="black", 
                fg_color="white",
                hover_color="#d1c7c7",
                corner_radius=15,
                command=recover)
            button_recover.place(x=50, y=235)
            
            button_back = ctk.CTkButton(
                master=frame_forgot_password, 
                width=220, 
                text="Voltar", 
                text_color="white", 
                fg_color="transparent",
                hover_color="#757272",
                border_color="white",
                border_width=2,
                corner_radius=15,
                command=back_login
                )
            button_back.place(x=50, y=270)
            
        
        button_forgot_password = ctk.CTkButton(
            master=frame_login,
            text="Esqueci a senha",
            width=100,
            font=("Roboto", 11, "underline"),
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=scren_forgot_password
        )
        button_forgot_password.place(x=170 ,y=210)
        
        
        global contador
        contador = 0
        
        def confirm_login():
            global user_id
            global user_nome
            global user_cpf
            global user_email
            global user_senha
            global contador
            
            validate_user = entry_user.get()
            validate_password = entry_password.get()
            
            
            user_id_check  = check_user_password(validate_user, validate_password)
           
            
            if user_id_check :
                CTkMessagebox(title="Info",icon="check",message="Login efetuado com sucesso!")
                
                user_id = user_id_check[0]
                user_nome = user_id_check[1]
                user_cpf = user_id_check[2]
                user_email = user_id_check[3]
                user_senha = user_id_check[4]

                entry_user.delete(0, "end")
                entry_password.delete(0, "end")
                
                contador = 0

                self.window.withdraw()
                self.main_screen()
            else:
                
                contador += 1

                   # Verificar o limite de tentativas
                if contador >= 5:
                        entry_user.delete(0, "end")
                        entry_password.delete(0, "end")
                        
                        button_login.configure(command=None)
                        entry_password.configure(state="readonly")
                        entry_user.configure(state="readonly")
                        
                        CTkMessagebox(title="Info", icon="cancel", message="Você atingiu o limite de tentativas!", sound=1)
                        contador = 0  # Reiniciar o contador após atingir o limite
                        
                        global time
                        time = 0
                        l_try_again = ctk.CTkLabel(master=frame_login,
                            text=f"Tente Novamente em: {time} segundos",
                            width=300,
                            font=("Roboto", 11),
                            height=1)
                        l_try_again.place(x=10,y=325)
                        
                        def animation_time():
                            global time
                            time+=1
                            if time <=10:
                                l_try_again.configure(text=f"Tente Novamente em: {time} segundos")
                                l_try_again.after(1000, animation_time)
                                
                            else:
                                l_try_again.configure(text="Tente Novamente")
                                
                                
                                def destroy():
                                    l_try_again.destroy()
                                l_try_again.after(2000, destroy) 
                                
                                
                                
                                def animation_limit_password():
                                    entry_password.configure(state="normal")
                                    entry_user.configure(state="normal")
                                    button_login.configure(command=confirm_login)
                                    
                                # Aguarda um tempo suficiente para a animação terminar antes de remover o frame e reposicionar o frame_login
                                    entry_password.after(10000, animation_limit_password) 
                               
                                
                                animation_limit_password()
                                
                        animation_time()
                                  
                else:
                        CTkMessagebox(title="Info", icon="cancel", message="E-mail ou senha incorretos!", sound=1)
                        entry_password.delete(0, "end")
            
        button_login = ctk.CTkButton(
            master=frame_login, 
            width=220,
            text="Entrar",
            text_color="black", 
            fg_color="white",
            hover_color="#d1c7c7",
            corner_radius=15,
            command=confirm_login,
            )
        button_login.place(x=50, y=250)
        
        # TELA DE REGISTRO =====================================================================
        def screen_register():
            frame_login.pack_forget()
            
            global frame_register
            global height
            height = 360
            frame_register=ctk.CTkFrame(
            master=l_pattern, 
            width=320, 
            height=height, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
            frame_register.place(x=455, rely=0.5, anchor=ctk.CENTER)
            animation_button_register()
            
            app_logo = ctk.CTkLabel(
            master=frame_register,
            image=self.images['logo'],
            width=300,
            compound="left",
            text="PYMYMONEY",
            font=('Impact',20, "underline"))
            app_logo.place(x=10, y=20)
            
            l_cadastro=ctk.CTkLabel(
            master=frame_register, 
            width=300, 
            text="FAÇA SEU CADASTRO",
            font=('Century Gothic',20))
            l_cadastro.place(x=10, y=70)
            
            entry_register_nome=ctk.CTkEntry(
            master=frame_register,
            width=220, 
            placeholder_text='Nome Completo',
            corner_radius=15,
            border_color="white",
            border_width=2)
            entry_register_nome.place(x=50, y=120)

            entry_register_cpf=ctk.CTkEntry(
            master=frame_register,
            width=220, 
            placeholder_text='CPF(Apenas Números)',
            corner_radius=15,
            border_color="white",
            border_width=2)
            entry_register_cpf.place(x=50, y=155)
            
            entry_register_email=ctk.CTkEntry(
            master=frame_register,
            width=220, 
            placeholder_text='E-mail',
            corner_radius=15,
            border_color="white",
            border_width=2)
            entry_register_email.place(x=50, y=190)
            
            entry_register_password=ctk.CTkEntry(
            master=frame_register,
            width=220, 
            placeholder_text='Senha',
            corner_radius=15,
            border_color="white",
            border_width=2)
            entry_register_password.place(x=50, y=225)
            
            entry_register_confirm_password=ctk.CTkEntry(
            master=frame_register,
            width=220, 
            placeholder_text='Confirme a senha',
            corner_radius=15,
            border_color="white",
            border_width=2)
            entry_register_confirm_password.place(x=50, y=260)
            
            entry_register_nome.bind("<Return>", on_enter_pressed)
            entry_register_cpf.bind("<Return>", on_enter_pressed)
            entry_register_email.bind("<Return>", on_enter_pressed)
            entry_register_password.bind("<Return>", on_enter_pressed)
            entry_register_confirm_password.bind("<Return>", on_enter_pressed)
            entry_register_cpf.bind("<FocusOut>", format_cpf)
            
            confirm_terms = ctk.BooleanVar()

            checkbox_terms = ctk.CTkCheckBox(
                master=frame_register,
                text="Aceito os termos de serviço",
                width=145,
                variable=confirm_terms,
                corner_radius=15,
                checkmark_color="black",
                hover_color="#302c2c",
                fg_color="white",
                border_color="white",
                border_width=2
            )
            checkbox_terms.place(x=50,y=300)
            
            def confirm_register():
                
                add_user = entry_register_nome.get()
                add_cpf = entry_register_cpf.get()
                add_email = entry_register_email.get()
                add_password = entry_register_password.get()
                add_password_confirm = entry_register_confirm_password.get()
                
                user = check_user_register(add_user)
                email = check_email_register(add_email)
                cpf = check_cpf_register(add_cpf)

                # Verifica se o email inserido é válido
                if (
                    all([add_user,add_cpf, add_email, add_password, add_password_confirm])
                    and confirm_terms.get()):
                    if is_valid_email(add_email):
                        if check_cpf_format(add_cpf):
                            if not user:
                                if not cpf:
                                    if not email:
                                        if add_password_confirm == add_password:
                                            dados_usuario = (add_user, add_cpf, add_email, add_password)
                                            insert_usuario(dados_usuario)

                                            # Limpar os campos de entrada após armazenar os valores
                                            entry_register_nome.delete(0, "end")
                                            entry_register_email.delete(0, "end")
                                            entry_register_password.delete(0, "end")
                                            entry_register_confirm_password.delete(0, "end")

                                            msg_successfully = CTkMessagebox(
                                                title="Info",
                                                icon="check",
                                                message="Cadastrado com sucesso!",
                                            )

                                            frame_register.destroy()
                                            frame_login.place(x=455, rely=0.5, anchor=ctk.CENTER)
                                            frame_login.lift()
                                        else:
                                            msg_successfully = CTkMessagebox(
                                                title="Info",
                                                icon="warning",
                                                message="Campo de 'senha' e 'confirmar senha' devem ser iguais!",
                                            )

                                            entry_register_confirm_password.delete(0, "end")
                                    else:
                                        msg_successfully = CTkMessagebox(
                                            title="Info",
                                            icon="warning",
                                            message="E-mail já existente!",
                                        )

                                        entry_register_email.delete("end", "end")
                                else:
                                    msg_successfully = CTkMessagebox(
                                    title="Info",
                                    icon="warning",
                                    message="CPF já existente!")
                            else:
                                msg_successfully = CTkMessagebox(
                                    title="Info",
                                    icon="warning",
                                    message="Usuário já existente!")

                                entry_register_cpf.delete("end", "end")
                        else:
                            msg_successfully = CTkMessagebox(
                                title="Info",
                                icon="warning",
                                message="CPF deve conter 11 Digitos Númericos!")

                            entry_register_cpf.delete("end", "end")
                    else:
                        msg_successfully = CTkMessagebox(
                            title="Info",
                            icon="warning",
                            message="Formato de E-mail inválido!",
                        )

                else:
                    msg_successfully = CTkMessagebox(
                        title="Info",
                        icon="warning",
                        message="Por favor preencha todos os campos!",
                    )
                
                
            
            button_confirm_register = ctk.CTkButton(
                master=frame_register, 
                width=220,
                text="Cadastrar",
                text_color="black", 
                fg_color="white",
                hover_color="#d1c7c7",
                corner_radius=15,
                command=confirm_register
                )
            button_confirm_register.place(x=50, y=335)
            
            def back():
                animation_confirm_register() 
                
                def remove_frame():
                    frame_register.destroy()
                    frame_login.place(x=455, rely=0.5, anchor=ctk.CENTER)
                    

                # Aguarda um tempo suficiente para a animação terminar antes de remover o frame e reposicionar o frame_login
                frame_register.after(400, remove_frame) 
                
                
            button_back = ctk.CTkButton(
                master=frame_register, 
                width=220, 
                text="Voltar", 
                text_color="white", 
                fg_color="transparent",
                hover_color="#757272",
                border_color="white",
                border_width=2,
                corner_radius=15,
                command=back
                )
            button_back.place(x=50, y=370)

            def show_terms():
                terms_message = """Bem-vindo ao PyMyMoney!\n\nAo utilizar nosso aplicativo, você concorda com os seguintes termos de uso:\n
                1. Privacidade e Segurança:\n
                - Todas as informações fornecidas serão mantidas em sigilo e segurança.\n
                - Não compartilharemos seus dados pessoais com terceiros.\n\n
                2. Responsabilidade:\n
                - Você é responsável por manter a segurança de suas credenciais de login.\n
                - Não nos responsabilizamos por transações não autorizadas na sua conta.\n\n
                3. Uso Adequado:\n
                - Não utilize o aplicativo para atividades ilegais ou antiéticas.\n
                - Respeite outros usuários e não publique conteúdo ofensivo ou impróprio.\n\n"""

                messagebox.showinfo("Termos de Uso", terms_message)

                
            button_terms = ctk.CTkButton(
                master=frame_register,
                text="Ver termos",
                width=300,
                font=("Roboto", 11, "underline"),
                fg_color="transparent",
                hover_color="#2B2B2B",
                command=show_terms
            )
            button_terms.place(x=10, y=410)
            # ================================================================================
        def animation_button_register():
            global frame_register
            global height
            height += 2  # Aumentando o tamanho do frame
            if height < 450:
                frame_register.configure(height=height)
                frame_register.after(1, animation_button_register)  # Chamando a função novamente após 1ms
        
        def animation_confirm_register():
            global frame_register
            global height
            height -= 2  # Aumentando o tamanho do frame
            if height > 360:
                frame_register.configure(height=height)
                frame_register.after(1, animation_confirm_register)  # Chamando a função novamente após 1ms
        
        
        button_register = ctk.CTkButton(
            master=frame_login, 
            width=220, 
            text="Cadastre-se", 
            text_color="white", 
            fg_color="transparent",
            hover_color="#757272",
            border_color="white",
            border_width=2,
            corner_radius=15,
            command=screen_register)
        button_register.place(x=50, y=290)
        

    def main_screen(self):
        def disable_close_button():
                pass 
        
        # CRIAÇÃO DA TOPLEVEL===========================================================================
        
        screen_principal = ctk.CTkToplevel(master=self.window)
        screen_principal.title("")
        screen_principal.geometry("1050x750")
        screen_principal.resizable(False, False)
        
        screen_principal.protocol("WM_DELETE_WINDOW", disable_close_button)
        
        l_pattern = ctk.CTkLabel(
            master=screen_principal,
            text="", 
            image=self.images['pattern'])
        l_pattern.pack()
        #animação =======================================
                
        def move_frames_out(x, frame, final_x):
            if x < final_x:
                frame.place(x=x, y=60)
                x += 5  
                l_pattern.after(1, move_frames_out, x, frame, final_x)

        def move_frame_in(x, frame, final_x):
            if x > final_x:
                frame.place(x=x, y=60)
                x -= 5  
                l_pattern.after(1, move_frame_in, x, frame, final_x)

        def animate_configure():
            move_frames_out(-500, frame_configure, 265)
        def animate_home():
            move_frame_in(265, frame_configure, -500)
        
        # CRIANDO OS FRAMES=====================================
        frame_cima=ctk.CTkFrame(
            master=l_pattern, 
            width=1030, 
            height=50, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_cima.place(x=10,y=2)
        
        frame_meio_grafico=ctk.CTkFrame(
            master=l_pattern, 
            width=350,
            height=361, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_meio_grafico.place(x=10,y=60)
        
        frame_meio_renda=ctk.CTkFrame(
            master=l_pattern, 
            width=300,
            height=115, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_meio_renda.place(x=365,y=60)
        
        frame_meio_despesa=ctk.CTkFrame(
            master=l_pattern, 
            width=300,
            height=115, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_meio_despesa.place(x=365,y=182)
        
        frame_meio_saldo=ctk.CTkFrame(
            master=l_pattern, 
            width=300,
            height=115, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_meio_saldo.place(x=365,y=305)
        
        frame_meio_pizza=ctk.CTkFrame(
            master=l_pattern, 
            width=370,
            height=361, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_meio_pizza.place(x=669,y=60)
        
        frame_baixo_tabela=ctk.CTkFrame(
            master=l_pattern, 
            width=350, 
            height=313, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_baixo_tabela.place(x=10,y=430)
        
        frame_baixo_despesas=ctk.CTkFrame(
            master=l_pattern, 
            width=300, 
            height=170, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_baixo_despesas.place(x=365,y=430)
        
        frame_baixo_receitas=ctk.CTkFrame(
            master=l_pattern, 
            width=300, 
            height=140, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_baixo_receitas.place(x=365,y=605)
        
        frame_baixo_categoria=ctk.CTkFrame(
            master=l_pattern, 
            width=370, 
            height=85, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_baixo_categoria.place(x=669,y=430)
        
        frame_baixo_welcome=ctk.CTkFrame(
            master=l_pattern, 
            width=370, 
            height=225, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_baixo_welcome.place(x=669,y=520)
        
        frame_configure=ctk.CTkFrame(
            master=l_pattern, 
            width=500, 
            height=540, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_configure.place(x=-500,y=60)
        
        # TUDO DO FRAME DE CONFIGURAÇÃO=========================================================
        l_config = ctk.CTkLabel(
                master=frame_configure,
                image=self.images['config'],
                width=1,
                compound="left", 
                text=" Configurações",
                height=1,
                anchor="nw",
                font=('Impact',20)
            )
        l_config.place(x=175,y=15)
        
        l_login=ctk.CTkLabel(
            master=frame_configure, 
            width=1, 
            height=1,
            text="ENCONTRE AQUI SUAS INFORMAÇÕES\nÉ POSSÍVEL REALIZAR ALTERAÇÕES!",
            font=('Century Gothic',20))
        l_login.place(x=60, y=70)
        
        l_name_config = ctk.CTkLabel(
            master=frame_configure,
            image=self.images['user'],
            compound="left", 
            text=" Nome de usuário",
            height=1,
            anchor="nw",
            font=('Impact',17))
        l_name_config.place(x=130,y=130)
        
        e_name_config = ctk.CTkEntry(
            master=frame_configure,
            width=250,
            height=30, 
            placeholder_text='Nome',
            corner_radius=15,
            border_color="white",
            border_width=2,
            font=('Arial 20',15,'bold')
        )
        e_name_config.insert(0,user_nome)
        e_name_config.place(x=130,y=160)
        
        l_cpf_config = ctk.CTkLabel(
            master=frame_configure,
            image=self.images['cpf'],
            compound="left", 
            text=" CPF",
            height=1,
            anchor="nw",
            font=('Impact',17))
        l_cpf_config.place(x=130,y=200)
        
        e_cpf_config = ctk.CTkEntry(
            master=frame_configure,
            width=250,
            height=30, 
            placeholder_text='CPF',
            corner_radius=15,
            border_color="white",
            border_width=2,
            font=('Arial 20',15,'bold')
        )
        e_cpf_config.insert(0,user_cpf)
        e_cpf_config.place(x=130,y=230)
        e_cpf_config.bind("<FocusOut>", format_cpf)
        
        l_email_config = ctk.CTkLabel(
            master=frame_configure,
            image=self.images['user'],
            compound="left", 
            text=" E-mail",
            height=1,
            anchor="nw",
            font=('Impact',17))
        l_email_config.place(x=130,y=270)
        
        e_email_config = ctk.CTkEntry(
            master=frame_configure,
            width=250,
            height=30, 
            placeholder_text='E-mail',
            corner_radius=15,
            border_color="white",
            border_width=2,
            font=('Arial 20',15,'bold')
        )
        e_email_config.insert(0,user_email)
        e_email_config.place(x=130,y=300)
        
        l_password_config = ctk.CTkLabel(
            master=frame_configure,
            image=self.images['password'],
            compound="left", 
            text=" Nova senha",
            height=1,
            anchor="nw",
            font=('Impact',17))
        l_password_config.place(x=130,y=340)
        
        e_new_password_config = ctk.CTkEntry(
            master=frame_configure,
            width=250,
            height=30, 
            placeholder_text='Senha',
            placeholder_text_color="white",
            corner_radius=15,
            border_color="white",
            border_width=2,
            font=('Arial 20',15,'bold'),
            state="normal",
            show="*")
        e_new_password_config.insert(0,user_senha)
        e_new_password_config.place(x=130,y=370)
        
        def save_alteration():   
            
            def disable_close_button():
                pass 
            def center_window(top):
                top.update_idletasks()
                width = top.winfo_width()
                height = top.winfo_height()
                screen_width = top.winfo_screenwidth()
                screen_height = top.winfo_screenheight()
                x = (screen_width - width) // 2
                y = (screen_height - height) // 2
                top.geometry(f"{width}x{height}+{x}+{y}")               
            
            screen_principal.withdraw()
            
            top_password_config = ctk.CTkToplevel(master=screen_principal)
            top_password_config.title("")
            top_password_config.geometry("180x110")
            top_password_config.resizable(False, False)
            
            l_check_password_config = ctk.CTkLabel(
                master=top_password_config,
                image=self.images['password'],
                compound="left", 
                text=" Digite sua senha atual",
                height=1,
                anchor="nw",
                font=('Impact',17))
            l_check_password_config.place(x=10,y=5)
            
            e_check_password_config = ctk.CTkEntry(
                master=top_password_config,
                width=200,
                height=30, 
                placeholder_text='Senha',
                placeholder_text_color="white",
                corner_radius=15,
                border_color="white",
                border_width=2,
                font=('Arial 20',15,'bold'),
                show="*")
            e_check_password_config.insert(0,"*******")
            e_check_password_config.place(x=10,y=35)
            
            def confirmation_for_config():
                check_password_config = e_check_password_config.get()
                new_name = e_name_config.get()
                new_cpf = e_cpf_config.get()
                new_email = e_email_config.get()
                new_password = e_new_password_config.get()
                
                user = check_user_register(new_name)
                email = check_email_register(new_email)
                cpf = check_cpf_register(new_cpf)
                
                if check_password_config == user_senha:
                    if not user or new_name==user_nome:   
                        if not cpf or new_cpf==user_cpf:       
                            if not email or new_email==user_email:      
                                update_data_user(new_name,new_cpf,new_email,new_password,user_id)
                                
                                CTkMessagebox(title="Info", message="Dados alterados com sucesso", icon="check")
                                
                                top_password_config.destroy()
                                screen_principal.deiconify()
                            
                            else:
                                CTkMessagebox(title="Error", message="E-mail já existente",sound=1, icon="cancel")
                                top_password_config.destroy()
                                screen_principal.deiconify()
                                e_email_config.delete("end", "end")
                                
                        else:
                            CTkMessagebox(title="Error", message="CPF já existente",sound=1, icon="cancel")
                            top_password_config.destroy()
                            screen_principal.deiconify()
                            e_cpf_config.delete("end", "end")
                    else:
                        CTkMessagebox(title="Error", message="Nome já existente!",sound=1, icon="cancel")
                        top_password_config.destroy()
                        screen_principal.deiconify()
                        e_name_config.delete("end", "end")
                else:
                    CTkMessagebox(title="Error", message="Senha Incorreta!",sound=1, icon="cancel")
            
            button_confirm_password = ctk.CTkButton(
                master=top_password_config, 
                width=200,
                height=30,
                text="Confirmar",
                text_color="black", 
                fg_color="white",
                hover_color="#d1c7c7",
                corner_radius=15,
                font=('Arial 20',15,'bold'),
                command=confirmation_for_config)
            button_confirm_password.place(x=10,y=68)
            
            def back_config():
                top_password_config.destroy()
                screen_principal.deiconify()
                
            button_back_config = ctk.CTkButton(
                master=top_password_config, 
                width=200,
                height=30,
                text="Voltar",
                text_color="white", 
                fg_color="black",
                hover_color="#101010",
                corner_radius=15,
                font=('Arial 20',15,'bold'),
                command=back_config)
            button_back_config.place(x=10,y=101)
            
            center_window(top_password_config)
            top_password_config.protocol("WM_DELETE_WINDOW", disable_close_button)
            
        button_add_alteration = ctk.CTkButton(
            master=frame_configure, 
            width=250,
            height=30,
            text="Salvar Alterações",
            text_color="black", 
            fg_color="white",
            hover_color="#d1c7c7",
            corner_radius=15,
            font=('Arial 20',15,'bold'),
            command=save_alteration)
        button_add_alteration.place(x=130, y=410)
        
        l_categoria_config = ctk.CTkLabel(
            master=frame_configure,
            image=self.images['tabela'],
            compound="left", 
            text=" Categorias",
            height=1,
            anchor="nw",
            font=('Impact',17))
        l_categoria_config.place(x=130,y=450)
        def update_combobox_values_config(event):
            typed_text = combo_categoria_config.get()  # Pega o texto digitado na Combobox
            category_function_search = view_category_search(typed_text, user_id)
            category_search = [i[1] for i in category_function_search]  # Coleta apenas os nomes das categorias
            combo_categoria_config.configure(values = category_search)  # Atualiza os valores da Combobox
        
        combo_categoria_config = ctk.CTkComboBox(
            master=frame_configure,
            width=130,
            font=('Ivy 10',12),
            fg_color='white',
            dropdown_fg_color='#909090',
            dropdown_text_color='black',
            text_color='black',
            values=[''],
            corner_radius=4,
            state='normal')
        def update_categoy():
            category_function = view_category(user_id)
            category = [i[1] for i in category_function]  # Coleta apenas os nomes das categorias
            combo_categoria_config.configure(values = category) 
        update_categoy()
        combo_categoria_config.place(x=130,y=480)
        
        combo_categoria_config.bind("<KeyRelease>", update_combobox_values_config)
        
        def delete_category_config():           
            combo_delete = combo_categoria_config.get()
            
            if combo_delete:
                delete_category(combo_delete, user_id)
                CTkMessagebox(title="info", message="categoria deletada com sucesso!", icon="check")
                update_categoy()
                combo_categoria_config.set('') 
                
            else:
                CTkMessagebox(title="Error", message="Escolha uma categoria!",sound=1, icon="cancel")
    
        
        button_delete_category = ctk.CTkButton(
            master=frame_configure,
            image=self.images['lixeira'],
            compound="left",
            text=" Excluir",
            anchor="nw",
            font=('Impact',15),
            text_color='white',
            width=1,
            fg_color="black",
            hover_color="#101010",
            corner_radius=20,
            command=delete_category_config
        )
        button_delete_category.place(x=270,y=475)
        
        
            
        
        # TUDO DO FRAME DE CIMA =================================================================
        app_logo = ctk.CTkLabel(
            master=frame_cima,
            image=self.images['logo principal'],
            width=300,
            compound="left",
            text="PYMYMONEY",
            font=('Impact',20, "underline"))
        app_logo.place(x=350, y=7)
        
        home = ctk.CTkButton(
            master=frame_cima,
            image=self.images['home'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=animate_home
            )
        home.place(x=13, y=2)
        
        def logout():
            msg = CTkMessagebox(
                title="Sair", 
                message="Deseja sair?",
                icon="question",
                cancel_button="circle",
                cancel_button_color="white",
                button_color="white",
                button_text_color="black",
                border_color="black",
                border_width=2,
                corner_radius=20,
                button_hover_color="#d1c7c7",
                fade_in_duration=0.01,
                option_1="Cancelar", 
                option_2="Sair e fechar aplicativo",
                option_3="Sair da conta")
            
            response = msg.get()
            
            if response=="Sair da conta":
                screen_principal.destroy()
                self.window.deiconify()
                
            elif response=="Sair e fechar aplicativo":
                sys.exit()
                
            else:
                pass
            
            
        button_logout = ctk.CTkButton(
            master=frame_cima,
            image=self.images['logout'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=logout
            )
        button_logout.place(x=964, y=2)
        
        button_config = ctk.CTkButton(
            master=frame_cima,
            image=self.images['config'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=animate_configure
            )
        button_config.place(x=914, y=2)
        
        # variavel global para as insirir dados na tabela  ===================================
        global tree
        
        def inserir_categoria():
            nome = e_nome_categoria.get()
            
            if nome:  # Verifica se o nome não está vazio
                if len(nome) <= 8:
                    if not check_category(nome,user_id):
                        insert_category(nome, user_id)
                        category_function = view_category(user_id)
                        category = [i[1] for i in category_function]  # Coleta apenas os nomes das categorias

                        combo_categoria.configure(values = category)
                        combo_categoria_config.configure(values = category) 
                        CTkMessagebox(title="info", message="Categoria adicionada com sucesso!", icon="check")
                    
                    else:
                        CTkMessagebox(title="Error", message="Categoria já existente!", icon="cancel")
                else:
                        CTkMessagebox(title="Error", message="Categoria deve conter 8 caracteres no maximo!", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="Preencha os campos corretamente", icon="cancel")

            e_nome_categoria.delete(0, 'end')
                          
        def inserir_receita():
            nome = 'Receita'
            data = e_cal_receita.get_date()
            valor = e_valor_receita.get()
            if check_real_brl(valor):
                if data and valor:
                    insert_revenue(nome,valor,data,user_id)
                    CTkMessagebox(title="info", message="Receita adicionada com sucesso!", icon="check")
                    
                    e_valor_receita.delete(0, 'end')
                    
                    # atualizar resumo
                    valor_resumo = bar_values(user_id)
                    l_renda_RS.configure(text="R${:,.2f}".format(valor_resumo[0]))                   
                    l_despesa_RS.configure(text="R${:,.2f}".format(valor_resumo[1]))
                    l_saldo_RS.configure(text="R${:,.2f}".format(valor_resumo[2]))
                    # atualizar porcentagem
                    valor_porcentagem = porcentagem_value(user_id)[0]
                    l_bar.configure(text="{:,.2f}%".format(valor_porcentagem))
                    bar_set = valor_porcentagem
            
                    if valor_porcentagem > 0 and valor_porcentagem <= 10:
                        bar_set = 0.1
                    elif valor_porcentagem >= 11 and valor_porcentagem <= 20:
                        bar_set = 0.2
                    elif valor_porcentagem >= 21 and valor_porcentagem <= 30:
                        bar_set = 0.3
                    elif valor_porcentagem >= 31 and valor_porcentagem <= 40:
                        bar_set = 0.4
                    elif valor_porcentagem >= 41 and valor_porcentagem <= 50:
                        bar_set = 0.5
                    elif valor_porcentagem >= 51 and valor_porcentagem <= 60:
                        bar_set = 0.6
                    elif valor_porcentagem >= 61 and valor_porcentagem <= 70:
                        bar_set = 0.7
                    elif valor_porcentagem >= 71 and valor_porcentagem <= 80:
                        bar_set = 0.8
                    elif valor_porcentagem >= 81 and valor_porcentagem <= 90:
                        bar_set = 0.9
                    elif valor_porcentagem >= 91 and valor_porcentagem <= 100:
                        bar_set = 1
                    else:
                        bar_set = 0
                    bar.set(bar_set)
                    grafico_bar()
                    grafico_pie()
                    mostrar_renda()
                else:
                    CTkMessagebox(title="Error", message="Preencha todos os campos", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="O campo de valor deve ser preenchido corretamente\nCantavos devem ser com '.'(ponto)\nExemplo: 0.00", icon="cancel")
                
        def inserir_despesas():
            nome = combo_categoria.get()
            data = e_cal_despesas.get_date()
            valor = e_valor_despesas.get()
            if check_real_brl(valor):
                if data and valor and nome:
                    insert_expense(nome,valor,data,user_id)
                    CTkMessagebox(title="info", message="Despesa adicionada com sucesso!", icon="check")
                    
                    e_valor_despesas.delete(0, 'end')
                    
                    # atualizar resumo
                    valor_resumo = bar_values(user_id)
                    l_renda_RS.configure(text="R${:,.2f}".format(valor_resumo[0]))
                    l_despesa_RS.configure(text="R${:,.2f}".format(valor_resumo[1]))
                    l_saldo_RS.configure(text="R${:,.2f}".format(valor_resumo[2]))
                    # atualizar porcentagem
                    valor_porcentagem = porcentagem_value(user_id)[0]
                    l_bar.configure(text="{:,.2f}%".format(valor_porcentagem))
                    bar_set = valor_porcentagem
            
                    if valor_porcentagem > 0 and valor_porcentagem <= 10:
                        bar_set = 0.1
                    elif valor_porcentagem >= 11 and valor_porcentagem <= 20:
                        bar_set = 0.2
                    elif valor_porcentagem >= 21 and valor_porcentagem <= 30:
                        bar_set = 0.3
                    elif valor_porcentagem >= 31 and valor_porcentagem <= 40:
                        bar_set = 0.4
                    elif valor_porcentagem >= 41 and valor_porcentagem <= 50:
                        bar_set = 0.5
                    elif valor_porcentagem >= 51 and valor_porcentagem <= 60:
                        bar_set = 0.6
                    elif valor_porcentagem >= 61 and valor_porcentagem <= 70:
                        bar_set = 0.7
                    elif valor_porcentagem >= 71 and valor_porcentagem <= 80:
                        bar_set = 0.8
                    elif valor_porcentagem >= 81 and valor_porcentagem <= 90:
                        bar_set = 0.9
                    elif valor_porcentagem >= 91 and valor_porcentagem <= 100:
                        bar_set = 1
                    else:
                        bar_set = 0
                    bar.set(bar_set)
                    grafico_bar()
                    grafico_pie()
                    mostrar_renda()
                else:
                    CTkMessagebox(title="Error", message="Preencha todos os campos", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="O campo de valor deve ser preenchido corretamente\nCantavos devem ser com '.'(ponto)\nExemplo: 0.00", icon="cancel")
        
        def delete_dados_table():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_list = treev_dicionario['values']
                valor = treev_list[0]
                nome = treev_list[1]
                
                if nome == 'Receita':
                    delete_revenue(valor,user_id)
                    
                    CTkMessagebox(title="info", message="Dados Excluidodos com sucesso!", icon="check")
                    
                    # atualizar resumo
                    valor_resumo = bar_values(user_id)
                    l_renda_RS.configure(text="R${:,.2f}".format(valor_resumo[0]))
                    l_despesa_RS.configure(text="R${:,.2f}".format(valor_resumo[1]))
                    l_saldo_RS.configure(text="R${:,.2f}".format(valor_resumo[2]))
                    # atualizar porcentagem
                    valor_porcentagem = porcentagem_value(user_id)[0]
                    l_bar.configure(text="{:,.2f}%".format(valor_porcentagem))
                    bar_set = valor_porcentagem
            
                    if valor_porcentagem > 0 and valor_porcentagem <= 10:
                        bar_set = 0.1
                    elif valor_porcentagem >= 11 and valor_porcentagem <= 20:
                        bar_set = 0.2
                    elif valor_porcentagem >= 21 and valor_porcentagem <= 30:
                        bar_set = 0.3
                    elif valor_porcentagem >= 31 and valor_porcentagem <= 40:
                        bar_set = 0.4
                    elif valor_porcentagem >= 41 and valor_porcentagem <= 50:
                        bar_set = 0.5
                    elif valor_porcentagem >= 51 and valor_porcentagem <= 60:
                        bar_set = 0.6
                    elif valor_porcentagem >= 61 and valor_porcentagem <= 70:
                        bar_set = 0.7
                    elif valor_porcentagem >= 71 and valor_porcentagem <= 80:
                        bar_set = 0.8
                    elif valor_porcentagem >= 81 and valor_porcentagem <= 90:
                        bar_set = 0.9
                    elif valor_porcentagem >= 91 and valor_porcentagem <= 100:
                        bar_set = 1
                    else:
                        bar_set = 0
                    bar.set(bar_set)
                    grafico_bar()
                    grafico_pie()
                    mostrar_renda()
                    
                else:
                    delete_expense(valor,user_id)
                    
                    CTkMessagebox(title="info", message="Dados Excluidodos com sucesso!", icon="check")
                    
                    # atualizar resumo
                    valor_resumo = bar_values(user_id)
                    l_renda_RS.configure(text="R${:,.2f}".format(valor_resumo[0]))
                    l_despesa_RS.configure(text="R${:,.2f}".format(valor_resumo[1]))
                    l_saldo_RS.configure(text="R${:,.2f}".format(valor_resumo[2]))
                    # atualizar porcentagem
                    valor_porcentagem = porcentagem_value(user_id)[0]
                    l_bar.configure(text="{:,.2f}%".format(valor_porcentagem))
                    bar_set = valor_porcentagem
            
                    if valor_porcentagem > 0 and valor_porcentagem <= 10:
                        bar_set = 0.1
                    elif valor_porcentagem >= 11 and valor_porcentagem <= 20:
                        bar_set = 0.2
                    elif valor_porcentagem >= 21 and valor_porcentagem <= 30:
                        bar_set = 0.3
                    elif valor_porcentagem >= 31 and valor_porcentagem <= 40:
                        bar_set = 0.4
                    elif valor_porcentagem >= 41 and valor_porcentagem <= 50:
                        bar_set = 0.5
                    elif valor_porcentagem >= 51 and valor_porcentagem <= 60:
                        bar_set = 0.6
                    elif valor_porcentagem >= 61 and valor_porcentagem <= 70:
                        bar_set = 0.7
                    elif valor_porcentagem >= 71 and valor_porcentagem <= 80:
                        bar_set = 0.8
                    elif valor_porcentagem >= 81 and valor_porcentagem <= 90:
                        bar_set = 0.9
                    elif valor_porcentagem >= 91 and valor_porcentagem <= 100:
                        bar_set = 1
                    else:
                        bar_set = 0
                    bar.set(bar_set)
                    grafico_bar()
                    grafico_pie()
                    mostrar_renda()
            
            except IndexError:
                CTkMessagebox(title="erro", message="Selecione um dos dados da tabela!", icon="cancel")
                
            
            pass
        
        # TUDO DOS FRAMES DO MEIO ========================================================================================
        # grafico
        #barra de porcentagem 
        def porcentagem():
            global l_bar
            global bar
            l_porcentagem = ctk.CTkLabel(
                master=frame_meio_grafico,
                image=self.images['saldo'],
                compound="left", 
                text=" Porcentagem de Saldo Restante",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_porcentagem.place(x=20,y=15)

            valor = porcentagem_value(user_id)[0]                
            bar_set = valor
            
            if valor > 0 and valor <= 10:
                bar_set = 0.1
            elif valor >= 11 and valor <= 20:
                bar_set = 0.2
            elif valor >= 21 and valor <= 30:
                bar_set = 0.3
            elif valor >= 31 and valor <= 40:
                bar_set = 0.4
            elif valor >= 41 and valor <= 50:
                bar_set = 0.5
            elif valor >= 51 and valor <= 60:
                bar_set = 0.6
            elif valor >= 61 and valor <= 70:
                bar_set = 0.7
            elif valor >= 71 and valor <= 80:
                bar_set = 0.8
            elif valor >= 81 and valor <= 90:
                bar_set = 0.9
            elif valor >= 91 and valor <= 100:
                bar_set = 1
            else:
                bar_set = 0
            
            l_bar = ctk.CTkLabel(
                master=frame_meio_grafico,
                text="", 
                anchor="nw",
                font=("Verdana 12", 20)    
            )
            l_bar.configure(text="{:,.2f}%".format(valor))
            l_bar.place(x=260, y=44)
            
            bar = ctk.CTkProgressBar(
                master=frame_meio_grafico,
                width=234,
                progress_color="white",
                corner_radius=0,
                height=25,
                border_color="black",
                border_width=2,

            )
            bar.place(x=20,y=42)
            bar.set(bar_set)
        #grafico matplotlib 
        def grafico_bar():
            
            lista_categorias = ['Renda', 'Despesa', 'Saldo']
            lista_valores = bar_values(user_id)

            figura = plt.Figure(figsize=(4, 3.45), dpi=100)  # Ajustando o tamanho do gráfico

            ax = figura.add_subplot(111) 
            
            # Criando um gradiente de preto a cinza
            num_cores = len(lista_valores)
            cor_gradiente = mcolors.LinearSegmentedColormap.from_list('cor_gradiente', ['#000000', '#AAAAAA'], N=num_cores)


            bars = ax.bar(lista_categorias, lista_valores, color=cor_gradiente(range(num_cores)), width=0.9)

            # Adicionando rótulos nas barras
            for i, bar in enumerate(bars):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                        "R${:,.2f}".format(lista_valores[i]),
                        ha='center', va='bottom', fontsize=12, color='white')

            ax.set_xticklabels(lista_categorias, fontsize=14)
            
            # Configurando cores dos eixos e rótulos para branco
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            
            ax.set_facecolor('#2B2B2B')

            # Removendo a cor de fundo
            ax.patch.set_facecolor('#2B2B2B')  # define a cor de fundo do meio 
            
            figura.patch.set_facecolor('#2B2B2B')

            # Removendo as bordas e os grids
            ax.spines['bottom'].set_visible(True)
            ax.spines['right'].set_visible(True)
            ax.spines['top'].set_visible(True)
            ax.spines['left'].set_visible(True)
            ax.tick_params(bottom=True, left=True)
            ax.set_axisbelow(True)
            ax.yaxis.grid(True)
            ax.xaxis.grid(False)

            # Inserindo o gráfico na tela
            canva = FigureCanvasTkAgg(figura, frame_meio_grafico)
            canva.get_tk_widget().place(x=25, y=80)
        # resumo
        def resumo():
            global l_renda_RS
            global l_despesa_RS
            global l_saldo_RS
            valor = bar_values(user_id)

            # renda--------------------------
                   
            l_renda = ctk.CTkLabel(
                master=frame_meio_renda,
                image=self.images['renda'],
                compound="left",
                text=" Renda Total",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_renda.place(x=20,y=15)
            
            l_renda_RS = ctk.CTkLabel(
                master=frame_meio_renda,
                text="", 
                anchor="nw",
                font=("Verdana 12", 30)    
            )
            l_renda_RS.configure(text="R${:,.2f}".format(valor[0]))            
            l_renda_RS.place(x=20, y=47)
            # despesa--------------------------
            
            l_despesa = ctk.CTkLabel(
                master=frame_meio_despesa,
                image=self.images['despesa'],
                compound="left",
                text=" Despesa Total",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_despesa.place(x=20,y=15)
            
            l_despesa_RS = ctk.CTkLabel(
                master=frame_meio_despesa,
                text="", 
                anchor="nw",
                font=("Verdana 12", 30)    
            )
            l_despesa_RS.configure(text="R${:,.2f}".format(valor[1]))
            l_despesa_RS.place(x=20, y=47)
            # despesa--------------------------
            
            l_saldo = ctk.CTkLabel(
                master=frame_meio_saldo,
                image=self.images['saldo'],
                compound="left",
                text=" Saldo Total",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_saldo.place(x=20,y=15)
            
            l_saldo_RS = ctk.CTkLabel(
                master=frame_meio_saldo,
                text="", 
                anchor="nw",
                font=("Verdana 12", 30))
            l_saldo_RS.configure(text="R${:,.2f}".format(valor[2]))
            l_saldo_RS.place(x=20, y=47)
            
        # pizza 
        def grafico_pie():
            l_porcentagem = ctk.CTkLabel(
                master=frame_meio_pizza,
                image=self.images['despesa'],
                compound="left", 
                text=" Gráfico De Despesas",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_porcentagem.place(x=105,y=15)
            
            frame_gra_pie = ctk.CTkFrame(
                master=frame_meio_pizza,
                width=580,
                height=250,
                bg_color="#2B2B2B"
                )
            frame_gra_pie.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            
            black = '#000000'
            white = '#FFFFFF'
            cmap = mcolors.LinearSegmentedColormap.from_list('custom', [black, white])
            #faça figura e atribua objetos de eixo
            figura = plt.Figure(figsize=(5, 3), dpi=90, facecolor='#2B2B2B')
            ax = figura.add_subplot(111)

            lista_valores = pie_valores(user_id)[1]
            lista_categorias = pie_valores(user_id)[0]

            #only "explode" the 2nd slice (i.e. 'Hogs')

            explode = [0.05 for _ in lista_categorias]

            ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=cmap(np.linspace(0.0, 1.0, len(lista_valores))),shadow=True, startangle=90, textprops={'color': 'white'})
            
            ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.45, 0.50))            
            
            canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
            canva_categoria.get_tk_widget().grid(row=0, column=0)        

            
        porcentagem()
        grafico_bar()
        resumo()  
        grafico_pie() 
        
        # TUDO DOS FRAMES DE BAIXO ====================================================================
        #frame para centralizar a tabela 
        frame_renda = ctk.CTkFrame(
            master=frame_baixo_tabela,
            width=300,
            height=250,
            bg_color="#2B2B2B"
        )
        frame_renda.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # funcao para mostrar_renda
        def mostrar_renda():
            
            l_tabela = ctk.CTkLabel(
                master=frame_baixo_tabela,
                image=self.images['tabela'],
                compound="left",
                text=" Tabela de Receitas e Despesas",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
            l_tabela.place(x=35,y=25)
            
            lixeira = ctk.CTkButton(
            master=frame_baixo_tabela,
            image=self.images['lixeira'],
            text="",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=delete_dados_table
            )
            lixeira.place(x=23, y=250)
             # Criando um estilo personalizado
            style = ttk.Style()
            
            # Configurando um tag para o estilo do cabeçalho em negrito
            style.configure("Treeview.Heading", font=('Arial', 11, 'bold'))
    
            # Mudando a cor de fundo para cinza claro
            style.configure("Treeview", background="#909090")

            # Mudando a cor de seleção para azul claro
            style.map("Treeview", background=[('selected', '#525252')])

            # Mudando a cor do texto para branco
            style.map("Treeview", foreground=[('selected', 'white')])
            
            global tree
            # creating a treeview with dual scrollbars
            tabela_head = ['ID','Categoria','Valor', 'Data']

            lista_itens = table(user_id)
            
            

            tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
            #vertical scrollbar
            vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
            
            

            tree.configure(yscrollcommand=vsb.set)

            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')

            hd=["center","center","center", "center"]
            h=[30,100,100,100]
            n=0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor="center")
                #adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])
                
                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)
            
        mostrar_renda()
        
        # TUDO DO FRAME DE ADICIONAR DESPESAS -------
        l_inserir_despesa = ctk.CTkLabel(
                master=frame_baixo_despesas,
                image=self.images['despesa'],
                compound="left",
                text=" Insira Novas Despesas",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
        l_inserir_despesa.place(x=35,y=10)  
        
        # categoria
        l_combo_categoria = ctk.CTkLabel(
                master=frame_baixo_despesas,
                text="Categoria",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_combo_categoria.place(x=35,y=50)  
        
        def update_combobox_values(event):
            typed_text = combo_categoria.get()  # Pega o texto digitado na Combobox
            category_function_search = view_category_search(typed_text, user_id)
            category_search = [i[1] for i in category_function_search]  # Coleta apenas os nomes das categorias
            combo_categoria.configure(values = category_search)  # Atualiza os valores da Combobox
            
        combo_categoria = ctk.CTkComboBox(
            master=frame_baixo_despesas,
            width=130,
            font=('Ivy 10',12),
            fg_color='white',
            dropdown_fg_color='#909090',
            dropdown_text_color='black',
            text_color='black',
            values=[''],
            corner_radius=4,
            state='normal')
        category_function = view_category(user_id)
        category = [i[1] for i in category_function]  # Coleta apenas os nomes das categorias
        combo_categoria.configure(values = category) 
        combo_categoria.place(x=125,y=42)
        
            
        combo_categoria.bind("<KeyRelease>", update_combobox_values)
        
        #data
        l_calendar_data = ctk.CTkLabel(
                master=frame_baixo_despesas,
                text="Data",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_calendar_data.place(x=35,y=75)
    

        e_cal_despesas = DateEntry(
            frame_baixo_despesas,
            width=10,
            height=10,
            font=('Arial', 12),
            background='#525252',
            foreground='white',
            borderwidth=2,
            locale='pt_BR',
            selectmode='day',
            date_pattern='dd/mm/yyyy',
            showweeknumbers=False,
            headersbackground='dark gray',
            headersforeground='white',
            year=2023,
            style="Custom.DateEntry"
        )
        e_cal_despesas.place(x=157, y=95)
        #Quantia      
            
        l_valor_despesas = ctk.CTkLabel(
                master=frame_baixo_despesas,
                text="Valor Total",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_valor_despesas.place(x=35,y=100)
        
        e_valor_despesas = ctk.CTkEntry(
                master=frame_baixo_despesas,
                fg_color="white",
                text_color="black",
                corner_radius=4,
                height=2,
                width=130,
                placeholder_text="0.00",
                placeholder_text_color="black"
        )
        e_valor_despesas.place(x=125,y=100)
        
        #adicionar
        button_adicionar_despesa = ctk.CTkButton(
                master=frame_baixo_despesas,
                image=self.images['adicionar'],
                compound="left",
                text="Adicionar",
                anchor="nw",
                font=('Impact',15),
                text_color='white',
                width=130,
                fg_color="black",
                hover_color="#101010",
                corner_radius=20,
                command=inserir_despesas
        )
        button_adicionar_despesa.place(x=125,y=125)
        
        # TUDO DO FRAME DE ADICIONAR RECEITAS ----
        l_inserir_receita = ctk.CTkLabel(
                master=frame_baixo_receitas,
                image=self.images['renda'],
                compound="left",
                text=" Insira Novas Receitas",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
        l_inserir_receita.place(x=35,y=10)
        
        #data
        l_calendar_data = ctk.CTkLabel(
                master=frame_baixo_receitas,
                text="Data",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_calendar_data.place(x=35,y=50)
    

        e_cal_receita = DateEntry(
            frame_baixo_receitas,
            width=10,
            height=10,
            font=('Arial', 12),
            background='#525252',
            foreground='white',
            borderwidth=2,
            locale='pt_BR',
            selectmode='day',
            date_pattern='dd/mm/yyyy',
            showweeknumbers=False,
            headersbackground='dark gray',
            headersforeground='white',
            year=2023,
            style="Custom.DateEntry"
        )
        e_cal_receita.place(x=156,y=65)
        
        #Quantia
            
        l_valor_receita = ctk.CTkLabel(
                master=frame_baixo_receitas,
                text="Valor Total",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_valor_receita.place(x=35,y=80)
        
        e_valor_receita = ctk.CTkEntry(
                master=frame_baixo_receitas,
                fg_color="white",
                text_color="black",
                corner_radius=4,
                height=2,
                width=130,
                placeholder_text="0.00",
                placeholder_text_color="black"
        )
        e_valor_receita.place(x=125,y=75)
        """ e_valor_receita.bind("<FocusOut>", formatar_valor_receita)
        e_valor_receita.bind("<Return>", formatar_valor_receita) """
        
        #add receita
        button_adicionar_receita = ctk.CTkButton(
                master=frame_baixo_receitas,
                image=self.images['adicionar'],
                compound="left",
                text="Adicionar",
                anchor="nw",
                font=('Impact',15),
                text_color='white',
                width=130,
                fg_color="black",
                hover_color="#101010",
                corner_radius=20,
                command=inserir_receita 
        )
        button_adicionar_receita.place(x=125,y=100)
        
        # FRAME DE ADD CATEGORIA----
        l_Inserir_categoria = ctk.CTkLabel(
                master=frame_baixo_categoria,
                image=self.images['tabela'],
                compound="left",
                text=" Insira Novas Categorias",
                height=1,
                anchor="nw",
                font=('Impact',17)
            )
        l_Inserir_categoria.place(x=25,y=10)
        
        #label categoria
        l_nome_categoria = ctk.CTkLabel(
                master=frame_baixo_categoria,
                text="Categoria",
                height=1,
                anchor="nw",
                font=('Ivy 10',17,'bold')
            )
        l_nome_categoria.place(x=25,y=50) 
        
        #entry nome categoria
        e_nome_categoria = ctk.CTkEntry(
                master=frame_baixo_categoria,
                fg_color="white",
                text_color="black",
                corner_radius=4,
                height=2,
                width=125,
                placeholder_text="Nome da categoria",
                placeholder_text_color="black"
                
        )
        e_nome_categoria.place(x=110,y=47)
        
        #botao add categoria
        button_adicionar_categoria = ctk.CTkButton(
                master=frame_baixo_categoria,
                image=self.images['adicionar'],
                compound="left",
                text="Adicionar",
                anchor="nw",
                font=('Impact',15),
                text_color='white',
                width=60,
                fg_color="black",
                hover_color="#101010",
                corner_radius=20,
                command=inserir_categoria)
        button_adicionar_categoria.place(x=240,y=42)
        
        # FRAME DE WELCOME -----
        l_welcome_user= ctk.CTkLabel(
            master=frame_baixo_welcome,
            text="",
            font =('Impact',17))
        l_welcome_user.configure(text=f"Olá, {user_nome}")
        l_welcome_user.place(x=38,y=5)
        
        def show_instruction():
            terms_message = """Bem-vindo ao PyMyMoney!\n\n
            
                A seguir veja instruções de como utilizar o app:\n\n
                
                1-Ao criar e logar a sua conta, você terá acesso aos seus dados de controle orçamentario.\n
                2-Adicione novas categorias a sua conta na aba de "Insira Novas Categorias":\n
                Nela você poderá adcionar categorias como: "Alimentação","Faculdade","Luz","Lazer" e etc...\n
                3-Adicione novas receitas na aba de "Insira Novas Receitas":\n
                Nela você poderá adcionar novas receitas ganhas, junto com a data em que ela foi recebida\n
                4-Adicione novas despesas na aba de "Insira Novas Despesas":\n
                Nela você poderá adcionar novas despesas gastas, escolhendo a categoria que foi usada(categoria adicionada no passo 2)\n
                Insira também o valor usado e a sua determinada data.\n
                5-Acompanhe todo o seu movimento orçamentário na aba de "Tabela de Receitas e Despesas":\n
                Nela você poderá acompanhar todas as movimentações inseridas nos passos anteriores.\n
                Poderá também deletar movimentações selecionando a movimentação na tabela e clicando na lixeira abaixo da tabela\n
                6-Acopanhe todas as outras informações no restante do app."""

            messagebox.showinfo("Termos de Uso", terms_message)
        
        button_instruction = ctk.CTkButton(
                master=frame_baixo_welcome,
                text="Instruções",
                width=1,
                font=("Roboto", 11, "underline"),
                fg_color="transparent",
                hover_color="#2B2B2B",
                command=show_instruction
            )
        button_instruction.place(x=280, y=190)
        
        l_logo_welcome= ctk.CTkLabel(
            master=frame_baixo_welcome,
            text="", 
            width=190,
            height=190,
            image=self.images['logo welcome'])
        l_logo_welcome.place(x=10,y=30)
        
        l_welcome = ctk.CTkLabel(
                master=frame_baixo_welcome,
                text=" Bem-Vindo\nao\nPyMyMoney",
                height=1,
                font=('Impact',30)
            )
        l_welcome.place(x=200,y=65)
                
                
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
