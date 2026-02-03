# Log Entry: 03 Feb 2026

**Focus:** JSON Parsing, Data Structures & Pythonic Syntax

## Achievements
1. **JSON Parsing:** Mastered the transition from "Text Parsing" (Regex) to "Structured Data" using the `json` standard library.
2. **Refactoring Win:** Refactored a standard `for` loop into a **Dictionary Comprehension** (`{k:v for x in data if y}`), reducing code verbosity while maintaining readability.
3. **Engineering Standard:** Implemented robust Error Handling (`try/except`) to catch `FileNotFoundError` and `JSONDecodeError` during file operations.

## Reflections & Lessons Learned
* **The "False Friend" (Regex Trap):** I initially tried to parse JSON using `re.search` (treating it as a raw string).
    * *Fix:* Realized that `json.load()` converts the file directly into Python objects (Lists and Dictionaries), allowing direct key access (`server["status"]`).
* **The "Shape" of Data:** I encountered a crash (`AttributeError: 'list' object has no attribute 'items'`) because I confused the JSON root (a **List** `[]`) with a **Dictionary** (`{}`).
    * *Fix:* Adjusted the loop to iterate through the List first (`for server in data`), then operate on the Dictionary items inside.

## Code Added
* `Scripts/Intermediate/audit.py` - Automates the identification of non-active servers from an inventory file and logs them to an incident report.

## Next Steps
* Move from "Filtering" to "Aggregation" (Summing uptime hours by Role).
* Explore standard library tools for counting without importing `Counter` or `Pandas`.
