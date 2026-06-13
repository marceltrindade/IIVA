import sqlite3
import yaml
import os
import glob
import re

caminho_alunos = "/mnt/almox/JD/20-29 Work/IIVA-classes/21.01 Alunos/"

conn = sqlite3.connect("iiva.db")
cursor = conn.cursor()

#Mapear nome do aluno -> id no banco
cursor.execute("SELECT id, nome FROM alunos WHERE status = 'Ativo'")
alunos_map = {row[1].lower(): row[0] for row in cursor.fetchall()}

for pasta in sorted (os.listdir(caminho_alunos)):
    caminho = os.path.join(caminho_alunos, pasta)
    if not os.path.isdir(caminho) or pasta.startswith("_") or pasta.startswith("."):
        continue

    arquivos_aula = sorted(glob.glob(os.path.join(caminho, "*_Aula_*.md")))

    for arquivo in arquivos_aula:
        nome_arq = os.path.basename(arquivo)

        match = re.search(r"(\d{4}-\d{2}-\d{2})_Aula_(\d+)_", nome_arq)
        if not match:
            continue

        data = match.group(1)
        aula_num = int(match.group(2))

        nome_aluno = nome_arq.split("_")[-1].replace(".md", "").lower()
        aluno_id = alunos_map.get(nome_aluno)
        if not aluno_id:
            print(f"❌ {nome_arq}: aluno não encontrado no banco")
            continue

        arquivo_log = arquivo.replace("_Aula_", "_Log_Aula_")
        status = "realizada" if os.path.exists(arquivo_log) else "planejada"

        topico = ""
        with open(arquivo, "r") as f:
            conteudo = f.read()
        if conteudo.startswith("---"):
            partes = conteudo.split("---", 2)
            if len(partes) >= 2:
                try:
                    dados = yaml.safe_load(partes[1])
                except:
                    dados = {}
                topico = (dados.get("topicos") or
                          dados.get("topico_planejado") or
                          dados.get("conteudo_principal") or
                          "")
                if isinstance(topico, list):
                    topico = "; ".join(topico)

        cursor.execute("""
            INSERT INTO aulas (aluno_id, data, aula_numero, topico, status)
            VALUES (?, ?, ?, ?, ?)
        """, (aluno_id, data, aula_num, str(topico)[:200], status))
        print(f"✅ {nome_aluno} -- Aula {aula_num} ({data}) -- {status}")

conn.commit()
conn.close()
