# Mission 5 — Numbers, Python and Text Encoding

### Task 5.1 — Convert numbers manually

**1. Convert decimal 13 into binary.**

13 = 8 + 4 + 1

Therefore:

13 (decimal) = 1101 (binary)

**2. Convert decimal 25 into binary.**

25 = 16 + 8 + 1

Therefore:

25 (decimal) = 11001 (binary)

**3. Convert binary 1010 into decimal.**

= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)

= 8 + 0 + 2 + 0

= 10

**4. Convert binary 1101 into decimal.**

= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)

= 8 + 4 + 0 + 1

= 13

**5. Convert hexadecimal A into decimal.**

A = 10

**6. Convert hexadecimal 1F into decimal.**

= (1 × 16) + (15 × 1)

= 16 + 15

= 31

**7. Convert binary 1111 into hexadecimal.**

1111 in binary = 15 in decimal.

15 in hexadecimal = F.

Therefore, the answer is F.

### Task 5.2 — Verify using Python

I used Python's built-in functions to verify my manual calculations.

| Python expression | Result |
|---|---|
| `bin(13)` | `0b1101` |
| `bin(25)` | `0b11001` |
| `int('1010', 2)` | `10` |
| `int('1101', 2)` | `13` |
| `int('A', 16)` | `10` |
| `int('1F', 16)` | `31` |
| `hex(15)` | `0xf` |

The Python results matched my manual calculations.

### Task 5.3 — Build a number converter

I created a Python program named `number_converter.py`.

The program accepts a decimal number from the user and converts it into binary and hexadecimal.

### Task 5.4 — Understand text encoding

**1. What is the ASCII decimal code for uppercase A?**

65.

**2. What is the ASCII decimal code for lowercase a?**

97.

**3. Why does a computer need a text encoding standard?**

A computer stores information in numerical form. Text encoding standards assign numerical representations to characters so that computers can store, process and display text correctly.

**4. Give an example of a character outside basic ASCII.**

₹ — Indian Rupee symbol.

Unicode supports characters from many languages and symbol sets, including characters that are not included in basic ASCII.

## 3. Commands / tools used

- `python3` — Runs Python programs.
- `input()` — Accepts user input.
- `int()` — Converts values into integers.
- `bin()` — Converts integers into binary.
- `hex()` — Converts integers into hexadecimal.
- `print()` — Displays results.
- `if/else` — Performs conditional checks.

