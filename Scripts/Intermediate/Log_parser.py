import re

def tally_statuses(filepath):
    """
    Parses a server log file to count status codes (INFO, WARN, ERROR).
    
    Logic:
    1. Opens file safely using 'with' context manager.
    2. Iterates line-by-line (memory efficient).
    3. Uses Regex r'^(\w+):' to capture the status before the colon.
    4. skips invalid lines using a guard clause.
    
    Args:
        filepath (str): Path to the log file.
        
    Returns:
        dict: Frequency count of statuses (e.g., {'INFO': 2, 'ERROR': 1})
    """
    status_count = {}
    
    with open(filepath, "r") as file:
        for line in file:
            # Match word at start of line followed by colon
            match = re.search(r'^(\w+):', line)
            
            # Guard Clause: Skip lines that don't match pattern
            if not match:
                continue
            
            status = match.group(1)
            status_count[status] = status_count.get(status, 0) + 1
            
    return status_count
