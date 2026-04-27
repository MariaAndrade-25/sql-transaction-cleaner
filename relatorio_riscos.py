import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT * FROM meu_banco
    WHERE status = "Concluído"
''')

print("\n--- Banco de Dados, Transações Concluídas ---")
dados = cursor.fetchall()
for linha in dados:
    print(linha)

conn.commit()
conn.close()
print("\nOperação concluída com sucesso!")

with open('concluidos.txt', 'w') as f:
    for linha in dados:
        f.write(str(linha) + '\n')