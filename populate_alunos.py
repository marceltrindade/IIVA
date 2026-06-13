import sqlite3
import yaml
import os
import glob

caminho_alunos = "/mnt/almox/JD/20-29 Work/IIVA-classes/21.01 Alunos/"

conn = sqlite3.connect("iiva.db")
cursor = conn.cursor()

for pasta in sorted(os.listdir(caminho_alunos)):
    caminho = os.path.join(caminho_alunos, pasta)
    if not os.path.isdir(caminho) or pasta.startswith("_") or pasta.startswith("."):
        continue

    perfis = glob.glob(os.path.join(caminho, "Perfil_*.md"))
    if not perfis:
        print(f"❌ {pasta}: sem perfil")
        continue

    with open(perfis[0], "r") as f:
        conteudo = f.read()

        if conteudo.startswith("---"):
            partes = conteudo.split("---", 2)
            if len(partes) >= 2:
                dados = yaml.safe_load(partes[1])

                nome = dados.get("name", pasta)
                nível = dados.get("level", "")
                frequencia = dados.get("frequency", "")
                objetivos = dados.get("goals", "")
                status = dados.get("status", "Ativo")
                ultima_atualizacao = dados.get("last_updated", None)

                cursor.execute("""
                    INSERT INTO alunos (nome, nível, frequencia, objetivos, status, ultima_atualizacao)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (nome, nível,frequencia, objetivos, status, ultima_atualizacao))
                print(f"✅ {nome} -- inserido")

conn.commit()
conn.close()
