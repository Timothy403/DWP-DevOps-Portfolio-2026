# Log Entry: 06 Feb 2026

**Focus:** Building a resilient, modular auditing tool for system configurations and inventory data.

## Achievements

1. **Modularity:** Refactored a monolithic script into distinct, reusable functions: `get_config()` for environmental parameter handling and `run_audit()` for data processing.
    
2. **Defensive Engineering:** Implemented multi-layered error handling, including `IndexError` to catch malformed config files and `sys.exit()` to prevent "downstream" crashes when critical dependencies fail.
    
3. **Flexible Parsing:** Developed a normalization strategy using `.replace()` and `.strip()` to ensure the script remains functional even if configuration separators ( `=` vs `:` ) vary across environments.
    

## Reflections & Lessons Learned

- **The "False Friend" (Nested I/O):** I initially tried to open multiple files (logs and reports) inside my main processing loop.
    
    - _Fix:_ Realized this causes unnecessary overhead and risks data corruption. Optimized by collecting audit results into memory first (`audit_list`, `matches`), then performing single-write operations at the end.
        
- **Scope Awareness:** Moving logic into functions introduced "Variable Scope" challenges where `app` was no longer globally available.
    
    - _Fix:_ Mastered the `return` / argument pattern to pass data cleanly between independent code blocks.
        

## Code Added

- `Scripts/Intermediate/audit_tool.py` - A modular Python script that parses local configuration and performs an automated server audit.
    

## Next Steps

- Transition from file-based auditing to **Automating System Processes** (monitoring CPU/Memory usage).
    
- Explore **Process Management** using the `subprocess` library to automate shell commands.
