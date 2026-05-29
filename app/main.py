from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return { "mensagem" : "API FastAPI Funcionando." }


@app.get("/health")
def health():
    return { "status" : "ok" }


@app.get("/soma")
def health(a: int, b: int):
    return { "resultado" : a + b }

from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


@app.get("/tarefas")
def criar_tarefa(tarefa : Tarefa):
    return { 
        "mensagem" : "Tarefa realizada com sucesso",
        "dados" : tarefa
    }