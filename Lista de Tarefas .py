lista = []
def adicionar_tarefa(tarefa):
     tarefa = {"nome": tarefa,
        "status": False}
     adicionar = lista.append(tarefa)
     return adicionar

def listar_tarefas(lista):
    if not lista:
        return print("Nenhuma tarefa diponível.")
    for i, tarefa in enumerate(lista):
       print(f"Indice {i+1} = {tarefa} ")

def marcar_concluida(lista, tarefa):
    if 0 <= tarefa < len(lista):
     marcar = lista[tarefa]["status"] = True  
     return marcar
    else:
       print("Não existe está tarefa na lista.")

def remover_lista(lista, tarefa):
    if 0 <= tarefa < len(lista):
         del lista[tarefa]
    else:
        print("Não existe está tarefa na lista.")     

while True:
  print("\nMenu:")
  print("1. Adicionar Tarefa")
  print("2. Listar Tarefa")
  print("3. Marcar Tarefa como Concluída")
  print("4. Remover Tarefa")
  print("5. Sair")    

  opcao = input("Digite a Opção: ")
  match opcao:
     case "1":
          usuario = input("Digite a Tarefa: ")
          adicionar_tarefa(usuario)
          while True:
           tarefa_adicionar = input("Deseja adicionar mais alguma Tarefa ? (S/N) ")
           if tarefa_adicionar == "s":
            usuario = input("Digite a tarefa: ")
            adicionar_tarefa(usuario)
           else:
            print(lista)
            break
     case "2":  
          listar_tarefas(lista)
     case "3":    
          marcar_tarefa = int(input("Qual tarefa deseja marcar como concluida: "))
          marcar_concluida(lista,marcar_tarefa)
          print(lista)
     case "4":
          remover = int(input("Digite o número da tarefa que deseja remover: "))
          remover_lista(lista,remover)
          print(f"Tarefa {remover} removida com Sucesso.")
     case "5":
          print("Programa finalizado.")
          break      

    
   
         
         
         

