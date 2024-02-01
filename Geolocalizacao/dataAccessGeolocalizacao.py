import psycopg2

def conecta_db():
  con = psycopg2.connect(host='ec2-3-228-213-219.compute-1.amazonaws.com', 
                         database='umovme_dbview_db',
                         user='rodrigoazevedo', 
                         password='naprLPh4xetrofiThujI')
  return con

def consultar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  cabecalho = [desc[0] for desc in cur.description]
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros, cabecalho

def consulta(data):
    consulta = montaQueryConsultaHistoricoGeolocalizacao(data)
    resultado, cabecalho = consultar_db(consulta)
    return resultado, cabecalho

def montaQueryConsultaHistoricoGeolocalizacao(data):
   consulta = (f"""
                SELECT 
                mcu.superintendencia SE,
                mcu.mcu,
                mcu.unidade,
                obj.distrito,
                obj.matricula_tecnico Matricula,
                --his.data_inicio,
                --his.data_fim Data,
                to_char(his.data_fim, 'YYYY-MM-DD') Dia, 
                to_char(his.data_fim, 'HH24:MI:SS') Hora,
                obj.cep,
                obj.numero,
                cor.latitude Latitude_Baixa,
                cor.longitude Longitude_Baixa,
                cor.local_altitude Latitude_Objeto,
                cor.local_longitude Longitude_Objeto,
                --cor.distancia,
                ent.nro_objeto Objeto,
                his.codigo Cod_Baixa,
                his.atividade Descricao_Baixa
                --his.codigo_atividade,
                --cor.observacao
                from dw_mae.historico his
                inner join dw_mae.entrega ent on ent.codigo = his.codigo_entrega
                inner join dw_mae.objeto obj on obj.codigo = ent.codigo_objeto
                inner join dw_mae.mcu mcu on mcu.codigo = ent.codigo_mcu
                left join dw_mae.coordenadas cor on cor.codigo_historico = his.codigo
                where his.data_inicio between '{data} 00:00:00.000' and '{data} 12:00:00.000'
                """
              )
   return consulta