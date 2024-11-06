import json
 
# Inicializa a agenda em uma lista  
agenda = []
 
# Função para carregar as informações ja existentes do json
def carregarAgenda():
    try:
        with open('agenda.json', 'r') as arquivo:
            return json.load(arquivo)  # Retorna a lista do json
    except:
        return []  # Se der algum problema retornar uma lista vazia
 
# Função para salvar as novas informaçoes no json    
def salvarAgenda():
    with open('agenda.json', 'w') as arquivo:
        json.dump(agenda, arquivo, indent=4) # Salva a agenda no json com indentação
 
# Função para mostrar todos os contatos na agenda
def mostrarAgenda():
        print("\nTodos os contatos na agenda:\n")
        for contato in agenda:
            for chave, valor in contato.items():
                print(f"{chave}: {valor}")
            print()  # Espaço vazio para separar cada contato
 
def excluirContato(): # Função que exclui o contato
    nomeApagar = input("Digite o nome do contato que você quer excluir: ")
    for contato in agenda:
        if contato["nome"].lower() == nomeApagar.lower(): # Verifica se o contato tem o mesmo nome 
            confirmacao = input("Tem certeza que deseja excluir? Digite s para confirmar")
            if confirmacao == 's' or confirmacao == 'S':
                agenda.remove(contato)
            else:
                print("Cancelado")
    salvarAgenda()

def editarContato(): # Função para editar contatos preexistentes
    nomeEditar = input("Digite o nome do contato que você deseja editar")
    for contato in agenda:
        if contato["nome"] == nomeEditar:
            nomeEditado = input("Escreva o nome para alterar") 
            telefoneEditado = input("Escreva o telefone para alterar") 
            emailEditado = input("Escreva o email para alterar")

            if nomeEditado:
                contato["nome"] = nomeEditado
            if telefoneEditado:
                contato["telefone"] = telefoneEditado
            if emailEditado:
                contato["email"] = emailEditado
            
            salvarAgenda()
            break
 
# Função para adicionar um novo contato
def adicionarContato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    
    for contato in agenda:
        if nome.lower() == contato["nome"].lower():
            print("ERRO: contato ja existente")
            return
        
        if nome == "":
            print("ERRO: É necessário colocar um nome")
            return
   
            contato = {
                "nome": nome,
                "telefone": telefone,
                "email": email
            }

            agenda.append(contato)  # Adiciona o contato a agenda
            salvarAgenda()

        
# Menu principal
agenda = carregarAgenda()

while True:
    # Exibe o menu de opções
    continuar = int(input(
        "\nEscolha uma opção:\n"
        "1 - Para adicionar contato\n"
        "2 - Para excluir algum contato\n"
        "3 - Para editar algum contato\n"
        "4 - Para mostrar a agenda\n"
        "5 - Para parar a execução\n"
        "Digite sua opção: "
    ))
 
 
    if continuar == 1:
        adicionarContato()
    elif continuar == 2:
       excluirContato() 
    elif continuar == 3:
        editarContato()
    elif continuar == 4:
        mostrarAgenda()  
    elif continuar == 5:
        break 
    else:
        print("Opção inválida! Tente novamente.")
