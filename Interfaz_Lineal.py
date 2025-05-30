import tkinter as tk
import threading
import random
import pygame
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from playsound import playsound 

HAMMING_GLOBAL = "null"
CORRECION = 0
BARRA = 0
VALIDEZ = True



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

style = ttk.Style()
style.theme_use("clam")
style.configure("Myneon.Vertical.TProgressbar" , troughcolor= "#1a0000" , background = "#ff1414" , thickness = 24, bordercolor = "#ff00ff" , lightcolor = "#ff00ff" , darkcolor = "#50039c")



    


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

def Texto_A_Binario(texto):
    return "".join(format(ord(char),"08b")for char in texto)


def Aplicar_Hamming(binario):
    if len(binario) % 4 != 0:
        binario = binario.ljust(len(binario) + (4 - len(binario) % 4), "0")

    bloques = [binario[i:i+4] for i in range(0,len(binario), 4)]
    resultado = ""

    for bloque in bloques:
        d1 = int(bloque[0])
        d2 = int(bloque[1])
        d3 = int(bloque[2])
        d4 = int(bloque[3])

        p1 = (d1 ^ d2 ^ d4) 
        p2 = (d1 ^ d3 ^ d4) 
        p3 = (d2 ^ d3 ^ d4) 

        hamming = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
        resultado += hamming

    return resultado

progreso_valor = 0
barra_progreso = ttk.Progressbar(Ventana_Principal, style= "Myneon.Vertical.TProgressbar" , orient = "vertical" , length = 250, mode = "determinate")
barra_progreso.place(x = 570, y = 260)
barra_progreso["maximum"] = 100
barra_progreso["value"] = progreso_valor

def Aumentar_barra(Cantidad):
    global progreso_valor
    progreso_valor += Cantidad
    if progreso_valor > 100:
        progreso_valor = 100
    barra_progreso["value"] = progreso_valor



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

Salida_Informacion = tk.Text(Decimo_Frame,  font = ("Neuropol X" , 10 , "bold") , bg = "gray" , fg = "beige" , borderwidth= 6 , width= 40 , height= 3, wrap = "word")
Salida_Informacion.config(state = "disabled")
Salida_Informacion.pack(side = "left" , fil = "both" , expand = True)



Opciones = [1 , 2 , 3 , 4]

Caja_Opciones = ttk.Combobox(Ventana_Principal, values = Opciones, width= 20 , state = "readonly")
Caja_Opciones.place(x = 295 , y = 360)
Estilo = ttk.Style()
Estilo.theme_use("default")
Estilo.configure("TCombobox" ,fieldbackground = "gray",  arrowcolor = "beige" , font = ("Century Gothic" , 20 , "bold"))


