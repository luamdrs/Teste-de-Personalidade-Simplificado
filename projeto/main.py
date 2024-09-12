from time import sleep


# Linha
def linha(tam=40):
    return '-' * tam

# Cabeçalho
def frase(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

# Função para cadastrar o nome da pessoa
def cadastrar_pessoa():
    nome = input("Digite seu nome: ")
    return nome

# Função que faz 5 perguntas de personalidade
def realizar_teste():
    perguntas = [
        "Você gosta de estar em grandes grupos de pessoas? (1-Discordo, 5-Concordo): ",
        "Você gosta de planejar e organizar suas tarefas? (1-Discordo, 5-Concordo): ",
        "Você se considera criativo? (1-Discordo, 5-Concordo): ",
        "Você costuma se preocupar muito com coisas? (1-Discordo, 5-Concordo): ",
        "Você se considera uma pessoa solidária? (1-Discordo, 5-Concordo): "
    ]
    
    respostas = []
    
    for pergunta in perguntas:
        while True:
            try:
                resposta = int(input(pergunta))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                respostas.append(resposta)
                break
            except ValueError:
                print("Por favor, insira um número entre 1 e 5.")
    
    return respostas

# Função que gera o perfil com base nas respostas
def gerar_perfil(respostas):
    total = sum(respostas)
    
    if total >= 20:
        return "Você parece uma pessoa muito extrovertida e solidária!"
    elif total >= 15:
        return "Você parece uma pessoa equilibrada, com características sociáveis."
    else:
        return "Você parece uma pessoa mais introspectiva e reservada."

# Programa principal
def main():

    frase('TESTE DE PERSONALIDADE')
    sleep(1)

    nome = cadastrar_pessoa()
    sleep(0.5)
    print(f"\nOlá, {nome}! Bem-vindo ao Teste de Personalidade.")
    sleep(1)
    print(f'\nVamos iniciar o nosso teste!\n')
    sleep(1)
    
    respostas = realizar_teste()
    perfil = gerar_perfil(respostas)
    sleep(1)
    
    print(f"\n{nome}, o seu perfil de personalidade é:\n{perfil}")

if __name__ == "__main__":
    main()

frase('>> FIM DO PROGRAMA. VOLTE SEMPRE! <<')