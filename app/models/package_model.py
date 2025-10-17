from app.db.connection import get_connection

class PackageModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                p.*, 
                GROUP_CONCAT(d.nombre SEPARATOR ', ') AS destinos,
                SUM(d.costo) AS precio_total
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
    def get_by_id(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, GROUP_CONCAT(d.id) AS destinos_ids
            FROM paquetes p
            JOIN paquete_destino pd ON p.id = pd.paquete_id
            JOIN destinos d ON pd.destino_id = d.id
            WHERE p.id = %s
            GROUP BY p.id
        """, (id,))
        paquete = cursor.fetchone()
        cursor.close()
        conn.close()
        return paquete

    @staticmethod
    def create(nombre, fecha_inicio, fecha_fin, destinos_ids):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Calcular el precio total sumando los costos de los destinos seleccionados
        format_strings = ','.join(['%s'] * len(destinos_ids))
        cursor.execute(f"SELECT SUM(costo) AS total FROM destinos WHERE id IN ({format_strings})", tuple(destinos_ids))
        total = cursor.fetchone()['total'] or 0

        cursor.execute(
            "INSERT INTO paquetes (nombre, fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s, %s)",
            (nombre, fecha_inicio, fecha_fin, total)
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
    def update(id, nombre, fecha_inicio, fecha_fin, destinos_ids):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Calcular el nuevo precio total
        format_strings = ','.join(['%s'] * len(destinos_ids))
        cursor.execute(f"SELECT SUM(costo) AS total FROM destinos WHERE id IN ({format_strings})", tuple(destinos_ids))
        total = cursor.fetchone()['total'] or 0

        cursor.execute(
            "UPDATE paquetes SET nombre=%s, fecha_inicio=%s, fecha_fin=%s, precio_total=%s WHERE id=%s",
            (nombre, fecha_inicio, fecha_fin, total, id)
        )

        cursor.execute("DELETE FROM paquete_destino WHERE paquete_id = %s", (id,))
        for destino_id in destinos_ids:
            cursor.execute(
                "INSERT INTO paquete_destino (paquete_id, destino_id) VALUES (%s, %s)",
                (id, destino_id)
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
