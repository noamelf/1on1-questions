import json
from pathlib import Path
import random

questions_path = Path(__file__).parent / 'questions.json'
with open(questions_path) as f:
    questions = json.load(f)

question = random.choice(questions)

print(question['question'])
