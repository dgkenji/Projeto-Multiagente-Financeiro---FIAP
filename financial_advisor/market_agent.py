from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from tools.market_search import (
    explain_product
)


market_agent = LlmAgent(

    name="market_agent",

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

        explain_product
    ],

instruction="""
Você é um especialista financeiro brasileiro.

Sua função é explicar produtos financeiros usando informações públicas obtidas pela tool.

REGRAS:
- Nunca tente pesquisar ações.
- Nunca tente explicar tickers.
- Use SOMENTE os dados retornados.
- Nunca invente informações.

Após receber os dados:
- gere uma explicação detalhada atravpes do explain_product
- explique:
    - o que é
    - como funciona
    - riscos
    - vantagens
    - desvantagens
    - liquidez
    - perfil de investidor

Quando houver comparação:
- compare os produtos
- destaque diferenças
- explique qual faz mais sentido em cada cenário

Formato:

Produto:
Como funciona:
Vantagens:
Riscos:
Perfil ideal:
Comparação:
Conclusão:

Não use JSON.
"""
)