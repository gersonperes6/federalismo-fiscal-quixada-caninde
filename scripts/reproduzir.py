#!/usr/bin/env python3
"""Reproduz indicadores municipais e suíços a partir dos CSVs consolidados.
Uso: python scripts/reproduzir.py (a partir da raiz do repositório).
Dependências: somente biblioteca padrão do Python 3.9+.
Não refaz a extração FINBRA/IBGE/FFA: parte das séries consolidadas preservadas.
"""
from pathlib import Path
import csv, math
ROOT=Path(__file__).resolve().parents[1]
DADOS=ROOT/'dados'/'tratados'
OUT=ROOT/'resultados'/'tabelas'; OUT.mkdir(parents=True,exist_ok=True)

def ler(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def n(row,key):
 v=row.get(key,'')
 if v is None or str(v).strip()=='':return None
 return float(v)
def razao(a,b):return a/b if a is not None and b is not None and b!=0 else None
def mult(a,b):return a*b if a is not None and b is not None else None
def fmt(v):return '' if v is None else f'{v:.12g}'
def confere(calc,reported,tag,relative=1e-8):
 if calc is None and reported is None:return
 if calc is None or reported is None or not math.isclose(calc,reported,rel_tol=relative,abs_tol=1e-6):raise ValueError(f'Divergência {tag}: calculado={calc} planilha={reported}')

def municipio():
 inp=ler(DADOS/'municipios_final.csv');out=[]
 for r in inp:
  y=int(r['Ano']);city=r['Município'];tag=f'{city}/{y}'
  rev=n(r,'Receita exc. intra R$');gross=n(r,'Receita bruta R$');tax=n(r,'Tributos R$');trans=n(r,'Transferências correntes R$');spent=n(r,'Empenhada R$');ed=n(r,'Educação empenhada R$');health=n(r,'Saúde empenhada R$');factor=n(r,'Fator IPCA 2025');pop=n(r,'População');gdp=n(r,'PIB mil R$')
  d={'dependencia_transferencias':razao(trans,rev),'participacao_tributos':razao(tax,rev),'participacao_educacao':razao(ed,spent),'participacao_saude':razao(health,spent),'despesa_empenhada_sobre_pib':razao(spent,mult(gdp,1000)),'receita_real_2025':mult(gross,factor),'despesa_real_2025':mult(spent,factor),'receita_real_per_capita':razao(mult(gross,factor),pop),'despesa_real_per_capita':razao(mult(spent,factor),pop)}
  mapping={'dependencia_transferencias':'Dependência transferências','participacao_tributos':'Esforço tributário','participacao_educacao':'Educação / empenhada','participacao_saude':'Saúde / empenhada','despesa_empenhada_sobre_pib':'Empenhada / PIB','receita_real_2025':'Receita real R$ 2025','despesa_real_2025':'Empenhada real R$ 2025','receita_real_per_capita':'Receita real per capita R$','despesa_real_per_capita':'Empenhada real per capita R$'}
  for key,ref in mapping.items():confere(d[key],n(r,ref),f'{tag}/{key}')
  out.append({'ano':y,'municipio':city,**{k:fmt(v) for k,v in d.items()}})
  
 with (OUT/'indicadores_municipais_reproduzidos.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
 return out

def suica():
 rows=ler(DADOS/'suica_final.csv');out=[]
 for r in rows:
  y=int(r['Ano']);gdp=n(r,'PIB CHF');receipts=n(r,'Receitas governo geral CHF');expenses=n(r,'Despesas governo geral CHF');debt=n(r,'Dívida FMI CHF');avg=n(r,'PTAX média BRL/CHF');end=n(r,'PTAX encerramento BRL/CHF');factor=n(r,'Fator IPC 2025')
  d={'receitas_sobre_pib':razao(receipts,gdp),'despesas_sobre_pib':razao(expenses,gdp),'divida_sobre_pib':razao(debt,gdp),'receitas_brl_nominais':mult(receipts,avg),'despesas_brl_nominais':mult(expenses,avg),'divida_brl_estoque':mult(debt,end),'receitas_chf_reais_2025':mult(receipts,factor),'despesas_chf_reais_2025':mult(expenses,factor)}
  mapping={'receitas_sobre_pib':'Receitas / PIB','despesas_sobre_pib':'Despesas / PIB','divida_sobre_pib':'Dívida / PIB','receitas_brl_nominais':'Receitas BRL nominal','despesas_brl_nominais':'Despesas BRL nominal','divida_brl_estoque':'Dívida BRL nominal fim do ano','receitas_chf_reais_2025':'Receitas CHF reais 2025','despesas_chf_reais_2025':'Despesas CHF reais 2025'}
  for k,ref in mapping.items():confere(d[k],n(r,ref),f'Suíça/{y}/{k}')
  out.append({'ano':y,**{k:fmt(v) for k,v in d.items()}})
 with (OUT/'indicadores_suica_reproduzidos.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
 return out

def resumo(rows):
 by={}
 for r in rows:by.setdefault(r['municipio'],[]).append(r)
 output=[]
 for city,rr in sorted(by.items()):
  rr.sort(key=lambda r:r['ano'])
  for field in ['dependencia_transferencias','participacao_tributos','participacao_educacao','participacao_saude']:
   vals=[float(r[field]) for r in rr if r[field]!='']
   output.append({'municipio':city,'indicador':field,'2016':rr[0][field],'2025':rr[-1][field],'media_periodo':fmt(sum(vals)/len(vals)) if vals else '', 'n_observacoes':len(vals)})
 with (OUT/'resumo_municipios.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(output[0]));w.writeheader();w.writerows(output)

if __name__=='__main__':
 m=municipio();s=suica();resumo(m)
 print(f'OK: {len(m)} registros municipais, {len(s)} registros suíços; cálculos conferidos contra os CSVs de origem.')
 print('Tabelas em resultados/tabelas/')
