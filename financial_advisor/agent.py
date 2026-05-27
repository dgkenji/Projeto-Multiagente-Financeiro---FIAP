from dotenv import load_dotenv

from google.adk.agents import (
    LlmAgent,
    SequentialAgent
)
from google.adk.models.lite_llm import LiteLlm

from .market_agent import market_agent
from .b3_agent import b3_agent


load_dotenv()


lead_advisor  = LlmAgent(

    name="lead_advisor",

    model=LiteLlm(
    #model="ollama_chat/llama3.1:8b"
    #model="ollama_chat/qwen2.5:14b"
    #model="ollama_chat/qwen2.5:14b-instruct-q4_K_M"
    #model="ollama_chat/qwen2.5:7b-instruct-q8_0"
    model="ollama_chat/llama3.1:8b-instruct-q4_K_M"
),

    generate_content_config={

        "max_output_tokens": 1500,

        "temperature": 0,

    },

    instruction="""
    Você é o Lead Advisor Final.

    Você consolida:
    - explicações do market_agent
    - dados do b3_agent

    REGRAS:

    - Nunca invente dados
    - Não repita informações
    - Não force comparações
    - Não crie seções vazias
    - Responda de forma natural e profissional

    Use apenas seções que fizerem sentido, como:

    # Resumo
    # Dados Financeiros
    # Comparação
    # Pontos Positivos
    # Pontos de Atenção
    # Conclusão

    Adapte a resposta ao tipo de investimento.
    """
    )

root_agent = SequentialAgent(

    name="financial_pipeline",

    sub_agents=[

        market_agent,

        b3_agent,

        lead_advisor
    ]
)