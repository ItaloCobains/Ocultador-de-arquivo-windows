import ctypes

atributo_ocultar = 0x02

arquivo = input('Path file: ')

retorne = ctypes.windll.kernel32.SetFileAttributesW(arquivo, atributo_ocultar)

if retorne:
    print("Arquivo foi ocultado")
else:
    print('Arquivo nao ocultado')

