#!/usr/bin/env python3
"""Gera gráficos a partir das tabelas reproduzidas (requer matplotlib)."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'resultados/tabelas/indicadores_municipais_reproduzidos.csv').open(encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
series={'Dependencia_reproduzida':'dependencia_transferencias','Participacao_tributos_reproduzida':'participacao_tributos'}
for filename,field in series.items():
 fig,ax=plt.subplots(figsize=(9,5))
 for city in ['Canindé','Quixadá']:
  data=sorted([r for r in rows if r['municipio']==city],key=lambda r:int(r['ano']))
  ax.plot([int(r['ano']) for r in data],[float(r[field])*100 for r in data],marker='o',label=city)
 ax.set(xlabel='Ano',ylabel='Participação (%)',title=field.replace('_',' ').capitalize())
 ax.legend();ax.grid(alpha=.25);fig.tight_layout()
 fig.savefig(ROOT/'resultados/graficos'/f'{filename}.png',dpi=160);plt.close(fig)
print('Gráficos regenerados em resultados/graficos/')
