import csv

def process_csv():
    # Read the CSV file and write to new CSV with hebrew(transliteration) and english
    with open('data/translated_words_with_transliteration.csv', 'r', encoding='utf-8') as infile:
        csv_reader = csv.DictReader(infile)
        
        with open('data/hebrew_english.csv', 'w', encoding='utf-8', newline='') as outfile:
            # Create CSV writer with headers
            writer = csv.writer(outfile)
            writer.writerow(['hebrew', 'english'])
            
            # Write each row with hebrew(transliteration) and english
            for row in csv_reader:
                hebrew_with_trans = f"{row['hebrew']}({row['transliteration']})"
                writer.writerow([hebrew_with_trans, row['english_translation']])

if __name__ == "__main__":
    process_csv()