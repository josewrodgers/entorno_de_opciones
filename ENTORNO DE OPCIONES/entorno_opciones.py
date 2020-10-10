"""
JUEGO OPCIONES


1. Crear la clase opción(base,side,vencimiento):                    LISTO
2. Crear todas las bases y meterlas en un diccionario               MEJOR EN UN DF
3. Crear la tenencia de las opciones                                                        FALTA
4. Crear un subyascente y sus variaciones RANDOM                    LISTO
5. Hacer que el comportamiento de las opciones tenga coherencia con el subyascente, respetando valor intrinseco y poniendo un valor extrinseco random     LISTO
6. Hacer grafico de resultado al vencimiento y resultado teórico    LISTO AL VTO            FALTA EL TEORICO
    A. Cotizacion fluyendo                                          LISTO
    B. Cuadro de posición                                           LISTO
    C. Agregar esos plots al tkinter                                LISTO
    D. Poner verde/rojo cuando titilen                              LISTO
    E. Poner los checkbox para cada opción                          LISTO
    F. Poner el formulario de cantidad para comprar y checks para market o limit   MEJOR NO
7. Hacer aplicación gráfica                                         LISTO
8. Guardar datos en .txt                                                                    FALTA


(ENTORNO DIDÁCTICO - PRÁCTICA)

.... and MOST IMPORTANT:
9. Conectar con Datos reales.                                                               FALTA
Para eso:
* Investigar conexión websocket de IOL                                                      FALTA
* Enlazar los JSON con las clases                                                           FALTA
* Crear un menú para elegir entre entorno práctica y entorno real                           FALTA


(ENTORNO REAL - OPERAR EN TIEMPO REAL)





*LINEA X
*ARREGLAR GGAL
"""
from datetime import datetime
import time
import numpy as np
import random
import pandas as pd
import tkinter as tk
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker
from scipy.stats import norm


"""
root = tk.Tk()
root.geometry("500x500")
root.title("Entorno de opciones GGAL")
root.pack_propagate(False)
root.resizable(0,0) #No puede agrandarse, ni achicarse la ventana


frame1 = tk.LabelFrame(root,text="Tabla")
frame1.place(height=250,width=500)

file_frame = tk.LabelFrame(root,text="Open File")
file_frame.place(height=100,width=400,rely=0.65,relx=0)

button1 = tk.Button(file_frame,text="Browse a File")
button1.place(rely=0.65,relx=0.5)

button2 = tk.Button(file_frame,text= "Load a File")
button2.place(rely=0.65,relx=0.3)

label_file = ttk.Label(file_frame,text="No file Selected")
label_file.place(rely=0,relx=0)

#Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1,relwidth=1)

treescrolly = tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
treescrollx = tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand = treescrollx.set,yscrollcommand= treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")





root.mainloop()

"""


# Poner mayusculas a las clases
# Eliminar al vender

class Ggal:

    def __init__(self,price):
        self.price = price
        self.pendientes = 0

    def __str__(self):
        return "GGAL"




class Contexto:

    def __init__(self):
        self.contextos = {1:{"Subiendo, muy volátil":[round(x,2) for x in np.arange(-1,4,0.1)]},
                     2:{"Subiendo, volatilidad media":[round(x,2) for x in np.arange(-1,3,0.1)]},
                     3:{"Subiendo, poca volatilidad": [round(x,2) for x in np.arange(-1,2,0.1)]},
                     4:{"Lateral, muy volátil": [round(x,2) for x in np.arange(-3,3,0.1)]},
                     5:{"Lateral, volatilidad media": [round(x,2) for x in np.arange(-2,2,0.1)]},
                     6:{"Lateral, poca volatilidad": [round(x,2) for x in np.arange(-1,1,0.1)]},
                     7:{"Bajando, muy volátil": [round(x,2) for x in np.arange(-4,1,0.1)]},
                     8:{"Bajando, volatilidad media": [round(x,2) for x in np.arange(-3,1,0.1)]},
                     9:{"Bajando, poca volatilidad": [round(x,2) for x in np.arange(-2,1,0.1)]}
                     }

        self.contexto = random.randint(1,9)
        self.possibilities = list(self.contextos[self.contexto].values())[0]
        self.vto = 0

    def __str__(self):
        return str(list(self.contextos[self.contexto].keys())[0]).upper()

    def sortear_contexto(self):
        print(random.randint(1, 9),list(self.contextos[self.contexto].values())[0])
        self.contexto = random.randint(1, 9)
        self.possibilities = list(self.contextos[self.contexto].values())[0]
        subyascente.price += random.choice(self.possibilities)







