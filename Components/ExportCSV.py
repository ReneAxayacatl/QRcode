import sqlite3
import csv


def exportar_a_csv(nombre_archivo):
    conn = sqlite3.connect("BaseQR.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM REGISTROS")
    datos = cursor.fetchall()

    with open(nombre_archivo, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["ID", "DateHour", "Supplier"])

        csv_writer.writerows(datos)

    conn.close()


nombre_archivo_csv = "DataSQLite.csv"
exportar_a_csv(nombre_archivo_csv)
