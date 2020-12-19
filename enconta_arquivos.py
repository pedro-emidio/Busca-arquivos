import os
"""
    Para mudar o inicio da busca alterar a variavel caminho_busca.
    Mudar o inicio da busca pode deixar a execução mais rápida!
"""
caminho_busca = 'C:/Users/home'
termo_busca = input('qual arquivo deseja encontrar?')
conta = 0
for raiz, diretorio, arquivos in os.walk(caminho_busca):
    for arquivo in arquivos:
        if termo_busca in arquivo:
            try:
                conta += 1
                caminho_Completo = os.path.join(raiz, arquivo)
                nome_arquivo, extencao_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_Completo)
                print()
                print(f'Encontrei o aquivo: {arquivo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {extencao_arquivo}')
                print(f'Caminho: {caminho_Completo}')
                print(f'Tamanho: {tamanho}b')


            except PermissionError as e:
                print('Sem permisão')
            except FileNotFoundError as e:
                print('Aquivo não encontrado')
            except Exception as e:
                print('Erro inesperado: ', e)

print(f'{conta} Arquivo(s) encontrado(s)')
