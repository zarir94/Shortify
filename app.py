from server import init_app

app = init_app(__name__, ver=3.4)

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)

