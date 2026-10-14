1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were the Flake8 style warnings and the Pylint docstring warnings[cite: 1]. Adding two blank lines between functions, fixing spaces around operators, and writing short descriptions for each function was very straightforward and did not risk breaking how the program runs. The hardest part was making sure the security and logic changes did not alter the expected output of the demo, such as switching from range and len to enumerate in print_all_reviews and updating the hashing and random functions while keeping the rest of the code working the same way.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, Bandit reported a Couple of warnings that act like false positives in the context of this small movie rating script[cite: 2]. For example, Bandit flagged random.choice in pick_featured (B311) because the random module is not cryptographically secure. Since the function is only picking a random movie to feature on a board and not generating passwords or security tokens, using standard random was not a real security threat, even though changing it to secrets.choice cleared the warning. Similarly, using MD5 in review_id was only creating a short 10 character display ID rather than storing sensitive data.

3. How would you integrate static analysis tools into your actual software development workflow?

I would set up Flake8 and Pylint inside my code editor so that formatting mistakes and code quality warnings show up right away while I am typing[cite: 1]. I would also add Pylint, Flake8, and Bandit to pre commit hooks and a continuous integration pipeline like GitHub Actions[cite: 1, 2]. That way, every time someone makes a commit or opens a pull request, the tools run automatically and block code from being merged if the Pylint score drops below 9.5 or if Bandit finds any security issues[cite: 2, 3].

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code is much easier to read now because of consistent spacing, uppercase constant names, and clear docstrings on every function. Removing the unnecessary else block and switching to enumerate made the functions shorter and cleaner. On the security side, loading the moderator password through os.getenv, binding the host to 127.0.0.1, and switching to sha256 removed bad habits that could cause real vulnerabilities in a larger application. The Pylint score went all the way up to 10.00 out of 10, and both Bandit and Flake8 reported zero issues[cite: 3].
