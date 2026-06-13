CREATE TABLE IF NOT EXISTS alunos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT,
  nível TEXT,
  frequencia TEXT,
  objetivos TEXT,
  interesses TEXT,
  status TEXT NOT NULL DEFAULT 'Ativo',
  data_inicio DATE,
  ultima_atualizacao DATE
);

CREATE TABLE IF NOT EXISTS aulas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  aluno_id INTEGER NOT NULL,
  data DATE NOT NULL,
  aula_numero INTEGER,
  topico TEXT,
  status TEXT DEFAULT 'planejada',
  FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);
