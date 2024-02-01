import csv
import os
import math

dados_duplicados = []
dados_consolidados_mes = []
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
chaves_unicas_mcu = set()

dados_consolidados_final = {}
arquivo_de_saida_consolidado = {}
quantidade_linhas_escritas_consolidado_arquivo = {}

pasta_origem = "D:/Projetos/Next Mile/Faturamento/23-10-06 - 23-10-20/Entrada/"
arquivo_periodo_anterior = pasta_origem + "Periodo Anterior/Periodo_anterior_2023-10-03_a_05 _202310231031.csv"
pasta_saida = "D:/Projetos/Next Mile/Faturamento/23-10-06 - 23-10-20/Saida/"

extensoes = ['csv']
arquivos = os.listdir(pasta_origem)
arquivos_csv = []

for i in arquivos:
    extensao = i.split('.')[-1]
    if extensao in extensoes:
        arquivos_csv.append(i)

print("Lendo arquivos...")

for arquivo in arquivos_csv:
    quantidade_linhas_arquivo = 0
    caminho_arquivo = pasta_origem + arquivo
    with open(caminho_arquivo, mode='r', encoding="utf8") as arquivo_csv:
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
    print ("Registros no arquivo",arquivo,":",quantidade_linhas_arquivo)

print ("TOTAIS:")
print ("Registros Duplicados:", quantidade_registros_duplicados)
print ("Registros Únicos:", quantidade_registros_unicos)

###
### Compara duplicados já faturados no período anterior e cria lotes de 1000 registros únicos
###

print("Comparando registros com o período anterior...")

### MELHORAR LÓGICA:

qtd_arquivos_saida = math.trunc(quantidade_registros_unicos/1000000)+1
i = 1
while i <= qtd_arquivos_saida:
  dados_consolidados_final[i] = []
  i += 1

with open(arquivo_periodo_anterior, mode='r', encoding="utf8") as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    next(dados_csv)  # pula a primeira linha (cabeçalho)
    for linha in dados_csv:
      quantidade_linhas_arquivo_periodo_anterior = quantidade_linhas_arquivo_periodo_anterior + 1
      chave = (linha[1], linha[3])
      chaves_periodo_anterior.add(chave)
cont_registros = 0
for linha in dados_consolidados_mes:
  chave = (linha[1], linha[3])
  if chave in chaves_periodo_anterior:
    dados_duplicados_periodo_anterior.append(linha)
    quantidade_registros_duplicados_periodo_anterior = quantidade_registros_duplicados_periodo_anterior + 1
    continue
  else:
    cont_registros += 1
    id_arquivo = math.ceil(cont_registros/1000000)
    dados_consolidados_final[id_arquivo].append(linha)
    quantidade_registros_unicos_final += 1
    chave_mcu = (linha[2])
    if linha[1] == "EC":
      if chave_mcu in chaves_unicas_mcu:
          continue
      else:
        chaves_unicas_mcu.add(chave_mcu)

print("\nCONTAGEM PERIODO ANTERIOR")
print("Registros periodo anterior: ", quantidade_linhas_arquivo_periodo_anterior)
print("Registros duplicados periodo anterior: ", quantidade_registros_duplicados_periodo_anterior)

print("\nCONTAGEM FINAL")
print("Registros unicos consolidados: ", quantidade_registros_unicos_final)


# Grava arquivos consolidados

print("Gerando arquivos com registros únicos...")

i = 1
while i <= qtd_arquivos_saida:
  arquivo_de_saida_consolidado[i] = pasta_saida + "registros_unicos_0" + str(i) + ".csv"
  with open(arquivo_de_saida_consolidado[i], mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_consolidados_final[i]:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_consolidado_final += 1
  print(arquivo_de_saida_consolidado[i])
  i += 1


print("Gerando arquivos com os registros duplicados...")
arquivo_de_saida_duplicados = pasta_saida + "registros_duplicados.csv"
arquivo_de_saida_duplicados_periodo_anterior = pasta_saida + "registros_duplicados_periodo_anterior.csv"

# Grava arquivo de duplicados no mês
with open(arquivo_de_saida_duplicados, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_duplicados:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_duplicado += 1

# Grava arquivo de Duplicados no preíodo anterior
with open(arquivo_de_saida_duplicados_periodo_anterior, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in dados_duplicados_periodo_anterior:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas_duplicado_periodo_anterior += 1
print("registros_duplicados.csv: ", quantidade_linhas_escritas_duplicado)
print("registros_duplicados_periodo_anterior.csv: ", quantidade_linhas_escritas_duplicado_periodo_anterior)


### POR MCU, APENAS EC

print("\n\nPOR MCU")

qtd_mcus = 0
mcus_dinamicas = {}

for linha in chaves_unicas_mcu:
   mcus_dinamicas[linha] = []
   qtd_mcus +=1

print("Quantidade MCUs: ", qtd_mcus)

i = 1
while i <= qtd_arquivos_saida:
  dados_consolidados_final[i] = []
  
  for linha in dados_consolidados_final[i]:
    chave_mcu = (linha[2])
    if linha[1] == "EC":
        mcus_dinamicas[chave_mcu].append(linha)
  for linha in chaves_unicas_mcu:
    contador = 0
    arquivo_de_saida_por_mcu = pasta_saida + chave_mcu + ".csv"
    with open(arquivo_de_saida_por_mcu, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
      escritor_csv = csv.writer(arquivo_csv_saida)
      escritor_csv.writerow(cabecalho)
      for registro in mcus_dinamicas[linha]:
          if registro[1] == "EC":
            contador += 1
            escritor_csv.writerow(registro)
    print("Registros em ",linha,":",contador)
  i += 1

print("FIM")
