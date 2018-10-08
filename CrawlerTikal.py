import urllib.request

print('>>>>LISTA DE MÚSICAS<<<<')
x = str(input('Digite o nome da banda usando "-" ao invés de espaços: ').lower())
while (' ' in x): # laço para substituir caractere
            x = x.replace(' ', '-')
texto = ''


def Solicita_banda(x = x): 
    """
    cria url em str
    """
    banda = 'https://www.vagalume.com.br/'+x+'/'
    return banda


def tratarY (x = x):
    """
    cria str para alteração no texto
    """
    y = 'href="/'+x+'/' 
    return y


def requisicaolista(banda = Solicita_banda()):
    """
    utiliza url para requisição de dados em página HTML
    """
    #acessa a url e lê a página html
    content = urllib.request.urlopen(banda).read()
    #transforma o html em str
    content = str(content)
    # laço para substituir caractere
    while (tratarY() in content):
            content = content.replace(tratarY(), '¬¬')
    # laço para substituir caractere
    while ('.html" data-song=' in content): 
            content = content.replace('.html" data-song=', '¬¬')
    # laço para substituir caractere
    while ('-' in content): 
            content = content.replace('-', ' ')

    #cortando espaços e transformando str em lista
    texto = content.split('¬¬')


    x = len(texto)#contar elementos da lista
    for i in range (0,x):
        while '>' not in texto[i]:#separa conteúdo útil
            print ('-',texto[i].title())
            i+=1
    return '---------------------------------------------'

    

print (requisicaolista())


    
