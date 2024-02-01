import csv
import os
import comparaJanelas
from datetime import datetime




def validaColavorativo(chaves_unicas_mcu, dados_consolidados_final_unico, cabecalho, pasta_saida):
    
    totais_mcu = []
    
    
    
    
    total_registros = 0
    total_entregas = 0
    total_tentativa1 = 0
    total_tentativa2 = 0
    total_tentativa3 = 0
    total_janelas_repetidas = 0
    janela_repetida_linha = 0
    total_sem_data = 0
    qtd_mcus = 0
    mcus_dinamicas = {}
    totais = {}
    totais2 = []
    registros_sem_data = []


    mcus_dinamicas = {}

    for linha in chaves_unicas_mcu:
        mcus_dinamicas[linha] = []
    qtd_mcus = len(chaves_unicas_mcu)
    print("Quantidade MCUs: ", qtd_mcus)
    
    
    for linha in dados_consolidados_final_unico:
        if linha[1] == "EC":
            chave_mcu = (linha[2])
            mcus_dinamicas[chave_mcu].append(linha)
    print("Quantidade linhas em ", chave_mcu ,": ", len(mcus_dinamicas[chave_mcu]))
    
    
    for mcu in chaves_unicas_mcu:
        print("DEBUG - ", str(datetime.now()) ," - MCU:", mcu, " - Registros:", len(mcus_dinamicas[mcu]))
        totais[mcu] = {}    
        registros_mcu = 0
        entregas_mcu = 0
        tentativa1_mcu = 0
        tentativa2_mcu = 0
        tentativa3_mcu = 0
        sem_datas_mcu = 0
        janelas_repetidas_mcu = 0
        linha_totais = ""



