import csv
import os
from datetime import datetime

total_registros = 0
total_entregas = 0
total_tentativa1 = 0
total_tentativa2 = 0
total_tentativa3 = 0
total_janelas_repetidas = 0
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

hora_inicio_janela1 = datetime.time(datetime.strptime("06:00:00", "%H:%M:%S"))
hora_fim_janela1 =  datetime.time(datetime.strptime("11:59:59", "%H:%M:%S"))
hora_inicio_janela2 =  datetime.time(datetime.strptime("12:00:00", "%H:%M:%S"))
hora_fim_janela2 =  datetime.time(datetime.strptime("17:59:59", "%H:%M:%S"))
hora_inicio_janela3 =  datetime.time(datetime.strptime("18:00:00", "%H:%M:%S"))
hora_fim_janela3 =  datetime.time(datetime.strptime("23:59:59", "%H:%M:%S"))


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
    janelas_repetidas_mcu = 0
    janela_repetida = 0
    data_tentativa1 = ""
    hora_tentativa1 = ""
    data_tentativa2 = ""
    hora_tentativa2 = ""
    data_tentativa3 = ""
    hora_tentativa3 = ""




    with open(caminho_arquivo, mode='r', encoding="utf8") as arquivo_csv:
        dados_csv = csv.reader(arquivo_csv)
        cabecalho = next(dados_csv)
        linha_totais = ""
        for linha in dados_csv:
            total_registros += 1
            registros_mcu += 1
            janela_repetida = 0
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
                mcus_dinamicas[nome_mcu].append(linha)
                data_entrega = entrega.split(" ")[0]
                hora_entrega = entrega.split(" ")[-1]
                if entrega != "":
                    total_entregas += 1
                    entregas_mcu += 1
                    data_hora_entrega = datetime.strptime(entrega, "%Y-%m-%d %H:%M:%S")
                    data_entrega = datetime.date(data_hora_entrega)
                    hora_entrega = datetime.time(data_hora_entrega)
                    if hora_inicio_janela1 <= hora_entrega <= hora_fim_janela1:
                        janela_entrega = "Manha"
                    elif hora_inicio_janela2 <= hora_entrega <= hora_fim_janela2:
                        janela_entrega = "Tarde"
                    elif hora_inicio_janela3 <= hora_entrega <= hora_fim_janela3:
                        janela_entrega = "Noite"
                    if hora_tentativa1 == hora_entrega:
                        janelas_repetidas_mcu +=1
                        total_janelas_repetidas +=1
                        
                    print("DEBUG -", objeto, "- ENTREGA:   ",entrega, "- DATE_TIME:",data_hora_entrega, "- DATE:",data_entrega, "- TIME:",hora_entrega, "Janela:",janela_entrega)

                if tentativa1 != "":
                    total_tentativa1 += 1
                    tentativa1_mcu += 1
                    data_hora_tentativa1 = datetime.strptime(tentativa1, "%Y-%m-%d %H:%M:%S")
                    data_tentativa1 = datetime.date(data_hora_tentativa1)
                    hora_tentativa1 = datetime.time(data_hora_tentativa1)
                    data_repete = "N"
                    if data_tentativa1 == data_entrega:
                        #print("DEBUG - ENTROU:", data_tentativa1, "=", data_entrega)
                        data_repete = "S"
                        if hora_inicio_janela1 <= hora_tentativa1 <= hora_fim_janela1:
                            janela_tentativa1 = "Manha"
                            #print("DEBUG - ENTROU MUITO!!!:", hora_tentativa1, ">", hora_inicio_janela1)
                        elif hora_inicio_janela2 <= hora_tentativa1 <= hora_fim_janela2:
                            janela_tentativa1 = "Tarde"
                            #print("DEBUG - ENTROU MUITO MAIS!!!:", hora_tentativa1, "<", hora_inicio_janela1)
                        elif hora_inicio_janela3 <= hora_tentativa1 <= hora_fim_janela3:
                            janela_tentativa1 = "Noite"
                        if janela_tentativa1 == janela_entrega:
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida += 1
                        print("DEBUG -", objeto, "- TENTATIVA1:",tentativa1, "- DATE_TIME:",data_hora_tentativa1, "- DATE:",data_tentativa1, "- TIME:",hora_tentativa1, "JANELAS:", janela_entrega, "+", janela_tentativa1, "JANELA REPETIDA:", janela_repetida)
                    if tentativa2 != "":
                        total_tentativa2 += 1
                        tentativa2_mcu += 1
                        data_hora_tentativa2 = datetime.strptime(tentativa2, "%Y-%m-%d %H:%M:%S")
                        data_tentativa2 = datetime.date(data_hora_tentativa2)
                        hora_tentativa2 = datetime.time(data_hora_tentativa2)
                        data_repete = "N"
                        janela_tentativa2 = ""
                        if data_tentativa2 == data_entrega:
                            data_repete = "S"
                            if hora_inicio_janela1 <= hora_tentativa2 <= hora_fim_janela1:
                                janela_tentativa2 = "Manha"
                                #print("DEBUG - ENTROU MUITO!!!:", hora_tentativa1, ">", hora_inicio_janela1)
                            elif hora_inicio_janela2 <= hora_tentativa2 <= hora_fim_janela2:
                                janela_tentativa2 = "Tarde"
                                #print("DEBUG - ENTROU MUITO MAIS!!!:", hora_tentativa1, "<", hora_inicio_janela1)
                            elif hora_inicio_janela3 <= hora_tentativa2 <= hora_fim_janela3:
                                janela_tentativa2 = "Noite"
                            if janela_tentativa2 == janela_entrega:
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    janela_repetida += 1
                            if hora_tentativa2 == hora_entrega:
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1          
                        if data_tentativa2 == data_tentativa1:
                            data_repete = "S"
                            if hora_tentativa2 == hora_tentativa1:
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                        print("DEBUG -", objeto, "- TENTATIVA2:",tentativa2, "- DATE_TIME:",data_hora_tentativa2, "- DATE:",data_tentativa2, "- TIME:",hora_tentativa2, "JANELAS:", janela_entrega, "+", janela_tentativa2, "JANELA REPETIDA:", janela_repetida)
                        if tentativa3 != "":
                            total_tentativa3 += 1
                            tentativa3_mcu += 1
                            data_hora_tentativa3 = datetime.strptime(tentativa3, "%Y-%m-%d %H:%M:%S")
                            data_tentativa3 = datetime.date(data_hora_tentativa3)
                            hora_tentativa3 = datetime.time(data_hora_tentativa3)
                            janela_tentativa3 = ""
                            if data_tentativa3 == data_entrega:
                                data_repete = "S"
                            if hora_inicio_janela1 <= hora_tentativa3 <= hora_fim_janela1:
                                janela_tentativa3 = "Manha"
                                #print("DEBUG - ENTROU MUITO!!!:", hora_tentativa1, ">", hora_inicio_janela1)
                            elif hora_inicio_janela2 <= hora_tentativa3 <= hora_fim_janela2:
                                janela_tentativa3 = "Tarde"
                                #print("DEBUG - ENTROU MUITO MAIS!!!:", hora_tentativa1, "<", hora_inicio_janela1)
                            elif hora_inicio_janela3 <= hora_tentativa3 <= hora_fim_janela3:
                                janela_tentativa3 = "Noite"
                            if janela_tentativa3 == janela_entrega:
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    janela_repetida += 1
                            if hora_tentativa2 == hora_entrega:
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                
                                if hora_tentativa3 == hora_entrega:
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    
                            if data_tentativa3 == data_tentativa1:
                                data_repete = "S"
                                if hora_tentativa3 == hora_tentativa1:
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    
                            if data_tentativa3 == data_tentativa2:
                                data_repete = "S"
                                if hora_tentativa3 == hora_tentativa2:
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    
                            print("DEBUG -", objeto, "- TENTATIVA3:",tentativa3, "- DATE_TIME:",data_hora_tentativa3, "- DATE:",data_tentativa3, "- TIME:",hora_tentativa3, "JANELAS:", janela_entrega, "+", janela_tentativa3, "JANELA REPETIDA:", janela_repetida)

            



            

        linha_totais = nome_mcu, registros_mcu, entregas_mcu, tentativa1_mcu, tentativa2_mcu, tentativa3_mcu, sem_datas_mcu, janelas_repetidas_mcu
        totais2.append(linha_totais)
        print("TOTAIS:",linha_totais)
        totais[nome_mcu] = {"mcu":nome_mcu ,"total_registros":registros_mcu, "entregas":entregas_mcu, "tentativa1":tentativa1_mcu, "tentativa2":tentativa2_mcu, "tentativa3":tentativa3_mcu, "sem_datas":sem_datas_mcu, "janelas_repetidas": janelas_repetidas_mcu}

    print("Arquivo ", arquivo, "\nRegistros no arquivo: ", registros_mcu, "\nEntregas no MCU", entregas_mcu,"\nTentativa1 no MCU:", tentativa1_mcu,"\nTentativa2 no MCU:", tentativa2_mcu,"\nTentativa3 no MCU:", tentativa3_mcu,"\nJanelas repetidas no MCU:", janelas_repetidas_mcu, "\nRegistros sem data:",sem_datas_mcu)
    print("\n")
