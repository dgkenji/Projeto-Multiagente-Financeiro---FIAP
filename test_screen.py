import asyncio

from tools.bolsai_client import call_tool


async def main():

    result = await call_tool(

        "screen_stocks",

        {
            "metric": "roe",
            "operator": "gt",
            "value": -999
        }
    )

    print(result)


asyncio.run(main())