def Crear_Ventanas_De_Aviso(Valor):

    global HAMMING_GLOBAL
    global BARRA
    global VALIDEZ
    global Salida_Informacion
    global CORRECION
    Ventana_Avisos = tk.Toplevel()
    Ventana_Avisos.title("Aviso.")
    Ventana_Avisos.resizable(False, False)

    

    if Valor == 1:
        
        Texto = Entrada_Informacion.get("1.0", "end-1c")
        

        
        if not Texto.strip():
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI3.png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            HAMMING_GLOBAL = "null"

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame_Gif.place(x = 10, y = 10)

            gif = Image.open("Migue_Pixel.gif")

            Personaje_GIF = tk.PhotoImage("Migue_Pixel.gif")
            Label_NPC = tk.Label(Frame_Gif, image = Personaje_GIF, bg = "yellow")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir(frame = 0):
                gif.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif.n_frames
                Ventana_Avisos.after(100, Reproducir, frame)

           
            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=255, height=80, bd = 2, relief = "ridge")
            Framee_Texto.place(x=160, y=60)  # Ajustado para quedar justo al lado del GIF

            mensajes = [
                "¡No puedo codificar el vacío!",
                "¿Acaso querés encriptar la nada?",
                "Recuerda, cyber-usuario: escribí tu mensaje y luego oprimí el botón."]
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(mensajes):
                    Animaar_Texto(mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Dale, escribí algo e intentá nuevamente.")


            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=396, y=122)
            BARRA = 0
            
            Reproducir()
            mostrar_Siguiente()
           
            
            return  


        Ventana_Avisos.geometry("300x150")
        fondo34 = Image.open("BI3.png").resize((300, 150))
        fondo34_tk = ImageTk.PhotoImage(fondo34)
        fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
        fondo34_Label.image = fondo34_tk
        fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)
        
        BINARIO = Texto_A_Binario(Texto)
        HAMMING_GLOBAL = Aplicar_Hamming(BINARIO)
        print(HAMMING_GLOBAL)
        CORRECION = 0

        VALIDEZ = True
        #Entrada_Informacion.delete("1.0", tk.END)

        
        Frame_Aviso1 = tk.Frame(Ventana_Avisos, bg="gray")
        Frame_Aviso1.place(x=25, y=40)

       
        Imagen_EXITO = Image.open("Icono8.png").resize((50, 50))
        imagen_B = ImageTk.PhotoImage(Imagen_EXITO)
        Label_Imagen100 = tk.Label(Frame_Aviso1, image=imagen_B, bg="gray")
        Label_Imagen100.grid(row=0, column=0, padx=5)

        
        Mensaje = "¡CÓDIGO ENCRIPTADO!"
        Texto_Label2 = tk.Label(Frame_Aviso1, text="", font=("Century Gothic", 10, "bold"), fg="beige", bg="gray", wraplength=180, justify="left")
        Texto_Label2.grid(row=0, column=1, padx=5)

        
        def Animar_Imagen(angulo=0):
            Imagen_Rotada = Imagen_EXITO.rotate(angulo)
            Imagen_B2 = ImageTk.PhotoImage(Imagen_Rotada)
            Label_Imagen100.config(image=Imagen_B2)
            Label_Imagen100.image = Imagen_B2
            Ventana_Avisos.after(100, Animar_Imagen, (angulo - 10) % 360)

        
        def Animar_Texto(i=0):
            if i <= len(Mensaje):
                Texto_Label2.config(text=Mensaje[:i])
                Ventana_Avisos.after(50, Animar_Texto, i + 1)

        
        Animar_Imagen()
        Animar_Texto()
        if BARRA == 0:
            Aumentar_barra(20)
            BARRA += 1


    elif Valor == 2:
        Valor = Caja_Opciones.get()

        if HAMMING_GLOBAL == "null":
            Ventana_Principal.withdraw
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI4.png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)
                
            Frame_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame_Gif.place(x = 10, y = 10)

            gif = Image.open("Sebas (1).gif")

            Personaje_GIF = tk.PhotoImage("Sebas (1).gif")
            Label_NPC = tk.Label(Frame_Gif, image = Personaje_GIF, bg = "red")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir(frame = 0):
                gif.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif.n_frames
                Ventana_Avisos.after(100, Reproducir, frame)

            
            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
            Framee_Texto.place(x=155, y=56)  # Ajustado para quedar justo al lado del GIF

            mensajes = [
                "¡Ey parce!... ¿Qué más pués?",
                "¿Pretendes integrar errores sin antes codificar?",
                "Recuerda, cyber-usuario: Antes de simular cualquier tipo de error, debes primero hacer estos pasos." ,
                "Escribe el mensaje en el recuadro y luego oprimes el botón." , "Una vez que te salga el aviso de Encriptación..." ,
                "Vuelves a mi apartado, seleccionas la cantidad de errores y oprimes el botón. "
                ]
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(mensajes):
                    Animaar_Texto(mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Dale, has el proceso y luego integra los errores.")


            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=400, y=122)

            Reproducir()
            mostrar_Siguiente()

                
        elif HAMMING_GLOBAL != "null" and Valor == "":
            Ventana_Principal.withdraw
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI4 (2).png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame1_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame1_Gif.place(x = 10, y = 10)

            gif1 = Image.open("Tomas.gif")

            Personaje_GIF = tk.PhotoImage("Tomas.gif")
            Label_NPC = tk.Label(Frame1_Gif, image = Personaje_GIF, bg = "purple")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir1(frame = 0):
                gif1.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif1.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif1.n_frames
                Ventana_Avisos.after(100, Reproducir1, frame)

            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
            Framee_Texto.place(x=155, y=56) 

            Mensajes = ["¿Qué tal, Cyber usuario?..." , "Veo que no entendiste al bobo de Sebastián..." ,
                 "No te preocupes, me pasa igual cuando estoy con él en los exámenes..." , "¡Ya tienes el mensaje codificado!" ,
                 "Solo debes escoger la cantidad de errores que quieres simular en la codificación."     
                        ]
            
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(Mensajes):
                    Animaar_Texto(Mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Dale parce, vamos con una buena codificación...")
                
            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=400, y=122)

            Reproducir1()
            mostrar_Siguiente()
            
        elif HAMMING_GLOBAL != "null" and Valor != "": 

            Ventana_Avisos.geometry("300x150")
            fondo34 = Image.open("BI4 (2).png").resize((300, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            Frame_Aviso1 = tk.Frame(Ventana_Avisos, bg="gray")
            Frame_Aviso1.place(x=25, y=40)
                    

            Imagen_EXITO = Image.open("Icono8.png").resize((50, 50))
            imagen_B = ImageTk.PhotoImage(Imagen_EXITO)
            Label_Imagen100 = tk.Label(Frame_Aviso1, image=imagen_B, bg="gray")
            Label_Imagen100.grid(row=0, column=0, padx=5)

            
            Mensaje = "¡ERRORES INTEGRADOS!"
            Texto_Label2 = tk.Label(Frame_Aviso1, text="", font=("Century Gothic", 10, "bold"), fg="beige", bg="gray", wraplength=180, justify="left")
            Texto_Label2.grid(row=0, column=1, padx=5)

            
            def Animar_Imagen(angulo=0):
                Imagen_Rotada = Imagen_EXITO.rotate(angulo)
                Imagen_B2 = ImageTk.PhotoImage(Imagen_Rotada)
                Label_Imagen100.config(image=Imagen_B2)
                Label_Imagen100.image = Imagen_B2
                Ventana_Avisos.after(100, Animar_Imagen, (angulo - 10) % 360)

            def Animar_Texto(i=0):
                if i <= len(Mensaje):
                    Texto_Label2.config(text=Mensaje[:i])
                    Ventana_Avisos.after(50, Animar_Texto, i + 1)

        
            Animar_Imagen()
            Animar_Texto()

            Errores_a_Insertar = int(Caja_Opciones.get())
            LISTA_BITS = list(HAMMING_GLOBAL)
            posiciones = random.sample(range(len(LISTA_BITS)) ,Errores_a_Insertar)

            for pos in posiciones:

                if LISTA_BITS[pos] == "1":
                    LISTA_BITS[pos] = "0"

                else:
                    LISTA_BITS[pos] = "1"

            HAMMING_GLOBAL = "".join(LISTA_BITS)
            print(HAMMING_GLOBAL)
            if BARRA == 1:
                Aumentar_barra(20)
                BARRA += 1
            CORRECION = 1
            
    elif Valor == 3:

        if HAMMING_GLOBAL == "null":
            Ventana_Principal.withdraw
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI5.png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame1_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame1_Gif.place(x = 10, y = 10)

            gif1 = Image.open("Valery.gif")

            Personaje_GIF = tk.PhotoImage("Valery.gif")
            Label_NPC = tk.Label(Frame1_Gif, image = Personaje_GIF, bg = "pink")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir1(frame = 0):
                gif1.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif1.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif1.n_frames
                Ventana_Avisos.after(100, Reproducir1, frame)

            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
            Framee_Texto.place(x=155, y=56) 

            Mensajes = ["¡¡Que gusto verte, Cyber usuario!!" , "Veo que intentas insertar un código en el recuadro de abajo..." ,
                 "Upss. Visualizo un problema, aún no has ingresado el mensaje..." , "No te preocupes, es super sencillo de solucionar..." ,
                       ]
            
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(Mensajes):
                    Animaar_Texto(Mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Escribe el mensaje y oprime el boton, ¡¡eso es todo!!...")
                
            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=400, y=122)

            Reproducir1()
            mostrar_Siguiente()
            
        
        else:
            Ventana_Avisos.destroy()
            Salida_Informacion.config(state = "normal")
            Salida_Informacion.delete("1.0" , tk.END) 
            Salida_Informacion.insert(tk.END , HAMMING_GLOBAL)
            Salida_Informacion.config(state = "disabled")
            if BARRA == 2:
                Aumentar_barra(20)
                BARRA += 1
            
        
            
    elif Valor == 4:

        if HAMMING_GLOBAL == "null":
            Ventana_Principal.withdraw
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI2.png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame1_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame1_Gif.place(x = 10, y = 10)

            gif1 = Image.open("XLP24.gif")

            Personaje_GIF = tk.PhotoImage("XLP24.gif")
            Label_NPC = tk.Label(Frame1_Gif, image = Personaje_GIF, bg = "blue")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir1(frame = 0):
                gif1.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif1.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif1.n_frames
                Ventana_Avisos.after(100, Reproducir1, frame)

            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
            Framee_Texto.place(x=155, y=56) 

            Mensajes = ["¡¡Hey, Cyber usuario!!" , "Es un placer conocerte, soy XLP24, el asistente pixel de los chicos..." ,
                 "Veo que intentas corregir errores simulados..." , "Sin embargo, los datos me dicen que no has codificado ningún mensaje..." ,
                       ]
            
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(Mensajes):
                    Animaar_Texto(Mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Escribe el mensaje, luego codificalo, selecciona la cantidad de errores, inserta y listo.")
                
            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=400, y=122)

            Reproducir1()
            mostrar_Siguiente()

        elif HAMMING_GLOBAL != "null" and CORRECION == 0:
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI3.png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)


            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame_Gif.place(x = 10, y = 10)

            gif = Image.open("Migue_Pixel.gif")

            Personaje_GIF = tk.PhotoImage("Migue_Pixel.gif")
            Label_NPC = tk.Label(Frame_Gif, image = Personaje_GIF, bg = "yellow")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir(frame = 0):
                gif.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif.n_frames
                Ventana_Avisos.after(100, Reproducir, frame)

           
            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=255, height=80, bd = 2, relief = "ridge")
            Framee_Texto.place(x=160, y=60)  # Ajustado para quedar justo al lado del GIF

            mensajes = [
                "¡Hey Cyber Usuario, es un gusto volverte a ver!... ",
                "Parece que intentas corregir un código que no tiene nigún tipo de error...",
                "Recuerda, cyber-usuario: Si deseas integrar errores..." , "dirigite a la caja de opciones y seleccionas la cantidad..."]
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(mensajes):
                    Animaar_Texto(mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="O directamente decodifica el mensaje con el botón de decodificación.")


            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=396, y=122)

            
            Reproducir()
            mostrar_Siguiente()

        elif HAMMING_GLOBAL != "null" and CORRECION == 1:
            Ventana_Avisos.destroy()
            bloques = [HAMMING_GLOBAL[i:i + 7] for i in range(0, len(HAMMING_GLOBAL), 7)]
            bloques_corregidos = []
            error_no_corregible = False
            errores_detectados = 0

            for bloque in bloques:
                if len(bloque) < 7:
                    continue

        
                bits = list(map(int, bloque))

        
                p1, p2, d1, p3, d2, d3, d4 = bits

        
                s1 = p1 ^ d1 ^ d2 ^ d4
                s2 = p2 ^ d1 ^ d3 ^ d4
                s3 = p3 ^ d2 ^ d3 ^ d4

        
                syndrome = s1 * 1 + s2 * 2 + s3 * 4

                if syndrome == 0:
            
                    bloques_corregidos.append(bloque)
                elif 1 <= syndrome <= 7:
                    errores_detectados += 1
                    if errores_detectados > 1:
                        Ventana_Avisos1 = tk.Toplevel()
                        Ventana_Avisos1.title("AVISO")
                        Ventana_Principal.withdraw()
                        Ventana_Avisos1.geometry("450x150")
                        fondo34 = Image.open("BI4.png").resize((450, 150))
                        fondo34_tk = ImageTk.PhotoImage(fondo34)
                        fondo34_Label = tk.Label(Ventana_Avisos1, image=fondo34_tk)
                        fondo34_Label.image = fondo34_tk
                        fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

                        def Cerra_Aviso():
                            Ventana_Avisos1.destroy()
                            Ventana_Principal.wm_deiconify()

                        Ventana_Avisos1.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)
                            
                        Frame_Gif = tk.Frame(Ventana_Avisos1, bg = "gray" , width= 150 , height = 130)
                        Frame_Gif.place(x = 10, y = 10)

                        gif = Image.open("Sebas (1).gif")

                        Personaje_GIF = tk.PhotoImage("Sebas (1).gif")
                        Label_NPC = tk.Label(Frame_Gif, image = Personaje_GIF, bg = "red")
                        Label_NPC.image = Personaje_GIF
                        Label_NPC.pack(expand =True)

                        def Reproducir(frame = 0):
                            gif.seek(frame)
                            Fotogramas = ImageTk.PhotoImage(gif.copy())
                            Label_NPC.config(image = Fotogramas)
                            Label_NPC.image = Fotogramas

                            frame = (frame + 1) % gif.n_frames
                            Ventana_Avisos1.after(100, Reproducir, frame)

            
                        Framee_Texto = tk.Frame(Ventana_Avisos1, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
                        Framee_Texto.place(x=155, y=56)  # Ajustado para quedar justo al lado del GIF

                        mensajes = [
                            "Que chimba volverte a ver, Cyber usuario...",
                            "Veo que ya estás comprendiendo cómo funciona este programa...",
                            "Has integrado más de un error..." , "pero ahora mismo contamos con HAMMING (7,4)..." ,
                            "Por lo cual solo podemos corregir un error a la vez..." 
                        ]
                        indice = [0]


                        Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
                        Textoo_Label.place(x=10, y=15)

                        def Animaar_Texto(texto, i=0):
                            if i <= len(texto):
                                Textoo_Label.config(text=texto[:i])
                                Ventana_Avisos1.after(40, lambda: Animaar_Texto(texto, i + 1))

                        def mostrar_Siguiente():
                            if indice[0] < len(mensajes):
                                Animaar_Texto(mensajes[indice[0]])
                                indice[0] += 1
                            else:
                                Textoo_Label.config(text="Estamos trabajando para actualizar nuestro código HAMMING.")


                        Botoon_Sig = tk.Button(
                        Ventana_Avisos1, text="▶", command=mostrar_Siguiente,
                        bg="gray20", fg="white", font=("Arial", 10, "bold"),
                        width=2, height=1, borderwidth=0, relief="flat",
                        activebackground="gray30")
                        Botoon_Sig.place( x=400, y=122)

                        Reproducir()
                        mostrar_Siguiente()
                        return  



                    bits[syndrome - 1] ^= 1
                    bloque_corregido = ''.join(map(str, bits))
                    bloques_corregidos.append(bloque_corregido)
                    VALIDEZ = True
        else:
            bloques_corregidos.append(bloque)
                
        HAMMING_GLOBAL = ''.join(bloques_corregidos)

        Salida_Informacion.config(state = "normal")
        Salida_Informacion.delete("1.0" , tk.END) 
        Salida_Informacion.insert(tk.END , HAMMING_GLOBAL)
        Salida_Informacion.config(state = "disabled")

    elif Valor == 5:

        if VALIDEZ == False:
            Ventana_Principal.withdraw()
            Ventana_Avisos.geometry("450x150")
            fondo34 = Image.open("BI4 (2).png").resize((450, 150))
            fondo34_tk = ImageTk.PhotoImage(fondo34)
            fondo34_Label = tk.Label(Ventana_Avisos, image=fondo34_tk)
            fondo34_Label.image = fondo34_tk
            fondo34_Label.place(x=0, y=0, relwidth=1, relheight=1)

            def Cerra_Aviso():
                Ventana_Avisos.destroy()
                Ventana_Principal.wm_deiconify()

            Ventana_Avisos.protocol("WM_DELETE_WINDOW" , Cerra_Aviso)

            Frame1_Gif = tk.Frame(Ventana_Avisos, bg = "gray" , width= 150 , height = 130)
            Frame1_Gif.place(x = 10, y = 10)

            gif1 = Image.open("Tomas.gif")

            Personaje_GIF = tk.PhotoImage("Tomas.gif")
            Label_NPC = tk.Label(Frame1_Gif, image = Personaje_GIF, bg = "purple")
            Label_NPC.image = Personaje_GIF
            Label_NPC.pack(expand =True)

            def Reproducir1(frame = 0):
                gif1.seek(frame)
                Fotogramas = ImageTk.PhotoImage(gif1.copy())
                Label_NPC.config(image = Fotogramas)
                Label_NPC.image = Fotogramas

                frame = (frame + 1) % gif1.n_frames
                Ventana_Avisos.after(100, Reproducir1, frame)

            Framee_Texto = tk.Frame(Ventana_Avisos, bg="gray", width=265, height=85, bd = 2, relief = "ridge")
            Framee_Texto.place(x=155, y=56) 

            Mensajes = ["Todo bien, Cyber usuario..." , "Veo que intentas decodificar un mensaje con errores..." ,
                 "Esto no es posible..."      
                ]
            
            indice = [0]


            Textoo_Label = tk.Label(Framee_Texto, text="", font=("Century Gothic", 10 , "bold"),fg="black", bg="gray", justify="left", wraplength=250)
            Textoo_Label.place(x=10, y=15)

            def Animaar_Texto(texto, i=0):
                if i <= len(texto):
                    Textoo_Label.config(text=texto[:i])
                    Ventana_Avisos.after(40, lambda: Animaar_Texto(texto, i + 1))

            def mostrar_Siguiente():
                if indice[0] < len(Mensajes):
                    Animaar_Texto(Mensajes[indice[0]])
                    indice[0] += 1
                else:
                    Textoo_Label.config(text="Por favor corrige los errores oprimiendo el botón corregir.")
                
            Botoon_Sig = tk.Button(
            Ventana_Avisos, text="▶", command=mostrar_Siguiente,
            bg="gray20", fg="white", font=("Arial", 10, "bold"),
            width=2, height=1, borderwidth=0, relief="flat",
            activebackground="gray30")
            Botoon_Sig.place( x=400, y=122)

            Reproducir1()
            mostrar_Siguiente()

        elif VALIDEZ == True:
            Ventana_Avisos.destroy()
            if BARRA == 3:
                Aumentar_barra(40)
                BARRA += 1
            bloques = [HAMMING_GLOBAL[i:i+7] for i in range (0,len(HAMMING_GLOBAL), 7)] 
            datos_binarios = ""

            for bloque in bloques:
                if len(bloque) == 7:
                    datos = bloque[2] + bloque[4] + bloque[5] + bloque[6]
                    datos_binarios += datos

            texto = ""
            for i in range(0, len(datos_binarios) , 8):
                byte = datos_binarios[i:i+8]
                if len(byte) == 8:
                    texto += chr(int(byte,2))

            Salida_Informacion.config(state = "normal")
            Salida_Informacion.delete("1.0" , tk.END) 
            Salida_Informacion.insert(tk.END , texto)
            Salida_Informacion.config(state = "disabled")

def REINICIO():
    global HAMMING_GLOBAL, BARRA, CORRECION, VALIDEZ, progreso_valor
    HAMMING_GLOBAL = "null"
    BARRA = 0
    CORRECION = 0
    VALIDEZ = True
    progreso_valor = 0
    barra_progreso["value"] = progreso_valor

    Entrada_Informacion.delete("1.0" , tk.END)

    Salida_Informacion.config(state = "normal")
    Salida_Informacion.delete("1.0" , tk.END) 
    Salida_Informacion.config(state = "disabled")




            












Primer_Boton = tk.Button(Cuarto_Frame, image = Img , bg = "dark slate gray" , borderwidth= 3, width= 65, height= 43 , command = lambda: Crear_Ventanas_De_Aviso(1) )
Primer_Boton.pack()
Primer_Boton.image = Img

Segundo_Boton = tk.Button(Octavo_Frame, text = "Generar errores", font = ("Century Gothic ", 10 , "bold") , fg = "beige" , bg = "gray" , borderwidth= 3, width= 13, command = lambda: Crear_Ventanas_De_Aviso(2))
Segundo_Boton.pack()

Tercer_Boton = tk.Button(Noveno_Frame, text = "Insertar", font = ("Century Gothic ", 10 , "bold") , fg = "beige" , bg = "gray" , borderwidth= 3, width= 13, command = lambda: Crear_Ventanas_De_Aviso(3) )
Tercer_Boton.pack()

Cuarto_Boton = tk.Button(Onceavo_Frame, image = Img3 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35, command = lambda: Crear_Ventanas_De_Aviso(5) )
Cuarto_Boton.pack()

Quinto_Boton = tk.Button(Doceavo_Frame, image = Img4 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35, command = lambda: Crear_Ventanas_De_Aviso(4))
Quinto_Boton.pack()

Sexto_Boton = tk.Button(Frame_13, image = Img5 ,bg = "dark slate gray" , borderwidth = 2, width= 50 , height = 35 , command= REINICIO)
Sexto_Boton.pack()







Ventana_Principal.mainloop() 