## GC Content Counter

A simple Python script to calculate the GC content of a DNA sequence. The program validates the DNA sequence input and calculates the number of G and C bases, the total GC content, and the GC percentage.
Features :
- Validates DNA sequences to ensure only A, T, G, and C are entered.
- Counts the number of G and C bases.
- Calculates total GC content and GC percentage.
- Interactive and user-friendly input prompt.

## Development Process:
Here’s how I developed this project through multiple attempts and what I learned from each:
Initiative 1:
Built a basic GC content calculator.
Learnings: Taking input, looping through input, performing calculations, using built-in count() function.

Initiative 2:
Realized that user input may contain invalid letters, so input validation is needed.
Learnings: Looping through input, using not in to check invalid characters.

Initiative 3:
Detected that initial validation only checked letters individually but didn’t handle sequences containing extra invalid characters.
Learnings: Applied a while loop to repeatedly ask for input until it is fully valid.

Initiative 4:
Improved feedback to the user to make errors more observable in their input.
Learnings: Used formatted strings (f'') for clearer messages.

## Requirements
- Python 3.x  

## Usage
Clone the repository:
```bash
git clone https://github.com/Joyeeta007/GC_Content_Counter.git
cd GC_Content_Counter
python GC_Content_Counter.py
```
Enter your DNA sequence when prompted. The program will validate your input and calculate the GC content.

Example Output:

Enter DNA Sequence: ATGCGCAT
C count: 3
G count: 3
GC sum: 6
Sequence length: 8
GC Content: 75.00%
