import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

janela = ctk.CTk()

class App():

    def __init__(self):
        self.janela = janela
        self.theme()
        self.tela() 
        self.tela_login()       
        janela.mainloop()
        
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


    def tela(self):    
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.resizable(False, False)
        #janela.iconbitmap("") img do icon

    def tela_login(self):
        #Titulo
        label_title = ctk.CTkLabel(master=janela, text="Bem vindo de volta!", 
                                            font=('Kanit', 20, 'bold')).place(x=80, y=150)
        label_subtitle = ctk.CTkLabel(master=janela, text="Faça login em sua conta", 
                                            font=('Roboto', 12),
                                            text_color="#00B0F0").place(x=80, y=175)

        #details
        label_detail = ctk.CTkLabel(master=janela, text=". . .\n. . .\n. . .\n. . .\n . .",
                                            font=("Kanit", 20, 'bold')).place(x=300, y=20)

        #sidemenu
        sidemenu_frame = ctk.CTkFrame(master=janela, width=350, height=396, fg_color="#1d1d1d")
        sidemenu_frame.pack(side=RIGHT)

        #sidemenu_frame widgets 
        label = ctk.CTkLabel(master=sidemenu_frame, text="Sistema de login", font=('Montserrat', 20)).place(x=25, y=25)

        #Usersame entrada
        username_entry = ctk.CTkEntry(master=sidemenu_frame, placeholder_text="Username", width=300, 
                                        font=("Montserrat", 15))
        username_entry.place(x=25, y=105)

        username_label = ctk.CTkLabel(master=sidemenu_frame, text="* O campo username deve ser preenchido", 
                                        text_color="green",
                                        font=("Montserrat", 12))
        username_label.place(x=25, y=135)
        
        def validar_entrada1(event):
            if username_entry.get():
                username_label.configure(text="")
            else:
                username_label.configure(text="* O campo Username deve ser preenchido", text_color="green")
        
        username_entry.bind("<KeyRelease>", validar_entrada1)
        
        # Senha entrada
        password_entry = ctk.CTkEntry(master=sidemenu_frame, placeholder_text="Password", width=300, 
                                      font=("Montserrat", 12), show="*")
        password_entry.place(x=25, y=175)

        password_label = ctk.CTkLabel(master=sidemenu_frame, text="* O campo Password deve ser preenchido", 
                                      text_color="green", font=("Montserrat", 12))
        password_label.place(x=25, y=205)

        def validar_entrada(event):
            if password_entry.get():
                password_label.configure(text="")
            else:
                password_label.configure(text="* O campo Password deve ser preenchido", text_color="green")

        password_entry.bind("<KeyRelease>", validar_entrada)


        #Lembrar senha
        checkbox = ctk.CTkCheckBox(master=sidemenu_frame, text="Lembrar a senha").place(x=25, y=240)

        def login():
            msg = messagebox.showinfo(title="Login concluido", message="Seja bem vindo!")
            pass

        #Botão de logar
        login_button =  ctk.CTkButton(master=sidemenu_frame, text="Login", width=300, command=login).place(x=25, y=285)
        register_span = ctk.CTkLabel(master=sidemenu_frame, text="Não possui conta? Cadastre-se", 
                                     font=("Montserrat", 10.5)).place(x=25, y=325)

        def tela_register():
            #Remove o frame de login
            sidemenu_frame.pack_forget()
            
            #sidemenu de cadastro
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396, fg_color="#1d1d1d" )
            rg_frame.pack(side=LEFT)
            
            wel_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            wel_frame.pack(side=RIGHT)
            
            label = ctk.CTkLabel(master=rg_frame, text="Sistema de registro", font=('Montserrat', 20)).place(x=25, y=25)

            span = ctk.CTkLabel(master=rg_frame, text="Todos os campos são obrigatórios!", font=("Roboto", 10),
                                text_color="gray").place(x=25, y=55)
            
            
            #
            label_welcome = ctk.CTkLabel(master=wel_frame, text="Seja bem vindo!", font=('Kanit', 20, 'bold')).place(x=25, y=150)
            label_Wsubtitle = ctk.CTkLabel(master=wel_frame, text="Crie sua conta!", font=('Roboto', 12), text_color="#00B0F0").place(x=25, y=175)
            label_detail1 = ctk.CTkLabel(master=wel_frame, text=". . .\n. . .\n. . .\n. . .\n . .",font=("Kanit", 20, 'bold')).place(x=300, y=20)
            label_detail2 = ctk.CTkLabel(master=wel_frame, text=". . . . . . . . .\n. . . . . . . .",font=("Kanit", 20, 'bold')).place(x=40, y=300)
            #


            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Username", width=300, 
                                        font=("Montserrat", 15)).place(x=25, y=105)
            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Email", width=300, 
                                        font=("Montserrat", 15)).place(x=25, y=145)
            password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Password", width=300, 
                                        font=("Montserrat", 15), show="*").place(x=25, y=185)
            cPassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirm Password", width=300, 
                                        font=("Montserrat", 15), show="*").place(x=25, y=225)
            
            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito os termos de uso").place(x=25, y=265)
        
            def back():
                #Remove o framde de cadastro
                rg_frame.pack_forget()
                wel_frame.pack_forget()
                #Retorna o frame de login
                sidemenu_frame.pack(side=RIGHT)
                pass
        
            back_button =  ctk.CTkButton(master=rg_frame, text="Voltar", width=145, fg_color="gray", 
                                         hover_color="#202020", command=back).place(x=25, y=320)
            
            def save_user():
                msg = messagebox.showinfo(title="Cadastro concluido", message="Usuario cadastrado com sucesso!")
                pass
            
            save_button =  ctk.CTkButton(master=rg_frame, text="Cadastrar", width=145, fg_color="green", 
                                         hover_color="#014B05", command=save_user).place(x=180, y=320)
            pass
        
        register_button =  ctk.CTkButton(master=sidemenu_frame, text="Cadastre-se",
                                         width=150, fg_color="green", hover_color="#2D9344",
                                         command=tela_register).place(x=175, y=325)

App()