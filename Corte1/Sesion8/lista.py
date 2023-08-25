
def agregar(milista):
    num=int(input('Que desea agregar: '))
    milista.append(num)
    print(milista)

def insertar(milista):
    idx=int(input('Indique el indice: '))
    val=int(input('Cual es valor que insertará: '))
    milista.insert(idx,val)
    print(milista)

def formateo(milista):
    milista.clear()
    print(milista)

def remover(milista):
    print(milista)
    n=int(input('que valor desea remover: '))
    milista.remove(n)
    print(milista)

def main(milista):
    opc=''
    while opc!='exit':

        if opc=='1':
            agregar(milista)
        elif opc=='2':
            insertar(milista)
        elif opc=='3':
            formateo(milista)
        elif opc=='4':
            remover(milista)

        print('\nSeleccione una opcion:\n',\
            '1. Append\n 2. Insertar\n 3.Formatear\n',\
                ' 4.remover')
        opc=input('Selección: ')

if __name__=="__main__":
    milista=[2,3,4]
    main(milista)