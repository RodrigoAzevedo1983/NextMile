import csv

dados_duplicados = []
dados_consolidados_mes = []
dados_consolidados_final = []
dados_duplicados_periodo_anterior = []

quantidade_registros_duplicados = 0
quantidade_registros_unicos = 0
quantidade_registros_unicos_final = 0
quantidade_linhas_arquivo = 0
quantidade_linhas_escritas_consolidado_final = 0
quantidade_linhas_escritas_duplicado = 0
quantidade_linhas_arquivo_periodo_anterior = 0
quantidade_registros_duplicados_periodo_anterior = 0
quantidade_linhas_escritas_duplicado_periodo_anterior = 0

chaves_lidas = set()
chaves_periodo_anterior = set()

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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1
      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_22.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_23.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_25.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_26.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_27.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_28.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_29.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_09_30.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10_02.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10_03.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10_04.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)

print("\nCONTAGEM INICIAL")
print("Total de linhas do arquivo: ", quantidade_linhas_arquivo)
print("Registros unicos: ", quantidade_registros_unicos)
print("Registros duplicados: ", quantidade_registros_duplicados)

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\2023_10_05.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
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
      dados_consolidados_mes.append(linha)
      quantidade_registros_unicos = quantidade_registros_unicos + 1

      # Marque a chave como vista nos registros duplicados
      chaves_lidas.add(chave)


###
### Compara duplicados já faturados no período anterior
###

with open('D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\anteriores_2023_09_18_a_2023_09_20.csv', mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      quantidade_linhas_arquivo_periodo_anterior = quantidade_linhas_arquivo_periodo_anterior + 1
      chave = (linha[1], linha[3])
      chaves_periodo_anterior.add(chave)

for linha in dados_consolidados_mes:
  chave = (linha[1], linha[3])
  if chave in chaves_periodo_anterior:
    dados_duplicados_periodo_anterior.append(linha)
    quantidade_registros_duplicados_periodo_anterior = quantidade_registros_duplicados_periodo_anterior + 1
    continue
    #dados_consolidados_mes.remove(linha)
  
  dados_consolidados_final.append(linha)
  quantidade_registros_unicos_final = quantidade_registros_unicos_final + 1

print("\nCONTAGEM PERIODO ANTERIOR")
print("Registros periodo anterior: ", quantidade_linhas_arquivo_periodo_anterior)
print("Registros duplicados periodo anterior: ", quantidade_registros_duplicados_periodo_anterior)

print("\nCONTAGEM FINAL")
print("Registros unicos consolidados: ", quantidade_registros_unicos_final)

arquivo_de_saida_consolidado = "D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\registros_unicos.csv"
arquivo_de_saida_duplicados = "D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\registros_duplicados.csv"
arquivo_de_saida_duplicados_periodo_anterior = "D:\\Projetos\\Next Mile\\Conciliação\\2023-09 - QUINZENA 02  21-09-2023 a 05-10-2023 - EP e EC\\registros_duplicados_periodo_anterior.csv"

with open(arquivo_de_saida_consolidado, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_consolidados_final:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_consolidado_final = quantidade_linhas_escritas_consolidado_final + 1

with open(arquivo_de_saida_duplicados, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_duplicados:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_duplicado = quantidade_linhas_escritas_duplicado + 1

with open(arquivo_de_saida_duplicados_periodo_anterior, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_duplicados_periodo_anterior:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_duplicado_periodo_anterior = quantidade_linhas_escritas_duplicado_periodo_anterior + 1

print("\nNOVOS ARQUIVOS:")
print("registros_unicos.csv: ", quantidade_linhas_escritas_consolidado_final)
print("registros_duplicados.csv: ", quantidade_linhas_escritas_duplicado)
print("registros_duplicados_periodo_anterior.csv: ", quantidade_linhas_escritas_duplicado_periodo_anterior)
