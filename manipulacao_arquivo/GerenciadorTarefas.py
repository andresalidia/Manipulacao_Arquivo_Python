
import time
import os

# Gerenciador de Tarefas
with open('tarefas.txt', 'r+') as arquivo:
    print("Bem- vindo ao seu gerenciador de Tarefas!")
    print("Vamos começar a organizar suas tarefas!")
    while True:
        # Exibe o menu de opções
        print("Informe a ação que deseja realizar:")
        print("Visualizar a lista de tarefas (1)")
        print("Adicionar uma nova tarefa (2)")
        print("Remover uma tarefa (3)")
        print("Sair (4)")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            os.system('cls') # Limpa a tela do terminal (Windows)
            # Visualiza a lista de tarefas
            arquivo.seek(0)
            lista = arquivo.readlines()
            if not lista:
                print("Não há tarefas cadastradas.")
                time.sleep(4)
            else:
                print("tarefas para hoje:")
                for tarefa in lista:
                    print(f"□ {tarefa.strip()}")# strip() remove os espaços em branco no início e no final da string

            print("\nPressione Enter para continuar...")
            input()
            os.system('cls') # Limpa a tela do terminal (Windows)
        if opcao =='2':

            # Adiciona uma nova tarefa
            while True:
                os.system('cls') # Limpa a tela do terminal (Windows)
                nova_tarefa = input("Informe sua nova tarefa: ")
                if nova_tarefa.strip():# Verifica se a tarefa não está vazia
                    arquivo.write(nova_tarefa + '\n')
                    print("Tarefa adicionada com sucesso!")
                    time.sleep(4)
                    sair = input("deseja adicionar mais uma tarefa? (s/n): ")
                    if sair.lower() != 's':
                        os.system('cls') # Limpa a tela do terminal (Windows)
                        break
                else:
                    print("Tarefa inválida. Tente novamente.")
                    time.sleep(4)
                