class Opcion:

    def __init__(self,base,side):
        self.base = base
        self.side = side
        self.ticker = "GGAL"+"_"+self.side+"_"+str(self.base)+"_10"
        self.arbitrado = True


        if self.side == "C":
            if subyascente.price >= self.base:
                self.prima = subyascente.price - self.base
                self.estado = True
            else:
                self.prima = 0.1
                self.estado = False
        else:
            if subyascente.price <= self.base:
                self.prima = self.base - subyascente.price
                self.estado = True
            else:
                self.prima = 0.1
                self.estado = False


    def __str__(self):
        return self.ticker

    def restar_día(self,arbitrado):
        self.arbitrado = arbitrado

    def actualizar_prima(self):
        if self.side == "C":
            if subyascente.price >= self.base:
                self.estado = True
            else:
                self.estado = False
        else:
            if subyascente.price <= self.base:
                self.estado = True
            else:
                self.estado = False

        if self.arbitrado:
            if self.side == "C":
                if subyascente.price >= self.base:
                    self.prima = subyascente.price - self.base
                else:
                    self.prima = 0.1
            else:
                if subyascente.price <= self.base:
                    self.prima = self.base - subyascente.price
                else:
                    self.prima = 0.1







class Cartera:

    def __init__(self,efectivo):
        self.efectivo = efectivo
        self.acciones = 0
        self.opciones = 0
        self.total_opciones = 0
        self.opciones_details = list()
        self.total = efectivo
        self.suma = [0 for x in x]

    def __str__(self):
        return "Mi Cartera"

    def buy_ggal(self,cant,market=True):
        if market:
            if self.efectivo >= cant * subyascente.price:
                self.efectivo -= cant * subyascente.price
                self.acciones += cant

        cant *= 100

        precio_conseguido = df.loc["GGAL", "Prima"]

        df.loc["GGAL", "Cantidad"] = self.acciones
        df.loc["GGAL", "Tenencia"] = df.loc["GGAL", "Prima"] * self.acciones

        total = (df.loc["GGAL", "Valor Actual"])

        df.loc["GGAL", "PP"] = (df.loc["GGAL", "PP"] * (df.loc["GGAL", "Cantidad"] - cant) + (
                    df.loc["GGAL", "Prima"] *
                    cant)) / total

        recta = [round((x - precio_conseguido)*cant,2) for x in x]
        self.suma = [self.suma[x] + recta[x] for x in range(len(self.suma))]










    def buy_opc(self,cant,name,market,prima,lote=100):
        list = name.split("_")
        if market == "y":
            if self.efectivo >= cant * lote * df.loc[name,"Prima"]:
                self.efectivo -= cant * lote * df.loc[name,"Prima"]

        if cant > 0:
            compra = True
        else:
            compra = False


        self.opciones_details.append([int(list[2]),prima,list[1],compra])
        self.suma = graph(self.suma,self.opciones_details[-1])




    def actualizar(self):
        self.opciones = list(df.loc[df["Cantidad"] != 0, "Tenencia"])
        self.total_opciones = round(sum(self.opciones),2)
        self.total = self.efectivo + self.acciones * subyascente.price + self.total_opciones




def y_graph(base,prima,side,compra,lote=100):
    """
    Determina la curva de una opción, sea call/put comprado/lanzado
    """
    global x


    if side == "C":
        """
        compra True = comprar call (view alcista)
        compra False = lanzar call (view bajista)
        """
        if compra:
            return [-prima * lote if x <= base else round((x - (base+prima)) * lote,2) for x in x ]
        return [prima * lote if x <= base else round(((base+prima) - x) * lote ,2)  for x in x ]

    else:
        """
        compra True = comprar put (view bajista)
        compra False = lanzar put (view alcista)
        """
        if compra:
            return [-prima * lote if x >= base else round(((base-prima) - x)*lote,2) for x in x]
        return [prima * lote if x >= base else round((x - (base - prima)) * lote,2) for x in x]

def graph(suma,new):
    """
    Calcula los valores de Y para la suma de todos los activos en cartera.
    Valores que muestra el gráfico en pantalla
    """
    #print("SUMA: ",suma)
    #print("NEW: ",new)

    propia = y_graph(new[0],new[1],new[2],new[3])
    for i in range(len(suma)):
        suma[i] += propia[i]

    return suma




def calculo_blackScholes(spot,strike,tiempo_al_vencimiento,type = "C"):
    """
    Cálculo teórico de valuación de opciones financieras.
    Parte del DataFrame.
    """
    #Variables
    interes = 0.3
    #spot = 108
    #strike = 104
    #tiempo_al_vencimiento = 14/365
    sigma = 0.3



    #Cálculo de
    d1 = (np.log(spot/strike) + (interes + sigma**2/2)*tiempo_al_vencimiento)/(sigma*np.sqrt(tiempo_al_vencimiento))
    d2 = d1 - sigma*np.sqrt(tiempo_al_vencimiento)

    try:
        if type == "C":
            price = spot*norm.cdf(d1,0,1) - strike*np.exp(-interes*tiempo_al_vencimiento) \
                    * norm.cdf(d2,0,1)
        elif type == "V":
            price = strike*np.exp(-interes*tiempo_al_vencimiento)*norm.cdf(-d2,0,1)\
            - spot*norm.cdf(-d1,0,1)

        return round(price,2)
    except:
        return "Error"









