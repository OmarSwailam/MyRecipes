from waitress import serve

from myrecipes.wsgi import application

if __name__ == "__main__":
    serve(application, port="8000")
