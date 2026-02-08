
  # Log Entry: 07 Feb 2026

**Focus:** Building a resilient, modular tool for system process monitoring and logging using the `subprocess` library.

## Achievements

1. **Modularity:** Refactored initial script into distinct, reusable functions: `load_config()` for environment parameters and `subprocess_output()` for task execution.
    
2. **System Integration:** Implemented `subprocess.run()` to execute shell commands (`uptime -p`) safely within Python, capturing `stdout` as text strings.
    
3. **Refactoring Win:** Successfully moved from a "flat" script to a modular architecture with specific functions for configuration loading and system auditing.
    

## Reflections & Lessons Learned

- **The "False Friend":** **Object vs. String.** I initially tried to write the `CompletedProcess` object directly to a log file, resulting in a `TypeError`.
    
    - **Fix:** Accessed the `.stdout` attribute specifically to extract the string data returned by the system.
        
-  **Scope Awareness:** Realized that passing `sys.argv[1]` directly into functions ensures the script remains dynamic and not hardcoded to a single file path.
        

## Code Added

- `Scripts/Intermediate/pre_flight_check.py` - A robust system audit tool that parses JSON configs and logs system uptime to an external file.

## Next Steps

    
-  Explore the `platform` or `os` modules to identify hardware-specific details of the Dell 5400 (e.g., CPU architecture or Kernel version) to add to the audit report.
    
-  Develop a Python utility to automate the `git add`, `commit`, and `push` process for these daily logs to streamline the portfolio update cycle.
