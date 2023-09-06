from random import uniform as u

def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))
    #print(comision)
    return comision

def ver_tasas(r,d,c):
    for i in range(5):
        print(f'divisa: {d[i]}, tasa: {c[i]}, comisión:{r[i]}')

def conversion(r,d,c):
    divisa=input('A que divisa desea hacer el cambio: ').upper()
    if divisa in d:
        idx=d.index(divisa)
        divisa=(d[idx])
        tasa=int(c[idx])
        comision=r[idx]
        Precio_venta=tasa+(tasa*comision)
        cambio=int(input('Que valor desea cambiar: '))
        total = cambio//Precio_venta
        vueltas=round((cambio - Precio_venta*total),2)
        print(f'Cambio: {total} {divisa}, Devolucion: {vueltas} COP')
        return 1
    print('ingrese un valor valido\n')

def menu():
    comision=rates()
    divisas=['USD','EUR','CNY','JPY','PEN']
    cambios=['4108','4454','563 ','28  ','1106']
    print(' 1. Cambio de divisas\n','2. Ver tasas de cambio\n','3. Salir')
    opc=input('Seleccione una opcion: ')

    while opc!='salir':
        if opc=='1':
            conversion(comision,divisas,cambios)
        elif opc=='2':
            ver_tasas(comision,divisas,cambios)
        elif opc=='salir' or '3':
            break
        else:
            print('Seleccion invalida')
        print(' 1. Cambio de divisas\n','2. Ver tasas de cambio\n','3. Salir')
        opc=input('Seleccione una opcion: ')

def inicio():
    menu()

if __name__=="__main__":
    inicio()