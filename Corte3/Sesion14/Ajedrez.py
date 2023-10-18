
def recuadro(n):
    n_granos=2**(n-1)
    print(f'{n_granos} granos')

def total():
    x=0
    for n in range(64):
        x+=2**n
    print(f'\n{x} granos')

def app():
    n=int(input('Escriba un numero entre 1 y 64: '))
    recuadro(n)
    total()


if __name__=="__main__":
    app()