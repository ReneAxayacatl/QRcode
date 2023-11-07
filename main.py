from flask import Flask, render_template
import sqlite3
from datetime import datetime


from twilio.rest import Client

app = Flask(__name__)

account_sid = "AC3e79496594c845b1537104fd87a0edaa"
auth_token = "dce0212979d4a48f5a5d2fe5fe6a9be6"

client = Client(account_sid, auth_token)


def enviar_mensaje_whatsapp(destinatario, mensaje):
    try:
        message = client.messages.create(
            body=mensaje,
            from_="whatsapp:+14155238886",
            to="whatsapp:+5215583723742",
        )
        return f"Mensaje enviado a whatsapp:+5215583723742: Error al enviar el Mensaje"
    except Exception as e:
        return f"Error al enviar el mensaje a +5215583723742: {str(e)}"


@app.route("/")
@app.route("/<string:codigo>")
def index(codigo=None):
    mi_conexion = sqlite3.connect("BaseQR.db")
    cursor = mi_conexion.cursor()

    try:
        consulta = cursor.execute("SELECT * FROM REGISTROS")
        consulta = cursor.fetchall()
        contador = len(consulta)

        if codigo is not None and codigo != "favicon.ico":
            ahora = datetime.now()
            ahora = ahora.strftime("%m/%d/%Y, %H:%M:%S")
            sql = "INSERT INTO REGISTROS(DateHour,Supplier) VALUES (?,?)"
            cursor.execute(sql, (ahora, codigo))
            mi_conexion.commit()
            contador += 1

            mensaje_whatsapp = (
                f"Nuevo registro: {codigo} ingreso al CU UAEMex Texcoco a las {ahora}"
            )
            enviar_mensaje_whatsapp(
                destinatario="NUMERO_DE_DESTINO", mensaje=mensaje_whatsapp
            )

        return render_template("index.html", codigo=codigo, contador=contador)

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        cursor.close()
        mi_conexion.close()


if __name__ == "__main__":
    app.run(debug=True)
