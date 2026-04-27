import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

cursor.execute("UPDATE meu_banco SET cliente = UPPER(cliente)")

cursor.execute('''
    DELETE FROM meu_banco
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM meu_banco
        GROUP BY cliente, valor_transacao, status, setor
    )
''')

print(f"Linhas removidas: {conn.total_changes}")

print("\n--- Banco de Dados Atualizado (Sem Duplicatas) ---")
cursor.execute("SELECT * FROM meu_banco")
for linha in cursor.fetchall():
    print(linha)

conn.commit()
conn.close()
print("\nOperação concluída com sucesso!")