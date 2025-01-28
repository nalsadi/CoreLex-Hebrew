from googletrans import Translator
import asyncio
import csv
import math
import time

async def translate_batch(translator, words):
    try:
        translations = await translator.translate(words, dest='en')
        return [translation.text for translation in translations]
    except Exception as e:
        print(f"Error translating batch: {e}")
        return ["ERROR" for _ in words]

async def translate_all_words(input_file, output_file, batch_size=10):
    translator = Translator()
    all_rows = []
    translated_count = 0
    
    # Read all words
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        all_rows = list(reader)
    
    total_rows = len(all_rows)
    total_batches = math.ceil(total_rows / batch_size)
    
    # Create/open output file with headers
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header + ['english_translation'])
        
        # Process in batches
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min((batch_num + 1) * batch_size, total_rows)
            batch = all_rows[start_idx:end_idx]
            
            # Extract Hebrew words from batch
            hebrew_words = [row[0] for row in batch]
            
            print(f"Translating batch {batch_num + 1}/{total_batches}")
            translations = await translate_batch(translator, hebrew_words)
            
            # Write batch results
            for row, translation in zip(batch, translations):
                writer.writerow(row + [translation])
            
            translated_count += len(batch)
            print(f"Progress: {translated_count}/{total_rows} words translated")
            
            # Small delay to avoid rate limiting
            time.sleep(1)

if __name__ == "__main__":
    input_file = 'data/top_80_percent_words.csv'
    output_file = 'data/translated_words.csv'
    asyncio.run(translate_all_words(input_file, output_file))