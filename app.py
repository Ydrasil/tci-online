from core import app
from core.views import *


# WSGI
application = app


def get_translations_files(language):
    return "readme.md"


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), host=app.config.get('HOST'),
            port=app.config.get('PORT'))