'''
        print("DEBUG - ", str(datetime.now()) )


        for linha in mcus_dinamicas[mcu]:
            #print("DEBUG - ", str(datetime.now()) ," - LINHA MCU:", linha)
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
                mcus_dinamicas[mcu].append(linha)
                if entrega != "":
                    total_entregas += 1
                    entregas_mcu += 1
                    data_entrega = comparaJanelas.getData(entrega)
                    hora_entrega = comparaJanelas.getHora(entrega)
                    janela_entrega = comparaJanelas.verificaJanela(entrega)
                    #print("DEBUG -", objeto, "- ENTREGA:   ",entrega, "- DATE:",data_entrega, "- TIME:",hora_entrega, "Janela:",janela_entrega)
                if tentativa1 != "":
                    total_tentativa1 += 1
                    tentativa1_mcu += 1
                    data_tentativa1 = comparaJanelas.getData(tentativa1)
                    hora_tentativa1 = comparaJanelas.getHora(tentativa1)
                    janela_tentativa1 = comparaJanelas.verificaJanela(tentativa1)
                    if data_tentativa1 == data_entrega:
                        if comparaJanelas.comparaJanela(janela_tentativa1,janela_entrega):
                            #print("DEBUG DEBUG DEBUG - JANELA1 = JANELA_ENTREGA")
                            janelas_repetidas_mcu +=1
                            total_janelas_repetidas +=1
                            janela_repetida_linha += 1
                    #print("DEBUG -", objeto, "- TENTATIVA1:",tentativa1, "- DATE:",data_tentativa1, "- TIME:",hora_tentativa1, "JANELAS:", janela_entrega, "+", janela_tentativa1, "JANELAS REPETIDAS:", janela_repetida_linha)
                    if tentativa2 != "":
                        total_tentativa2 += 1
                        tentativa2_mcu += 1
                        data_tentativa2 = comparaJanelas.getData(tentativa2)
                        hora_tentativa2 = comparaJanelas.getHora(tentativa2)
                        janela_tentativa2 = comparaJanelas.verificaJanela(tentativa2)
                        if data_tentativa2 == data_entrega:
                            if comparaJanelas.comparaJanela(janela_tentativa2,janela_entrega):
                                #print("DEBUG DEBUG DEBUG - JANELA2 = JANELA_ENTREGA")
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida_linha += 1
                        if data_tentativa2 == data_tentativa1:
                            if comparaJanelas.comparaJanela(janela_tentativa2,janela_tentativa1):
                                #print("DEBUG DEBUG DEBUG - JANELA2 = JANELA1")
                                janelas_repetidas_mcu +=1
                                total_janelas_repetidas +=1
                                janela_repetida_linha += 1
                        #print("DEBUG -", objeto, "- TENTATIVA2:",tentativa2, "- DATE:",data_tentativa2, "- TIME:",hora_tentativa2, "JANELAS:", janela_entrega, "+", janela_tentativa1, "+", janela_tentativa2, "JANELAS REPETIDAS:", janela_repetida_linha)
                        if tentativa3 != "":
                            total_tentativa3 += 1
                            tentativa3_mcu += 1
                            data_tentativa3 = comparaJanelas.getData(tentativa3)
                            hora_tentativa3 = comparaJanelas.getHora(tentativa3)
                            janela_tentativa3 = comparaJanelas.verificaJanela(tentativa3)
                            if data_tentativa3 == data_entrega:
                                if comparaJanelas.comparaJanela(janela_tentativa3,janela_entrega):
                                    #print("DEBUG DEBUG DEBUG - JANELA3 = JANELA_ENTREGA")
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    janela_repetida_linha += 1
                            if data_tentativa3 == data_tentativa1:
                                if comparaJanelas.comparaJanela(janela_tentativa3,janela_tentativa1):
                                    #print("DEBUG DEBUG DEBUG - JANELA3 = JANELA1")
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    janela_repetida_linha += 1
                            if data_tentativa3 == data_tentativa2:
                                if comparaJanelas.comparaJanela(janela_tentativa3,janela_tentativa2):
                                    #print("DEBUG DEBUG DEBUG - JANELA3 = JANELA2")
                                    janelas_repetidas_mcu +=1
                                    total_janelas_repetidas +=1
                                    janela_repetida_linha += 1
                        #print("DEBUG -", objeto, "- TENTATIVA3:",tentativa3, "- DATE:",data_tentativa3, "- TIME:",hora_tentativa3, "JANELAS:", janela_entrega, "+", janela_tentativa3, "JANELAS REPETIDAS:", janela_repetida_linha)
            



                

        linha_totais = mcu, registros_mcu, entregas_mcu, tentativa1_mcu, tentativa2_mcu, tentativa3_mcu, sem_datas_mcu, janelas_repetidas_mcu
        totais2.append(linha_totais)
        print("TOTAIS:",linha_totais)
        totais[mcu] = {"mcu":mcu ,"total_registros":registros_mcu, "entregas":entregas_mcu, "tentativa1":tentativa1_mcu, "tentativa2":tentativa2_mcu, "tentativa3":tentativa3_mcu, "sem_datas":sem_datas_mcu, "janelas_repetidas": janelas_repetidas_mcu}

        print("MCU ", mcu, "\nRegistros no arquivo: ", registros_mcu, "\nEntregas no MCU", entregas_mcu,"\nTentativa1 no MCU:", tentativa1_mcu,"\nTentativa2 no MCU:", tentativa2_mcu,"\nTentativa3 no MCU:", tentativa3_mcu,"\nJanelas repetidas no MCU:", janelas_repetidas_mcu, "\nRegistros sem data:",sem_datas_mcu)
        print("\n")
    print("Total de registros:", total_registros, "\nTotal de Entregas:", total_entregas, "\ntotal de tentativas1:", total_tentativa1, "\ntotal de tentativas2:", total_tentativa2, "\ntotal de tentativas3:", total_tentativa3, "\ntotal de janelas repetidas: ", total_janelas_repetidas, "\nTotal sem data:", total_sem_data, "\nTotal de MCUs:", qtd_mcus, "\n")

    for chave, registros in mcus_dinamicas.items():
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

    arquivo_de_saida_totais = pasta_saida + "por mcu/Totais.txt"
    arquivo_csv_saida = open(arquivo_de_saida_totais, mode="w", encoding="utf8")
    arquivo_csv_saida.write(qtd_mcus)
    arquivo_csv_saida.write(str_total_registros)
    arquivo_csv_saida.write(str_total_entregas)
    arquivo_csv_saida.write(str_total_tentativa1)
    arquivo_csv_saida.write(str_total_tentativa2)
    arquivo_csv_saida.write(str_total_tentativa3)
    arquivo_csv_saida.write(str_total_sem_data)
    arquivo_csv_saida.close()
'''