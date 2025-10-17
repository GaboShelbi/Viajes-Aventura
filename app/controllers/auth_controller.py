from flask import session, redirect, render_template, request, url_for, flash
from app.models.user_model import UserModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = UserModel.find_by_email(email)

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['nombre']
            session['user_rol'] = user['rol']
            return redirect(url_for('dashboard.index'))
        else:
            flash('Credenciales incorrectas', 'danger')
            return render_template('login.html')
    return render_template('login.html')

def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        rol = request.form.get('rol', 'cliente')

        if UserModel.find_by_email(email):
            flash('El correo ya está registrado', 'warning')
            return render_template('register.html')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        UserModel.create_user(nombre, email, hashed_password, rol)

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

def logout():
    session.clear()
    return redirect(url_for('auth.login'))