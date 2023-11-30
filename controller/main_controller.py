from flask import redirect, url_for

from app import app


@app.get('/')
def index():
    return redirect(url_for('matrix'))
