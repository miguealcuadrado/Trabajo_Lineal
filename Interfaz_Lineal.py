import tkinter as tk
import pygame
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from playsound import playsound 





pygame.mixer.init()
pygame.mixer.music.load("116-bpm-oldschool-electronica-18063.mp3")
pygame.mixer.music.play(-1)

Ventana_Principal = tk.Tk()
Ventana_Principal.withdraw()

Ventana_Bienvenida = tk.Toplevel()
Ventana_Bienvenida.title("BIENVENIDO.")
Ventana_Bienvenida.geometry("300x150")
Ventana_Bienvenida.resizable(False, False)



def Cerrar_Bienvenida():
    pygame.mixer.stop()
    Ventana_Bienvenida.destroy()


Imagen_Fondo_Bienvenida = Image.open("BI.png").resize((300,150))
Fondo1 = ImageTk.PhotoImage(Imagen_Fondo_Bienvenida)
Fondo1_Label = tk.Label(Ventana_Bienvenida, image=Fondo1)
Fondo1_Label.image = Fondo1
Fondo1_Label.place(x=0, y=0, relwidth=1, relheight=1)


Frame_Central = tk.Frame(Ventana_Bienvenida, bg="dark slate gray")
Frame_Central.place(x=10, y=20)


Imagen_Bienvenida = Image.open("Icono8.png").resize((50, 50))
imagen_B = ImageTk.PhotoImage(Imagen_Bienvenida)
Label_Imagen2 = tk.Label(Frame_Central, image=imagen_B, bg="dark slate gray")
Label_Imagen2.grid(row=0, column=0, padx=5)

def Girar_Imagen(angulo=0):
    Imagen_Rotada = Imagen_Bienvenida.rotate(angulo)
    Imagen_B2 = ImageTk.PhotoImage(Imagen_Rotada)
    Label_Imagen2.config(image=Imagen_B2)
    Label_Imagen2.image = Imagen_B2
    Ventana_Bienvenida.after(100, Girar_Imagen, (angulo - 10) % 360)

Girar_Imagen()


Mensaje_Bienvenida = "¡Bienvenido, Cyber Usuario!"
Texto_Label = tk.Label(Frame_Central, text="", font=("Century Gothic", 9, "bold"), fg="beige", bg="dark slate gray", wraplength=180, justify="left")
Texto_Label.grid(row=0, column=1, padx=5)

def Animar_Texto(i=0):
    if i <= len(Mensaje_Bienvenida):
        Texto_Label.config(text=Mensaje_Bienvenida[:i])
        Ventana_Bienvenida.after(50, Animar_Texto, i + 1)

Animar_Texto()


def Pasar_a_principal():
    Ventana_Bienvenida.destroy()
    Ventana_Principal.deiconify()


Boton_Ingresar = tk.Button(Ventana_Bienvenida, text="Ingresar", font=("Century Gothic", 10), command=Pasar_a_principal)
Boton_Ingresar.place(relx=0.5, rely=0.85, anchor="center")




Ventana_Principal.title("Codificación Hamming.")
Ventana_Principal.geometry("600x650")
Ventana_Principal.resizable(width=False, height=False)



