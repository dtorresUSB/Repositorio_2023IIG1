#uso de la libreria pyserial
# para instalar ejecutar -m pip install pyserial
import serial
import time

puerto=serial.Serial('COM1',baudrate=9600,timeout=1)
lista=[]
while 1:
    dato=input('Dato a enviar: ')
    for i in range (3):
        puerto.write(dato.encode('utf-8'))
        line=puerto.readline().decode('ascii')
        time.sleep(0.3)
        #print(str(line).rstrip('\r\n'))
        if str(line).rstrip('\r\n')=='Dato incorrecto':
            print('Error en los datos')
            break
        lista.append(str(line).rstrip('\r\n'))
    print(lista)
    lista=[]
    