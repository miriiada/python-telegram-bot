from openai import AsyncOpenAI
from config import OPENROUTER_API_KEY

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

async def get_chatgpt_response(messages: list) -> str:
    try:
        response = await client.chat.completions.create(
            model="mistralai/devstral-2512:free",
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error for connect to AI: {str(e)}"