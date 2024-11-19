import pytest
from app import app, db
from models import QA
import openai
from unittest.mock import patch

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()  # Cleanup after tests

# Test for a valid question
def test_ask(client):
    """Test the /ask endpoint with a valid question."""
    with patch('openai.ChatCompletion.create') as mock_openai:
        mock_openai.return_value = {
            'choices': [
                {'message': {'role': 'assistant', 'content': 'AI stands for Artificial Intelligence.'}}
            ]
        }
        response = client.post('/ask', json={'question': 'What is AI?'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'answer' in data
        assert 'Artificial Intelligence' in data['answer']  # Check if the correct answer is returned

# Test for an empty question
def test_ask_empty_question(client):
    """Test the /ask endpoint with an empty question."""
    response = client.post('/ask', json={'question': ''})
    assert response.status_code == 400  # Expecting bad request for empty question
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Question is required!'  # Check the error message

# Test for missing question field
def test_ask_missing_question_field(client):
    """Test the /ask endpoint with no question field in the request."""
    response = client.post('/ask', json={})
    assert response.status_code == 400  # Expecting bad request for missing field
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Question is required!'  # Check the error message

# Test for invalid HTTP method
def test_ask_invalid_method(client):
    """Test the /ask endpoint using an invalid HTTP method (GET instead of POST)."""
    response = client.get('/ask')
    assert response.status_code == 405  # Method not allowed (GET instead of POST)

# Test for quota exceeded scenario
def test_ask_quota_exceeded(client, mocker):
    """Test the /ask endpoint when OpenAI API quota is exceeded."""
    mocker.patch('openai.ChatCompletion.create', side_effect=openai.error.RateLimitError('Quota exceeded'))
    response = client.post('/ask', json={'question': 'What is AI?'})
    assert response.status_code == 429  # Quota exceeded should return 429
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'You have exceeded your OpenAI quota. Please check your plan and billing details.'  # Check error message

# Test for internal server error scenario
def test_ask_internal_error(client, mocker):
    """Test the /ask endpoint when there is an internal server error."""
    mocker.patch('openai.ChatCompletion.create', side_effect=Exception('Internal Server Error'))
    response = client.post('/ask', json={'question': 'What is AI?'})
    assert response.status_code == 500  # Internal server error should return 500
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Error fetching data from OpenAI'  # Check if the error message is correct

# Test for persistence (storing question and answer in the database)
def test_ask_persistence(client):
    """Test that the question and answer are stored in the database."""
    with patch('openai.ChatCompletion.create') as mock_openai:
        mock_openai.return_value = {
            'choices': [
                {'message': {'role': 'assistant', 'content': 'AI stands for Artificial Intelligence.'}}
            ]
        }
        response = client.post('/ask', json={'question': 'What is AI?'})
        assert response.status_code == 200  # Check if the request was successful

    with app.app_context():
        qa_entry = QA.query.filter_by(question='What is AI?').first()
        assert qa_entry is not None  # Ensure that the question and answer are stored
        assert qa_entry.question == 'What is AI?'
        assert 'Artificial Intelligence' in qa_entry.answer  # Ensure the correct answer is stored

# Test for multiple questions and persistence
def test_multiple_questions(client):
    """Test that multiple questions are stored and handled correctly."""
    questions = [
        'What is AI?',
        'Explain machine learning.',
        'What is deep learning?'
    ]

    with patch('openai.ChatCompletion.create') as mock_openai:
        mock_openai.side_effect = [
            {'choices': [{'message': {'content': 'AI stands for Artificial Intelligence.'}}]},
            {'choices': [{'message': {'content': 'Machine learning is a subset of AI.'}}]},
            {'choices': [{'message': {'content': 'Deep learning is a subset of machine learning.'}}]}
        ]

        for question in questions:
            response = client.post('/ask', json={'question': question})
            assert response.status_code == 200  # Check if each question returns a successful response

    with app.app_context():
        for question in questions:
            qa_entry = QA.query.filter_by(question=question).first()
            assert qa_entry is not None  # Ensure that each question is stored in the database

# Test for long question input
def test_long_question(client):
    """Test handling of a long question."""
    long_question = "What are the applications of AI in healthcare, including machine learning, natural language processing, and robotic process automation, and how can they be used to improve patient outcomes and streamline operations in medical institutions?"
    
    with patch('openai.ChatCompletion.create') as mock_openai:
        mock_openai.return_value = {
            'choices': [
                {'message': {'role': 'assistant', 'content': 'AI can be used in healthcare for improving patient outcomes.'}}
            ]
        }
        response = client.post('/ask', json={'question': long_question})
        assert response.status_code == 200  # Ensure that the response is successful
        data = response.get_json()
        assert 'answer' in data
        assert 'healthcare' in data['answer']  # Validate the response content
