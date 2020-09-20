import random
import json
import requests
import locale
from datetime import datetime, timedelta
import pandas as pd
from collections import Counter
import os


locale.setlocale(locale.LC_ALL, 'es-ES') 

headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  'c4ec5b71-787c-48de-85aa-c88447288de0'}
parametros = {'symbol': '/v1/cryptocurrency/quotes/latest'}
requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)



data = requests.get("https://api.coinmarketcap.com/v2/ticker/").json()


bien = "Bienvenido a la bibliteca virtual"
print("-------------------------------------------------".center(100))
print(bien.center(100))
print("--------------------------------------------------".center(100))
numero_banco = int(random.uniform(100000, 999999))
num_guardado = numero_banco
print("Numero de cuenta ".rjust(100),"", numero_banco)
print("Menu de opciones: ")
print("1. Recibir la cantidad ")
print("2. Transferir monto ")
print("3. Mostrar balance de una moneda ")
print("4. Mostrar balance general ")
print("5. Mostrar historico de transacciones ")
print("6. Salir del programa ")
while True:
    try:
        opcion = int(input("Selecciona una opcion: "))
        break
    except ValueError:
        print("El valor es incorrecto, debes ingresar un numero entero")
    

while opcion > 6 or opcion < 1:
    print("Opcion incorrecta ")
    while True:
        try:
            opcion = int(input("Selecciona una opcion: "))
            break
        except ValueError:
            print("El valor es incorrecto, debes ingresar un numero entero")


def esmoneda(cripto):
    return cripto in monedas

moneda1=()
moneda1_dic={}
for id in data["data"]:
    moneda1_dic[data["data"][id]["symbol"]]=data["data"][id]["symbol"]
    
    
moneda1 = moneda1_dic.keys()


