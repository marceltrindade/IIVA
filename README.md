# IIVA — Idioma Independente Virtual Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-FastAPI-009688" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Banco-SQLite-003B57" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Status-Ativo-success" alt="Status"/>
</p>

API FastAPI + watcher de arquivos + SQLite para gestão de aulas particulares de inglês.

---

## Sobre

IIVA é um sistema de gestão pedagógica que centraliza alunos, aulas e progresso em um banco SQLite, com uma API REST para consulta e um file watcher que atualiza automaticamente o banco a partir de arquivos Markdown.

O watcher monitora uma pasta de planos de aula (`.md` com frontmatter YAML) e mantém o banco sincronizado — criação de arquivo vira insert, modificação vira update.

## Stack

- **API:** FastAPI + uvicorn (porta 8000)
- **Banco:** SQLite (2 tabelas: alunos, aulas)
- **Watcher:** watchdog (monitora arquivos .md)
- **Deploy:** rsync + systemd

## Endpoints

| Rota | Descrição |
|------|-----------|
| `GET /` | Status da API |
| `GET /alunos` | Lista todos os alunos |
| `GET /aulas?status=&data=` | Filtra aulas por status/data |
| `GET /alunos/{id}/aulas` | Aulas de um aluno específico |

## Como usar

```bash
# ambiente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# config
cp .env.example .env
# edite .env com seus caminhos

# popular banco
python populate_alunos.py
python populate_aulas.py

# iniciar API
uvicorn main:app

# iniciar watcher (opcional)
python watcher.py
```
