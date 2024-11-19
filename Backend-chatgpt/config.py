from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file
import os  # Import os to interact with environment variables

# Load environment variables from the .env file
load_dotenv()  # This function loads all variables defined in the .env file into the environment

# Define the Config class to store application configuration settings
class Config:
    # Get the database URL from the environment variable, with a default value if not set
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@db:5432/dbname')

    # Disable SQLAlchemy's track modifications feature to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Get the OpenAI API key from the environment variable
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # This key is required to interact with OpenAI's API
