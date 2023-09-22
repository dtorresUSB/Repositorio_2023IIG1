def lectura():
    f=open('wcm.csv','r',encoding="utf8")
    lectura=f.readlines()
    datos=[]
    for i in lectura:
        datos.append(i.rstrip('\n').split(','))
    return datos