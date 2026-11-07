# Mission 05 – Numbers & Data

## Objective

Understand how computers represent numbers using different number systems and learn how to convert values between binary, decimal, octal, and hexadecimal systems.

## 1. Number Systems

A number system is a way of representing numbers using a set of digits.

| Number System | Base | Digits |
|---|---:|---|
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F |

## 2. Binary Number System

Binary is a base-2 number system used internally by computers.

Example:

```text
1010₂ = 10₁₀
```

Calculation:

```text
1 × 8 + 0 × 4 + 1 × 2 + 0 × 1 = 10
```

## 3. Decimal Number System

Decimal is the base-10 number system commonly used in everyday calculations.

Example:

```text
25₁₀ = 11001₂
```

## 4. Octal Number System

Octal uses eight digits, from 0 to 7.

Example:

```text
17₈ = 15₁₀
```

## 5. Hexadecimal Number System

Hexadecimal uses sixteen symbols: 0–9 and A–F.

| Decimal | Hexadecimal |
|---:|---|
| 10 | A |
| 11 | B |
| 12 | C |
| 13 | D |
| 14 | E |
| 15 | F |

Example:

```text
1A₁₆ = 26₁₀
```

## 6. Number Conversion in Python

Python provides built-in functions for converting numbers between different bases.

| Function | Purpose |
|---|---|
| `bin()` | Convert decimal to binary |
| `oct()` | Convert decimal to octal |
| `hex()` | Convert decimal to hexadecimal |
| `int(value, base)` | Convert a number from a specified base to decimal |

Example:

```python
number = 10

print(bin(number))
print(oct(number))
print(hex(number))
```

Output:

```text
0b1010
0o12
0xa
```

## 7. Practical Work

Created a Python program named `number_converter.py` to practise number-system conversions.

### Program Location

`mission-05-numbers-data/number_converter.py`

## Learning Outcome

Understood binary, decimal, octal, and hexadecimal number systems and learned how to convert values between different bases using mathematical methods and Python functions.
