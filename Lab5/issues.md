| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| Weak MD5 hash (B324) | High Security | 44 | Using hashlib.md5 is insecure and weak for generating hashes | Replace hashlib.md5 with hashlib.sha256 |
| Binding to all interfaces (B104) | Medium Security | 4 | Hardcoding 0.0.0.0 exposes the service to all network interfaces | Change the host address to 127.0.0.1 |
| Hardcoded password (B105) | Low Security | 6 | Storing the moderator password directly as a plain text string in the code | Load the password from environment variables using os.getenv |
| Insecure random generator (B311) | Low Security | 39 | Standard random module is not cryptographically secure | Import the secrets module and use secrets.choice instead |
| Unnecessary else after return (R1705) | Code Quality | 29 | Using an else block right after an if block that already returns a value | Remove the else keyword and unindent the final return statement |
| Using range and len in loop (C0200) | Code Quality | 49 | Looping with range(len(titles)) instead of iterating directly | Use enumerate(titles) to get both the index and the movie title |
| Missing docstrings and constant naming (C0114, C0116, C0103) | Style and Quality | 1, 4, 5, 6 | Missing module and function docstrings and lowercase global constants | Add docstrings to the file and functions and rename constants to uppercase |
| Missing blank lines and spacing (E302, E225, E231) | Style | Multiple | Functions only had one blank line before them and operators lacked spaces | Add two blank lines before each function and fix spacing around operators |
