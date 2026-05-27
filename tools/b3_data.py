from tools.bolsai_client import (
    call_tool
)


# =========================
# COTAÇÃO
# =========================

async def get_stock_quote(
    ticker: str
):

    return await call_tool(

        "get_stock_quote",

        {
            "ticker": ticker
        }
    )


# =========================
# FUNDAMENTOS
# =========================

async def get_fundamentals(
    ticker: str
):

    return await call_tool(

        "get_fundamentals",

        {
            "ticker": ticker
        }
    )


# =========================
# DIVIDENDOS
# =========================

async def get_dividends(
    ticker: str
):

    return await call_tool(

        "get_dividends",

        {
            "ticker": ticker
        }
    )


# =========================
# COMPARAÇÃO
# =========================

async def compare_stocks(
    ticker1: str,
    ticker2: str
):

    return await call_tool(

        "compare_stocks",

        {
            "tickers": [
                ticker1,
                ticker2
            ]
        }
    )


# =========================
# BUSCA DE EMPRESAS
# =========================

async def search_companies(
    company: str
):

    return await call_tool(

        "search_companies",

        {
            "query": company
        }
    )


# =========================
# SCREENING
# =========================

async def screen_stocks(
    metric: str,
    operator: str,
    value: float
):

    return await call_tool(

        "screen_stocks",

        {
            "metric": metric,
            "operator": operator,
            "value": value
        }
    )


# =========================
# RECOMENDAÇÕES
# =========================

async def recommend_growth_stocks():

    return await call_tool(

        "screen_stocks",

        {
            "metric": "roe",
            "operator": "gt",
            "value": 0.15
        }
    )

async def recommend_dividend_stocks():

    return await call_tool(

        "screen_stocks",

        {
            "metric": "dividend_yield",
            "operator": "gt",
            "value": 0.03
        }
    )

async def recommend_value_stocks():

    return await call_tool(

        "screen_stocks",

        {
            "metric": "pl",
            "operator": "lt",
            "value": 0.1
        }
    )