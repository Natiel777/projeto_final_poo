def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Menu de Alunos")
        print("2. Menu de Professores")
        print("3. Menu de Disciplinas")
        print("4. Menu de Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_disciplinas()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alunos():
    while True:
        print("\n--- Menu de Alunos ---")
        print("1. Cadastrar novo Aluno")
        print("2. Listar Alunos")
        print("3. Buscar aluno por matrícula")
        print("4. Editar aluno")
        print("5. Excluir aluno")
        print("6. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Cadastrar novo Aluno")
        elif opcao == "2":
            print("Listar Alunos")
        elif opcao == "3":
            print("Buscar aluno por matrícula")
        elif opcao == "4":
            print("Editar aluno")
        elif opcao == "5":
            print("Excluir aluno")
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_professores():
    while True:
        print("\n--- Menu de Professores ---")
        print("1. Cadastrar novo Professor")
        print("2. Listar Professores")
        print("3. Buscar professor por SIAPE")
        print("4. Editar professor")
        print("5. Excluir professor")
        print("6. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Cadastrar novo Professor")
        elif opcao == "2":
            print("Listar Professores")
        elif opcao == "3":
            print("Buscar professor por SIAPE")
        elif opcao == "4":
            print("Editar professor")
        elif opcao == "5":
            print("Excluir professor")
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_disciplinas():
    while True:
        print("\n--- Menu de Disciplinas ---")
        print("1. Criar nova Disciplina")
        print("2. Listar Disciplinas")
        print("3. Buscar disciplina por código")
        print("4. Editar disciplina")
        print("5. Excluir disciplina")
        print("6. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Criar nova Disciplina")
        elif opcao == "2":
            print("Listar Disciplinas")
        elif opcao == "3":
            print("Buscar disciplina por código")
        elif opcao == "4":
            print("Editar disciplina")
        elif opcao == "5":
            print("Excluir disciplina")
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_relatorios():
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Alunos aprovados")
        print("2. Alunos reprovados")
        print("3. Professores com muitos alunos")
        print("4. Estatísticas gerais")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Relatório de Alunos aprovados")
        elif opcao == "2":
            print("Relatório de Alunos reprovados")
        elif opcao == "3":
            print("Relatório de Professores com muitos alunos")
        elif opcao == "4":
            print("Estatísticas gerais")
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()