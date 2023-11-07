import sqlite3


def eliminar_datos_por_id(id):
    conn = sqlite3.connect("BaseQR.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM REGISTROS WHERE id = ?", (id,))
    conn.commit()
    conn.close()


id_a_eliminar = 20  # ID del registro para eliminar
eliminar_datos_por_id(id_a_eliminar)
