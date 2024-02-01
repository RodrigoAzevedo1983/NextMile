import csv
import os
import math
from datetime import datetime
import comparaJanelas
import configparser

cfg = configparser.ConfigParser()
cfg.read('./faturamento/consolidador/config.ini')
#cfg.read('./config.ini')
pasta_origem = cfg.get('pastas', 'pasta_origem')
pasta_saida = cfg.get('pastas', 'pasta_saida')
pasta_periodo_anterior = cfg.get('pastas', 'pasta_periodo_anterior')
pasta_logs = cfg.get('pastas', 'pasta_logs')
arquivo_de_log = pasta_logs + "/log_" + datetime.now().strftime("%Y-%m-%d_%H%M%S")+".log"

arquivo_periodo_anterior = pasta_periodo_anterior + "periodo_anterior_23-10-21_a_23-11-05.csv"


dados_duplicados = []
dados_consolidados_mes = []
dados_duplicados_periodo_anterior = []

quantidade_linhas_arquivo = 0
quantidade_linhas_escritas_consolidado_final = 0
quantidade_linhas_escritas_duplicado = 0
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
mcus_dinamicas = {}
mcus_dinamicas_ok = {}
totais_mcu = {}



extensoes = ['csv']
arquivos = os.listdir(pasta_origem)
arquivos_csv = []

arquivos_periodo_anterior = os.listdir(pasta_periodo_anterior)
arquivos_periodo_anterior_csv = []



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
        quantidade_linhas_arquivo += 1
        chave = (linha[1], linha[3])

        # Verifique se a chave já existe nos registros duplicados
        if chave in chaves_lidas:
          # Se já existe, este é um registro duplicado, então não o adicionamos a lista2
          dados_duplicados.append(linha)
          continue

        # Adicione a string de registro a lista2
        dados_consolidados_mes.append(linha)
        # Marque a chave como vista nos registros duplicados
        chaves_lidas.add(chave)
    print ("Registros no arquivo",arquivo,":",quantidade_linhas_arquivo)

print ("TOTAIS:")
print ("Registros Duplicados:", len(dados_duplicados))
print ("Registros Únicos:", len(dados_consolidados_mes))

###
### Compara duplicados já faturados no período anterior e cria lotes de 1000 registros únicos
###

print("\nComparando registros com o período anterior...")


for i in arquivos_periodo_anterior:
    extensao = i.split('.')[-1]
    if extensao in extensoes:
        arquivos_periodo_anterior_csv.append(i)

for arquivo in arquivos_periodo_anterior_csv:
    caminho_arquivo_periodo_anterior = pasta_periodo_anterior + arquivo
    with open(caminho_arquivo_periodo_anterior, mode='r', encoding="utf8") as arquivo_csv:
      dados_csv = csv.reader(arquivo_csv)
      cabecalho = next(dados_csv)
      for linha in dados_csv:
          chave = (linha[1], linha[3])
          chaves_periodo_anterior.add(chave)
                  
qtd_arquivos_saida = math.trunc(len(dados_consolidados_mes)/1000000)+1
i = 1
while i <= qtd_arquivos_saida:
  dados_consolidados_final[i] = []
  i += 1

cont_registros = 0
for linha in dados_consolidados_mes:
  chave = (linha[1], linha[3])
  if chave in chaves_periodo_anterior:
    dados_duplicados_periodo_anterior.append(linha)
    continue
  else:
    cont_registros += 1
    id_arquivo = math.ceil(cont_registros/1000000)
    dados_consolidados_final[id_arquivo].append(linha)
    dados_consolidados_final_unico.append(linha)
    chave_mcu = (linha[2])
    if linha[1] == "EC":
      if chave_mcu in chaves_unicas_mcu:
          continue
      else:
        chaves_unicas_mcu.add(chave_mcu)

