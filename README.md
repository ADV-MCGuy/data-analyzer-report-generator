# Data Analyzer & Report Generator

Analyze CSV data and generate beautiful HTML reports with summaries and insights.

## Features
- Load and analyze CSV data
- Calculate summaries (counts, totals, averages)
- Group data by columns
- Generate HTML reports

## Usage

```bash
python src/main.py data/input.csv
```

This generates `data/input_report.html` that you can open in your browser.

## Project Structure
- `src/analyzer.py` — Data analysis functions
- `src/report_generator.py` — HTML generation
- `src/main.py` — Entry point
- `data/` — Input CSV and output HTML files

## Example Data

See `data/sample.csv` for example input format.
