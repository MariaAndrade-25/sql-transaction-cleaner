# sql-transaction-cleaner
📊 Transaction Data Pipeline & Audit
Este projeto simula um pipeline de dados financeiro simples, focado na limpeza, padronização e auditoria de transações utilizando Python e SQLite.

🎯 Objetivo
Demonstrar habilidades em manipulação de bancos de dados relacionais (SQL), tratamento de inconsistências em dados brutos e automação de relatórios.

🛠️ Tecnologias Utilizadas
Python 3.x

SQLite3: Banco de dados relacional leve e persistente.

VS Code: Ambiente de desenvolvimento.

🏗️ Estrutura do Projeto
O projeto é dividido em três etapas principais para garantir a integridade dos dados:

main.py: Criação do banco de dados e inserção de dados "brutos" (simulando uma entrada de dados com erros, minúsculas e duplicatas).

limpeza_banco.py:

Padronização: Converte todos os nomes de clientes para UPPERCASE.

Deduplicação: Identifica e remove registros duplicados mantendo apenas a entrada original (via subconsultas SQL).

relatorio_riscos.py: Realiza consultas filtradas para auditoria e exporta os resultados de transações concluídas para um arquivo externo (concluidos.txt).

🚀 Como Executar
Para replicar o banco de dados e as análises, execute os scripts na seguinte ordem:

Bash
# 1. Gerar o banco e dados iniciais
python main.py

# 2. Limpar e padronizar os dados
python limpeza_banco.py

# 3. Gerar relatório de auditoria
python relatorio_riscos.py
📈 Conceitos SQL Aplicados
CREATE TABLE com Chaves Primárias.

INSERT INTO com prevenção de SQL Injection.

UPDATE para sanitização de strings.

DELETE com Subqueries para remoção de redundância.

SELECT com filtros (WHERE) e agrupamentos (GROUP BY).