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
chaves_datas = set()

dados_consolidados_final_unico = []
dados_consolidados_final = {}
arquivo_de_saida_consolidado = {}
quantidade_linhas_escritas_consolidado_arquivo = {}
totais_ep_ec_por_data = []


pasta_base = "D:/Projetos/Next Mile/Faturamento/23-11-06 - 23-11-20/"
pasta_origem = pasta_base + "entrada/"
arquivo_periodo_anterior = pasta_origem + "periodo anterior/periodo_anterior_23-10-21_a_23-11-05.csv"
pasta_saida = pasta_base + "saida/"

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

print("\nComparando registros com o período anterior...")

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
    dados_consolidados_final_unico.append(linha)
    quantidade_registros_unicos_final += 1
    chave_mcu = (linha[2])
    if linha[1] == "EC":
      if chave_mcu in chaves_unicas_mcu:
          continue
      else:
        chaves_unicas_mcu.add(chave_mcu)

print("CONTAGEM PERIODO ANTERIOR")
print("Registros periodo anterior:", quantidade_linhas_arquivo_periodo_anterior)
print("Registros duplicados periodo anterior:", quantidade_registros_duplicados_periodo_anterior)
print("\nCONTAGEM FINAL")
print("Registros unicos consolidados:", quantidade_registros_unicos_final)

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


### Contadores por data:

for linha in dados_consolidados_final_unico:
   chave = (linha[0])
   if chave in chaves_datas:
      continue
   else:
    chaves_datas.add(chave)

for registro in chaves_datas:
   quantidade_ep = 0
   quantidade_ec = 0
   for linha in dados_consolidados_final_unico:
      chave_data = (linha[0])
      chave_entrega = (linha[1])
      if chave_data == registro:
        if chave_entrega == "EP":
            quantidade_ep += 1
        elif chave_entrega == "EC":
           quantidade_ec += 1
   totais = str(registro) + "," + str(quantidade_ep) + "," + str(quantidade_ec) + "," + str(quantidade_ep + quantidade_ec)
   totais_ep_ec_por_data.append(totais)
   #print("DEBUG -", totais)

print("Gerando arquivos com totais de EP e EC por data")
arquivo_de_saida_totais_por_data = pasta_saida + "totais_ep_ec_por_data.csv"
arquivo_saida = open(arquivo_de_saida_totais_por_data, mode="w", encoding="utf8")
arquivo_saida.write("Data,Plataformizado,Colaborativo,Total\n")
for linha in totais_ep_ec_por_data:
   arquivo_saida.write(linha + "\n")
arquivo_saida.close()



######## AAAAAAAAAAAAAAAAAA
'''
arquivo_de_saida_totais_por_data = pasta_saida + "totais_ep_ec_por_data.csv"
# Grava arquivo de totais EP e EC por data
with open(arquivo_de_saida_totais_por_data, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    cabecalho = "Data,Plataformizado,Colaborativo,Total"
    escritor_csv.writerow(cabecalho)
    for linha in totais_ep_ec_por_data:
        print("DEBUG - LINHA -", linha)
        escritor_csv.writerow(linha)
'''
######### AAAAAAAAAAAA FIM



#for linha in dados_consolidados_final_unico:
#    print("DEBUG -", linha)



### POR MCU, APENAS EC
print("\n\nPOR MCU")

qtd_mcus = 0
mcus_dinamicas = {}

for linha in chaves_unicas_mcu:
   mcus_dinamicas[linha] = []
   qtd_mcus +=1

print("Quantidade MCUs: ", qtd_mcus)

for linha in dados_consolidados_final_unico:
  if linha[1] == "EC":
    chave_mcu = (linha[2])
    mcus_dinamicas[chave_mcu].append(linha)
for registro_mcu in chaves_unicas_mcu:
  contador = 0
  arquivo_de_saida_por_mcu = pasta_saida + "por mcu/" + registro_mcu + ".csv"
  with open(arquivo_de_saida_por_mcu, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in mcus_dinamicas[registro_mcu]:
        escritor_csv.writerow(linha)
        contador += 1
  print("Registros em",registro_mcu,":",contador)
  

print("FIM")