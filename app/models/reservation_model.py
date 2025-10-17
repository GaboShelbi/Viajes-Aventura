from app.db.connection import get_connection

class ReservationModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT r.id, r.fecha_reserva, u.nombre AS usuario, p.nombre AS paquete
            FROM reservas r
            JOIN users u ON r.user_id = u.id
            JOIN paquetes p ON r.paquete_id = p.id
        """)
        reservas = cursor.fetchall()
        cursor.close()
        conn.close()
        return reservas

    @staticmethod
    def get_by_user(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT r.id, r.fecha_reserva, p.nombre AS paquete 
            FROM reservas r
            JOIN paquetes p ON r.paquete_id = p.id
            WHERE r.user_id = %s
        """, (user_id,))
        reservas = cursor.fetchall()
        cursor.close()
        conn.close()
        return reservas

    @staticmethod
    def create(user_id, paquete_id, fecha_reserva):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservas (user_id, paquete_id, fecha_reserva)
            VALUES (%s, %s, %s)
        """, (user_id, paquete_id, fecha_reserva))
        conn.commit()
        cursor.close()
        conn.close()
