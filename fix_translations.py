import pandas as pd
from deep_translator import GoogleTranslator
from pathlib import Path

# File paths
csv_path = Path(__file__).parent / 'data' / 'translated_words.csv'

def translate_word(word):
    try:
        translation = GoogleTranslator(source='iw', target='en').translate(word)
        return translation.lower()
    except Exception as e:
        print(f"Error translating '{word}': {str(e)}")
        return "ERROR"

def fix_translations():
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Count how many errors we need to fix
    errors = df[df['english_translation'] == 'ERROR']
    print(f"Found {len(errors)} translations to fix...")

    # Fix each error
    fixed = 0
    for idx, row in errors.iterrows():
        new_translation = translate_word(row['hebrew'])
        if new_translation != "ERROR":
            df.at[idx, 'english_translation'] = new_translation
            fixed += 1
            print(f"Fixed: {row['hebrew']} -> {new_translation}")
        
    print(f"\nFixed {fixed} out of {len(errors)} translations")
    
    # Save the updated data
    df.to_csv(csv_path, index=False)
    print(f"Saved updated translations to {csv_path}")

if __name__ == "__main__":
    fix_translations()