def Crear_Ventana_Dialogo():
    Ventana_Dialogo = tk.Toplevel()
    Ventana_Dialogo.title("Diálogo")
    Ventana_Dialogo.geometry("700x400")
    Ventana_Dialogo.resizable(False, False)
    

    fondo33 = Image.open("BI2.png").resize((700, 400))
    fondo33_tk = ImageTk.PhotoImage(fondo33)
    fondo33_Label = tk.Label(Ventana_Dialogo, image=fondo33_tk)
    fondo33_Label.image = fondo33_tk
    fondo33_Label.place(x=0, y=0, relwidth=1, relheight=1)

    frame_Texto_D = tk.Frame(Ventana_Dialogo, bg="gray")
    frame_Texto_D.place(x=220, y=280, width=420, height=100)

    Etiqueta_Texto = tk.Label(frame_Texto_D, text="", font=("Century Gothic", 11, "bold"),
                              fg="black", bg="gray", wraplength=400, justify="left")
    Etiqueta_Texto.pack(padx=10, pady=10)

    Titulo_Frame = tk.Frame(Ventana_Dialogo, bg = "gray")
    Titulo_Frame.place(x = 230 , y = 12)

    Titulo3 = tk.Label(Titulo_Frame, text = "Cyber", font = ("Century Gothic" , 20, "bold") , fg = "beige" , bg = "gray")
    Titulo3.pack(side = "left")

    Titulo4 = tk.Label(Titulo_Frame, text = "Cuestiones", font = ("Century Gothic" , 20, "bold") , fg = "orange" , bg = "gray")
    Titulo4.pack(side = "left")
    
    
    Personaje_Frame = tk.Label(Ventana_Dialogo, bg="gray")
    Personaje_Frame.place(x = 40, y = 200, width = 180, height = 180)

    gif = Image.open("Val_Pixel1.gif")
    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animar_gif(indice=0):
        frame_actual = frames[indice]
        Personaje_Frame.config(image=frame_actual)
        Personaje_Frame.image = frame_actual
        Ventana_Dialogo.after(100, animar_gif, (indice + 1) % len(frames))

    animar_gif()

    def Cerrar_Ventana():
        pygame.mixer.music.stop()
        Ventana_Dialogo.destroy()

    Ventana_Dialogo.protocol("WM_DELETE_WINDOW" , Cerrar_Ventana)

    def Regresar():
        pygame.mixer.music.fadeout(1000)
        pygame.time.delay(1000)
        pygame.mixer.music.load("116-bpm-oldschool-electronica-18063.mp3")
        pygame.mixer.music.play(-1,fade_ms=1000)

        Ventana_Dialogo.destroy()
        Ventana_Principal.deiconify()


    Boton_Regresar = tk.Button(Ventana_Dialogo, text = "<--" , font = ("Century Gothic", 13) , command = Regresar)
    Boton_Regresar.place(x = 10, y = 12, width = 35, height = 35)

    Boton_Avanzar = tk.Button(Ventana_Dialogo, text="▶", font=("Arial", 12))
    Boton_Avanzar.place(x=619, y=350, width=30, height=30)

    Ventana_Dialogo.Etiqueta_Texto = Etiqueta_Texto
    Ventana_Dialogo.Boton_Avanzar = Boton_Avanzar

    dialogos = ["¡Hola, Cyber Usuario!",
                "Te habla Val Pixel, tu compañera digital...",
                "¿Tienes dudas sobre cómo funciona ENCRIPTACIÓN IUE?",
                "No te preocupes. Yo te contare cómo funciona nuestro código y de que forma aplicamos Espacios vectoriales y matrices."]
    
    indice = {"valor": 0}  

    def Mostrar_Dialogo():
        if indice["valor"] >= len(dialogos):
            Boton_Avanzar.config(state="disabled")
            return

        texto_actual = dialogos[indice["valor"]]

        def Escribir(i=0):
            if i <= len(texto_actual):
                Ventana_Dialogo.Etiqueta_Texto.config(text=texto_actual[:i])
                Ventana_Dialogo.after(40, Escribir, i + 1)

        Escribir()
        indice["valor"] += 1

    Boton_Avanzar.config(command=Mostrar_Dialogo)
    Mostrar_Dialogo()

    