print("CONTAGEM PERIODO ANTERIOR")
print("Registros periodo anterior:", len(chaves_periodo_anterior))
print("Registros duplicados periodo anterior:", len(dados_duplicados_periodo_anterior))
print("\nCONTAGEM FINAL")
print("Registros unicos consolidados:", len(dados_consolidados_final_unico))


#####################################

# Grava arquivos consolidados
print("Gerando arquivos com registros únicos...")
i = 1
while i <= qtd_arquivos_saida:
  arquivo_de_saida_consolidado[i] = pasta_saida + "registros_unicos_" + str(i) + ".csv"
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

#####################################



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

print("Gerando arquivos com totais de EP e EC por data")
arquivo_de_saida_totais_por_data = pasta_saida + "totais_ep_ec_por_data.csv"
arquivo_saida = open(arquivo_de_saida_totais_por_data, mode="w", encoding="utf8")
arquivo_saida.write("Data,Plataformizado,Colaborativo,Total\n")
for linha in totais_ep_ec_por_data:
   arquivo_saida.write(linha + "\n")
arquivo_saida.close()


### POR MCU

qtd_mcus = len(chaves_unicas_mcu)
print("Quantidade MCUs: ", qtd_mcus)

for linha in chaves_unicas_mcu:
  mcus_dinamicas[linha] = []
  mcus_dinamicas_ok[linha] = []
  totais_mcu[linha] = []
  #print("\n\nDEBUG - for linha in chaves_unicas_mcu: ", linha)

for linha in dados_consolidados_final_unico:
  if linha[1] == "EC":
      chave_mcu = (linha[2])
      mcus_dinamicas[chave_mcu].append(linha)


'''
print("\nDEBUG - len(dados_consolidados_final_unico): ", len(dados_consolidados_final_unico), "\n")
for linha in chaves_unicas_mcu:
  print("DEBUG - len(mcus_dinamicas[linha]): ", len(mcus_dinamicas[linha]))
for registro in mcus_dinamicas:
   print("\nDEBUG - for registro in mcus_dinamicas: ", registro, "\nDEBUG - Tamanho: ", len(mcus_dinamicas[registro]))
   #for linha in mcus_dinamicas[registro]: print("DEBUG LINHA:", linha[3])
'''


total_registros = 0
total_entregas = 0
total_tentativa1 = 0
total_tentativa2 = 0
total_tentativa3 = 0
total_janelas_repetidas = 0
janela_repetida_mcu = 0
janela_repetida_linha = 0
total_sem_data = 0
totais = {}
totais2 = []


registros_sem_data = []

