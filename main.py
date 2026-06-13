from fastapi import FastAPI
import sqlite3

app = FastAPI(title="IIVA - Idioma Independente Virtual Assistant")

def get_db():
    conn = sqlite3.connect("iiva.db")
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
def listar_aulas(status: str = None):
    conn = get_db()
    if status:
        aulas = conn.execute(
            "SELECT * FROM aulas WHERE status = ? ORDER BY data DESC", (status,)
        ).fetchall()
    else:
        aulas = conn.execute("SELECT * FROM aulas ORDER BY data DESC").fetchall()
    
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
           ORDER BY a.data DESC""", (aluno_id,)
    ).fetchall()
    conn.close()
    return [dict(a) for a in aulas]
