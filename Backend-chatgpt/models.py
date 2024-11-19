from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for ORM functionality

# Initialize the SQLAlchemy instance (used for database interactions)
db = SQLAlchemy()

# Define the model for storing questions and answers
class QA(db.Model):
    """
    Model representing the 'questions_answers' table in the database.
    This table will store the questions asked by users and the corresponding answers.
    """
    # Define the name of the table in the database
    __tablename__ = 'questions_answers'
    
    # Define the columns of the table:
    id = db.Column(db.Integer, primary_key=True)  # Primary key, automatically incrementing ID
    question = db.Column(db.String, nullable=False)  # Column for storing the question, cannot be null
    answer = db.Column(db.String, nullable=False)  # Column for storing the answer, cannot be null
