import csv
import os

total_registros = 0
total_entregas = 0
total_tentativa1 = 0
total_tentativa2 = 0
total_tentativa3 = 0
total_sem_data = 0
qtd_mcus = 0
mcus_dinamicas = {}
totais = {}
totais2 = []

pasta_origem = "D:/Projetos/Next Mile/Faturamento/23-10-06 - 23-10-20/Saida/por mcu/"
extensoes = ['csv']
arquivos = os.listdir(pasta_origem)
arquivos_csv = []
registros_sem_data = []

for i in arquivos:
    extensao = i.split('.')[-1]
    if extensao in extensoes:
        arquivos_csv.append(i)

print(arquivos_csv)

for arquivo in arquivos_csv:
    caminho_arquivo = pasta_origem + arquivo
    
    #print(pasta_origem)
    #print(arquivo.split(".")[0])
    #print(caminho_arquivo)

    nome_mcu = arquivo.split(".")[0]
    mcus_dinamicas[nome_mcu] = []
    totais[nome_mcu] = {}
    qtd_mcus += 1
        
    registros_mcu = 0
    entregas_mcu = 0
    tentativa1_mcu = 0
    tentativa2_mcu = 0
    tentativa3_mcu = 0
    sem_datas_mcu = 0
    with open(caminho_arquivo, mode='r', encoding="utf8") as arquivo_csv:
        dados_csv = csv.reader(arquivo_csv)
        cabecalho = next(dados_csv)
        linha_totais = ""
        for linha in dados_csv:
            total_registros += 1
            registros_mcu += 1
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
                mcus_dinamicas[nome_mcu].append(linha)
                total_entregas += 1
                entregas_mcu += 1
                data_entrega = entrega.split(" ")[0]
                hora_entrega = entrega.split(" ")[-1]
                #print("\nEntrega:", entrega, "Data Entrega:", data_entrega, "Hora Entrega:", hora_entrega)
                if tentativa1 != "":
                    total_tentativa1 += 1
                    tentativa1_mcu += 1
                    data1 = tentativa1.split(" ")[0]
                    hora1 = tentativa1.split(" ")[-1]
                    #print("Tentativa1:", tentativa1, "Data1:", data1, "Hora1:", hora1)
                    if tentativa2 != "":
                        total_tentativa2 += 1
                        tentativa2_mcu += 1
                        data2 = tentativa2.split(" ")[0]
                        hora2 = tentativa2.split(" ")[-1]
                        if data2 == data1:
                            print("datas repetem")
                            print("Tentativa2:", tentativa2, "Data2:", data2, "Hora2:", hora2)
                        if tentativa3 != "":
                            total_tentativa3 += 1
                            tentativa3_mcu += 1
                            data3 = tentativa3.split(" ")[0]
                            hora3 = tentativa3.split(" ")[-1]
                            #print("Tentativa3:", tentativa3, "Data3:", data3, "Hora3:", hora3)
        linha_totais = nome_mcu, registros_mcu, entregas_mcu, tentativa1_mcu, tentativa2_mcu, tentativa3_mcu, sem_datas_mcu, 0
        totais2.append(linha_totais)
        print("TOTAIS:",linha_totais)
        totais[nome_mcu] = {"mcu":nome_mcu ,"total_registros":registros_mcu, "entregas":entregas_mcu, "tentativa1":tentativa1_mcu, "tentativa2":tentativa2_mcu, "tentativa3":tentativa3_mcu, "sem_datas":sem_datas_mcu, "janelas_repetidas": 0}
        #totais[nome_mcu] = {nome_mcu, registros_mcu, entregas_mcu, tentativa1_mcu, total_tentativa2, total_tentativa3, sem_datas_mcu, 0}
            
            #if data1 == data2: 
    print("Arquivo ", arquivo, "\nRegistros no arquivo: ", registros_mcu, "\nEntregas no MCU", entregas_mcu,"\nTentativa1 no MCU:", tentativa1_mcu,"\nTentativa2 no MCU:", tentativa2_mcu,"\nTentativa3 no MCU:", tentativa3_mcu, "\nRegistros sem data:",sem_datas_mcu)
    print("\n")
print("Total de registros:", total_registros, "\nTotal de Entregas:", total_entregas, "\ntotal de tentativas1: ", total_tentativa1, "\ntotal de tentativas2: ", total_tentativa2, "\ntotal de tentativas3: ", total_tentativa3, "\nTotal sem data:", total_sem_data, "\nTotal de MCUs:", qtd_mcus)

'''
for chave, linhas in mcus_dinamicas.items():
    print(f'Chave: {chave}\nLinhas:')
    for dado in linhas:
        print(dado)
'''

for chave, registros in mcus_dinamicas.items():
  arquivo_de_saida_por_mcu = pasta_origem + "totais/" + chave + ".csv"
  with open(arquivo_de_saida_por_mcu, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
     escritor_csv = csv.writer(arquivo_csv_saida)
     escritor_csv.writerow(cabecalho)
     for linha in registros:
        if linha[1] == "EC":
           escritor_csv.writerow(linha)
  print("Arquivo gerado:", arquivo_de_saida_por_mcu)

arquivo_de_saida_registros_sem_data = pasta_origem + "totais/registros_sem_data.csv"
with open(arquivo_de_saida_registros_sem_data, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in registros_sem_data:
        escritor_csv.writerow(linha)
    print("Arquivo gerado:", arquivo_de_saida_registros_sem_data)

arquivo_de_saida_totais_csv = pasta_origem + "totais/totais_por_mcu.csv"
with open(arquivo_de_saida_totais_csv, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    cabecalho = ["mcu","total_registros","entregas","tentativa1","tentativa2","tentativa3","sem_datas","janelas_repetidas"]
    escritor_csv.writerow(cabecalho)
    for linha in totais2:
        escritor_csv.writerow(linha)
    print("Arquivo gerado:", arquivo_de_saida_totais_csv)

qtd_mcus = "Total de MCUs: " + str(qtd_mcus) + "\n"
total_registros = "Total de registros: " + str(total_registros) + "\n"
total_entregas = "Total de Entregas: " + str(total_entregas) + "\n"
total_tentativa1 = "Total de tentativas 1: " + str(total_tentativa1) + "\n"
total_tentativa2 = "Total de tentativas 2: " + str(total_tentativa2) + "\n"
total_tentativa3 = "Total de tentativas 3: " + str(total_tentativa3) + "\n"
total_sem_data = "Total sem datas: " + str(total_sem_data) + "\n"

arquivo_de_saida_totais = pasta_origem + "totais/Totais.txt"
arquivo_csv_saida = open(arquivo_de_saida_totais, mode="w", encoding="utf8")
arquivo_csv_saida.write(qtd_mcus)
arquivo_csv_saida.write(total_registros)
arquivo_csv_saida.write(total_entregas)
arquivo_csv_saida.write(total_tentativa1)
arquivo_csv_saida.write(total_tentativa2)
arquivo_csv_saida.write(total_tentativa3)
arquivo_csv_saida.write(total_sem_data)
arquivo_csv_saida.close()
