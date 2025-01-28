# Hebrew Corpus Analysis Tool

A Python-based tool for analyzing Hebrew text corpora with visualization capabilities. This tool helps identify word frequency distributions and analyze vocabulary coverage patterns in Hebrew texts.

## Features

- Recursively processes all .txt files in the directory structure
- Identifies words that constitute 80% of the corpus usage
- Generates detailed statistics including:
  - Total word count
  - Unique word count
  - Vocabulary richness metrics
  - Word frequency distributions
- Creates visualizations:
  - Word frequency distribution charts
  - Cumulative frequency curves
  - Coverage threshold indicators

## Installation

```bash
pip install matplotlib seaborn wordcloud numpy
```

## Usage

1. Place your Hebrew text files (.txt) in the directory
2. Run the script:
```bash
python compile_corpus.py
```

The script will generate:
- Detailed statistics in the console
- Visualizations in the `visualizations` directory

## Output Examples

### Console Output
```
Corpus Statistics:
================
Total words: 10,000
Unique words: 2,500
Vocabulary richness (unique/total): 25.00%
Number of words occupying 80% of the corpus: 500
Percentage of unique words needed for 80% coverage: 20.00%
```

### Generated Visualizations
- `frequency_distribution.png`: Bar chart showing word frequencies
- `cumulative_frequency.png`: Curve showing cumulative word coverage

## Data Sources

This tool can be used with various Hebrew corpora. Some recommended sources include:

1. [Hebrew Diacritized Text Corpus](https://github.com/elazarg/hebrew_diacritized)
   - Comprehensive collection of diacritized Hebrew texts
   - Includes biblical and modern Hebrew sources

2. [SVLM Hebrew Wikipedia Corpus](https://github.com/NLPH/SVLM-Hebrew-Wikipedia-Corpus/tree/master)
   - Large-scale corpus derived from Hebrew Wikipedia
   - Modern Hebrew usage patterns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- Hebrew diacritized corpus by [Erez Elazar](https://github.com/elazarg/hebrew_diacritized)
- SVLM Hebrew Wikipedia Corpus by [NLPH](https://github.com/NLPH)