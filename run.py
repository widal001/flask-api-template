from app import create_app


def init_app():
    app = create_app()
    return app

if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)
