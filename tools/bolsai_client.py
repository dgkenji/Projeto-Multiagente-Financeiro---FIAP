import os

from dotenv import load_dotenv

from mcp import ClientSession

from mcp.client.stdio import (

    stdio_client,

    StdioServerParameters
)


load_dotenv()


async def call_tool(

    tool_name: str,

    arguments: dict
):

    api_key = os.getenv(
        "BOLSAI_API_KEY"
    )

    if not api_key:

        raise Exception(
            "BOLSAI_API_KEY não encontrada"
        )

    server = StdioServerParameters(

        command="uvx",

        args=[

            "bolsai-mcp"

        ],

        env={

            **os.environ,

            "BOLSAI_API_KEY":

            api_key
        }
    )

    async with stdio_client(
        server
    ) as (
        read,
        write
    ):

        async with ClientSession(
            read,
            write
        ) as session:

            await session.initialize()

            result = await session.call_tool(

                tool_name,

                arguments
            )

            return result