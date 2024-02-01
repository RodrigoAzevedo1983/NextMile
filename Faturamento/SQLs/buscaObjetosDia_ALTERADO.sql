select 
	max(DataUltimaExecucao::Date) DataUltimaExecucaoD,
	max(TIPO_ENTREGA) TIPO_ENTREGA,
	max(mcu) mcuNome,
	numeroObjeto numeroObjeto,
	max(categoriaNome) categoriaNome,
	max(nomeAgente) nomeAgente,
	max(DataEntradaPlataforma) DataEntradaPlataforma,
	max(case when row_number = 2 then datatentativa else null end ) dataTentativa1,
	max(case when row_number = 3 then datatentativa else null end ) dataTentativa2,
	max(case when row_number = 4 then datatentativa else null end ) dataTentativa3,
	max(entregarealizada) entregarealizada,
	max(dataDevolucao) dataDevolucaoCD,
	max(nomeRecebedor) nomeRecebedor
	
	
from (

select 
	*,
	row_number () over (
	partition by tskId
order by
	idEventoCorreios desc nulls last,
	htyId asc 
) row_number
from
	(
	select
		case when strpos(t.tsk_integrationid, '-') = 0 then 'EC' else 'EP' end TIPO_ENTREGA,
		t.tsk_id as tskId,
		t.tsk_realinitialdatehour as tskDate ,
		h.hty_id as htyId,
		max(case when acf_id in (6855481, 6855889, 8194026) then a.act_description else null end) activityDescription ,
		max(case when acf_id in (6855481, 6855889, 8194026) then htv_externalvalue else null end) idEventoCorreios,
		max(case when acf_id in (6855481) then TO_CHAR(h.hty_finaldatehour , 'YYYY-MM-DD HH24:MI:SS') else null end) entregaRealizada,
		max(case when acf_id in (6855889, 8194026) then TO_CHAR(h.hty_finaldatehour , 'YYYY-MM-DD HH24:MI:SS') else (case when acf_id = 6342614 then hv.htv_internalvalue else null end) end) dataTentativa,
		max(case when acf_id in (6342622) then (select MAX(ta.tsk_realfinaldatehour) from u28966.task ta where ta.tsk_integrationid = hv.htv_internalvalue) else null end) dataDevolucao,
		max(case when acf_id in (6342622) then (select max(hva.htv_internalvalue) from u28966.task ta join u28966.history ha on ha.tsk_id = ta.tsk_id join u28966.historyvalue hva on hva.hty_id = ha.hty_id where ta.tsk_integrationid = hv.htv_internalvalue and hva.acf_id = 6343590) else null end) nomeRecebedor,
		t.tsk_integrationid numeroObjeto,
		null nomeAgente,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '961688'
			and cfv_registerid = t.tsk_id ) mcu,
		t.tsk_scheduleinitialdatehour DataEntradaPlataforma,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '961690'
			and cfv_registerid = t.tsk_id ) categoriaNome,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '803743'
			and cfv_registerid = t.tsk_id ) nome,
		t.tsk_lastexecutiondatehour DataUltimaExecucao
	from
		u28966.task t
	join u28966.history h on
		h.tsk_id = t.tsk_id
	join u28966.activity a on
		a.act_id = h.act_id
	join u28966.historyvalue hv on
		hv.hty_id = h.hty_id
	where
		t.tsk_id in (
		select
			tsk.tsk_id
		from
			u28966.task tsk
		-------------------------> ################## DATAS PARA SELEÇÃO ##########################################################
		WHERE
			tsk.tsk_lastexecutiondatehour between  '2023-11-03 00:00:00.000' and '2023-11-04 00:00:00.000' and
			tsk.tsk_situation = 'Retornada de Campo'
				)
		and hv.acf_id in (6855481, 6855889, 8194026, 6342622)
	group by
		h.hty_id,
		t.tsk_id,
		a.act_description,
		t.tsk_realinitialdatehour  
union
	select
		case when strpos(t.tsk_integrationid, '-') = 0 then 'EC' else 'EP' end TIPO_ENTREGA,
		t.tsk_id,
		t.tsk_realinitialdatehour as tskDate ,
		null htyid,
		'1. Encaminhamento objeto' activitydescription,
		'UP' ideventocorreios,
		null entregaRealizada,
		null dataTentativa,
		null dataDevolucao,
		null nomeRecebedor, 
		case when strpos(t.tsk_integrationid, '-') = 0 then t.tsk_integrationid else left(t.tsk_integrationid, strpos(t.tsk_integrationid, '-') - 1) end numeroObjeto,
		(select age_name from u28966.agent a2 where a2.age_id = t.age_id) nomeAgente,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '961688'
			and cfv_registerid = t.tsk_id ) mcu,
		t.tsk_scheduleinitialdatehour DataEntradaPlataforma,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '961690'
			and cfv_registerid = t.tsk_id ) categoriaNome,
		(
		select
			max(cfv_internalvalue)
		from
			u28966.customfieldvalue c
		where
			c.cfd_id = '803743'
			and cfv_registerid = t.tsk_id ) nome,
		t.tsk_lastexecutiondatehour DataUltimaExecucao
	from
		u28966.task t
	join u28966.customfieldvalue v on
		v.cfv_registerid = t.tsk_id
	join u28966.customfield c on
		c.cfd_id = v.cfd_id
	where
		t.tsk_id in (
		select
			tsk.tsk_id
		from
			u28966.task tsk
		-------------------------> ################## DATAS PARA SELEÇÃO ##########################################################
		where
			tsk.tsk_lastexecutiondatehour between  '2023-11-03 00:00:00.000' and '2023-11-04 00:00:00.000' and
			tsk.tsk_situation = 'Retornada de Campo'				)
		and (c.cfd_id = '968803'
			or c.cfd_id = '8cb1f68ffd5bfcf7c7d3618892b1b332')
) tab where tab.ideventocorreios is not null
order by
	tskId asc ,
	htyId nulls first ) tab2 group by numeroObjeto;