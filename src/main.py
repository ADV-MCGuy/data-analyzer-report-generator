"""
main.py - Entry point for data analyzer
"""

import sys
from analyzer import load_csv, get_summary, get_column_analysis
from report_generator import create_html_report


def main():
    """Main orchestration function."""
    
    # Handle command-line arguments (same pattern as Project 1)
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter the input CSV file path: ")
    
    # Generate output filename
    output_file = input_file.replace('.csv', '_report.html')
    
    print("Analyzing data...")
    
    # Load data
    headers, rows = load_csv(input_file)
    if headers is None:
        return
    
    print(f"Loaded {len(rows)} rows with {len(headers)} columns")
    
    # Get summary
    summary = get_summary(headers, rows)
    
    # Analyze each column
    column_analyses = []
    for header in headers:
        analysis = get_column_analysis(headers, rows, header)
        if analysis:
            column_analyses.append(analysis)
            print(f"  ✓ Analyzed column: {header}")
    
    # Generate report
    create_html_report(output_file, summary, column_analyses)
    
    print("Done!")


if __name__ == '__main__':
    main()