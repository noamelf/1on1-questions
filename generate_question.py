import json
import random
from pathlib import Path

questions_path = Path(__file__).parent / 'questions.json'
with open(questions_path) as f:
    questions = json.load(f)


def run(event, context):
    question = random.choice(questions)

    print(question['question'])

    response = {
        "statusCode": 200,
        "body": json.dumps(question['question'])
    }

    return response
