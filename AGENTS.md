# IIVA — Idioma Independente

## Propósito
Gestão de alunos e aulas da Idioma Independente (aulas de inglês). API FastAPI + watcher de arquivos + SQLite.

## Stack
- **API:** FastAPI + uvicorn na porta 8000
- **Banco:** SQLite (`iiva.db` — 2 tabelas: alunos, aulas)
- **Watcher:** watchdog (monitora arquivos .md e atualiza DB)
- **Deploy:** VALIS (100.100.188.33) via rsync + systemd

## Onde está

| Ambiente | Caminho | Função |
|---|---|---|
| **UBIK (código fonte)** | `~/Projects/IIVA/` | Desenvolvimento |
| **VALIS (deploy)** | `~/docker/iiva/` | Produção (via rsync) |
| **VALIS (aulas)** | `~/IIVA-classes/` | Dados dos alunos (SyncThing) |

## Serviços (VALIS, systemd root)
- `iiva-api.service` — FastAPI na porta 8000
- `iiva-watcher.service` — File watcher (monitora `~/IIVA-classes/`)

## Variáveis de Ambiente
Consulte `.env` na raiz do projeto:
- `VAULT_ALUNOS` — path para a pasta com arquivos de alunos
- `DB_PATH` — path para o SQLite (`iiva.db`)

## Regras para Joi
1. **NUNCA executar sem OK do Marcel.** IIVA é laboratório pedagógico — explicar, guiar, ele decide.
2. **Deploy:** `rsync -av ~/Projects/IIVA/ marcel@100.100.188.33:~/docker/iiva/` + reiniciar systemd.
3. **Recriar venv no VALIS após deploy:** ssh + `rm -rf venv && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
4. **Após deploy:** `ssh VALIS 'sudo systemctl restart iiva-api iiva-watcher'`
5. **Consultar `_Mapeamento IIVA.md` no SB** para verificar acoplamentos antes de mudar paths.
6. **Referência completa:** skill `iiva` (umbrella) + `references/backend-infra.md`.
