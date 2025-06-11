from litellm import completion
from prompt import generate_clues_prompt
import json
import os
# api_key = os.environ.get('GEMINI_API_KEY')

MODEL_GEMINI = "gemini/gemini-2.5-flash-preview-04-17"
MODEL_ANTHROPIC = "claude-3-5-haiku-latest"

def get_llm_clues(puzzle_solution):
    print('puzzle_solution', puzzle_solution)

    messages = [
        {
            'content': generate_clues_prompt,
            'role': 'developer',
        },
        {
            'content': f"here is the puzzle: {puzzle_solution}",
            'role': 'user'
        },
    ]
    print(messages)
    response = completion(MODEL_GEMINI, messages)
    print(response)
    raw_clues = response.choices[0].message.content
    clues = raw_clues.replace('```', '').replace('json', '')
    print(clues)
    import pdb; pdb.set_trace()


if __name__ == "__main__":
    with open('answers.txt', 'r') as f:
        puzzle_solution = json.load(f)
    get_llm_clues(puzzle_solution)
    