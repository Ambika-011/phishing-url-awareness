# Test Results

Python version used:  3.15.0 | Operating system:Windows 11  | Date: 2026-11-04

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain. / Uses HTTP. HTTPS alone does not prove trust. / REVIEW CAREFULLY: 2 warning sign(s) found. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully. / Uses HTTP. HTTPS alone does not prove trust. / REVIEW CAREFULLY: 2 warning sign(s) found. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. / REVIEW CAREFULLY: 1 warning sign(s) found. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. / REVIEW CAREFULLY: 1 warning sign(s) found. | PASS |

## Bonus checks

| Input | Actual result |
|-------|---------------|
| (empty, just Enter) | No URL entered. |
| www.example.com | Uses HTTP. HTTPS alone does not prove trust. |
| https://secure-login.example.invalid | No listed warning signs found. A tricky name can still slip through. |
| http://[bad | This text is not a valid URL format. (no crash, thanks to Improvement C) |

## Notes


While testing this project, I learned that a URL can be checked just by reading its text, without ever opening it. The most interesting thing for me was that a link with no warning signs, like https://secure-login.example.invalid, still isn't proven safe, because my tool only checks six clues.

What surprised me was that typing www.example.com without http:// still showed the HTTP warning, because the program adds http:// by itself when it is missing. I also had a few errors at first because my terminal was in the wrong folder, and I fixed that by checking the folder with dir and moving into the right one with cd.
