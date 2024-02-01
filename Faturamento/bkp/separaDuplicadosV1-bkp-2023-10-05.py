import csv

dados_duplicados = []
dados_consolidados_unicos = []

quantidade_registros_duplicados = 0
quantidade_registros_unicos = 0
quantidade_linhas_arquivo = 0
quantidade_linhas_escritas_consolidado = 0
quantidade_linhas_escritas_duplicado = 0

chaves_lidas = set()

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_21.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    cabecalho = next(dados_csv)
    for linha in dados_csv:
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1
      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_22.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_23.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_25.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_26.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_27.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_28.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_29.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_30.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10-02.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10-03.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10-04.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      
      quantidade_linhas_arquivo = quantidade_linhas_arquivo + 1
      chave = (linha[1], linha[3])
      #print("DEBUG: ", chave)

      # Verifique se a chave já existe nos registros duplicados
      if chave in chaves_lidas:
        # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
        dados_duplicados.append(linha)
        quantidade_registros_duplicados = quantidade_registros_duplicados + 1
        continue

      # Adicione a string de registro a lista2
      dados_consolidados_unicos.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)


print("\nCONTAGEM")
print("Total de linhas do arquivo: ", quantidade_linhas_arquivo)
print("Registros unicos: ", quantidade_registros_unicos)
print("Registros duplicados: ", quantidade_registros_duplicados)



arquivo_de_saida_consolidado = "D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\registros_unicos.csv"
arquivo_de_saida_duplicados = "D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\registros_duplicados.csv"

with open(arquivo_de_saida_consolidado, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_consolidados_unicos:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_consolidado = quantidade_linhas_escritas_consolidado + 1

with open(arquivo_de_saida_duplicados, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_duplicados:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_duplicado = quantidade_linhas_escritas_duplicado + 1


print("\nNOVOS ARQUIVOS:")
print("registros_unicos.csv: ", quantidade_linhas_escritas_consolidado)
print("registros_duplicados.csv: ", quantidade_linhas_escritas_duplicado)