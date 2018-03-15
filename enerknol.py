from app import app, db, mongo
from app.models import User, Movies

if __name__ == '__main__':
    app.run(debug=True)


@app.shell_context_processor
def shell_ctx():
    return {'db': db, 'User': User, 'mongo': mongo, 'Movies': Movies}
