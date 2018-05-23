import urllib.request

print('>>>>LISTA DE MÚSICAS<<<<')
x = str(input('Digite o nome da banda usando "-" ao invés de espaços: ').lower())
while (' ' in x): # laço para substituir caractere
            x = x.replace(' ', '-')
texto = ''


def Solicita_banda(x = x):    #cria url em str
    banda = 'https://www.vagalume.com.br/'+x+'/'
    return banda


def tratarY (x = x):#cria str para alteração no texto
    y = 'href="/'+x+'/' 
    return y


def requisicaolista(banda = Solicita_banda()):#utiliza url para requisição de dados em página HTML
    content = urllib.request.urlopen(banda).read()#acessa a url e lê a página html
    content = str(content)#transforma o html em str

    while (tratarY() in content): # laço para substituir caractere
            content = content.replace(tratarY(), '¬¬')
    while ('.html" data-song=' in content): # laço para substituir caractere
            content = content.replace('.html" data-song=', '¬¬')
    while ('-' in content): # laço para substituir caractere
            content = content.replace('-', ' ')


    texto = content.split('¬¬')#cortando espaços e transformando str em lista


    x = len(texto)#contar elementos da lista
    for i in range (0,x):
        while '>' not in texto[i]:#separa conteúdo útil
            print ('-',texto[i].title())
            i+=1
    return '---------------------------------------------'

    

print (requisicaolista())


    