def comprar(activo,cant_comprada=1):
    """
    Comprar un activo, actualizar el DataFrame
    """

    if cant_comprada == 1:
        print("COMPRANDO", opcion.get())
    else:
        print("VENDIENDO", opcion.get())

    if activo == "GGAL":
        mi_cartera.buy_ggal(cant_comprada)
    else:
        mi_cartera.buy_opc(cant_comprada,activo,True,df.loc[activo,"Prima"]) #cantidad,activo,market,prima

        #Actualizo DataFrame
        df.loc[activo, "Cantidad"] += cant_comprada  # Nueva Cantidad
        total = (df.loc[activo, "Cantidad"])


        df.loc[activo, "PP"] = (df.loc[activo, "PP"] * (df.loc[activo, "Cantidad"] - cant_comprada) + (df.loc[activo, "Prima"] *
                                    cant_comprada)) / total


        df.loc[activo, "Tenencia"] = df.loc[activo, "Prima"] * df.loc[activo, "Cantidad"] * 100 # Tenencia

    actualizar()





def mostrar_cartera():
    """
    Mostrar el rendimiento de mi cartera de activos.
    """
    pass

def actualizar():
    """
    Actualiza los datos de opciones, acciones y el paso del tiempo.
    También actualiza el gráfico
    """

    global figure







    plt.close()

    #Destruyo texto anterior y creo el nuevo
    text1.delete("1.0", "end")
    text2.delete("1.0", "end")
    text4.delete("1.0", "end")


    #Paso del tiempo
    mi_contexto.vto += 1
    if mi_contexto.vto % 15 == 0:
        mi_contexto.sortear_contexto()

    #Actualizo GGAL
    subyascente.price += random.choice(mi_contexto.possibilities)
    df.loc["GGAL", "Cantidad"] = mi_cartera.acciones
    df.loc["GGAL", "Prima"] = subyascente.price
    df.loc["GGAL", "Tenencia"] = df.loc["GGAL", "Prima"] * mi_cartera.acciones
    if mi_cartera.acciones == 0:
        df.loc["GGAL","PP"] = 0


    #Actualizo gráfico
    figure.clear()
    figure = plt.figure(figsize=(5, 4), dpi=100)
    ax1 = figure.add_subplot(111)
    ax1.plot(x, mi_cartera.suma)
    if any(mi_cartera.suma) is False:
        rango = [0,100]
    else:
        rango = mi_cartera.suma

    ax2 = figure.add_subplot(111)
    ax2.plot((subyascente.price, subyascente.price), (max(rango), min(rango)))
    ax3 = figure.add_subplot(111)
    ax3.plot(x,[0 for x in x],color = "black",linewidth= 1)

    ax1.set_xlabel("Precio GGAL")
    ax1.set_ylabel("($) Ganancia")
    ax1.xaxis.set_major_formatter(ticks_x)
    ax1.yaxis.set_major_formatter(ticks_y)
    plt.xlim(subyascente.price-40,subyascente.price+40)
    #SUBPLOT = 1 RENGLON, 1 COLUMNA, POSICIÓN 1
    chart = FigureCanvasTkAgg(figure, root)
    chart.get_tk_widget().place(x="1100")

    text1.insert(tk.INSERT, df.iloc[[x for x in range(1, len(df) - 1, 2)]].to_string())  # Calls
    text2.insert(tk.INSERT, df.iloc[[x for x in range(2, len(df), 2)]].to_string())  # Puts
    text4.insert(tk.INSERT, "GGAL: \n" + df.loc["GGAL"].to_string())  # GGAL

    renglon = 1
    for i in opciones:
        #Actualizar precios de prima
        i.restar_día(random.choice([True,False,False,False,False]))
        i.actualizar_prima()


        if i.arbitrado:
            df.loc[i.ticker,"Prima"] = round(i.prima,2)

        df.loc[i.ticker,"B&Sch"] = calculo_blackScholes(subyascente.price,i.base,8/360,i.side)
        df.loc[i.ticker, "Tenencia"] = df.loc[i.ticker, "Prima"] * df.loc[i.ticker, "Cantidad"] * 100

        if df.loc[i.ticker, "Cantidad"] != 0:
            df.loc[i.ticker, "Rendimiento"] = round(((df.loc[i.ticker, "Prima"] - df.loc[i.ticker, "PP"]) / df.loc[i.ticker, "PP"]) * 100, 2)
        else:
            df.loc[i.ticker, "PP"] = 0
            df.loc[i.ticker, "Rendimiento"] = 0


        #Colores a las opciones
        etiqueta, inicio, fin = "et" + str(renglon) + i.side, str(renglon + 2) + ".0", str(renglon + 3) + ".0"

        if i.side == "C":
            text1.tag_add(etiqueta, inicio, fin)
            if i.estado:
                text1.tag_config(etiqueta, background="#76D7C4", foreground="black")
            else:
                text1.tag_config(etiqueta, background="#F1948A", foreground="black")

        else:
            text2.tag_add(etiqueta, inicio, fin)
            if i.estado:
                text2.tag_config(etiqueta, background="#76D7C4", foreground="black")
            else:
                text2.tag_config(etiqueta, background="#F1948A", foreground="black")
            renglon += 1




    text3["text"] = "EFECTIVO ${} OPCIONES ${}    -     DÍAS DESDE EL INICIO --> {}    - CONTEXTO --> {}".format\
        (mi_cartera.efectivo,mi_cartera.total_opciones,mi_contexto.vto,mi_contexto)

    plt.grid()





