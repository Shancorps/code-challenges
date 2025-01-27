# URL Shortener Challenge

## Objective
Create a simple URL shortener that converts long URLs into shorter, unique codes and maintains a record of the mappings.

## Requirements
1. Create two main functions:
   - `shorten_url(url: str) -> str`: Converts a long URL into a short code
   - `get_original_url(short_code: str) -> str`: Retrieves the original URL from a short code

2. Implementation requirements:
   - Store URL mappings in a simple dictionary
   - Generate short codes of 6 characters (letters and numbers)
   - Handle basic error cases (invalid URLs, non-existent codes)
   - Add simple input validation

3. Bonus points for:
   - Adding URL validation
   - Implementing persistent storage (JSON file)
   - Adding a simple command-line interface

## Evaluation Criteria
- Code organization and readability
- Error handling
- Input validation
- Documentation and comments
- Basic testing
