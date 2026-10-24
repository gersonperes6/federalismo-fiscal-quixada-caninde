# Registro de atualizações, correções e decisões metodológicas

Este registro compara a **Prova 1** (arquivo `dados/originais/trabalho_anterior_PROVA1.pdf`) com a pesquisa consolidada em 2026. Para o detalhamento de cada atualização, consultar também `registro_correcoes_original.csv` e as abas `FINAL_Alteracoes`, `Registro_alteracoes`, `ENTREGA_historico` e `FINAL_Metodologia` na planilha-mestre.

| Aspecto | Material anterior | Versão consolidada | Consequência |
|---|---|---|---|
| Período de referência | Diagnóstico anterior, principalmente 2014–2023 | Série fiscal municipal anual 2016–2025 | Janela comum de dez exercícios. |
| Recorte municipal | Quixadá e Canindé; receitas, despesas, PIB e educação | Mantém os municípios; acrescenta indicadores de transferências correntes e participação tributária | Maior ênfase na composição das receitas e na autonomia fiscal. |
| Referencial teórico | Trabalho acadêmico anterior | Literatura sobre federalismo fiscal, transferências, ilusão fiscal e efeito flypaper, com 80 artigos priorizados | Amplia a fundamentação, sem transformar correlações em causalidade. |
| Denominador dos indicadores | Indicadores descritivos anteriores | Receita total **excluídas intraorçamentárias** | Dependência e participação tributária são comparáveis dentro do recorte da base atual. |
| IPCA 2022 | Taxa de 5,78% registrada em versão intermediária | Corrigida para **5,79%**, conforme referência IBGE na planilha | Refaz fatores e valores reais de 2016–2025. |
| PTAX 2016 | Alerta intermediário incorreto de cobertura parcial | Conferência de 251 datas únicas e revisão da indicação de cobertura | Evita classificar a série anual como incompleta por engano. |
| PTAX 2016–2025 | Consolidações anteriores | Deduplicação e recálculo das médias anuais e taxas de encerramento | Padroniza a conversão CHF/BRL. |
| Câmbio de fluxos e estoques | Critério não suficientemente distinguido | Fluxos pela PTAX média anual; dívida pela PTAX de encerramento | Evita aplicar câmbio médio a estoque de dívida. |
| Dados ausentes IBGE | Disponibilidade desigual | Lacunas preservadas sem imputação (população 2022–23; PIB 2024–25) | Indicadores dependentes desses dados ficam vazios. |
| Suíça | Referência comparativa | Contextualização institucional; governo geral FFA/GFS e fontes auxiliares | Não equipara governo geral suíço a municípios brasileiros. |
| Dados suíços de 2025 | Informação a verificar | Status final ainda **não confirmado** | Não tratar 2025 como dado fiscal definitivo. |
| Auditoria FINBRA | Extrações originais | Auditoria independente parcial, com rastreio e ressalvas | Mapeamento de algumas rubricas e reconciliação integral **pendentes**. |
| Documentação/reprodutibilidade | Arquivo da prova | Planilha-mestre, dicionário, log, scripts, tabelas e gráficos | Permite conferir fórmulas a partir da base consolidada. |

## Ressalva identificada ao preparar este pacote

A coluna `Receita real R$ 2025` da aba `FINAL_Municipios` corresponde a **receita bruta × fator IPCA**, enquanto os indicadores de dependência e participação tributária usam **receita exceto intraorçamentárias**. Isso é uma distinção de base de cálculo, não uma correção silenciosa. O script `reproduzir.py` mantém ambas as escolhas e verifica os resultados registrados. Em 2019, por exemplo, a diferença é observável em Canindé, onde receita bruta e receita exceto intra diferem.

## Pendências a não ocultar

1. Validar e reconciliar integralmente as rubricas FINBRA de receitas/transferências em todos os exercícios.
2. Confirmar a classificação e a natureza (observado, estimado, provisório) dos dados fiscais suíços, especialmente 2025.
3. Verificar metadados e textos integrais dos artigos priorizados antes de afirmar revisão completa dos 80 artigos.
4. Conferir as condições de publicação pública de arquivos de terceiros antes de subir o ZIP integral ao GitHub.