def clicked(value):
    """
    Informa por consola la compra/venta realizada
    """
    myLabel = Label(root,text=value)
    myLabel.place(x="15",y="570")
    print("CLICKED")


def main():
    """
    Loop principal
    """
    i = 0
    while 1:
        if i % 4 == 0:
            actualizar()
        time.sleep(0.5)
        root.update()
        i += 1









#Variables
hoy = datetime(2020,10,6)
dict_opc = dict()
df = pd.DataFrame(columns=["Serie","Prima","B&Sch","Tenencia","PP","Cantidad","Rendimiento"])
df.set_index("Serie",inplace=True)
x = [x for x in range(20,300,2)]
ticks_x = ticker.FuncFormatter(lambda x,pos:"{:.0f}".format(x))
ticks_y = ticker.FuncFormatter(lambda y,pos:"{:.2f}K".format(y/1000))

#Creando Objetos
subyascente = Ggal(125)
mi_cartera = Cartera(100000)
mi_contexto = Contexto()
opciones = list()


df.loc["GGAL"] = [subyascente.price,0,0,0,0,0]

for i in range(98, 189, 3):
    for j in ["C", "V"]:
        new = Opcion(i, j)
        df.loc[new.ticker] = [new.prima, 0, 0, 0, 0, 0]
        opciones.append(new)



#Tkinter
root = tk.Tk()
root.geometry("1600x600")
root.title("Entorno de opciones GGAL")
root.pack_propagate(False)
root.resizable(0,0) #No puede agrandarse, ni achicarse la ventana


#Cuadros calls/puts
text1 = tk.Text(root)
text1.place(x=30,height=550,width=500)
text2 = tk.Text(root)
text2.place(x=580, height=550, width=500)
text3 = tk.Label(root,text="")
text3.place(x="415",y="575")
text4 = tk.Text(root)
text4.place(x=1100,y=425, height=100, width=200)



opcion = StringVar()
opcion.set(df.index[0])
clicked(opcion.get())

value = 1
y = 30
for i in range(-1,len(df)-1):
    if i == -1:
        b1 = Radiobutton(root, var=opcion, value="GGAL", command=lambda: clicked(opcion.get())).place(x = "1300", y ="475")
    else:
        if i%2 == 0:
            b1 = Radiobutton(root, var=opcion, value=df.index[i+1],command=lambda: clicked(opcion.get())).place(y=str(y))
        else:
            b1 = Radiobutton(root, var=opcion, value=df.index[i+1],command=lambda: clicked(opcion.get())).place(x="550",y=str(y))
            y += 16

button2 = tk.Button(root,text="Comprar",command=lambda: comprar(opcion.get()))
button2.place(x="125",y="567")
button3 = tk.Button(root,text="Vender",command=lambda: comprar(opcion.get(),-1))
button3.place(x="200",y="567")



#Grafico
figure = plt.figure(figsize=(5, 4), dpi=100)
ax1 = figure.add_subplot(111)
ax1.plot(x,mi_cartera.suma)
ax1.set_xlabel("Precio GGAL")
ax1.set_xlabel("($) Ganancia")
ax1.xaxis.set_major_formatter(ticks_x)
ax1.yaxis.set_major_formatter(ticks_y)


chart = FigureCanvasTkAgg(figure, root)
chart.get_tk_widget().place(x="1100")



#y = graph(mi_cartera.opciones_details)
figure.add_subplot(111).plot((subyascente.price,subyascente.price), (max(mi_cartera.suma),min(mi_cartera.suma)))






main()

mostrar_cartera()


root.mainloop()

mi_cartera.actualizar()

main()







