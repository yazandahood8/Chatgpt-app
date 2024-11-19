from flask import Flask
from flask_cors import CORS  # Import CORS
from models import db  # Import database instance
from config import Config  # Import configuration class
from flask_migrate import Migrate  # Import Flask-Migrate
from route import routes  # Import the routes Blueprint

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for all routes
CORS(app)

# Initialize database and Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register the Blueprint
app.register_blueprint(routes)

# Use app context to create tables
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
