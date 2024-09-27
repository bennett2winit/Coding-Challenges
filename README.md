# Coding Challenges

## Coding Challenges Word Count (ccwc)

Recreated the word count GNU Utility. Pretty standard affair with for loops being the bread and butter. It did, however, serve as a great experience familiarizing myself with the system library in Python. Allowing for piping input served as a particular challenge as the sys.stdin takes files as well as pipes, resulting in exception handling being a necessity. Additionally the use of encoding served as the largest hangup for me. I assumed that treating each ASCII character as a byte would be sufficient, but was sorely mistaken.

Top 3 new things learned from this challenge:

1. Taking input using the sys library in Python
2. Exception handling - If statements for errors!
3. Handling UTF-8 encoding
