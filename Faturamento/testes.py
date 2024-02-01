import math
from datetime import datetime
#import comparaJanelas
#import dataAccess
import configparser

cfg = configparser.ConfigParser()
cfg.read('./Faturamento/exportador/config.ini')


destino = cfg.get('pastas', 'destino')
data = cfg.get('data', 'exportaDiaEspecifico')
print(destino)
print(data)


arquivo_de_log = destino + "logs/log.txt"
log = open(arquivo_de_log, mode="w", encoding="utf8")



log.write(str(datetime.now()) + " - Pasta Destino: " + destino + "\n")
log.write(str(datetime.now()) + " - Data do log: " + data + "\n")


log.close()






'''
def teste(variavel_teste):
   return variavel_teste + 2


dados_consolidados_final = {}

nomes_var = ['var1', 'var2', 'var3']

dic_variaveis = {}

conta = 0

for nome in nomes_var:
    dic_variaveis[nome] = nome


dic_variaveis[conta,'var1'] = 10
dic_variaveis['var2'] = 20
dic_variaveis['var3'] = 30

print(dic_variaveis[conta,'var1'])
print(dic_variaveis['var2'])
print(dic_variaveis['var3'])



print("\n\n\n")

total = math.trunc(3567849/1000000)+1
contador = 0
print("valor inicial:", contador)

while contador != total:
    contador += 1
    arquivo_de_saida = "registros_unicos_0" + str(contador) + ".csv"
    print("Arquivo", contador, ":", arquivo_de_saida)

id_arquivo = math.ceil(1000001/1000000)
print("Arredondado", id_arquivo)
print("\n\n\n")


qtd_arquivos_saida = math.trunc(3567849/1000000)+1
i = 1
while i <= qtd_arquivos_saida:
  print(i)
  dados_consolidados_final[i] = []
  i += 1


aaa = teste(1)

print("\nRESULTADO", aaa)

bbb = comparaJanelas.teste(1)
print("\nRESULTADO", bbb)


data_hora_entrega = datetime.strptime("2023-10-10 10:17:53", "%Y-%m-%d %H:%M:%S")
data_entrega = datetime.date(data_hora_entrega)
hora_entrega = datetime.time(data_hora_entrega)

print(comparaJanelas.verificaJanela(hora_entrega))


print("\n\n\n", datetime.now())

print("\n\n\n", datetime.now().strftime("%Y%m%d%H%M%S%f"))


print("\n\n\nData correta: 2023-11-15 00:00:00.000")

data = datetime.now().strftime("%Y-%m-%d 00:00:00.000")
print(data)

data_ano_mes = datetime.now().strftime("%Y-%m")
data_dia = datetime.now().strftime("%d")
data_dia_1 = int(data_dia) - 1
hora = ('00:00:00.000')
data = str(datetime.now().strftime("%Y-%m") + '-' + str(int(datetime.now().strftime("%d"))-1) + ' 00:00:00.000')
print(data_ano_mes)
print(data_dia)
print(data_dia_1)
print(hora)
print(data)

data_ontem = str(datetime.now().strftime("%Y-%m") + '-' + str(int(datetime.now().strftime("%d"))-1))
data_hoje = str(datetime.now().strftime("%Y-%m-%d") + ' 00:00:00.000')
print("Ontem:" + data_ontem)
print("Hoje:" + data_hoje)

consulta = dataAccess.monta_query_consulta_movimentos_dia_teste(data_ontem)
print("Consulta:" + consulta)

consulta = dataAccess.montaQueryConsultaMovimentosDia(data_ontem)
print("Consulta:\n" + consulta)
'''