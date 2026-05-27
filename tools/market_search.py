from duckduckgo_search import DDGS


def explain_product(
    product: str
):

    with DDGS() as ddgs:

        results = list(

            ddgs.text(
                product,
                max_results=3
            )
        )

    if not results:

        return "Nenhuma informação encontrada."

    response = ""

    for i, r in enumerate(results, start=1):

        response += f"""

Fonte {i}:

Título:
{r['title']}

Resumo:
{r['body']}

Link:
{r['href']}

"""

    return response