from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('Minha idade é:' + str(year))

def lerDoBanco(nome):
    lista_nomes=[
        {'nome':'Ana','idade': 20},
        {'nome':'Pedro','idade': 70},
        {'nome':'Joaquim','idade': 90}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return{'nome': 'nao encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    if result['idade'] > 0 :
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('nao encontrado')

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade} )  