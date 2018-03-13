from app import app, db
from app.models import User

if __name__ == '__main__':
    app.run(debug=True)


@app.shell_context_processor
def shell_ctx():
    return {'db': db, 'User':User}