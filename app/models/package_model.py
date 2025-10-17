from app.db.connection import get_connection

class PackageModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, GROUP_CONCAT(d.nombre) as destinos 
            FROM paquetes p 
            JOIN paquete_destino pd ON p.id = pd.paquete_id 
            JOIN destinos d ON pd.destino_id = d.id 
            GROUP BY p.id
        """)
        paquetes = cursor.fetchall()
        cursor.close()
        conn.close()
        return paquetes

    @staticmethod
    def create(nombre, fecha_inicio, fecha_fin, destinos_ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO paquetes (nombre, fecha_inicio, fecha_fin) VALUES (%s, %s, %s)",
            (nombre, fecha_inicio, fecha_fin)
        )
        paquete_id = cursor.lastrowid

        for destino_id in destinos_ids:
            cursor.execute(
                "INSERT INTO paquete_destino (paquete_id, destino_id) VALUES (%s, %s)",
                (paquete_id, destino_id)
            )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM paquete_destino WHERE paquete_id = %s", (id,))
        cursor.execute("DELETE FROM paquetes WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