print("Total de registros:", total_registros, "\nTotal de Entregas:", total_entregas, "\ntotal de tentativas1:", total_tentativa1, "\ntotal de tentativas2:", total_tentativa2, "\ntotal de tentativas3:", total_tentativa3, "\ntotal de janelas repetidas: ", total_janelas_repetidas, "\nTotal sem data:", total_sem_data, "\nTotal de MCUs:", qtd_mcus, "\n")

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
str_total_registros = "Total de registros:" + str(total_registros) + "\n"
str_total_entregas = "Total de Entregas:" + str(total_entregas) + "\n"
str_total_tentativa1 = "Total de tentativas 1:" + str(total_tentativa1) + "\n"
str_total_tentativa2 = "Total de tentativas 2:" + str(total_tentativa2) + "\n"
str_total_tentativa3 = "Total de tentativas 3:" + str(total_tentativa3) + "\n"
str_total_sem_data = "Total sem datas:" + str(total_sem_data) + "\n"

arquivo_de_saida_totais = pasta_origem + "totais/Totais.txt"
arquivo_csv_saida = open(arquivo_de_saida_totais, mode="w", encoding="utf8")
arquivo_csv_saida.write(qtd_mcus)
arquivo_csv_saida.write(str_total_registros)
arquivo_csv_saida.write(str_total_entregas)
arquivo_csv_saida.write(str_total_tentativa1)
arquivo_csv_saida.write(str_total_tentativa2)
arquivo_csv_saida.write(str_total_tentativa3)
arquivo_csv_saida.write(str_total_sem_data)
arquivo_csv_saida.close()
