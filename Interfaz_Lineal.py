import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound 

def Click_PrimerBoton():
    playsound("sfx28-attack-338386.mp3")

Ventana_Principal = tk.Tk()
Ventana_Principal.title("Codificación Hamming.")
Ventana_Principal.geometry("600x650")
Ventana_Principal.resizable(width=False, height=False)

Imagen1 = Image.open("BI.png")
Imagen1 = Imagen1.resize((600,650))

Imag1 = ImageTk.PhotoImage(Imagen1)

Fondo_Label = tk.Label(Ventana_Principal, image = Imag1)
Fondo_Label.place(x = 0, y = 0, relwidth= 1 , relheight= 1)





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


Imagen = Image.open("Icono5.png")
Imagen = Imagen.resize((170,170))

Img = ImageTk.PhotoImage(Imagen)

Imagen2 = Image.open("Icono8.png")
Imagen2 = Imagen2.resize((50,35))
Img3 = ImageTk.PhotoImage(Imagen2)

Imagen3 = Image.open("Icono9.png")
Imagen3 = Imagen3.resize((50,35))
Img4 = ImageTk.PhotoImage(Imagen3)




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


Primer_Boton = tk.Button(Cuarto_Frame, image = Img , bg = "dark slate gray" , borderwidth= 3, width= 65, height= 43, command = Click_PrimerBoton)
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

Opciones = [1 , 2 , 3 , 4]

Caja_Opciones = ttk.Combobox(Ventana_Principal, values = Opciones, width= 20 , state = "readonly")
Caja_Opciones.place(x = 295 , y = 360)
Estilo = ttk.Style()
Estilo.theme_use("default")
Estilo.configure("TCombobox" ,fieldbackground = "gray",  arrowcolor = "beige" , font = ("Century Gothic" , 20 , "bold"))





Ventana_Principal.mainloop() 