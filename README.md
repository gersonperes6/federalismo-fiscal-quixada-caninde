# Federalismo fiscal, transferências e autonomia municipal: Quixadá e Canindé (2016–2025)

Repositório de materiais complementares ao artigo acadêmico sobre finanças públicas municipais, transferências intergovernamentais e autonomia fiscal em Quixadá e Canindé (CE), com comparação institucional contextual com a Suíça. A pesquisa integra o projeto de Finanças do Setor Público (UnB).

## O que há neste repositório

| Caminho | Conteúdo |
|---|---|
| `artigo/` | Artigo em Word e PDF, com formatação acadêmica. |
| `dados/originais/` | Cópia preservada dos arquivos originais e do trabalho anterior (Prova 1). |
| `dados/tratados/base_integrada_2016_2025.xlsx` | Planilha-mestre com 35 abas, dados, dicionários, cálculos, auditorias, histórico e ressalvas. |
| `dados/tratados/municipios_final.csv` | Extração de `FINAL_Municipios` (20 observações: dois municípios × dez anos). |
| `dados/tratados/suica_final.csv` | Extração de `FINAL_Suica` (dez anos; 2025 sujeito a ressalva). |
| `dados/tratados/ipca_fatores.csv`, `ptax_auditada.csv` | Insumos documentados de inflação e câmbio. |
| `documentacao/dicionario_variaveis.csv` | Definições, fontes, unidades, períodos e fórmulas, extraídas de `ENTREGA_dicionario`. |
| `documentacao/REGISTRO_ATUALIZACOES.md` | Comparação entre trabalho anterior e versão atual e correções. |
| `documentacao/registro_correcoes_original.csv` | Histórico registrado na aba `FINAL_Alteracoes`. |
| `documentacao/` (demais CSVs) | Fórmulas, metodologia, lacunas e protocolo de validação. |
| `scripts/reproduzir.py` | Recalcula e verifica os indicadores a partir dos CSVs consolidados. |
| `scripts/gerar_graficos.py` | Recria dois gráficos principais a partir das tabelas reproduzidas. |
| `resultados/tabelas/` | Resultados reproduzidos, inclusive resumo por município. |
| `resultados/graficos/` | Gráficos do estudo e versões regeneradas. |
| `bibliometria/` | Lista de 80 artigos priorizados e matriz de leitura/triagem. |

## Como reproduzir os resultados

1. Baixe o ZIP, extraia e abra um terminal na pasta `repositorio_federalismo_fiscal_quixada_caninde`.
2. Instale **Python 3.9 ou superior**. O script principal não requer pacotes adicionais.
3. Execute `python scripts/reproduzir.py` (ou `python3 scripts/reproduzir.py`).
4. Consulte os três CSVs em `resultados/tabelas/`: `indicadores_municipais_reproduzidos.csv`, `indicadores_suica_reproduzidos.csv` e `resumo_municipios.csv`.
5. Para recriar os gráficos, instale `matplotlib` (`python -m pip install matplotlib`) e execute `python scripts/gerar_graficos.py`.
6. Abra `dados/tratados/base_integrada_2016_2025.xlsx` para examinar os insumos, a rastreabilidade e as abas de auditoria.

O script confere as fórmulas derivadas contra os valores já registrados nas planilhas; caso haja divergência, encerra com erro e identifica município/ano/indicador. A reprodução **começa na base consolidada**: não automatiza o download ou a reconciliação de todas as fontes primárias FINBRA, IBGE e FFA.

## Conceitos essenciais

- **Dependência de transferências** = transferências **correntes** / receita orçamentária total **excluídas as intraorçamentárias**. Não inclui necessariamente todas as transferências de capital.
- **Participação tributária** (rotulada “esforço tributário” na base) = impostos, taxas e contribuições de melhoria / receita total excluídas intraorçamentárias. É uma *proxy descritiva*, não uma medida econométrica de esforço ou de toda receita própria.
- **Receita real** na planilha = **receita bruta** × fator IPCA para dezembro/2025. Esse numerador difere do denominador usado nas participações; o script reproduz exatamente essa escolha.
- **Despesa empenhada / PIB** = despesa empenhada em R$ / (PIB municipal em mil R$ × 1.000).
- **Educação e saúde** = despesa empenhada na função / despesa total empenhada. Não representam automaticamente cumprimento dos pisos constitucionais.
- **Valores reais do Brasil**: fator cumulativo dos IPCA anuais posteriores ao ano observado até 2025, conforme a planilha. Não equivale à atualização por índices médios anuais.
- **Suíça**: governo geral, não municípios suíços. Fluxos CHF→BRL pela PTAX média anual; dívida (estoque) pela cotação de encerramento. Conversão cambial não equivale a paridade de poder de compra.

## Fontes declaradas na planilha

- Tesouro Nacional — Siconfi/FINBRA, DCA, anexos I-C (receitas), I-D (despesas) e I-E (despesas por função): https://siconfi.tesouro.gov.br/siconfi/
- IBGE/SIDRA — população (tabela 6579) e PIB municipal (tabela 5938): https://sidra.ibge.gov.br/
- IBGE — IPCA, série histórica utilizada na base (consulta referenciada a fevereiro/2026): https://www.ibge.gov.br/
- Banco Central do Brasil — PTAX BRL/CHF: https://www.bcb.gov.br/
- Swiss Federal Finance Administration (FFA), estatísticas financeiras GFS; Banco Mundial/WDI, PIB e população: https://www.efv.admin.ch/ e https://data.worldbank.org/

Os CSVs preservam o conteúdo registrado na planilha. O repositório **não afirma que todos os valores foram independentemente reextraídos ou integralmente conciliados**.

## Limitações e pendências

- A auditoria independente FINBRA foi iniciada, mas o mapeamento/reconciliação de algumas rubricas de receitas e transferências municipais **não foi concluído**. Ver abas `FINAL_Auditoria_FINBRA`, `Rastreio_contas_municipais` e `FINAL_Metodologia`.
- População municipal ausente em 2022–2023 e PIB municipal ausente em 2024–2025 na base consultada. Não há imputação nem substituição por zero.
- A situação de 2025 para os dados fiscais suíços não foi validada como observação final. A comparação institucional deve privilegiar o período com status confirmado, não tratar 2025 como definitivo.
- A lista de 80 artigos foi selecionada para o referencial, mas a conferência de todos os textos integrais e metadados editoriais não está certificada aqui.
- Os resultados são descritivos: dependência de transferências, por si só, **não demonstra** efeito *flypaper* nem ilusão fiscal.

## Reprodução do processo completo

A pasta `dados/originais/` permite inspecionar o material de entrada preservado. Para reproduzir a pesquisa desde a fonte primária, é necessário obter as séries originais nas fontes acima, confrontar as classificações contábeis de cada exercício e validar as pendências descritas; o script disponível reproduz os **tratamentos e indicadores sobre as séries consolidadas**.

## Licenças e uso

Material acadêmico para consulta e reprodução. Os dados de terceiros, artigos e PDFs preservam seus direitos e condições originais de uso. Antes de tornar público o repositório, confira as permissões de redistribuição de cada arquivo, especialmente documentos anexados ao trabalho anterior.
