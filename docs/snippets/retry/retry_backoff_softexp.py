import asyncio

import httpx

from pyfaulttolerance.retry import retry
from pyfaulttolerance.retry.backoffs import softexp


@retry(on=httpx.NetworkError, backoff=softexp(median_delay_secs=35, max_delay_secs=60))
async def get_poke_data(pokemon: str) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

        return response.json()


asyncio.run(get_poke_data("arrokuda"))