for mcu in mcus_dinamicas:
    #print("\nDEBUG - for mcu in mcus_dinamicas: " ,mcu)
    #print("DEBUG - len(mcus_dinamicas[mcu]): " ,len(mcus_dinamicas[mcu]))
    nome_mcu = mcu
    registros_mcu = 0
    entregas_mcu = 0
    tentativa1_mcu = 0
    tentativa2_mcu = 0
    tentativa3_mcu = 0
    sem_datas_mcu = 0
    janelas_repetidas_mcu = 0
    linha_totais = ""
    contador = 0
    for linha in mcus_dinamicas[mcu]:
        total_registros += 1
        registros_mcu += 1
        janela_repetida_linha = 0
        data_tentativa1 = ""
        hora_tentativa1 = ""
        data_tentativa2 = ""
        hora_tentativa2 = ""
        data_tentativa3 = ""
        hora_tentativa3 = ""
        objeto = linha[3]
        tentativa1 = linha[7]
        tentativa2 = linha[8]
        tentativa3 = linha[9]
        entrega = linha[10]
        devolucao = linha[11]
        if entrega == "" and tentativa1 == "" and tentativa2 == "" and tentativa3 == "" and devolucao == "":
            sem_datas_mcu += 1
            total_sem_data += 1
            registros_sem_data.append(linha)
        else:
            mcus_dinamicas_ok[mcu].append(linha)
            if entrega != "":
                total_entregas += 1
                entregas_mcu += 1
                data_entrega = comparaJanelas.getData(entrega)
                hora_entrega = comparaJanelas.getHora(entrega)
                janela_entrega = comparaJanelas.verificaJanela(entrega)
                print("DEBUG -", objeto, "- ENTREGA:   ",entrega, "- DATE:",data_entrega, "- TIME:",hora_entrega, "Janela:",janela_entrega)
            if tentativa1 != "":
                total_tentativa1 += 1
                tentativa1_mcu += 1
                data_tentativa1 = comparaJanelas.getData(tentativa1)
                hora_tentativa1 = comparaJanelas.getHora(tentativa1)
                janela_tentativa1 = comparaJanelas.verificaJanela(tentativa1)
                if data_tentativa1 == data_entrega:
                    if comparaJanelas.comparaJanela(janela_tentativa1,janela_entrega):
                        print("DEBUG DEBUG DEBUG - JANELA1 = JANELA_ENTREGA")
                        janelas_repetidas_mcu +=1
                        total_janelas_repetidas +=1
                        janela_repetida_linha += 1
                    print("DEBUG -", objeto, "- TENTATIVA1:",tentativa1, "- DATE:",data_tentativa1, "- TIME:",hora_tentativa1, "JANELAS:", janela_entrega, "+", janela_tentativa1, "JANELAS REPETIDAS:", janela_repetida_linha)
                if tentativa2 != "":
                    total_tentativa2 += 1
                    tentativa2_mcu += 1
                    data_tentativa2 = comparaJanelas.getData(tentativa2)
                    hora_tentativa2 = comparaJanelas.getHora(tentativa2)
                    janela_tentativa2 = comparaJanelas.verificaJanela(tentativa2)
                    if data_tentativa2 == data_entrega:
                        if comparaJanelas.comparaJanela(janela_tentativa2,janela_entrega):
                            print("DEBUG DEBUG DEBUG - JANELA2 = JANELA_ENTREGA")
                            janelas_repetidas_mcu +=1
                            total_janelas_repetidas +=1
                            janela_repetida_linha += 1
                    if data_tentativa2 == data_tentativa1:
                        if comparaJanelas.comparaJanela(janela_tentativa2,janela_tentativa1):
                            print("DEBUG DEBUG DEBUG - JANELA2 = JANELA1")
                            janelas_repetidas_mcu +=1
                            total_janelas_repetidas +=1
                            janela_repetida_linha += 1
                    print("DEBUG -", objeto, "- TENTATIVA2:",tentativa2, "- DATE:",data_tentativa2, "- TIME:",hora_tentativa2, "JANELAS:", janela_entrega, "+", janela_tentativa1, "+", janela_tentativa2, "JANELAS REPETIDAS:", janela_repetida_linha)
                    if tentativa3 != "":
                        total_tentativa3 += 1
                        tentativa3_mcu += 1
                        data_tentativa3 = comparaJanelas.getData(tentativa3)
                        hora_tentativa3 = comparaJanelas.getHora(tentativa3)
                        janela_tentativa3 = comparaJanelas.verificaJanela(tentativa3)
                        if data_tentativa3 == data_entrega:
                            if comparaJanelas.comparaJanela(janela_tentativa3,janela_entrega):
                                print("DEBUG DEBUG DEBUG - JANELA3 = JANELA_ENTREGA")
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida_linha += 1
                        if data_tentativa3 == data_tentativa1:
                            if comparaJanelas.comparaJanela(janela_tentativa3,janela_tentativa1):
                                print("DEBUG DEBUG DEBUG - JANELA3 = JANELA1")
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida_linha += 1
                        if data_tentativa3 == data_tentativa2:
                            if comparaJanelas.comparaJanela(janela_tentativa3,janela_tentativa2):
                                print("DEBUG DEBUG DEBUG - JANELA3 = JANELA2")
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida_linha += 1
                        print("DEBUG -", objeto, "- TENTATIVA3:",tentativa3, "- DATE:",data_tentativa3, "- TIME:",hora_tentativa3, "JANELAS:", janela_entrega, "+", janela_tentativa3, "JANELAS REPETIDAS:", janela_repetida_linha)
    linha_totais = nome_mcu, registros_mcu, entregas_mcu, tentativa1_mcu, tentativa2_mcu, tentativa3_mcu, sem_datas_mcu, janelas_repetidas_mcu
    totais2.append(linha_totais)
    print("TOTAIS:",linha_totais)
    totais[nome_mcu] = {"mcu":nome_mcu ,"total_registros":registros_mcu, "entregas":entregas_mcu, "tentativa1":tentativa1_mcu, "tentativa2":tentativa2_mcu, "tentativa3":tentativa3_mcu, "sem_datas":sem_datas_mcu, "janelas_repetidas": janelas_repetidas_mcu}
    
    print("Arquivo ", arquivo, "\nRegistros no arquivo: ", registros_mcu, "\nEntregas no MCU", entregas_mcu,"\nTentativa1 no MCU:", tentativa1_mcu,"\nTentativa2 no MCU:", tentativa2_mcu,"\nTentativa3 no MCU:", tentativa3_mcu,"\nJanelas repetidas no MCU:", janelas_repetidas_mcu, "\nRegistros sem data:",sem_datas_mcu)
    print("\n")


    print("DEBUG - len(mcus_dinamicas[mcu]) - ", nome_mcu, ":" ,len(mcus_dinamicas[nome_mcu]))
    print("DEBUG - len(mcus_dinamicas_ok[mcu]) - ", nome_mcu, ":" ,len(mcus_dinamicas_ok[nome_mcu]))

