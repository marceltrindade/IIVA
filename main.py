import os
import sqlite3

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "iiva.db")

app = FastAPI(title="IIVA - Idioma Independente Virtual Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
def raiz():
    return {"mensagem": "IIVA API rodando"}


@app.get("/alunos")
def listar_alunos():
    conn = get_db()
    alunos = conn.execute("SELECT * FROM alunos ORDER BY nome").fetchall()
    conn.close()
    return [dict(a) for a in alunos]


@app.get("/aulas")
def listar_aulas(status: str = None, data: str = None):
    conn = get_db()
    query = """SELECT aulas.*, alunos.nome AS aluno_nome
               FROM aulas
               JOIN alunos ON aulas.aluno_id = alunos.id
               WHERE 1=1"""

    params = []

    if status:
        query += " AND status = ?"
        params.append(status)
    if data:
        query += " AND data = ?"
        params.append(data)

    query += " ORDER BY data DESC"
    aulas = conn.execute(query, params).fetchall()

    conn.close()
    return [dict(a) for a in aulas]


@app.get("/alunos/{aluno_id}/aulas")
def aulas_do_aluno(aluno_id: int):
    conn = get_db()
    aulas = conn.execute(
        """SELECT a.id, a.data, a.aula_numero, a.topico, a.status,
                  al.nome AS aluno_nome
           FROM aulas a
           JOIN alunos al ON a.aluno_id = al.id
           WHERE a.aluno_id = ?
           ORDER BY a.data DESC""",
        (aluno_id,),
    ).fetchall()
    conn.close()
    return [dict(a) for a in aulas]
