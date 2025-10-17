from app.db.connection import get_connection

class DestinationModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destinos")
        destinos = cursor.fetchall()
        cursor.close()
        conn.close()
        return destinos

    @staticmethod
    def get_by_id(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destinos WHERE id = %s", (id,))
        destino = cursor.fetchone()
        cursor.close()
        conn.close()
        return destino

    @staticmethod
    def create(nombre, descripcion, actividades, costo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO destinos (nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s)",
            (nombre, descripcion, actividades, costo)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(id, nombre, descripcion, actividades, costo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE destinos SET nombre=%s, descripcion=%s, actividades=%s, costo=%s WHERE id=%s",
            (nombre, descripcion, actividades, costo, id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM destinos WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
