"""
Script: Server Inventory Audit
------------------------------
Parses a server inventory in JSON format to identify and log infrastructure 
issues. It filters for servers that are not in an 'active' state and 
generates an incident report.

Usage: python3 audit.py
Context: DWP DevOps Portfolio
"""

import json

def audit_py():
"""
    Reads 'server_inventory.json', filters for non-active statuses, and 
    writes results to 'issues.txt'.

    Logic:
    1. Safe-opens the JSON file using a 'with' context manager.
    2. Loads data into a list of dictionaries.
    3. Iterates through the list to filter servers where status != 'active'.
    4. Writes the 'hostname: status' pair to 'issues.txt'.

    Args:
        None (Uses hardcoded filenames for this exercise).

    Returns:
        None (Outputs directly to a file).
    
    Raises:
        FileNotFoundError: If the input JSON file is missing.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    json_dict = {}
    try:
        with open("server_inventory.json", "r") as file:
            data = json.load(file)
            for server in data:
                if server["status"] != "active":
                    hostname = server["hostname"]
                    status = server["status"]
                    json_dict[hostname] = status
                else:
                    pass
        with open("issues.text", "w") as destination:
            for hostname, status in json_dict.items():
                destination.write(f"{hostname}: {status}\n")

    except FileNotFoundError:
        print("Error: The file 'server_inventory.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {e}")


if __name__ == "__main__":
    audit_py()
