"""
report_generator.py - HTML report generation
"""


def create_html_report(filename, summary, column_analyses):
    """
    Generate an HTML report from analysis data.
    
    Args:
        filename (str): Where to save the HTML
        summary (dict): Summary data
        column_analyses (list): List of column analysis dicts
    """
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Analysis Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                max-width: 1000px;
                margin: 0 auto;
            }}
            h1 {{
                color: #333;
                border-bottom: 2px solid #007bff;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #555;
                margin-top: 30px;
            }}
            .summary {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                margin: 20px 0;
            }}
            .stat {{
                background-color: #f9f9f9;
                padding: 15px;
                border-left: 4px solid #007bff;
            }}
            .stat-value {{
                font-size: 24px;
                font-weight: bold;
                color: #007bff;
            }}
            .stat-label {{
                color: #666;
                font-size: 14px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #007bff;
                color: white;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Data Analysis Report</h1>
            
            <h2>Summary</h2>
            <div class="summary">
                <div class="stat">
                    <div class="stat-label">Total Rows</div>
                    <div class="stat-value">{summary['total_rows']}</div>
                </div>
                <div class="stat">
                    <div class="stat-label">Total Columns</div>
                    <div class="stat-value">{summary['total_columns']}</div>
                </div>
            </div>
            
            <h2>Column Analysis</h2>
    """
    
    # Add analysis for each column
    for analysis in column_analyses:
        html_content += f"""
            <h3>{analysis['column']}</h3>
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Count</td>
                    <td>{analysis['count']}</td>
                </tr>
                <tr>
                    <td>Unique Values</td>
                    <td>{analysis['unique_count']}</td>
                </tr>
        """
        
        if analysis['is_numeric']:
            html_content += f"""
                <tr>
                    <td>Sum</td>
                    <td>{analysis['sum']:.2f}</td>
                </tr>
                <tr>
                    <td>Average</td>
                    <td>{analysis['average']:.2f}</td>
                </tr>
                <tr>
                    <td>Min</td>
                    <td>{analysis['min']:.2f}</td>
                </tr>
                <tr>
                    <td>Max</td>
                    <td>{analysis['max']:.2f}</td>
                </tr>
            """
        
        html_content += """
            </table>
        """
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    # Write to file
    try:
        with open(filename, 'w') as f:
            f.write(html_content)
        print(f"Report saved to '{filename}'")
    except Exception as e:
        print(f"Error saving report: {e}")