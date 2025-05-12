import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound 

def Click_PrimerBoton():
    playsound("sfx28-attack-338386.mp3")

Ventana_Principal = tk.Tk()
Ventana_Principal.title("Codificación Hamming.")
Ventana_Principal.geometry("600x600")
Ventana_Principal.resizable(width=False, height=False)

Imagen1 = Image.open("BI.png")
Imagen1 = Imagen1.resize((600,600))

Imag1 = ImageTk.PhotoImage(Imagen1)

Fondo_Label = tk.Label(Ventana_Principal, image = Imag1)
Fondo_Label.place(x = 0, y = 0, relwidth= 1 , relheight= 1)





Primer_Frame = tk.Frame(Ventana_Principal, bg="dark slate gray")
Primer_Frame.place(x = 176, y = 20)

Segundo_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Segundo_Frame.place(x = 205, y = 56)

Tercer_Frame = tk.Frame(Ventana_Principal, bg= "dark slate gray")
Tercer_Frame.place(x = 12 , y = 120)

Cuarto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Cuarto_Frame.place(x = 290, y = 168)

Quinto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Quinto_Frame.place(x = 65 , y = 254)

Sexto_Frame = tk.Frame(Ventana_Principal, bg = "dark slate gray")
Sexto_Frame.place(x = 100 , y = 290)

Septimo_Frame = tk.Frame(Ventana_Principal , bg = "dark slate gray")
Septimo_Frame.place(x = 570, y = 560)



Imagen = Image.open("Icono5.png")
Imagen = Imagen.resize((170,170))

Img = ImageTk.PhotoImage(Imagen)




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




Entrada_Informacion = tk.Text( font = ("Century Gothic" , 10 , "bold") , bg = "gray" , fg = "beige" , borderwidth= 3, width = 35, height= 3,)
Entrada_Informacion.place( x = 18 , y = 165)


Primer_Boton = tk.Button(Cuarto_Frame, image = Img , bg = "dark slate gray" , borderwidth= 3, width= 65, height= 43, command = Click_PrimerBoton)
Primer_Boton.pack()
Primer_Boton.image = Img

Boton_Duda = tk.Button(Septimo_Frame, text = "?", font = ("Century Gothic" , 10, "bold") , fg = "black", bg = "gray" , borderwidth= 1 , width= 1 , height= 1)
Boton_Duda.pack()

Opciones = [1 , 2 , 3 , 4]

Caja_Opciones = ttk.Combobox(Ventana_Principal, values = Opciones, width= 20 , state = "readonly")
Caja_Opciones.place(x = 110 , y = 324)
Estilo = ttk.Style()
Estilo.theme_use("default")
Estilo.configure("TCombobox" ,fieldbackground = "gray",  arrowcolor = "beige" , font = ("Century Gothic" , 20 , "bold"))





Ventana_Principal.mainloop() 