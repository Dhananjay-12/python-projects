import requests
import sys

def process_wordlist():
    for word in sys.stdin:
        stripped_word= word.strip()

        if not stripped_word.isalpha():
            continue

        try:
            res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{stripped_word}")
            
            if res.status_code == 404:
                print(f"Word {stripped_word} does not exist in dictionary")
            
            else:
                res.raise_for_status()
                print(f"Word: {stripped_word}")
                print(res.json())
        except requests.exceptions.httpError as e:
            print(f"HTTP error for word {stripped_word}: {e}")

process_wordlist()          

