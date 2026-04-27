import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE meu_banco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    valor_transacao REAL,
    status TEXT,
    setor TEXT
)
''')
dados_para_inserir = [
    ('BANCO ALFA', 5000.00, 'Concluído', 'Financeiro'),
    ('banco alfa', 5000.00, 'Concluído', 'Financeiro'), 
    ('Escritório ASBZ', 1200.50, 'Pendente', 'Jurídico'),
    ('Loja Tech', 850.00, 'Erro', 'TI'), 
    ('Hospital Alpha', 3200.00, 'Concluído', 'Saúde'),
    ('Logistica S.A', 0.10, 'Falha', 'Operacoes'),
    ('Contabilidade SMART', 700.00, 'Pendente', 'Financeiro') 
]

cursor.executemany('INSERT INTO meu_banco (cliente, valor_transacao, status, setor) VALUES (?,?,?,?)', dados_para_inserir)

conn.commit()

conn.close()

