# Ocultador de arquivos windows

## Explicação do codigo:

### E um programa que usa a biblioteca ctypes assim fazendo a programação em python ficar mais low level.
### Ao iniciado o programa pede um Path file (Caminho do arquivo), por meio da lib ctypes ele acessa o ctypes.windll.kernel32.SetFileAttributesW para setar e escrever um atributo no arquivo, passamos 2 paramentro dentro da func o path e o atributo 0x02 para ocultação. Depois de todo processo ele faz uma vereficação para retorna se o arquivo foi ocultado ou não.
