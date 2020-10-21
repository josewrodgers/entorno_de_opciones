import requests
import json
from datetime import datetime,timedelta
import pandas as pd

def log_in():
    """
    Establece conexión con la API-REST de InvertirOnline
    """

    url = "https://api.invertironline.com/token"

    user = input("User: ")
    password = input("Password: ")

    data = {"username":user,
            "password":password,
            "grant_type":"password"}

    r = requests.post(url=url, data=data)
    access = json.loads(r.text)

    return access["access_token"], access["refresh_token"]

def get_options(bearer_token):
    """
    Obtenemos listas con las opciones del próximo ejercicio
    También devuelve el OPEX (OPtion Expiration Date)
    """

    vencimiento = "2020-12-18T00:00:00"

    headers = {"Authorization":"Bearer "+bearer_token}
    r2 = requests.get(url="https://api.invertironline.com/api/v2/bCBA/Titulos/GGAL/Opciones",
                                headers = headers)

    opciones_GGAL = json.loads(r2.text)

    opc = []

    for i in range(len(opciones_GGAL)):
        side = opciones_GGAL[i]["tipoOpcion"]
        if opciones_GGAL[i]["fechaVencimiento"] == vencimiento:
                opc.append([opciones_GGAL[i]["simbolo"],opciones_GGAL[i]["cotizacion"]["ultimoPrecio"],
                            opciones_GGAL[i]["descripcion"].split(" ")[2]])

    return opc, vencimiento

def get_ggal(bearer_token):
    """
    Obtenemos precios de GGAL
    """
    headers = {"Authorization": "Bearer " + bearer_token}

    r3 = requests.get(url="https://api.invertironline.com/api/v2/bCBA/Titulos/GGAL/Cotizacion",
                      headers= headers)

    try:
        GGAL = json.loads(r3.text)
        GGAL = GGAL["ultimoPrecio"]
        return GGAL
    except:
        pass

def get_ggal_adr():
    """
    Proximamente -  Hacer webscraping del precio de GGAL ADR y calcular el CCL
    """
    pass

def get_opex(string):
    """
    Devuelve tiempo hasta el vencimiento
    """
    year,month,day = int(string[:4]),\
                     int(string[5:7]),\
                     int(string[8:10])
    opex = datetime(year,month,day)
    today = datetime.today()
    remains = (opex - today).days
    return remains

def get_volatilidad_historica(bearer_token,media=58):
    """
    Obtenemos precios de GGAL
    *56 días son 40 ruedas*
    """
    headers = {"Authorization": "Bearer " + bearer_token}
    hasta = datetime.today()
    desde = hasta - timedelta(days=media)

    print(desde,hasta)

    r3 = requests.get(url="https://api.invertironline.com/api/v2/bCBA/Titulos/GGAL/Cotizacion/seriehistorica/"+
                          desde.strftime("%Y-%m-%d")+"/"+hasta.strftime("%Y-%m-%d")+"/ajustada",
                      headers=headers)

    df = pd.DataFrame(columns=["Día","Minimo","Máximo","Cierre"])
    df.set_index("Día",inplace=True)

    print(r3.text)


    for i in json.loads(r3.text):
        df.loc[i["fechaHora"][:10]] = [i["minimo"],i["maximo"],i["ultimoPrecio"]]

    print(df)
    df.to_excel('example.xls', sheet_name='Volatilidad Histótica')



#bearer_token, refresh_token = log_in()

#opciones, opex = get_options(bearer_token)
#print(opciones)
#print(opex)

#get_ggal_adr()
#print("BEARER TOKEN: ",bearer_token)
#print(get_volatilidad_historica(bearer_token))




