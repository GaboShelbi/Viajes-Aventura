from flask import session, redirect, url_for, flash

def admin_required(view_func):
    def wrapper(*args, **kwargs):
        if session.get('user_rol') != 'admin':
            flash('Acceso restringido a administradores.', 'danger')
            return redirect(url_for('dashboard.index'))
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper