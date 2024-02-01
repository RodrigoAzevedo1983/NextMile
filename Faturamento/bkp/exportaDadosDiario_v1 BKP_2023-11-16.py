import dataAccess
import csv
from datetime import datetime

print (datetime.now(),"- Início do processamento.")
arquivo_consulta = "D:/dev/NextMile/Faturamento/buscaObjetosDia.sql"
arquivo_de_saida = "D:/Projetos/Next Mile/Faturamento/23-11-06 - 23-11-12/2023-11-15_"+datetime.now().strftime("%Y%m%d%H%M%S")+".csv"
quantidade_linhas_escritas = 0

print (datetime.now(),"- Realizando busca no BD...")
resultado, cabecalho = dataAccess.consulta(arquivo_consulta)

print (datetime.now(),"- Gerando arquivo csv...")
with open(arquivo_de_saida, mode="w", encoding="utf8", newline="") as arquivo_csv_saida:
    escritor_csv = csv.writer(arquivo_csv_saida)
    escritor_csv.writerow(cabecalho)
    for linha in resultado:
        escritor_csv.writerow(linha)
        quantidade_linhas_escritas += 1

print (datetime.now(),"- Arquivo gerado:", arquivo_de_saida)
print (datetime.now(),"- Total de registros gerados:", quantidade_linhas_escritas)
print (datetime.now(),"- Fim do processamento.")
