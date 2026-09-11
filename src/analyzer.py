"""
analyzer.py - Data analysis functions
"""


def load_csv(filepath):
    """Load CSV and return headers + rows."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            return None, None
        
        headers = lines[0].strip().split(',')
        rows = [line.strip().split(',') for line in lines[1:]]
        
        return headers, rows
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, None


def get_summary(headers, rows):
    """
    Get basic summary statistics.
    
    Returns:
        dict: Summary with total rows, columns, etc.
    """
    if rows is None:
        return None
    
    summary = {
        'total_rows': len(rows),
        'total_columns': len(headers),
        'columns': headers
    }
    
    return summary


def get_column_analysis(headers, rows, column_name):
    """
    Analyze a specific column.
    
    For numeric columns: count, sum, average
    For text columns: count, unique values
    
    Returns:
        dict: Analysis results
    """
    if rows is None or column_name not in headers:
        return None
    
    col_index = headers.index(column_name)
    values = [row[col_index] for row in rows]
    
    analysis = {
        'column': column_name,
        'count': len(values),
        'unique_count': len(set(values))
    }
    
    # Try to analyze as numeric
    try:
        numeric_values = [float(v) for v in values]
        analysis['sum'] = sum(numeric_values)
        analysis['average'] = sum(numeric_values) / len(numeric_values)
        analysis['min'] = min(numeric_values)
        analysis['max'] = max(numeric_values)
        analysis['is_numeric'] = True
    except ValueError:
        analysis['is_numeric'] = False
        analysis['unique_values'] = list(set(values))[:10]  # Show first 10
    
    return analysis

def group_by(headers, rows, group_column, numeric_column=None):
    """
    Group rows by a column and optionally calculate statistics.
    
    Args:
        headers (list): Column headers
        rows (list): Data rows
        group_column (str): Column name to group by
        numeric_column (str): Optional numeric column to sum/average
    
    Returns:
        dict: Grouped data with summaries
    """
    if rows is None or group_column not in headers:
        return {}

    group_col_index = headers.index(group_column)
    numeric_col_index = headers.index(numeric_column) if numeric_column else None

    groups = {}
    
    # First pass: group rows and calculate totals
    for row in rows:
        group_key = row[group_col_index]
        
        if group_key not in groups:
            groups[group_key] = {
                'count': 0,
                'items': [],
                'total': 0,
                'average': 0
            }
        
        groups[group_key]['count'] += 1
        groups[group_key]['items'].append(row)
        
        # Add to total if numeric_column is provided
        if numeric_col_index is not None:
            groups[group_key]['total'] += float(row[numeric_col_index])
    
    # Second pass: calculate averages
    for group_key in groups:
        if numeric_col_index is not None and groups[group_key]['count'] > 0:
            groups[group_key]['average'] = groups[group_key]['total'] / groups[group_key]['count']
    
    return groups