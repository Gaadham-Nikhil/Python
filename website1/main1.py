from Todo import create_app

#calling create_app function from file __init__1.py
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)