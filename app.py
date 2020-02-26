import web  # pip install web.py

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
    '/delete/?', 'application.controllers.delete.Alumnos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
