import web  # pip install web.py

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
    '/alumnos2/?', 'application.controllers.alumnos2.Alumnos',
    '/alumnos3/?', 'application.controllers.alumnos3.Alumnos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
