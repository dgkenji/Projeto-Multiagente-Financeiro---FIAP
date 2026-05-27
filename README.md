# Quantum Finance Advisor

Sistema Multiagente para Consultoria Financeira utilizando:

* Google Agent Development Kit (ADK)
* MCP Tools (Conectado com a plataforma BOLSAI para dados reais da B3)
* LLMs locais via Ollama
* Arquitetura Multi-Agent

---

# Objetivo

O projeto tem como objetivo construir um consultor financeiro inteligente capaz de:

* explicar produtos financeiros
* consultar dados do mercado brasileiro
* comparar ativos
* recomendar ações
* consolidar respostas financeiras de forma confiável

O sistema prioriza o uso de ferramentas (tools/MCP) para evitar hallucinations e garantir maior confiabilidade nas respostas. O sistema é capaz de fazer pesquisas e consumir dados oficiais do mercado brasileiro.

---

# Arquitetura Geral

O sistema foi construído utilizando arquitetura multiagente com separação clara de responsabilidades. 
Foi utilizado o SequentialAgent para que todos os agentes sempre sejam executados. Esta escolha foi devido ao fato de estarmos usando uma LLM local pequena, que teria problemas em orquestrar perfeitamente todos os subagentes.

Fluxo principal:

Usuário
↓
Market Agent + B3 Agent
↓
MCP Tools / APIs
↓
Lead Advisor
↓
Resposta consolidada

---

# Agentes

## 1. Lead Advisor

Responsável por:

* consolidar respostas
* produzir resposta final organizada

Modelo utilizado:

* Llama 3.1 8B Instruct (Ollama)

Funções:

* identificar intenção do usuário
* encaminhar perguntas para os agentes corretos
* consolidar resultados finais

O Lead Advisor NÃO gera dados financeiros diretamente.

---

## 2. Market Agent

Responsável por:

* explicar conceitos financeiros
* explicar produtos de investimento
* responder dúvidas educacionais

Exemplos:

* CDB
* Tesouro Direto
* FIIs
* dividendos
* renda fixa

Tool principal:

* explain_product()

Características:

* foco conceitual
* educação financeira
* não consulta cotações

---

## 3. B3 Agent

Responsável por:

* consultar ativos da bolsa brasileira
* buscar cotações
* buscar fundamentos
* comparar ações
* analisar dividendos

O agente utiliza MCP linkado ao BOLSAI, buscando dados reais e proibindo respostas inventadas.

Exemplos:

* PETR4
* VALE3
* ITUB4
* BBAS3

---

# MCP Tools Utilizadas

## get_stock_quote

Consulta:

* preço atual
* retorno
* volume
* faixa de preço

Uso:

* consultas de cotação

---

## get_fundamentals

Consulta:

* P/L
* P/VP
* ROE
* ROIC
* EV/EBITDA

Uso:

* análise fundamentalista

---

## get_dividends

Consulta:

* histórico de dividendos
* dividend yield

Uso:

* análise de renda passiva

---

## compare_stocks

Compara múltiplos ativos.

Exemplo:

* PETR4 vs VALE3

---

## search_companies

Busca empresas e tickers válidos.

Objetivo:

* evitar hallucinations
* validar ativos

---

## screen_stocks

Executa screening de ações utilizando métricas fundamentalistas.
PS: Notou-se que nem todos os dados do BOLSAI estão funcionando perfeitamente, com algumas funções/outputs tendo limitações (e.g., screen_stocks e os dividendos)

Métricas suportadas:

* ROE
* P/L
* P/VP
* EV/EBITDA
* ROIC

---

# Estratégia de Confiabilidade

O sistema foi desenvolvido priorizando confiabilidade e redução de hallucinations.

Medidas adotadas:

* Separação entre agentes conceituais e agentes financeiros
* Uso obrigatório de MCP tools antes de responder sobre ações
* Bloqueio de geração de dados financeiros sem consulta
* Validação de tickers
* Uso de dados externos ao invés de respostas puramente geradas pelo LLM

O B3 Agent nunca deve inventar:

* preços
* fundamentos
* dividendos
* tickers

---

# Modelos Utilizados

Execução local via Ollama.
Inicialmente, tentou-se utilizar LLMs maiores como gemini-2.5-flash. No entanto, chegávamos aos limites de tokens extremamente rápido mesmo com prompts simplies, inviabilizando seu uso.

Modelos testados:

* gemini-2.5-flash
* llama3.1:8b
* qwen2.5:14b
* llama3.1:8b-instruct-q4_K_M

Modelo final escolhido:

* llama3.1:8b-instruct-q4_K_M

Motivos:

* melhor equilíbrio entre:

  * velocidade
  * uso de RAM
  * tool calling
  * estabilidade


---

# Tecnologias Utilizadas

* Python
* Google ADK
* Ollama
* MCP
* LiteLLM
* AsyncIO

---

# Estrutura do Projeto

financial_advisor/
│
├── agent.py
├── market_agent.py
├── b3_agent.py
│
├── tools/
│   ├── market_search.py
│   ├── b3_data.py
│   └── bolsai_client.py
│
└── test_screen.py

---

# Fluxo de Execução

## Exemplo 1 — Explicação financeira

Pergunta:
"Qual a diferença entre CDB e Tesouro Direto?"

Fluxo:
Lead Advisor
→ Market Agent
→ explain_product()
→ resposta consolidada

---

## Exemplo 2 — Cotação de ação

Pergunta:
"Como está a PETR4?"

Fluxo:
Lead Advisor
→ B3 Agent
→ get_stock_quote("PETR4")
→ resposta consolidada

---

## Exemplo 3 — Comparação de ativos

Pergunta:
"PETR4 ou VALE3?"

Fluxo:
Lead Advisor
→ B3 Agent
→ compare_stocks([...])
→ resposta consolidada

---

# Considerações Finais

O projeto demonstra:

* arquitetura multiagente
* orquestração de agentes
* integração com MCP
* uso de ferramentas externas
* prevenção de hallucinations
* consolidação inteligente de respostas

O foco principal foi construir um sistema confiável e modular, aproximando o comportamento de um consultor financeiro real.
