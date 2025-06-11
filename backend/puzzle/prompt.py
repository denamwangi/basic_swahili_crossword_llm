generate_clues_prompt = """
Prompt:

You are a crossword clue generator for a Swahili crossword puzzle.

You are given a list of words. For each word, generate one crossword clue in **Swahili** that would help a solver guess the word. 
The clues should be:

- Clear and grammatically correct
- Definitions, synonyms, or short descriptive hints
- Not translations from English — use native Swahili clue style
- No more than one sentence per clue
- Clues at a high school conversational level

Input:
{
  "across": ["SAA", "ALAMA", "RILABA", "IPI", "AGH", "AMEDAI", "UBANI", "ONA"],
  "down": ["ARI", "SLIPA", "AALIMU", "AMA", "EBO", "ABADAN", "AGANA", "HII"]
}

Output format (same structure, but each word replaced with a clue).:

{
  "across": {
    "SAA": "Kifaa cha kuonyesha muda",
    "ALAMA": "Ishara au nembo",
    ...
  },
  "down": {
    "ARI": "Hamasa au shauku ya kufanya jambo",
    ...
  }
}

Respond only in JSON, Do *NOT* include any markdown
"""
