"""
Script Name: audit_tool.py
Description: Performs a modular audit of server inventory based on an external configuration file.
Usage: python3 audit_tool.py
Context: DWP Portfolio 2026
"""

import json
import sys

def get_config():
    """
    Finds the correct configuration string for the auditing process.

    Description:
        Normalizes and parses the 'app_config.txt' file to extract the target application.

    Logic:
        1. Opens 'app_config.txt' in read mode.
        2. Normalizes separators by replacing colons with equals signs.
        3. Splits the string into a list and verifies content length.
        4. Strips whitespace and returns the target application name.

    Args:
        None

    Returns:
        str: The name of the application to audit (e.g., 'auth').

    Raises:
        FileNotFoundError: If 'app_config.txt' does not exist.
        IndexError: If the config file is missing the required value or separator.
    """
    try:
        with open("app_config.txt", "r") as text_file:
            dirty_file = text_file.read()
            clean_file = dirty_file.replace(":", "=")
            target_split = clean_file.split("=")
            app = target_split[1].strip()
            return app
    except FileNotFoundError:
        print("Error: The file 'app_config.txt' was not found.")
        sys.exit(1)
    except IndexError:
        print("Error: Configuration file is empty or missing a valid separator.")
        sys.exit(1)

def run_audit(app):
    """
    Creates an audit report for entries matching the target application.

    Description:
        Analyzes inventory data and logs the results to both JSON and text formats.

    Logic:
        1. Loads server data from 'inventory.json' into Python objects.
        2. Iterates through servers to validate IP formatting and app membership.
        3. Aggregates matched data and audit status messages into memory.
        4. Appends standardized status lines to 'devops_audit.log'.
        5. Dumps final match results into a structured 'audit_report.json'.

    Args:
        app (str): The name of the application to search for in the inventory.

    Returns:
        None

    Raises:
        FileNotFoundError: If 'inventory.json' is missing from the working directory.
        json.JSONDecodeError: If the inventory data contains syntax errors.
    """
    try:
        with open("inventory.json", "r") as json_file:
            parse_data = json.load(json_file)
            audit_list = []
            matches = []
            
            for server in parse_data:
                audit_list.append(f"Auditing server {server.get('server_id')}...")
                
                # Validation check for malformed system data
                if "malformed" in server.get("ip", ""):
                    audit_list.append(f"WARNING: Malformed IP detected for server: {server.get('server_id')}")
                elif app in server.get("apps", []):
                    matches.append({"server_id": server["server_id"], "ip": server["ip"]})
                    audit_list.append(f"Found match: {server['server_id']}")
                else:
                    audit_list.append(f"Match not found: {server['server_id']}")

        with open("devops_audit.log", "w") as log:
            for line in audit_list:
                log.write(f"{line}\n")

        with open("audit_report.json", "w") as report:
            json.dump(matches, report, indent=4)

    except FileNotFoundError:
        print("Error: The file 'inventory.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {e}")

if __name__ == "__main__":
    target_app = get_config()
    run_audit(target_app))