def Abrir_Ventana_Dialogo():
    Ventana_Principal.withdraw()
    pygame.mixer.music.fadeout(1000)
    pygame.time.delay(1000)
    pygame.mixer.music.load("8bit-music-for-game-68698.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1,fade_ms=1000)
    Crear_Ventana_Dialogo()


gif= Image.open("Gen-4 Turbo Make this binary code pulse, shimmer, or shift vertically in a seamless loop, green futurist style 341999774.mp4.gif")
frames = [ImageTk.PhotoImage(frame.copy().resize((600,650))) for frame in ImageSequence.Iterator(gif)]

Fondo_Label = tk.Label(Ventana_Principal)
Fondo_Label.place(x = 0, y = 0, relwidth= 1 , relheight= 1)

def animar (i):
    Fondo_Label.config(image=frames[i])
    Ventana_Principal.after(100, animar, (i + 1) % len(frames))

animar(0)




Primer_Frame = tk.Frame(Ventana_Principal, bg="dark slate gray")
Primer_Frame.place(x = 176, y = 20)

Segundo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Segundo_Frame.place(x = 205, y = 56)

Tercer_Frame = tk.Frame(Ventana_Principal, bg= "dark slate gray")
Tercer_Frame.place(x = 70 , y = 120)

Cuarto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Cuarto_Frame.place(x = 375, y = 192)

Quinto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Quinto_Frame.place(x = 170 , y = 297)

Sexto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Sexto_Frame.place(x = 120 , y = 358)

Septimo_Frame = tk.Frame(Ventana_Principal , bg = "dark slate gray")
Septimo_Frame.place(x = 570, y = 560)

Octavo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Octavo_Frame.place(x = 233, y = 413)

Noveno_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray" )
Noveno_Frame.place(x = 233, y = 453)

Decimo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Decimo_Frame.place(x = 137, y = 500)

Onceavo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Onceavo_Frame.place(x = 315 , y = 590)

Doceavo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Doceavo_Frame.place(x = 215, y = 590 )

Frame_13 = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Frame_13.place(x= 525, y = 605)


Imagen = Image.open("Icono11.png")
Imagen = Imagen.resize((170,170))

Img = ImageTk.PhotoImage(Imagen)

Imagen2 = Image.open("Icono8.png")
Imagen2 = Imagen2.resize((50,35))
Img3 = ImageTk.PhotoImage(Imagen2)

Imagen3 = Image.open("Icono9.png")
Imagen3 = Imagen3.resize((50,35))
Img4 = ImageTk.PhotoImage(Imagen3)

Imagen4 = Image.open("Icono10.png")
Imagen4 = Imagen4.resize((50,35))
Img5 = ImageTk.PhotoImage(Imagen4)





Titulo1 = tk.Label(Primer_Frame, text = "Encriptación" , font =("Century gothic" , 20, "bold"), fg = "beige", bg = "dark slate gray")
Titulo1.pack(side = "left")

Titulo2 = tk.Label(Primer_Frame, text = "IUE." , font =("Century gothic" , 20, "bold"), fg = "orange", bg = "dark slate gray")
Titulo2.pack(side = "left")

Eslogan = tk.Label(Segundo_Frame, text = "Codificando el futuro..." , font = ("Century gothic" , 10, "bold" ) , fg = "Orange" , bg = "dark slate gray")
Eslogan.pack()

Frase1 = tk.Label(Tercer_Frame, text = "Ingrese por favor el mensaje que desea codificar:" , font = ("Segoe UI" , 13 , "bold") , fg = "beige" , bg = "dark slate gray")
Frase1.pack()

Frase_2 = tk.Label(Quinto_Frame, text = "Simular Error de transmisión:" , font = ("Neuropol X" , 13 , "bold" ) , fg = "beige" , bg = "dark slate gray" )
Frase_2.pack()

Frase_3 = tk.Label(Sexto_Frame, text = "Cantidad de Errores:" , font = ("Neuropol X" , 11 , "bold" ) , fg = "Orange" , bg = "dark slate gray")
Frase_3.pack()


Entrada_Informacion = tk.Text( font = ("Century Gothic" , 10 , "bold") , bg = "gray" , fg = "beige" , borderwidth= 6, width = 35, height= 3,)
Entrada_Informacion.place( x = 70 , y = 185)

Salida_Informacion = tk.Text(Decimo_Frame,  font = ("Neuropol X" , 10 , "bold") , bg = "gray" , fg = "beige" , borderwidth= 6 , width= 40 , height= 3)
Salida_Informacion.config(state = "disabled")
Salida_Informacion.pack()


Primer_Boton = tk.Button(Cuarto_Frame, image = Img , bg = "dark slate gray" , borderwidth= 3, width= 65, height= 43)
Primer_Boton.pack()
Primer_Boton.image = Img

Segundo_Boton = tk.Button(Octavo_Frame, text = "Generar errores", font = ("Century Gothic ", 10 , "bold") , fg = "beige" , bg = "gray" , borderwidth= 3, width= 13)
Segundo_Boton.pack()

Tercer_Boton = tk.Button(Noveno_Frame, text = "Insertar", font = ("Century Gothic ", 10 , "bold") , fg = "beige" , bg = "gray" , borderwidth= 3, width= 13)
Tercer_Boton.pack()

Cuarto_Boton = tk.Button(Onceavo_Frame, image = Img3 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35 )
Cuarto_Boton.pack()

Quinto_Boton = tk.Button(Doceavo_Frame, image = Img4 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35)
Quinto_Boton.pack()

Sexto_Boton = tk.Button(Frame_13, image = Img5 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35 , command= Abrir_Ventana_Dialogo)
Sexto_Boton.pack()

Opciones = [1 , 2 , 3 , 4]

Caja_Opciones = ttk.Combobox(Ventana_Principal, values = Opciones, width= 20 , state = "readonly")
Caja_Opciones.place(x = 295 , y = 360)
Estilo = ttk.Style()
Estilo.theme_use("default")
Estilo.configure("TCombobox" ,fieldbackground = "gray",  arrowcolor = "beige" , font = ("Century Gothic" , 20 , "bold"))





Ventana_Principal.mainloop() 