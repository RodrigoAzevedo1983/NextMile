from datetime import datetime

hora_inicio_janela1 = datetime.time(datetime.strptime("06:00:00", "%H:%M:%S"))
hora_fim_janela1 =  datetime.time(datetime.strptime("12:00:00", "%H:%M:%S"))
hora_inicio_janela2 =  datetime.time(datetime.strptime("12:00:01", "%H:%M:%S"))
hora_fim_janela2 =  datetime.time(datetime.strptime("18:00:00", "%H:%M:%S"))
hora_inicio_janela3 =  datetime.time(datetime.strptime("18:00:01", "%H:%M:%S"))
hora_fim_janela3 =  datetime.time(datetime.strptime("23:00:00", "%H:%M:%S"))

def getData(data_hora):
    data_hora_entrega = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
    data_entrega = datetime.date(data_hora_entrega)
    return data_entrega

def getHora(data_hora):
    data_hora_entrega = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
    hora_entrega = datetime.time(data_hora_entrega)
    return hora_entrega

def verificaJanela(data_hora):
    data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
    hora = datetime.time(data_hora)
    janela = ""
    if hora_inicio_janela1 <= hora <= hora_fim_janela1:
        janela = "Manha"
    elif hora_inicio_janela2 <= hora <= hora_fim_janela2:
        janela = "Tarde"
    elif hora_inicio_janela3 <= hora <= hora_fim_janela3:
        janela = "Noite"
    return janela

def verificaJanela2(horario):
    if hora_inicio_janela1 <= horario <= hora_fim_janela1:
        janela = "Manha"
    elif hora_inicio_janela2 <= horario <= hora_fim_janela2:
        janela = "Tarde"
    elif hora_inicio_janela3 <= horario <= hora_fim_janela3:
        janela = "Noite"
    return janela

def comparaJanela(janela1, janela2):
    if janela1 == janela2:
        return True
    else:
        return False
