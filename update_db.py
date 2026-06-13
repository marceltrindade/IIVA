import sqlite3
import yaml
import os
import re
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH")

def processar_arquivo(caminho):
    """Identifica o tipo de arquivo e chama a função de atualização correta."""
    nome = os.path.basename(caminho)

    if nome.startswith("Perfil_"):
        atualizar_aluno(caminho)
    elif "_Aula_" in nome and not "Exercicios_" in nome:
        atualizar_aula(caminho)

def atualizar_aluno(caminho):
    """Atualiza ou insere um aluno na tabela de alunos a partir do Perfil_*.md"""
    with open(caminho, "r") as f:
        conteudo = f.read()

    if not conteudo.startswith("---"):
        return

    partes = conteudo.split("---", 2)
    if len(partes) < 2:
        return

    try:
        dados = yaml.safe_load(partes[1])
        nome = dados.get("name", "")
        if not nome:
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        #Verifica se já existe
        cursor.execute("SELECT id FROM alunos WHERE nome = ?", (nome,))
        existe = cursor.fetchone()

        nivel = dados.get("level", "")
        frequencia = dados.get("frequency", "")
        objetivos = dados.get("goals", "")
        status = dados.get("status", "Ativo")

        if existe:
            cursor.execute("""
                UPDATE alunos SET nivel=?, frequencia=?, objetivos=?, status=?
                WHERE nome=?
            """, (nivel, frequencia, objetivos, status, nome))
        else:
            cursor.execute("""
                INSERT INTO alunos (nome, nivel,frequencia, objetivos, status)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, nivel, frequencia, objetivos, status))

        conn.commit()
        conn.close()
        print(f"✅ Aluno atualizado: {nome}")
    except Exception as e:
        print(f"❌ Erro ao processar {caminho}: {e}")

def atualizar_aula(caminho):
    """Atualiza ou insere uma aula na tabela aulas a partir de *_Aula_*.md"""
    nome_arq = os.path.basename(caminho)

    #Extrair dados do nome do arquivo
    match = re.search(r"(\d{4}-\d{2}-\d{2})_Aula_(\d+)_", nome_arq)
    if not match:
        return
    
    data = match.group(1)
    aula_num = int(match.group(2))

    #Extrair nome do aluno do final do arquivo
    nome_aluno = nome_arq.split("_")[-1].replace(".md", "")

    #Determinar status: Log existe? -> realizada. Só plano? -> planejada
    if "Log_" in nome_arq:
        status = "realizada"
    else:
        #Verificar se existe arquivo de log correspondente
        arquivo_log = caminho.replace("_Aula_", "_Log_Aula")
        status = "realizada" if os.path.exists(arquivo_log) else "planejada"

    #Ler YAML pra extrair tópico
    topico = ""
    with open(caminho, "r") as f:
        conteudo = f.read()
    if conteudo.startswith("---"):
        partes = conteudo.split("---", 2)
        if len(partes) >= 2:
            try:
                dados = yaml.safe_load(partes[1])
                topico = (dados.get("topicos") or
                          dados.get("topico_planejado") or
                          dados.get("conteudo_principal") or "")
                if isinstance(topico, list):
                    topico = "; ".join(topico)
            except:
                pass

    #Buscar aluno_id no banco
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM alunos WHERE LOWER(nome) = ?", (nome_aluno.lower(),))
    aluno = cursor.fetchone()
    if not aluno:
        conn.close()
        return
    aluno_id = aluno[0]

    #Verificar se a aula já existe
    cursor.execute("""
        SELECT id FROM aulas WHERE aluno_id = ? AND data = ? AND aula_numero = ?
    """, (aluno_id, data, aula_num))
    existe = cursor.fetchone()

    if existe:
        cursor.execute("""
            UPDATE aulas SET topico=?, status=? WHERE id=?
        """, (str(topico)[:200], status, existe[0]))
    else:
        cursor.execute("""
            INSERT INTO aulas (aluno_id, data, aula_numero, topico, status)
            VALUES (?, ?, ?, ?, ?)
        """, (aluno_id, data, aula_num, str(topico)[:200], status))

    conn.commit()        
    conn.close()
    print(f"✅ Aula atualizada: {nome_aluno} - Aula {aula_num} ({data})")
