from app.db.connection import get_connection

class UserModel:
    @staticmethod
    def find_by_email(email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def create_user(nombre, email, password, rol='cliente'):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (nombre, email, password, rol) VALUES (%s, %s, %s, %s)",
                       (nombre, email, password, rol))
        conn.commit()
        cursor.close()
        conn.close()