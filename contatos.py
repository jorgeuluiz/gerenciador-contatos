def adicionar_contato(contato, nome_contato, telefone_contato, email_contato, favorito):  
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": favorito}
  contatos.append(contato)
  print(f"Contato {nome_contato} {telefone_contato} {email_contato} {favorito} foi adicionada com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"{indice}. [{favorito}] nome: {nome_contato}, telefone: {telefone_contato}, email: {email_contato}")

def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email, favorito):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    contatos[indice_contato_ajustado]["favorito"] = favorito
    print(f"contato {indice_contato} atualizada para {novo_nome}")
  else:
    print("Índice de contatos inválido.")
  return

def ver_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  contador_favoritos = 0
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      contador_favoritos += 1
      favorito = "✓"
      nome_contato = contato["nome"]
      telefone_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"{indice}. [{favorito}] nome: {nome_contato}, telefone: {telefone_contato}, email: {email_contato}")
  if contador_favoritos == 0:
        print("Nenhum contato favorito encontrado.")    

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
    print(f"Contato {indice_contato} marcado/desmarcado.")
  else:
    print("Índice de contatos inválido.")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos.remove(contatos[indice_contato_ajustado])
    print(f"Contato {indice_contato} apagado.")
  else:
    print("Índice de contatos inválido.")
  return

contatos = []
while True:
  print("\nMenu do Gerenciador de Lista de contatos:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Atualizar Contato")
  print("4. Marcar/Desmarcar um contato como favorito")
  print("5. Lista de Favoritos")
  print("6. Deletar contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
    email_contato = input("Digite o email do contato que deseja adicionar: ")
    favorito = input("Esse contato é favorito? (True/False): ")    
    valor_booleano = None
    if favorito.lower() == "true":
        valor_booleano = True
    elif favorito.lower() == "false":
        valor_booleano = False
    else:
        print("Valor inválido. Por favor, digite True ou False.")   
    if valor_booleano is not None:
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, valor_booleano)
    else:
        print("Contato não adicionado devido a valor inválido para favorito.")

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    favorito = input("Esse contato é favorito? (True/False): ")    
    valor_booleano = None
    if favorito.lower() == "true":
        valor_booleano = True
    elif favorito.lower() == "false":
        valor_booleano = False
    else:
        print("Valor inválido. Por favor, digite True ou False.")   
    if valor_booleano is not None:
        atualizar_contato(contatos, indice_contato, nome_contato, telefone_contato, email_contato, valor_booleano)
    else:
        print("Contato não adicionado devido a valor inválido para favorito.")

  elif escolha =="4":
    ver_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja marcar/desmarcar como favorito: ")
    favoritar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha =="5":
    ver_contatos_favoritos(contatos)    

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja apagar: ")
    deletar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha == "7":
    break

print("Programa finalizado")