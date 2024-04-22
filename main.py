from config import API_KEY, API_URL, FOLDER_ID
from pydantic import BaseModel
from typing import Annotated

import requests
from requests import Response
from fastapi import FastAPI, Body

app = FastAPI()


class GptItems(BaseModel):
    prompt: Annotated[str, Body(title="Промт для gpt")]
    gpt_role: Annotated[str, Body(default="Помощник по всем вопросам", title="Роль, которую примет gpt при ответе")]


class Result(BaseModel):
    result: str | None = None
    code: str


@app.post("/ask_gpt", response_model=Result, description="Отправляем промт в yandex gpt и получаем ответ")
async def ask_gpt(body_items: GptItems):
    prompt: str = body_items.prompt
    gpt_role: str = body_items.gpt_role

    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'modelUri': f'gpt://{FOLDER_ID}/yandexgpt-lite',
        'completionOptions': {
            'stream': False,
            'temperature': 0.3,
            'maxTokens': '2000'
        },
        'messages': [
            {
                'role': 'system',
                'text': gpt_role
            },
            {
                'role': 'user',
                'text': prompt
            }
        ]
    }

    response: Response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        response: dict = response.json()
        try:
            response_txt: str = response["result"]["alternatives"][0]["message"]["text"]
        except TypeError:
            return {"code": "TypeError"}
        else:
            return {"result": response_txt, "code": "OK"}

    return {"code": "ERROR"}
