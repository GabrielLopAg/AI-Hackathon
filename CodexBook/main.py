from src.core import create_app

app = create_app()

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)