monedas = ()
monedas_dic = {}
#permitir al usuario ingresar ya sea por symbol, name, website_slug 
for id in data["data"]:
    monedas_dic[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["price"]
monedas = monedas_dic.keys()
#nombre de la moneda
monedanom = ()
monedanom_dic = {}
for id in data["data"]:
    monedanom_dic[data["data"][id]["symbol"]]=data["data"][id]["name"]
monedanom=monedanom_dic.keys()


rang=()
rango_dic={}
for id in data["data"]:
    rango_dic[data["data"][id]["symbol"]]=data["data"][id]["rank"]
   
rang=rango_dic.keys()

##capital vendido 24h
monedas24 = ()
monedas24_dic = {}
#permitir al usuario ingresar ya sea por symbol, name, website_slug 
for id in data["data"]:
    monedas24_dic[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["volume_24h"]
    
monedas24 = monedas24_dic.keys()

monedascap = ()
monedascap_dic = {}
#capital final 
for id in data["data"]:
    monedascap_dic[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["market_cap"]
    
monedascap = monedascap_dic.keys()
# opcion 1
#listas de recibido



preee={}

moneda1ga={}
moneda1pe={}
gh=[]

saldo = 1200
saldot=0
cantidaTranferido=[]
codigos_recibidos=[]
fecha_recibido=[]
moneda_virtua=[]
tipo1=[]
ph=[]
#opcion 2
##listas de tranferencia
tipo2=[]
cantidaTransferencia=[]
codigos_tranferidos=[]
fecha_tranferidos=[]
moneda_virtua_trnaferida=[]

x=0
y=0

monedafina={}
listamone=[]

monedafina2={}
listamone2=[]
##opcionn 3

moneda_virtual3=[]
canti_virtual=[]
dias=[]
ganancia=[]
fecha_moneda=[]
acumulado=[]
precio_moene=[]
cotizacion=[]

hrango=[]
fgg=[]
saldot=saldo+x-y

fgg1=[]
os.system("cls")
while opcion!=6:
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("Vuelve a digitar una opcion ".center(120))
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("Numero de cuenta ".rjust(99),"", numero_banco)    
    print("Menu de opciones: ")
    print("\n")
    print("1. Recibir la cantidad ")
    print("2. Transferir monto ")
    print("3. Mostrar balance de una moneda ")
    print("4. Mostrar balance general ")
    print("5. Mostrar historico de transacciones ")
    print("6. Salir del programa ")
    while True:
        try:
            opcion = int(input("Selecciona una opcion: "))
            break
        except ValueError:
            print("El valor es incorrecto, debes ingresar un numero entero")
            
    while opcion > 6 or opcion < 1:
        print("Opcion incorrecta ")
        while True:
            try:
                opcion = int(input("Selecciona una opcion: "))
                break
            except ValueError:
                print("El valor es incorrecto, debes ingresar un numero entero")
                
    os.system("cls")
    
    if opcion == 1:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Recibir cantidad".center(150))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Tu saldo es de: ".rjust(150), "$", saldot," USD")
        print()
        
        moneda = input("Ingrese el nombre de la moneda:  ")
        moneda=moneda.upper()
        while not esmoneda(moneda):
            print("Moneda Invalida")
            moneda = input("Ingrese el nombre de la moneda ")
        
        if moneda in monedafina:
            moneda_virtua.append(moneda1_dic.get(moneda))  #para alojar la moneda en la lista
            s=monedafina.get(moneda)
            l=float(s)
            while True:
                try:
                    cantidad_recibido=float(input("Ingresar la cantidad de la moneda a recibir "))
                    break
                except ValueError:
                    print("El valor es incorrecto, debes ingresar un numero ")
            f=round(monedas_dic.get(moneda),4) #obtiene el valor de la moneda
            g=cantidad_recibido*f
            
            m=l+cantidad_recibido
            monedafina[moneda]=m
            cantidaTranferido.append(g)
            listamone.append(m)
            
            
            
        if moneda not in monedafina:
            moneda_virtua.append(moneda1_dic.get(moneda))   #para alojar la moneda en la lista
            while True:
                try:
                    cantidad_recibido=float(input("Ingresar la cantidad de la moneda a recibir "))
                    break
                except ValueError:
                    print("El valor es incorrecto, debes ingresar un numero ")
            
            f=round(monedas_dic.get(moneda),7) #obtiene el valor de la moneda
            g=cantidad_recibido*f
            
            cantidaTranferido.append(g)
            listamone.append(cantidad_recibido)
            
             
        ahora = datetime.now() ## para carturar la fecha
        fecha_recibido.append(ahora.strftime("%d-%m-%Y %H:%M:%S"))
        tipo1.append("Recibido")
        
        #suma el todos los valores de esa lista
        
        x=sum(cantidaTranferido)
        saldot=saldo+x-y #suma el valor incial mas la cantidad recibida menos la canridad transferida
        
      
        while True:
            try:
                codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                while len(codigo_transfe)!=6:
                    print("La cuenta debe tener 6 digitos")
                    codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                codigo_transfe=int(codigo_transfe)
                break
            except ValueError:
                print("El valor es incorrecto, debes ingresar SOLO NUMEROS ENTEROS ")
            
        codigos_recibidos.append(codigo_transfe)

        monedafina=dict(zip(moneda_virtua,listamone))

        ls=round(monedas_dic.get(moneda),7)
        ls=float(ls)
        ms=monedafina.get((moneda))
        ms=float(ms)
        lsi=ls*ms
        gh.append(lsi)
        moneda1ga=dict(zip(moneda_virtua,gh))
        
        
        fgg.append(saldo)
        print("\nDinero recibido con exito....")
        # balance=pd.DataFrame(cantidaTranferido)
        # print("NOmbre",balance) tabla

        print("Tu numero de cuenta es: ",numero_banco, "\nRebiste una tansferencia de la cuenta: ",codigo_transfe, 
              "\nRecibite: ",cantidad_recibido," monedas de ",monedanom_dic.get(moneda),"\nTu saldo actual es de: ",saldot," USD, "
              "\nRecibistes",g,"dolares \nRecibido el ",ahora.strftime("%A, %d de %B del %Y a las %H:%M:%S"))
        print(tipo1)
        continue
    if opcion == 2:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("TRANFERIR MONTOS".center(150))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Tu saldo es de: ".rjust(150), "$", saldot," USD")
        
        moneda = input("Ingrese el nombre de la moneda:  ")
        moneda=moneda.upper()
        while not esmoneda(moneda):
            print("Moneda Invalida")
            moneda = input("Ingrese el nombre de la moneda ")
        
           
        if moneda in monedafina2:
            moneda_virtua_trnaferida.append(moneda1_dic.get(moneda))  #para alojar la moneda en la lista 
            s=monedafina2.get(moneda)
            l=float(s)
            cantidad_recibido=float(input("Ingresar la cantidad de la moneda a enviar "))
            f=round(monedas_dic.get(moneda),7) #obtiene el valor de la moneda
            g=cantidad_recibido*f
            if saldot<g:
                print("No puedes enviar esa cantidad ya que solo tienes ",saldot," y vas e enviar ",cantidad_recibido," de la moneda ",moneda," que eso es: ",g," USD")
            else:
                m=l+cantidad_recibido
                monedafina2[moneda]=m
                cantidaTransferencia.append(g)
                listamone2.append(m)
            
                while True:
                    try:
                        codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                        while len(codigo_transfe)!=6:
                            print("La cuenta debe tener 6 digitos")
                            codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                        codigo_transfe=int(codigo_transfe)
                        break
                    except ValueError:
                        print("El valor es incorrecto, debes ingresar SOLO NUMEROS ENTEROS ")
                
                codigos_tranferidos.append(codigo_transfe)
                
                ahora = datetime.now() ## para carturar la fecha
                fecha_tranferidos.append(ahora.strftime("%d-%m-%Y %H:%M:%S"))
                #funcion para sumar los elementos del las cuotas recibidas
                y=sum(cantidaTransferencia)
                
                monedafina2=dict(zip(moneda_virtua_trnaferida,listamone2))
                saldot=saldo+x-y
                ls=round(monedas_dic.get(moneda),7)
                ms=monedafina2.get(moneda)
                lsi=ls*ms
                ph.append(lsi)
                moneda1pe=dict(zip(moneda_virtua_trnaferida,ph))
                tipo2.append("Enviado")

                print("Dinero Enviado con exito....")
                
                fgg1.append(saldo)
                
                print()
                print("Tu numero de cuenta es: ",numero_banco, "\nHas hecho una tansferencia a la cuenta ",codigo_transfe, 
                    "\nEnviaste ",cantidad_recibido," monedas de ",monedanom_dic.get(moneda),"\nTu saldo actual es de: ",saldot," USD, "
                    "\nEnviaste ",g,"dolares \nRecibido el ",ahora.strftime("%A, %d de %B del %Y a las %H:%M:%S"))
                       
        if moneda not in monedafina2:
            moneda_virtua_trnaferida.append(moneda1_dic.get(moneda))  #para alojar la moneda en la lista
            cantidad_recibido=float(input("Ingresar la cantidad de la a enviar "))
            f=round(monedas_dic.get(moneda),7) #obtiene el valor de la moneda
            g=cantidad_recibido*f
            if saldot<g:
                print("No puedes enviar esa cantidad ya que solo tienes ",saldot," y vas e enviar ",cantidad_recibido," de la moneda ",moneda," que eso es: ",g," USD")
            else:
                cantidaTransferencia.append(g)
                listamone2.append(cantidad_recibido)
                
                while True:
                    try:
                        codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                        while len(codigo_transfe)!=6:
                            print("La cuenta debe tener 6 digitos")
                            codigo_transfe=(input("Por favor digita el numero de la cuenta del que deseas recibir dinero "))
                        codigo_transfe=int(codigo_transfe)
                        break
                    except ValueError:
                        print("El valor es incorrecto, debes ingresar SOLO NUMEROS ENTEROS ")
                        
                codigos_tranferidos.append(codigo_transfe)
                
                ahora = datetime.now() ## para carturar la fecha
                fecha_tranferidos.append(ahora.strftime("%d-%m-%Y %H:%M:%S"))
                #funcion para sumar los elementos del las cuotas recibidas
                y=sum(cantidaTransferencia)
                saldot=saldo+x-y
                monedafina2=dict(zip(moneda_virtua_trnaferida,listamone2))
                
                tipo2.append("Enviado")

                if moneda not in monedafina:
                    ls=round(monedas_dic.get(moneda),7)
                    ms=monedafina2.get(moneda)
                    lsi=ls*ms

                ph.append(lsi)
                moneda1pe=dict(zip(moneda_virtua_trnaferida,ph))
                
                fgg1.append(saldo)
   
                print("Dinero Enviado con exito....")
                print()

                print("Tu numero de cuenta es: ",numero_banco, "\nHas hecho una tansferencia a la cuenta ",codigo_transfe, 
                    "\nEnviaste ",cantidad_recibido," monedas de ",monedanom_dic.get(moneda),"\nTu saldo actual es de: ",saldot," USD, "
                    "\nEnviaste",g,"dolares \nRecibido el ",ahora.strftime("%A, %d de %B del %Y a las %H:%M:%S"))
        
        continue
    if opcion==3:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("BALANCE POR MONEDA COTIZACION, PRECIO, GANACIA ".center(150))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

        while True:
            moneda = input("Ingrese el nombre de la moneda:  ")
            moneda=moneda.upper()
            while not esmoneda(moneda):
                print("Moneda Invalida")
                moneda = input("Ingrese el nombre de la moneda ")
            moneda_virtual3.append(monedanom_dic.get(moneda))
            
            
            while True:
                try:
                    canti=float(input("Digite la cantidad acumulada inicial: "))
                    break
                except ValueError:
                    print("El valor es incorrecto, debes ingresar SOLO NUMEROS ")
            
            canti_virtual.append(round(canti,4))
            
            while True:
                try:
                    coti=(input("Ingrese el numero de dias para saber la cantidad acumulada en esos dias: "))
                    while len(coti)>3:
                        print("NO PUEDEN SER MAS DE 999 DIAS")
                        coti=(input("Ingrese el numero de dias para saber la cantidad acumulada en esos dias: "))
                    coti=int(coti)
                    break
                except ValueError:
                    print("El valor es incorrecto, debes ingresar SOLO NUMEROS ")
                    
            dias.append(coti)
            porcen=((monedas24_dic.get(moneda))/(monedascap_dic.get(moneda))+1) # es el total vendido de la moneda sobre el capital completo de la moneda + 1 que para la multiplicacon de interes compuesto
            cotizacion.append((porcen))
            tf=canti*(porcen)**coti
            acumulado.append(round(tf,4))
            h=tf-canti
            ganancia.append(round(h,4))
            precio_moene.append(round(monedas_dic.get(moneda),2))
            ahora = datetime.now() ## para carturar la fecha
            fecha_moneda.append(ahora.strftime("%A, %d de %B del %Y a las %H:%M:%S"))

            hrango.append(rango_dic.get(moneda))
            
            balance3={'Nº':hrango,'Nombre':moneda_virtual3,'Cantidad':canti_virtual,
                      'Precio en USD':precio_moene,'Ganacia Diaria':cotizacion,'Dias':dias,'Ganancias':ganancia,
                      'Monto Final':acumulado,'Fecha':fecha_moneda}
            dicci3=pd.DataFrame.from_dict(balance3)
            dicci3.transpose
            print("\n")
            
            print("\n\nLa moneda Nº",rango_dic.get(moneda),": ",monedanom_dic.get(moneda)," tiene un precio de: ",round(monedas_dic.get(moneda),4),"USD, tiene una ganacia diaria de: \n",round(porcen,5)," USD; te ganaras ",h," en ",int(coti)," dias osea tu monto final sera de: ",tf, "\n hiciste esta consulta el: ",ahora.strftime("%d-%m-%Y %H:%M:%S") )

            print("\n"*2)
            print(dicci3)
            print()
            opp=input("Desea ingresar otra moneda: (S/N) ")
            if opp=="s" or opp=="S":
                os.system("cls")  
                continue
            else:
                os.system("cls")  
                break
              
        continue
    if opcion==4:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("BALANCE GENERAL".center(150))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Tu saldo es de: ".rjust(150), "$", saldot," USD")
        print("\n"*2)
        mende=Counter(monedafina) # con estas dos lineas resta lo que hay en el dict monedafina con el de monedafina2
        mende.subtract(monedafina2)
        
        l1=list(mende.keys())
        l2=list(mende.values())
        
        xf=Counter(moneda1ga) # con estas dos lineas resta lo que hay en el dict moneda1ga con el de moneda1pe
        xf.subtract(moneda1pe)
        
        l11=list(xf.values())
        
        
        def dividio(lista1, lista2):
            if lista1 and lista2:
                resultado=[]
                for i in range(0, len(lista1)):
                    resultado.append(lista1[i]/lista2[i])
                return resultado
            else:
                print([])
        cvb=dividio(l11,l2)    
   
          
        opccc={'Moneda':l1,'Cantidad Final':l2,'Precio Unitario':cvb,'Valor Total en USD':l11}
        if cvb:
            sf=pd.DataFrame.from_dict(opccc,orient='columns')
            sf.transpose
            print(sf)
            sl=sum(l11)
            print("\n\nTotal en dolares de las monedas ",l1," es: ",sl,"USD")
            
        else:
            print("NO HAS RECIBIDO NI HAS ENVIADOS")
        continue
    if opcion==5:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Historico de Transacciones ".center(150))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Tu saldo es de: ".rjust(150), "$", saldot," USD")
        print("\n")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("CANTIDAD RECIBIDA".center(100))
        print("------------------------------------------------------------------------------------------------------------------------------")
         
        
        def sumaaa(lista1, lista2):
            sumaass=[]
            if lista1 and lista2:
                for i in range(0, len(lista1)):
                    sumaass.append((lista1[i])+(lista2[i]))
                return sumaass
            else:
                print()
        saldoff=sumaaa(fgg,gh)

        tranferenciass={'Fecha Recibida':fecha_recibido,'Moneda':moneda_virtua,'Tipo de operacion':tipo1,'C Usuario Recibido':codigos_recibidos,
                        'Cantidad de Moneda':listamone,'Monto inicial':saldo,'Monto de la moneda':gh,'Saldo':saldoff}
        if saldoff:
            lss=pd.DataFrame.from_dict(tranferenciass,orient='columns')
            lss.transpose
            print(lss)
        else:
            print("NO HAY DATOS RECIBIDOS")
        
        print("\n"*2)
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("CANTIDAD ENVIADA".center(100))
        print("------------------------------------------------------------------------------------------------------------------------------")
        
        
        def yus(lita1, lita2):
            resulta=[]
            if lita1 and lita2:
                for i in range(0, len(lita1)):
                    resulta.append((lita1[i])-(lita2[i]))
                return resulta
            else:
                print() 
                
        saldoff1=yus(fgg1,ph)
        
        enviadosss={'Fecha Enviada':fecha_tranferidos,'Moneda':moneda_virtua_trnaferida,'Tipo de operacion':tipo2,'Codigo del Usuario Enviado':codigos_tranferidos,
                        'Cantidad de Moneda':listamone2,'Monto inicial':saldo,'Monto de la moneda':ph,'Saldo':saldoff1}
        if saldoff1:           
            lss1=pd.DataFrame.from_dict(enviadosss,orient='columns')
            lss1.transpose
            print(lss1)
        else:
            print("NO HAY DATOS ENVIADOS")
       
os.system("cls")
print("\n"*2)
print("MUCHAS GRACIAS POR UTILIZAR TU BILLERA VIRTUAL TE ESPERAMOS".rjust(100))
        
      