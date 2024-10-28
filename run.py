from app import create_app, db

app = create_app()

# Crée les tables si elles n'existent pas encore
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
