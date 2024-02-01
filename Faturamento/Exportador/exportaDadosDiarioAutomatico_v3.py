import dataAccess_v2
import csv
from datetime import datetime
import configparser

cfg = configparser.ConfigParser()
cfg.read('./faturamento/exportador/config.ini')
#cfg.read('./config.ini')
destino = cfg.get('pastas', 'destino')

arquivo_de_log = destino + "logs/log_"+datetime.now().strftime("%Y-%m-%d_%H%M%S")+".log"
log = open(arquivo_de_log, mode="w", encoding="utf8")

print (datetime.now(),"- Início do processamento.")
log.write(str(datetime.now()) + "- Início do processamento." + "\n")

data_ontem = str(datetime.now().strftime("%Y-%m") + '-' + str(int(datetime.now().strftime("%d"))-1))
arquivo_de_saida = destino + data_ontem + "_"+datetime.now().strftime("%Y%m%d%H%M%S")+".csv"
quantidade_linhas_escritas = 0

print (datetime.now(),"- Realizando busca no BD...")
log.write(str(datetime.now()) + "- Realizando busca no BD..." + "\n")
resultado, cabecalho = dataAccess_v2.consulta(data_ontem)

print (datetime.now(),"- Gerando arquivo csv...")
log.write(str(datetime.now()) + "- Gerando arquivo csv..." + "\n")
with open(arquivo_de_saida, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in resultado:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas += 1

print (datetime.now(),"- Arquivo gerado:", arquivo_de_saida)
log.write(str(datetime.now()) + "- Arquivo gerado:" + arquivo_de_saida + "\n")
print (datetime.now(),"- Total de registros gerados:", quantidade_linhas_escritas)
log.write(str(datetime.now()) + "- Total de registros gerados:" + str(quantidade_linhas_escritas) + "\n")
print (datetime.now(),"- Fim do processamento.")
log.write(str(datetime.now()) + "- Fim do processamento." + "\n")
log.close()

#wait = input("Press Enter to continue.")