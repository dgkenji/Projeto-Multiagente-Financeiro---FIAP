from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from tools.b3_data import (
    get_stock_quote,
    get_fundamentals,
    compare_stocks,
    get_dividends,
    search_companies,

    recommend_dividend_stocks,
    recommend_growth_stocks,
    recommend_value_stocks
)


b3_agent = LlmAgent(

    name="b3_agent",

    model=LiteLlm(
    #model="ollama_chat/llama3.1:8b"
    #model="ollama_chat/qwen2.5:14b"
    #model="ollama_chat/qwen2.5:14b-instruct-q4_K_M"
    #model="ollama_chat/qwen2.5:7b-instruct-q8_0"
    model="ollama_chat/llama3.1:8b-instruct-q4_K_M"
),

    generate_content_config={

        "max_output_tokens": 500,

        "temperature": 0,


    },

    tools=[

        search_companies,
        get_stock_quote,
        get_fundamentals,
        compare_stocks,
        get_dividends,

        recommend_dividend_stocks,
        recommend_growth_stocks,
        recommend_value_stocks

    ],

instruction="""
Você é especialista da B3.

Você responde SOMENTE sobre:
- ações
- dividendos
- valuation
- fundamentos
- bolsa brasileira

REGRAS:

- Nunca explique raciocínio
- Nunca diga o que fará
- Nunca descreva tools
- Nunca invente tickers
- Nunca invente dados
- Nunca use .SA nos tickers

Sempre use UMA tool antes de responder.

TOOLS:

- search_companies(company)
- get_stock_quote(ticker)
- get_fundamentals(ticker)
- get_dividends(ticker)
- compare_stocks(ticker1, ticker2)

- recommend_dividend_stocks()
- recommend_growth_stocks()
- recommend_value_stocks()

USO:

- empresa -> search_companies
- cotação -> get_stock_quote
- fundamentos -> get_fundamentals
- dividendos -> get_dividends
- comparação -> compare_stocks

- ações para dividendos -> recommend_dividend_stocks
- ações de crescimento -> recommend_growth_stocks
- ações baratas -> recommend_value_stocks

Se tool falhar:
responda:
"Nenhum ativo encontrado."

Após usar tool:
gere resposta objetiva.
"""
)