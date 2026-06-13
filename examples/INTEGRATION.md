# Integração — IIVA API + Agentes de IA + Automação

## Para Agentes de IA (Hermes, ChatGPT, Claude)

A API IIVA permite que um agente de IA consulte dados de alunos e aulas
sem precisar ler arquivos .md diretamente. Isso economiza tokens e tempo.

### Consultar alunos ativos
```bash
curl http://localhost:8000/alunos
```

### Consultar aulas de um aluno
```bash
curl http://localhost:8000/alunos/1/aulas
```
> Substitua `1` pelo ID do aluno. Use `GET /alunos` primeiro para
> descobrir o ID.

### Consultar aulas por status
```bash
# Apenas aulas realizadas
curl "http://localhost:8000/aulas?status=realizada"

# Apenas aulas planejadas
curl "http://localhost:8000/aulas?status=planejada"
```

## Para n8n (Automação)

A API retorna JSON puro — qualquer nó HTTP no n8n consegue consumir.

### Exemplo: briefing matinal
1. Nó HTTP: `GET http://localhost:8000/aulas?status=planejada`
2. Nó Function: agrupa por aluno
3. Nó Telegram: envia resumo do dia

### Exemplo: detectar nova aula no vault
1. Nó Webhook: espera o watcher notificar
2. Nó HTTP: `GET /alunos/{id}/aulas` para contexto
3. Nó AI: prepara rascunho do plano da próxima aula

## File Watcher

O `watcher.py` monitora a pasta de alunos e atualiza o banco
automaticamente quando um arquivo .md é criado ou modificado.

```bash
python3 watcher.py
```

O watcher rodando em background + API + n8n formam um pipeline
completo: edição → banco → consulta → automação.
