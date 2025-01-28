import os
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
import pandas as pd
import unicodedata
import re

def remove_nikud(text):
    """Remove Hebrew diacritical marks (nikud) from text."""
    return ''.join(char for char in text if not unicodedata.combining(char))

def clean_text(text):
    """Clean and normalize Hebrew text."""
    # Remove nikud (vowel points)
    text = remove_nikud(text)
    
    # Replace Hebrew quotation marks with space
    text = text.replace('״', ' ').replace('"', ' ').replace('׳', ' ')
    
    # Remove punctuation (keeping Hebrew characters)
    text = re.sub(r'[^\u0590-\u05FF\s]', ' ', text)
    
    # Remove multiple spaces and strip
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def compile_corpus(root_directory):
    corpus = ""
    for subdir, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".txt"):
                with open(os.path.join(subdir, filename), 'r', encoding='utf-8') as file:
                    text = file.read()
                    # Clean text before adding to corpus
                    corpus += clean_text(text) + " "
    return corpus.strip()

def get_words_occupying_80_percent(corpus):
    words = corpus.split()
    total_count = len(words)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common()
    
    cumulative = np.cumsum([count for _, count in most_common_words])
    percentages = cumulative / total_count * 100
    words_for_80 = np.searchsorted(percentages, 80) + 1
    
    return words_for_80, most_common_words[:words_for_80]

def create_visualizations(corpus, top_words, output_dir="visualizations"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Word frequency distribution
    plt.figure(figsize=(15, 8))
    words, counts = zip(*top_words)
    plt.bar(range(len(counts)), counts)
    plt.title("Word Frequency Distribution")
    plt.xticks(range(len(words)), words, rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/frequency_distribution.png")
    plt.close()

    # Cumulative frequency curve
    plt.figure(figsize=(10, 6))
    cumsum = np.cumsum(counts)
    cumsum_percent = cumsum / cumsum[-1] * 100
    plt.plot(range(len(cumsum)), cumsum_percent)
    plt.axhline(y=80, color='r', linestyle='--', label='80% threshold')
    plt.title("Cumulative Word Frequency")
    plt.xlabel("Number of unique words")
    plt.ylabel("Cumulative percentage")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/cumulative_frequency.png")
    plt.close()


def show_stats(corpus, top_words):
    words = corpus.split()
    total_words = len(words)
    unique_words = len(set(words))
    words_for_80_percent = len(top_words)
    
    print(f"\nCorpus Statistics:")
    print(f"================")
    print(f"Total words: {total_words:,}")
    print(f"Unique words: {unique_words:,}")
    print(f"Vocabulary richness (unique/total): {(unique_words/total_words)*100:.2f}%")
    print(f"Number of words occupying 80% of the corpus: {words_for_80_percent:,}")
    print(f"Percentage of unique words needed for 80% coverage: {(words_for_80_percent/unique_words)*100:.2f}%")
    print(f"\nTop 10 most frequent words:")
    print("=======================")
    for word, count in top_words[:10]:
        percentage = (count/total_words)*100
        print(f"{word}: {count:,} ({percentage:.2f}%)")

def save_words_to_csv(top_words, output_dir="visualizations"):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.DataFrame(top_words, columns=['hebrew', 'count'])
    csv_path = os.path.join('data', 'top_80_percent_words.csv')
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')  # utf-8-sig for Hebrew support
    print(f"\nTop words have been saved to: {csv_path}")

if __name__ == "__main__":
    root_directory = os.getcwd()
    corpus = compile_corpus(root_directory)
    num_words, top_words = get_words_occupying_80_percent(corpus)
    show_stats(corpus, top_words)
    #create_visualizations(corpus, top_words)
    save_words_to_csv(top_words)
    print("\nVisualizations have been saved in the 'visualizations' directory.")
