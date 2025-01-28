import pandas as pd
from gimeltra.gimeltra import Transliterator

def add_transliteration():
    # Initialize transliterator
    tr = Transliterator()
    
    # Read the CSV file
    df = pd.read_csv('data/translated_words.csv')
    
    # Add transliteration column
    df['transliteration'] = df['hebrew'].apply(lambda x: tr.tr(x, sc='Hebr', to_sc='Latn'))
    
    # Save to new CSV file
    df.to_csv('data/translated_words_with_transliteration.csv', index=False)

if __name__ == "__main__":
    add_transliteration()