print("Total de registros:", total_registros, "\nTotal de Entregas:", total_entregas, "\ntotal de tentativas1:", total_tentativa1, "\ntotal de tentativas2:", total_tentativa2, "\ntotal de tentativas3:", total_tentativa3, "\ntotal de janelas repetidas: ", total_janelas_repetidas, "\nTotal sem data:", total_sem_data, "\nTotal de MCUs:", qtd_mcus, "\n")

for chave, registros in mcus_dinamicas_ok.items():
  arquivo_de_saida_por_mcu = pasta_saida + "por mcu/" + chave + ".csv"
  with open(arquivo_de_saida_por_mcu, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
     escritor_csv = csv.writer(arquivo_csv_saida)
     escritor_csv.writerow(cabecalho)
     for linha in registros:
        if linha[1] == "EC":
           escritor_csv.writerow(linha)
  print("Arquivo gerado:", arquivo_de_saida_por_mcu)


arquivo_de_saida_registros_sem_data = pasta_saida + "por mcu/registros_sem_data.csv"
with open(arquivo_de_saida_registros_sem_data, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in registros_sem_data:
        escritor_csv.writerow(linha)
    print("Arquivo gerado:", arquivo_de_saida_registros_sem_data)


arquivo_de_saida_totais_csv = pasta_saida + "por mcu/totais_por_mcu.csv"
with open(arquivo_de_saida_totais_csv, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    cabecalho = ["mcu","total_registros","entregas","tentativa1","tentativa2","tentativa3","sem_datas","janelas_repetidas"]
    escritor_csv.writerow(cabecalho)
    for linha in totais2:
        escritor_csv.writerow(linha)
    print("Arquivo gerado:", arquivo_de_saida_totais_csv)


qtd_mcus = "Total de MCUs: " + str(qtd_mcus) + "\n"
str_total_registros = "Total de registros:" + str(total_registros) + "\n"
str_total_entregas = "Total de Entregas:" + str(total_entregas) + "\n"
str_total_tentativa1 = "Total de tentativas 1:" + str(total_tentativa1) + "\n"
str_total_tentativa2 = "Total de tentativas 2:" + str(total_tentativa2) + "\n"
str_total_tentativa3 = "Total de tentativas 3:" + str(total_tentativa3) + "\n"
str_total_sem_data = "Total sem datas:" + str(total_sem_data) + "\n"

print("FIM")
