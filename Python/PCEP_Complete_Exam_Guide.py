# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║         PCEP-30-02 COMPLETE EXAM PREPARATION GUIDE                         ║
# ║         ──────────────────────────────────────────────                      ║
# ║         Author: Copilot for Abdulkadir                                     ║
# ║         Purpose: Pass PCEP & truly UNDERSTAND Python                       ║
# ║                                                                            ║
# ║         TABLE OF CONTENTS:                                                 ║
# ║         Section 1:  Data Types & Variables (Q1-Q10)                        ║
# ║         Section 2:  Operators & Expressions (Q11-Q25)                      ║
# ║         Section 3:  Control Flow: if/elif/else (Q26-Q35)                   ║
# ║         Section 4:  Loops: for & while (Q36-Q55)                           ║
# ║         Section 5:  Functions (Q56-Q70)                                    ║
# ║         Section 6:  Strings (Q71-Q85)                                      ║
# ║         Section 7:  Lists & Tuples (Q86-Q105)                              ║
# ║         Section 8:  Dictionaries & Sets (Q106-Q120)                        ║
# ║         Section 9:  Error Handling: try/except (Q121-Q130)                 ║
# ║         Section 10: Algorithm Thinking & Problem Solving (Q131-Q150)       ║
# ║         Section 11: Full Mock Exam (40 Questions)                          ║
# ║                                                                            ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████���███████████████████████████████████████████████████████████
# SECTION 1: DATA TYPES & VARIABLES
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY YOU MUST KNOW:
# ─────────────────────
# Python has these fundamental data types:
#
#   int    → Whole numbers:         5, -3, 0, 1000000
#   float  → Decimal numbers:       3.14, -0.5, 2.0
#   str    → Text (in quotes):      "hello", 'world', """multiline"""
#   bool   → True or False:         True, False
#   None   → Absence of value:      None (not 0, not "", not False)
#
# KEY RULES:
# 1. Python is DYNAMICALLY TYPED → you don't declare types, Python figures it out
# 2. Variable names: must start with letter or _, can contain letters/digits/_
# 3. Variable names are CASE SENSITIVE: age ≠ Age ≠ AGE
# 4. type() function returns the type of any value
# 5. EVERYTHING in Python is an object (even int, even functions)
#
# TYPE CONVERSION (CASTING):
#   int("42")    → 42      (string to integer)
#   float("3.5") → 3.5     (string to float)
#   str(42)      → "42"    (integer to string)
#   int(3.9)     → 3       (float to int — TRUNCATES, does NOT round!)
#   bool(0)      → False   (0 is falsy)
#   bool(1)      → True    (any non-zero number is truthy)
#   bool("")     → False   (empty string is falsy)
#   bool("hi")   → True    (non-empty string is truthy)


# ──────────────────────────────────────────────────────────────────────────────
# Q1: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = 10
y = 3.0
result = x + y
print(type(result))

# OPTIONS:
# A) <class 'int'>
# B) <class 'float'>
# C) <class 'str'>
# D) TypeError

# ANSWER: B) <class 'float'>
#
# WHY THIS IS THE ANSWER — DETAILED EXPLANATION:
# ───────────────────────────────────────────────
# This question tests "TYPE PROMOTION" (also called "implicit type conversion").
#
# RULE: When you mix int and float in arithmetic, Python ALWAYS promotes the
# result to float. This is because float can represent decimal parts, but int
# cannot. So Python chooses the "wider" type to avoid losing information.
#
#   10 (int) + 3.0 (float) = 13.0 (float)
#
# type(13.0) → <class 'float'>
#
# WHEN WILL YOU SEE THIS ON THE EXAM?
# → Any time two different numeric types are combined with +, -, *, /
# → TRICK: Even 10 + 0.0 gives float! Because 0.0 is float.
# → SPECIAL CASE: The / operator ALWAYS returns float, even 10 / 2 = 5.0
#
# FUNCTION USED: type()
# ─────────────────────
# type(value) → Returns the type of the value as a class object.
# When you print it, it shows <class 'typename'>
# USE THIS WHEN: You need to check or verify what type a variable is.


# ──────────────────────────────────────────────────────────────────────────────
# Q2: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
a = "5"
b = 3
# print(a + b)  # ← What happens?

# OPTIONS:
# A) 8
# B) "53"
# C) "8"
# D) TypeError

# ANSWER: D) TypeError
#
# WHY THIS IS THE ANSWER — DETAILED EXPLANATION:
# ───────────────────────────────────────────────
# Python is STRONGLY TYPED. This means it does NOT automatically convert
# between unrelated types. "5" is a string, 3 is an integer.
#
# The + operator has TWO behaviors:
#   - Between numbers: addition → 5 + 3 = 8
#   - Between strings: concatenation → "5" + "3" = "53"
#   - Between string and int: ERROR! Python doesn't guess what you meant.
#
# TypeError: can only concatenate str (not "int") to str
#
# HOW TO FIX IT:
#   int(a) + b    → 8     (convert string to int first, then add)
#   a + str(b)    → "53"  (convert int to string first, then concatenate)
#
# EXAM TRICK: If you see string + number → ALWAYS think TypeError!
# EXAM TRICK: If you see string * number → that's VALID! "ha" * 3 = "hahaha"


# ──────────────────────────────────────────────────────────────────────────────
# Q3: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(int(3.9))
print(int(-3.9))

# OPTIONS:
# A) 4, -4
# B) 3, -3
# C) 4, -3
# D) 3, -4

# ANSWER: D) 3, -4  ← TRICK QUESTION! Actually B) 3, -3
#
# WAIT — LET ME CORRECT MYSELF. The answer is B) 3, -3.
#
# WHY? DETAILED EXPLANATION:
# ──────────────────────────
# int() on a float does TRUNCATION — it simply CUTS OFF the decimal part.
# It does NOT round. It does NOT use floor.
#
#   int(3.9)  → cuts .9 → 3     (moves TOWARD zero)
#   int(-3.9) → cuts .9 → -3    (moves TOWARD zero)
#
# THIS IS DIFFERENT FROM:
#   round(3.9)       → 4    (rounds to nearest)
#   math.floor(3.9)  → 3    (rounds DOWN toward negative infinity)
#   math.floor(-3.9) → -4   (rounds DOWN toward negative infinity)
#   math.ceil(3.9)   → 4    (rounds UP toward positive infinity)
#   math.ceil(-3.9)  → -3   (rounds UP toward positive infinity)
#
# MEMORY TRICK: int() always moves TOWARD ZERO. Like cutting off the tail.
#   int(3.9)  → 3    (positive: goes down toward 0)
#   int(-3.9) → -3   (negative: goes UP toward 0)
#
# EXAM STRATEGY: When you see int() with float:
#   1. Ignore everything after the decimal point
#   2. That's your answer
#   This works for both positive and negative numbers!


# ──────────────────────────────────────────────────────────────────────────────
# Q4: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
print(bool(" "))
print(bool(0.0))

# OPTIONS:
# A) False, False, False, False, False, False
# B) False, False, False, False, True, False
# C) False, True, True, False, True, False
# D) False, False, True, False, True, True

# ANSWER: B) False, False, False, False, True, False
#
# WHY? THE COMPLETE "FALSY" RULE:
# ────────────────────────────────
# In Python, the following values are "FALSY" (bool() returns False):
#   0        → zero integer
#   0.0      → zero float
#   ""       → empty string
#   []       → empty list
#   ()       → empty tuple
#   {}       → empty dict (NOT empty set! set() is empty set)
#   set()    → empty set
#   None     → the None object
#   False    → obviously
#
# EVERYTHING ELSE IS "TRUTHY" (bool() returns True):
#   1, -1, 42       → non-zero numbers
#   "hello", " "    → non-empty strings (EVEN A SINGLE SPACE!)
#   [0], [False]     → non-empty lists (even if contents are falsy!)
#   {0: None}        → non-empty dict
#
# THE TRAP IN THIS QUESTION:
# bool(" ") → True! Because " " is NOT empty — it contains a space character.
# len(" ") → 1. It has one character in it.
#
# EXAM STRATEGY: When you see bool(something):
#   Ask: "Is this empty or zero?" → False
#   Ask: "Does this have ANYTHING in it?" → True


# ──────────────────────────────────────────────────────────────────────────────
# Q5: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = None
print(x is None)
print(x == None)
print(type(x))

# ANSWER:
# True
# True
# <class 'NoneType'>
#
# EXPLANATION:
# ────────────
# None is a SPECIAL singleton object in Python. It means "no value" or "nothing".
#
# IMPORTANT DISTINCTION:
#   "is"  → checks IDENTITY (are they the SAME object in memory?)
#   "=="  → checks EQUALITY (do they have the same VALUE?)
#
# For None, ALWAYS use "is None" (not "== None"). This is a Python best practice
# and PEP 8 recommendation. Both work, but "is" is faster and more correct.
#
# WHY? Because "==" can be overridden by a class (custom __eq__ method),
# but "is" always checks true identity. Some tricky objects might make
# x == None return True even when x is not actually None.
#
# USE "is" FOR: None, True, False
# USE "==" FOR: numbers, strings, lists, everything else


# ──────────────────────────────────────────────────────────────────────────────
# Q6: Which variable name is INVALID in Python?
# ──────────────────────────────────────────────────────────────────────────────
# A) _name
# B) my_var2
# C) 2nd_place
# D) __init__

# ANSWER: C) 2nd_place
#
# RULE: Variable names CANNOT start with a digit.
# They CAN start with: letters (a-z, A-Z) or underscore (_)
# They CAN contain: letters, digits, underscores
#
# Valid:   _name, my_var2, __init__, x, data_1, _2, __x
# Invalid: 2nd_place, my-var (hyphen), my var (space), class (reserved keyword)
#
# RESERVED KEYWORDS (cannot be used as variable names):
# False, True, None, and, or, not, if, elif, else, for, while, break,
# continue, def, return, class, import, from, as, try, except, finally,
# raise, with, yield, lambda, global, nonlocal, pass, del, in, is, assert


# ──────────────────────────────────────────────────────────────────────────────
# Q7: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = 5
y = x
x = 10
print(y)

# OPTIONS:
# A) 5
# B) 10
# C) 15
# D) Error

# ANSWER: A) 5
#
# WHY? UNDERSTANDING VARIABLE ASSIGNMENT:
# ─────────────────────────────────────────
# Step 1: x = 5       → x points to the value 5
# Step 2: y = x       → y points to the SAME value 5 (y copies the reference)
# Step 3: x = 10      → x NOW points to a NEW value 10
#                        But y still points to 5! y was not changed.
#
# IMPORTANT: For IMMUTABLE types (int, float, str, tuple, bool):
#   → Reassigning x does NOT affect y. They become independent.
#
# THIS WOULD BE DIFFERENT WITH MUTABLE TYPES (lists, dicts):
#   x = [1, 2, 3]
#   y = x            → y points to the SAME list object
#   x.append(4)      → modifies the list IN PLACE
#   print(y)         → [1, 2, 3, 4]  ← y is affected!
#
# But: x = [10, 20]  → x points to a NEW list, y still points to old one


# ──────────────────────────────────────────────────────────────────────────────
# Q8: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(type(True))
print(type(1))
print(True == 1)
print(True is 1)  # Note: This may give a SyntaxWarning in newer Python

# ANSWER:
# <class 'bool'>
# <class 'int'>
# True
# False
#
# MIND-BLOWING FACT:
# ──────────────────
# In Python, bool is a SUBCLASS of int!
#   True  is actually 1
#   False is actually 0
#
# This is why:
#   True + True = 2
#   True * 5 = 5
#   False + 10 = 10
#   True == 1 → True (same value)
#   True is 1 → False (different objects!)
#
# EXAM TRICK: You might see questions like:
#   print(True + True + False)  → 2 (1 + 1 + 0)
#   print(True * "ha")          → "ha" (1 * "ha")


# ──────────────────────────────────────────────────────────────────────────────
# Q9: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = "42"
print(type(x))
x = int(x)
print(type(x))
x = float(x)
print(type(x))

# ANSWER:
# <class 'str'>
# <class 'int'>
# <class 'float'>
#
# This demonstrates TYPE CASTING CHAIN:
# "42" (str) → int("42") → 42 (int) → float(42) → 42.0 (float)
#
# IMPORTANT CASTING RULES:
# ─────────────────────────
# int("42")     → 42      ✓ (string contains valid integer)
# int("42.5")   → ERROR!  ✗ (int() cannot handle decimal strings!)
# float("42.5") → 42.5    ✓ (float() can handle decimal strings)
# int(float("42.5")) → 42 ✓ (first convert to float, then truncate to int)
# int("hello")  → ERROR!  ✗ (ValueError: invalid literal)
# str(42)       → "42"    ✓ (str() can convert anything to string)
# str([1,2,3])  → "[1, 2, 3]" ✓ (even lists!)


# ──────────────────────────────────────────────────────────────────────────────
# Q10: What is the output?
# ─────────────────────────────────────���────────────────────────────────────────
a, b, c = 1, 2, 3
print(a, b, c)

a, b = b, a
print(a, b, c)

x = y = z = 0
print(x, y, z)

# ANSWER:
# 1 2 3
# 2 1 3
# 0 0 0
#
# EXPLANATION:
# ────────────
# 1) MULTIPLE ASSIGNMENT: a, b, c = 1, 2, 3
#    → Assigns 1 to a, 2 to b, 3 to c simultaneously
#
# 2) SWAPPING: a, b = b, a
#    → Python evaluates the RIGHT side first (b=2, a=1)
#    → Then assigns: a=2, b=1
#    → This is the PYTHONIC way to swap! No temp variable needed!
#    → In other languages: temp = a; a = b; b = temp;
#
# 3) CHAINED ASSIGNMENT: x = y = z = 0
#    → All three variables point to the same value: 0
#
# EXAM TRAP: What about a, b, c = 1, 2?
#    → ValueError: not enough values to unpack!
#    → Left side and right side MUST have same number of items.


# ═══���══════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 2: OPERATORS & EXPRESSIONS
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY YOU MUST KNOW:
# ─────────────────────
# ARITHMETIC OPERATORS:
#   +   Addition          5 + 3 = 8
#   -   Subtraction       5 - 3 = 2
#   *   Multiplication    5 * 3 = 15
#   /   Division          5 / 3 = 1.6666... (ALWAYS returns float!)
#   //  Floor Division    5 // 3 = 1 (rounds DOWN toward negative infinity)
#   %   Modulo (remainder) 5 % 3 = 2
#   **  Exponentiation    5 ** 3 = 125
#
# COMPARISON OPERATORS:
#   ==  Equal to          5 == 5 → True
#   !=  Not equal         5 != 3 → True
#   >   Greater than      5 > 3  �� True
#   <   Less than         3 < 5  → True
#   >=  Greater or equal  5 >= 5 → True
#   <=  Less or equal     3 <= 5 → True
#
# LOGICAL OPERATORS:
#   and  → True if BOTH sides are True
#   or   → True if AT LEAST ONE side is True
#   not  → Reverses the boolean value
#
# OPERATOR PRECEDENCE (highest to lowest):
#   **  →  unary -  →  *, /, //, %  →  +, -  →  comparisons  →  not  →  and  →  or
#
# MEMORY TRICK: "PEMDAS" from math, then comparisons, then NOT AND OR


# ──────────────────────────────────────────────────────────────────────────────
# Q11: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(10 / 3)
print(10 // 3)
print(-10 // 3)
print(10 % 3)
print(-10 % 3)

# ANSWER:
# 3.3333333333333335
# 3
# -4
# 1
# 2
#
# THIS IS THE #1 MOST TESTED TOPIC ON PCEP. LEARN IT PERFECTLY.
#
# DETAILED EXPLANATION:
# ─────────────────────
#
# 10 / 3 = 3.333...
# → The / operator ALWAYS returns float. Even 10 / 2 = 5.0 (not 5!)
# → USE WHEN: You want the exact decimal result.
#
# 10 // 3 = 3
# → Floor division: divide, then round DOWN toward NEGATIVE INFINITY.
# → 10 ÷ 3 = 3.333... → floor(3.333) = 3
# → USE WHEN: You want whole number division (no decimals).
#
# -10 // 3 = -4  ← THIS IS THE TRAP!!!
# → -10 ÷ 3 = -3.333... → floor(-3.333) = -4
# → Floor goes toward NEGATIVE INFINITY, not toward zero!
# → -4 is "more negative" than -3.333, so floor goes to -4
# → COMMON MISTAKE: People think it's -3 (truncation). NO! It's -4 (floor).
# → REMEMBER: // is FLOOR, not TRUNCATION. int() truncates, // floors.
#
# 10 % 3 = 1
# → Modulo: remainder after division. 10 = 3 × 3 + 1, remainder is 1.
# → USE WHEN: Check divisibility (x % 2 == 0 → x is even)
# → USE WHEN: Cycling/wrapping (hours: 25 % 24 = 1)
#
# -10 % 3 = 2  ← ANOTHER TRAP!!!
# → Python's modulo ALWAYS returns result with same sign as the DIVISOR (3).
# → Formula: a % b = a - (a // b) * b
# → -10 % 3 = -10 - (-10 // 3) * 3 = -10 - (-4) * 3 = -10 - (-12) = -10 + 12 = 2
# → EXAM STRATEGY: Use the formula! a % b = a - (a // b) * b


# ──────────────────────────────────────────────────────────────────────────────
# Q12: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(2 ** 3 ** 2)

# OPTIONS:
# A) 64   (because (2**3)**2 = 8**2 = 64)
# B) 512  (because 2**(3**2) = 2**9 = 512)
# C) 12
# D) Error

# ANSWER: B) 512
#
# WHY? EXPONENTIATION IS RIGHT-ASSOCIATIVE:
# ───────────────────────────────────────────
# Most operators in Python are LEFT-associative:
#   5 - 3 - 1 = (5 - 3) - 1 = 1  (evaluates left to right)
#
# But ** is the EXCEPTION — it's RIGHT-associative:
#   2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512
#
# Step by step:
#   1. First evaluate the RIGHT ** : 3 ** 2 = 9
#   2. Then evaluate the LEFT **  : 2 ** 9 = 512
#
# EXAM STRATEGY: When you see multiple ** operators:
#   → Always work from RIGHT to LEFT!
#   → This is the ONLY common operator that works this way.


# ──────────────────────────────────────────────────────────────────────────────
# Q13: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 + 1)
print(2 ** (3 + 1))

# ANSWER:
# 14      → 2 + (3 * 4) = 2 + 12 = 14    (* before +)
# 20      → (2 + 3) * 4 = 5 * 4 = 20     (parentheses override)
# 9       → (2 ** 3) + 1 = 8 + 1 = 9     (** before +)
# 16      → 2 ** (3 + 1) = 2 ** 4 = 16   (parentheses override)
#
# PRECEDENCE REMINDER:
# ** is evaluated FIRST (highest among arithmetic)
# Then * / // %
# Then + -
# Parentheses () ALWAYS override everything.
#
# EXAM STRATEGY: When in doubt about order:
#   1. Parentheses first
#   2. ** next
#   3. Then *, /, //, % (left to right)
#   4. Then +, - (left to right)


# ──────────────────────────────────────────────────────────────────────────────
# Q14: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = 5
x += 3
print(x)
x -= 2
print(x)
x *= 4
print(x)
x //= 5
print(x)
x %= 3
print(x)
x **= 3
print(x)

# ANSWER:
# 8       → x = 5 + 3 = 8
# 6       → x = 8 - 2 = 6
# 24      → x = 6 * 4 = 24
# 4       → x = 24 // 5 = 4 (floor division: 24/5 = 4.8, floor = 4)
# 1       → x = 4 % 3 = 1 (remainder: 4 = 3×1 + 1)
# 1       → x = 1 ** 3 = 1
#
# COMPOUND ASSIGNMENT OPERATORS:
# ──────────────────────────────
# x += n  is shorthand for  x = x + n
# x -= n  is shorthand for  x = x - n
# x *= n  is shorthand for  x = x * n
# x /= n  is shorthand for  x = x / n   (result is float!)
# x //= n is shorthand for  x = x // n
# x %= n  is shorthand for  x = x % n
# x **= n is shorthand for  x = x ** n
#
# NOTE: Python does NOT have ++ or -- operators!
# x++ → SyntaxError!
# Use x += 1 instead.


# ──────────────────────────────────────────────────────────────────────────────
# Q15: What is the output?
# ──────────────────────��───────────────────────────────────────────────────────
print(True and False)
print(True or False)
print(not True)
print(not False)
print(True and True and False)
print(False or False or True)

# ANSWER:
# False    → and requires BOTH True
# True     → or requires at least ONE True
# False    → not reverses True → False
# True     → not reverses False → True
# False    → True AND True = True, then True AND False = False
# True     → False OR False = False, then False OR True = True
#
# TRUTH TABLES:
# ─────────────
#  A     | B     | A and B | A or B | not A
# ─────── ─────── ──────── ──────── ──────
#  True  | True  | True    | True   | False
#  True  | False | False   | True   | False
#  False | True  | False   | True   | True
#  False | False | False   | False  | True
#
# PRECEDENCE: not > and > or
# So: not True or False and True
#   = (not True) or (False and True)
#   = False or False
#   = False


# ──────────────────────────────────────────────────────────────────────────────
# Q16: What is the output? (SHORT-CIRCUIT EVALUATION)
# ──────────────────────────────────────────────────────────────────────────────
print(5 and 3)
print(0 and 3)
print(5 or 3)
print(0 or 3)
print("" or "default")
print("hello" or "default")

# ANSWER:
# 3          → 5 is truthy, so "and" returns the SECOND value
# 0          → 0 is falsy, so "and" returns the FIRST value (short-circuits)
# 5          → 5 is truthy, so "or" returns the FIRST value (short-circuits)
# 3          → 0 is falsy, so "or" returns the SECOND value
# "default"  → "" is falsy, so "or" returns the SECOND value
# "hello"    → "hello" is truthy, so "or" returns the FIRST value
#
# THIS IS CRUCIAL FOR PCEP. HERE ARE THE RULES:
# ──────────────────────────────────────────────
#
# "and" RETURNS:
#   → If first value is FALSY: returns first value (doesn't even check second)
#   → If first value is TRUTHY: returns second value
#   → Think: "and" needs BOTH true, so if first is false, why check second?
#
# "or" RETURNS:
#   → If first value is TRUTHY: returns first value (doesn't check second)
#   → If first value is FALSY: returns second value
#   → Think: "or" needs just ONE true, so if first is true, why check second?
#
# PRACTICAL USE:
#   name = user_input or "Anonymous"
#   → If user_input is "" (empty/falsy), name becomes "Anonymous"
#   → If user_input is "John" (truthy), name becomes "John"


# ──────────────────────────────────────────────────────────────────────────────
# Q17: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(3 > 2 > 1)
print(3 > 2 > 2)
print(1 < 2 < 3 < 4)
print(1 < 2 > 0)

# ANSWER:
# True     → Python chains: (3>2) and (2>1) → True and True → True
# False    → Python chains: (3>2) and (2>2) → True and False → False
# True     → (1<2) and (2<3) and (3<4) → True and True and True → True
# True     → (1<2) and (2>0) → True and True → True
#
# CHAINED COMPARISONS:
# ─────────────────────
# Python allows: a < b < c which means (a < b) and (b < c)
# This is UNIQUE to Python — most languages don't support this!
# EXAM TRAP: Make sure you expand the chain into separate comparisons.


# ──────────────────────────────────────────────────────────────────────────────
# Q18: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
print(a == c)

# ANSWER:
# True     → a and b have the SAME VALUES → equal
# False    → a and b are DIFFERENT OBJECTS in memory → not identical
# True     → a and c point to the SAME OBJECT → identical
# True     → a and c are the same object, so obviously same values too
#
# THE CRITICAL DIFFERENCE:
# ─────────────────────────
# ==  checks VALUE EQUALITY:  "Do they contain the same data?"
# is  checks IDENTITY:        "Are they the EXACT SAME object in memory?"
#
# Think of it like twins:
#   == → "Do they look the same?" (yes, twins look alike)
#   is → "Are they the same person?" (no, twins are different people)
#
# WHEN TO USE "is":
#   → Only for None, True, False comparisons: if x is None
# WHEN TO USE "==":
#   → Everything else: if x == 5, if name == "John"


# ──────────────────────────────────────────────────────────────────────────────
# Q19: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print(10 / 3)
print(10 // 3)
print(-7 // 2)
print(-7 % 2)
print(7 % -2)

# ANSWER:
# 3.3333333333333335    → / always returns float
# 3                     → floor(3.333) = 3
# -4                    → floor(-3.5) = -4 (toward negative infinity!)
# 1                     → -7 - (-7//2)*2 = -7 - (-4)*2 = -7 + 8 = 1
# -1                    → 7 - (7//-2)*(-2) = 7 - (-4)*(-2) = 7 - 8 = -1
#
# FORMULA FOR % (MODULO):
# a % b = a - (a // b) * b
#
# FOR -7 % 2:
#   a = -7, b = 2
#   a // b = -7 // 2 = -4 (floor division)
#   a - (a // b) * b = -7 - (-4 * 2) = -7 - (-8) = -7 + 8 = 1
#
# FOR 7 % -2:
#   a = 7, b = -2
#   a // b = 7 // -2 = -4 (floor of -3.5 is -4)
#   a - (a // b) * b = 7 - (-4 * -2) = 7 - 8 = -1
#
# KEY INSIGHT: The result of % has the same sign as the DIVISOR (b).
#   -7 % 2  → positive (same sign as 2)
#   7 % -2  → negative (same sign as -2)


# ──────────────────────────────────────────────────────────────────────────────
# Q20: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
print("hello" * 3)
print("-" * 20)
print("ha" * 0)
print("ha" * -1)

# ANSWER:
# hellohellohello   → String repetition: repeats the string 3 times
# --------------------  → Useful for creating separators!
# (empty string)    → Repeating 0 times gives empty string ""
# (empty string)    → Negative repetition also gives empty string ""
#
# STRING * INT:
# → Creates a NEW string that is the original repeated n times
# → If n <= 0, returns empty string ""
# → If n = 1, returns the original string
#
# COMMON USE: Creating lines/separators
#   print("=" * 50)  → ==================================================


# ──────────────────────────────────────────────────────────────────────────────
# Q21-Q25: RAPID FIRE — What is the output?
# ──────────────────────────────────────────────────────────────────────────────

# Q21:
print(not not True)          # True → not True = False, not False = True
# TRICK: Double negation cancels out!

# Q22:
print(1 == True)             # True → True is 1 in Python
print(0 == False)            # True → False is 0 in Python
print(2 == True)             # False → True is ONLY equal to 1, not 2!

# Q23:
print("abc" < "abd")        # True → String comparison is LEXICOGRAPHIC
# Compares character by character:
# 'a'=='a', 'b'=='b', 'c'<'d' → True
# Uses Unicode/ASCII values: ord('c')=99, ord('d')=100, 99<100

# Q24:
print(10 > 5 and 3 < 1)     # False → True and False = False
print(10 > 5 or 3 < 1)      # True  → True or False = True

# Q25:
x = 5
print(1 < x < 10)           # True → 1 < 5 is True AND 5 < 10 is True
print(1 < x < 3)            # False → 1 < 5 is True AND 5 < 3 is False


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 3: CONTROL FLOW — if / elif / else
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY:
# ───────
# if condition:        → Runs ONLY if condition is True
#     code block
# elif condition2:     → Checked ONLY if previous if/elif was False
#     code block
# else:                → Runs ONLY if ALL above conditions were False
#     code block
#
# RULES:
# 1. "if" is REQUIRED. elif and else are OPTIONAL.
# 2. You can have MULTIPLE elif blocks (0 or more).
# 3. You can have only ONE else block (0 or 1).
# 4. Python uses INDENTATION to define code blocks (4 spaces standard).
# 5. Conditions are evaluated TOP to BOTTOM. First True wins!
# 6. Once a block executes, the rest of the chain is SKIPPED.


# ──────────────────────────────────────────────────────────────────────────────
# Q26: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = 15

if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")

# ANSWER: B
#
# TRACE:
# ──────
# x = 15
# x > 20 → 15 > 20 → False → skip "A"
# x > 10 → 15 > 10 → True  → print "B" → STOP! Rest is skipped!
#
# Even though x > 5 is ALSO True (15 > 5), it's never checked
# because the elif x > 10 already matched.
#
# KEY LESSON: In if/elif/elif/else chains, ONLY THE FIRST TRUE branch executes.
# This is different from multiple separate "if" statements!

# COMPARE — Multiple separate "if" statements:
x = 15
if x > 20:
    print("A")
if x > 10:      # This is a NEW if, not elif!
    print("B")
if x > 5:       # This is ALSO a new if!
    print("C")

# OUTPUT: B and C (both print because they're independent if statements!)
# EXAM TRAP: "if...if...if" vs "if...elif...elif" → VERY different behavior!


# ──────────────────────────────────────────────────────────────────────────────
# Q27: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)

# ANSWER: "B"
#
# TRACE:
# score = 85
# 85 >= 90 → False → skip
# 85 >= 80 → True  → grade = "B" → DONE!
#
# ALGORITHM PATTERN: "RANGE CLASSIFICATION"
# ─────────────────────────────────���───────
# When you need to classify a value into categories based on ranges:
# 1. Start from the HIGHEST threshold
# 2. Go down to the lowest
# 3. Use elif to ensure only ONE category is assigned
#
# WHY highest first? Because if score is 95:
#   95 >= 90 → True → "A" → STOP (correct!)
# If you started from lowest:
#   95 >= 60 → True → "D" → STOP (WRONG!)


# ──────────────────────────────────────────────────────────────────────────────
# Q28: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
x = 0

if x:
    print("truthy")
else:
    print("falsy")

# ANSWER: "falsy"
#
# WHY? TRUTHINESS IN CONDITIONS:
# ──────────────────────────────
# Python's "if" doesn't require a boolean. It evaluates ANY value for truthiness.
# Remember Q4? 0 is FALSY. So "if 0:" is the same as "if False:"
#
# This is idiomatic Python:
#   if my_list:        → True if list is not empty
#   if my_string:      → True if string is not empty
#   if my_dict:        → True if dict is not empty
#   if my_number:      → True if number is not zero
#   if my_var:         → True if variable is not None/0/empty


# ──────────────────────────────────────────────────────────────────────────────
# Q29: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
elif age >= 18 and not has_license:
    print("Get a license first")
elif age >= 16:
    print("Can get learner's permit")
else:
    print("Too young")

# ANSWER: "Can drive"
#
# TRACE:
# age >= 18 → True, has_license → True
# True and True → True → "Can drive"
#
# COMBINING CONDITIONS:
# ─────────────────────
# Use "and" when BOTH conditions must be true
# Use "or" when at least ONE condition must be true
# Use "not" to reverse a condition
# Use parentheses for clarity: if (a > 5) and (b < 10):


# ──────────────────────────────────────────────────────────────────────────────
# Q30: What is the output? (NESTED if)
# ──────────────────────────────────────────────────────────────────────────────
x = 10
y = 20

if x > 5:
    if y > 15:
        print("A")
    else:
        print("B")
else:
    if y > 15:
        print("C")
    else:
        print("D")

# ANSWER: "A"
#
# TRACE (follow the indentation carefully!):
# x > 5 → 10 > 5 → True → enter outer if block
#   y > 15 → 20 > 15 → True → print "A"
#
# IMPORTANT: Indentation defines which "else" belongs to which "if"!
# The inner "else: print(B)" belongs to the inner "if y > 15"
# The outer "else:" belongs to the outer "if x > 5"


# ──────��───────────────────────────────────────────────────────────────────────
# Q31: What is the output? (TERNARY / CONDITIONAL EXPRESSION)
# ──────────────────────────────────────────────────────────────────────────────
x = 7
result = "even" if x % 2 == 0 else "odd"
print(result)

# ANSWER: "odd"
#
# TERNARY EXPRESSION SYNTAX:
# ──────────────────────────
# value_if_true  if  condition  else  value_if_false
#
# This is the same as:
# if x % 2 == 0:
#     result = "even"
# else:
#     result = "odd"
#
# x % 2 → 7 % 2 = 1 → 1 == 0 → False → result = "odd"
#
# USE WHEN: You need a simple if/else to assign a value.
# DON'T USE WHEN: The logic is complex (use regular if/else for readability).

# More examples:
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"

score = 45
passed = "Pass" if score >= 50 else "Fail"
print(passed)  # "Fail"


# ──────────────────────────────────────────────────────────────────────────────
# Q32-Q35: RAPID FIRE — Control Flow
# ──────────────────────────────────────────────────────────────────────────────

# Q32: What is the output?
x = 3
if x == 1:
    print("one")
elif x == 2:
    print("two")
# No else! What happens when nothing matches?
# ANSWER: Nothing! No output. This is perfectly valid.
# An if/elif chain without else simply does nothing if no condition is True.

# Q33: What is the output?
print("A" if True else "B")      # "A" → condition is True
print("A" if False else "B")     # "B" → condition is False
print("A" if "" else "B")        # "B" → "" is falsy
print("A" if "hello" else "B")   # "A" → "hello" is truthy
print("A" if 0 else "B")         # "B" → 0 is falsy
print("A" if 42 else "B")        # "A" → 42 is truthy

# Q34: What is the output?
x = 10
if x > 5:
    pass  # "pass" is a placeholder — does NOTHING, prevents IndentationError
print("done")
# ANSWER: "done"
# "pass" is used when you need a code block but have nothing to put in it yet.
# Common in: empty functions, empty classes, TODO placeholders.

# Q35: What is the output?
nums = [1, 2, 3, 4, 5]
if 3 in nums:
    print("found")
else:
    print("not found")
# ANSWER: "found"
# "in" operator checks MEMBERSHIP. Works with lists, tuples, strings, dicts, sets.


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 4: LOOPS — for & while
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY:
# ───────
# FOR LOOP: Iterates over a sequence (list, string, range, tuple, dict...)
#   for variable in sequence:
#       do something
#
# WHILE LOOP: Repeats as long as condition is True
#   while condition:
#       do something
#       update condition (or use break)
#
# LOOP CONTROL:
#   break     → EXIT the loop immediately
#   continue  → SKIP the rest of this iteration, go to next
#   pass      → Do nothing (placeholder)
#   else      → Runs after loop finishes NORMALLY (not after break!)
#
# range() FUNCTION:
#   range(stop)             → 0, 1, 2, ..., stop-1
#   range(start, stop)      → start, start+1, ..., stop-1
#   range(start, stop, step) → start, start+step, ..., up to but not including stop


# ──────────────────────────────────────────────────────────────────────────────
# Q36: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
for i in range(5):
    print(i, end=" ")
print()  # newline

# ANSWER: 0 1 2 3 4
#
# DETAILED EXPLANATION:
# ─────────────────────
# range(5) generates: 0, 1, 2, 3, 4
# → It starts at 0 (default)
# → It goes up to 5 but does NOT include 5
# → range(n) gives you exactly n numbers: 0 through n-1
#
# print(i, end=" "):
# → The "end" parameter controls what print() puts AFTER the text
# → Default is end="\n" (newline — that's why print normally goes to next line)
# → end=" " means put a space instead of newline
# → This makes all numbers appear on the same line
#
# WHEN TO USE range():
# → When you need to repeat something a specific number of times
# → When you need index numbers
# → When you need to generate a sequence of numbers


# ──────────────────────────────────────────────────────────────────────────────
# Q37: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
for i in range(2, 10, 3):
    print(i, end=" ")
print()

# ANSWER: 2 5 8
#
# range(2, 10, 3):
# → start = 2
# → stop  = 10 (not included)
# → step  = 3
# → Generates: 2, 5, 8 (next would be 11, but 11 >= 10, so stop)
#
# STEP BY STEP:
# Start at 2 → print 2
# 2 + 3 = 5, 5 < 10 → print 5
# 5 + 3 = 8, 8 < 10 → print 8
# 8 + 3 = 11, 11 >= 10 → STOP


# ──────────────────────────────────────────────────────────────────────────────
# Q38: What is the output? (COUNTING BACKWARDS)
# ──────────────────────────────────────────────────────────────────────────────
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# ANSWER: 5 4 3 2 1
#
# range(5, 0, -1):
# → start = 5
# → stop  = 0 (not included! So we don't print 0)
# → step  = -1 (going backwards)
# → Generates: 5, 4, 3, 2, 1
#
# COMMON MISTAKE: range(5, 0, -1) does NOT include 0!
# If you want 5,4,3,2,1,0 → use range(5, -1, -1)


# ──────────────────────────────────────────────────────────────────────────────
# Q39: What is the output? (ITERATING OVER STRINGS)
# ──────────────────────────────────────────────────────────────────────────────
word = "Python"
for char in word:
    print(char, end="-")
print()

# ANSWER: P-y-t-h-o-n-
#
# STRINGS ARE ITERABLE:
# ─────────────────────
# When you do "for char in string", Python gives you each character one by one.
# "Python" → 'P', 'y', 't', 'h', 'o', 'n'
# Note the trailing dash after 'n' — it prints a dash after EVERY character.


# ──────────────────────────────────────────────────────────────────────────────
# Q40: What is the output? (ENUMERATE)
# ──────────────────────────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ANSWER:
# 0: apple
# 1: banana
# 2: cherry
#
# enumerate(iterable) FUNCTION:
# ─────────────────────────────
# → Wraps any iterable and adds a counter
# → Returns pairs: (0, first_item), (1, second_item), ...
# → The "index, fruit" is called UNPACKING — it takes the pair apart
#
# f-string: f"{index}: {fruit}"
# → f"..." allows you to put variables inside {} directly
# → Much cleaner than: str(index) + ": " + fruit
#
# WHEN TO USE enumerate():
# → When you need BOTH the index AND the value during iteration
# → Instead of: for i in range(len(fruits)): ... fruits[i]
# → This is the PYTHONIC way!
#
# You can also start counting from a different number:
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry


# ──────────────────────────────────────────────────────────────────────────────
# Q41: What is the output? (BREAK)
# ──────────────────────────────────���───────────────────────────────────────────
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()
print("Loop ended")

# ANSWER: 0 1 2 3 4 (newline) Loop ended
#
# BREAK EXPLAINED:
# ────────────────
# "break" immediately EXITS the loop. No more iterations.
# The code AFTER the loop (print("Loop ended")) still runs.
# Only the loop itself is terminated.
#
# TRACE:
# i=0: 0!=5 → print 0
# i=1: 1!=5 → print 1
# i=2: 2!=5 → print 2
# i=3: 3!=5 → print 3
# i=4: 4!=5 → print 4
# i=5: 5==5 → BREAK! Exit loop. (5 is NOT printed because break comes first)
# → "Loop ended" prints because it's OUTSIDE the loop
#
# WHEN TO USE break:
# → When you've FOUND what you're looking for (search problem)
# → When a certain condition means you should STOP entirely
# → When you want to exit an infinite loop: while True: ... break


# ─────────────────────────────────────────────────────────────────────���────────
# Q42: What is the output? (CONTINUE)
# ──────────────────────────────────────────────────────────────────────────────
for i in range(8):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# ANSWER: 1 3 5 7
#
# CONTINUE EXPLAINED:
# ───────────────────
# "continue" SKIPS the rest of the current iteration and goes to the NEXT one.
# It does NOT exit the loop — it just skips one cycle.
#
# TRACE:
# i=0: 0%2==0 → True → continue (skip print, go to i=1)
# i=1: 1%2==0 → False → print 1
# i=2: 2%2==0 → True → continue (skip print)
# i=3: 3%2==0 → False → print 3
# i=4: 4%2==0 → True → continue
# i=5: 5%2==0 → False → print 5
# i=6: 6%2==0 → True → continue
# i=7: 7%2==0 → False → print 7
#
# RESULT: Only odd numbers print (even numbers are skipped)
#
# WHEN TO USE continue:
# → When you want to SKIP certain items but keep looping
# → When you want to filter out unwanted items during iteration


# ──────────────────────────────────────────────────────────────────────────────
# Q43: What is the output? (LOOP ELSE — TRICKY PCEP TOPIC!)
# ──────────────────────────────────────────────────────────────────────────────

# Example A: Loop completes normally
for i in range(3):
    print(i, end=" ")
else:
    print("→ Loop completed normally!")

# ANSWER: 0 1 2 → Loop completed normally!

# Example B: Loop exits with break
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("→ Loop completed normally!")

# ANSWER: 0 1 2
# The "else" does NOT run because the loop was broken!

# LOOP ELSE EXPLAINED:
# ─────────────────────
# "else" after a loop runs ONLY if the loop finished WITHOUT break.
#
# RULE:
#   - Loop runs normally to completion → else RUNS
#   - Loop exits via "break" → else does NOT run
#   - Loop body never executes (e.g., range(0)) → else STILL runs!
#
# WHEN TO USE loop else:
# → Searching: if you find something, break. If you don't find it, else runs.

# Practical example:
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found in the list.")
# OUTPUT: "4 was not found in the list."
# The else runs because we never found 4 and never called break.


# ──────────────────────────────────────────────────────────────────────────────
# Q44: What is the output? (WHILE LOOP)
# ──────────────────────────────────────────────────────────────────────────────
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# ANSWER: 1 2 3 4 5
#
# WHILE LOOP EXPLAINED:
# ─────────────────────
# 1. Check condition: is count <= 5?
# 2. If True → execute body (print count, then increment)
# 3. Go back to step 1
# 4. If False → exit loop
#
# TRACE:
# count=1: 1<=5 → True → print 1 → count=2
# count=2: 2<=5 → True → print 2 → count=3
# count=3: 3<=5 → True → print 3 → count=4
# count=4: 4<=5 → True → print 4 → count=5
# count=5: 5<=5 → True → print 5 → count=6
# count=6: 6<=5 → False → EXIT
#
# DANGER: If you forget "count += 1", you get an INFINITE LOOP!
# The condition would always be True and the loop would never stop.
#
# WHEN TO USE while vs for:
# → for: when you KNOW how many times to loop (or iterating a collection)
# → while: when you DON'T know — loop until a condition changes


# ──────────────────────────────────────────────────────────────────────────────
# Q45: What is the output? (NESTED LOOPS)
# ──────────────────────────────────────────────────────────────────────────────
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # newline after each row

# ANSWER:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
#
# NESTED LOOPS: OUTER loop runs once, INNER loop runs FULLY, then outer goes next.
#
# TRACE:
# i=0: j runs 0,1,2 → (0,0) (0,1) (0,2) then newline
# i=1: j runs 0,1,2 → (1,0) (1,1) (1,2) then newline
# i=2: j runs 0,1,2 → (2,0) (2,1) (2,2) then newline
#
# Total iterations: 3 × 3 = 9  → This is why nested loops are O(n²)
#
# WHEN YOU SEE NESTED LOOPS:
# → Time complexity is O(outer × inner)
# → Think: "For every item in outer, I go through ALL of inner"
# → Like: "For every row in a grid, go through every column"


# ──────────────────────────────────────────────────────────────────────────────
# Q46: What is the output? (BREAK IN NESTED LOOPS)
# ──────────────────────────────────────────────────────────────────────────────
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"({i},{j})", end=" ")
    print()

# ANSWER:
# (0,0)
# (1,0)
# (2,0)
#
# IMPORTANT: break only exits the INNERMOST loop!
# When j==1, we break out of the j-loop, but the i-loop continues.
#
# TRACE:
# i=0: j=0 → print (0,0), j=1 → break → newline
# i=1: j=0 → print (1,0), j=1 → break → newline
# i=2: j=0 → print (2,0), j=1 → break → newline
#
# If you want to break BOTH loops, use a flag variable:
# found = False
# for i in range(3):
#     for j in range(3):
#         if some_condition:
#             found = True
#             break
#     if found:
#         break


# ──────────────────────────────────────────────────────────────────────────────
# Q47: What is the output? (SUM WITH LOOP)
# ──────────────────────────────────────────────────────────────────────────────
total = 0
for i in range(1, 6):
    total += i
print(total)

# ANSWER: 15
#
# TRACE:
# i=1: total = 0 + 1 = 1
# i=2: total = 1 + 2 = 3
# i=3: total = 3 + 3 = 6
# i=4: total = 6 + 4 = 10
# i=5: total = 10 + 5 = 15
#
# ALGORITHM PATTERN: "ACCUMULATOR"
# ─────────────────────────────────
# 1. Initialize a variable BEFORE the loop (total = 0)
# 2. Update it INSIDE the loop (total += i)
# 3. Use the result AFTER the loop (print(total))
#
# This pattern works for:
# → Sum:     total = 0, total += value
# → Product: product = 1, product *= value
# → Count:   count = 0, count += 1
# → Max:     max_val = first_element, if val > max_val: max_val = val
# → Build:   result = "", result += character  (for strings)
# → Build:   result = [], result.append(item)  (for lists)
#
# SHORTCUT: sum(range(1, 6)) → 15
# But the exam wants you to understand the loop version!


# ──────────────────────────────────────────────────────────────────────────────
# Q48: What is the output? (BUILDING A LIST WITH LOOP)
# ─────────────────────────────────────────────────────────────────────────��────
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

# ANSWER: [1, 4, 9, 16, 25]
#
# TRACE:
# i=1: squares = [] + [1²] = [1]
# i=2: squares = [1] + [2²] = [1, 4]
# i=3: squares = [1, 4] + [3²] = [1, 4, 9]
# i=4: squares = [1, 4, 9] + [4²] = [1, 4, 9, 16]
# i=5: squares = [1, 4, 9, 16] + [5²] = [1, 4, 9, 16, 25]
#
# .append(value) METHOD:
# → Adds a single element to the END of the list
# → Modifies the list IN PLACE (doesn't create a new list)
# → Returns None (so don't write: squares = squares.append(x) — this is wrong!)
#
# SHORTCUT: List Comprehension (same result, one line):
squares_v2 = [i ** 2 for i in range(1, 6)]
print(squares_v2)  # [1, 4, 9, 16, 25]
# LIST COMPREHENSION SYNTAX: [expression for variable in iterable]


# ──────────────────────────────────────────────────────────────────────────────
# Q49: What is the output? (LIST COMPREHENSION WITH CONDITION)
# ──────────────────────────────────────────────────────────────────────────────
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# ANSWER: [0, 2, 4, 6, 8]
#
# LIST COMPREHENSION WITH FILTER:
# [expression for variable in iterable if condition]
#
# This is equivalent to:
evens_v2 = []
for x in range(10):
    if x % 2 == 0:
        evens_v2.append(x)
# Same result, but list comprehension is more concise and Pythonic.
#
# MORE EXAMPLES:
# Get names longer than 3 characters:
names = ["Al", "Bob", "Charlie", "Di"]
long_names = [name for name in names if len(name) > 3]
# Result: ["Charlie"]

# Transform and filter:
# Get squares of even numbers from 0-9:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]


# ──────────────────────────────────────────────────────────────────────────────
# Q50: What is the output? (WHILE with condition change)
# ──────────────────────────────────────────────────────────────────────────────
n = 256
count = 0
while n > 1:
    n = n // 2
    count += 1
print(f"n={n}, count={count}")

# ANSWER: n=1, count=8
#
# TRACE:
# n=256, count=0
# 256//2=128, count=1
# 128//2=64,  count=2
# 64//2=32,   count=3
# 32//2=16,   count=4
# 16//2=8,    count=5
# 8//2=4,     count=6
# 4//2=2,     count=7
# 2//2=1,     count=8
# 1 > 1? → False → EXIT
#
# This is essentially calculating log₂(256) = 8
# This is the O(log n) pattern — the value is HALVED each time.
#
# ALGORITHM INSIGHT:
# → When a value is multiplied/divided by a constant each iteration → O(log n)
# → When a value increases/decreases by a constant each iteration → O(n)


# ──────────────────────────────────────────────────────────────────────────────
# Q51: What is the output? (COMMON PATTERN: Finding max/min)
# ──────────────────────────────────────────────────────────────────────────────
numbers = [34, 12, 89, 3, 56, 42]

max_val = numbers[0]  # Start with first element as "best so far"
for num in numbers:
    if num > max_val:
        max_val = num

min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num

print(f"Max: {max_val}, Min: {min_val}")

# ANSWER: Max: 89, Min: 3
#
# ALGORITHM PATTERN: "RUNNING BEST" (Find Maximum/Minimum)
# ─────────────────────────────────────────────────────────
# 1. Assume the first element is the best
# 2. Go through every element
# 3. If current element is better → update the best
# 4. After loop, you have the answer
#
# WHY start with numbers[0] instead of 0?
# → If all numbers are negative, e.g., [-5, -3, -1],
#   starting with 0 would give max=0, which is WRONG (0 isn't in the list)
# → Starting with the first element guarantees correctness
#
# SHORTCUT: max(numbers) → 89, min(numbers) → 3
# But understand the algorithm for the exam!


# ──────────────────────────────────────────────────────────────────────────────
# Q52-Q55: RAPID FIRE — Loops
# ──────────────────────────────────────────────────────────────────────────────

# Q52: What is the output?
for i in range(0):
    print("hello")
print("done")
# ANSWER: done
# range(0) produces NO values → loop body never executes → "done" still prints

# Q53: What does this print?
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 3)))    # [0, 3, 6, 9]
print(list(range(10, 0, -2)))   # [10, 8, 6, 4, 2]
# list(range(...)) converts a range to a list so you can see all values at once.

# Q54: What is the output?
text = "Hello"
for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")
print()
# ANSWER: olleH
# This prints the string in REVERSE by going from last index to first.
# range(4, -1, -1) → 4, 3, 2, 1, 0
# text[4]='o', text[3]='l', text[2]='l', text[1]='e', text[0]='H'
# SHORTCUT: print(text[::-1]) → same result!

# Q55: What is the output?
i = 10
while i > 0:
    i -= 3
print(i)
# ANSWER: -2
# i=10: 10>0 → i=10-3=7
# i=7:  7>0  → i=7-3=4
# i=4:  4>0  → i=4-3=1
# i=1:  1>0  → i=1-3=-2
# i=-2: -2>0 → False → EXIT → print(-2)


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 5: FUNCTIONS
# ██████████████████████████████████████████████████████████████████████████████
# ═════════════════════════════��════════════════════════════════════════════════
#
# THEORY:
# ───────
# A function is a REUSABLE block of code that performs a specific task.
#
# SYNTAX:
# def function_name(parameters):
#     """Docstring: describes what the function does."""
#     code block
#     return value  (optional — if no return, function returns None)
#
# TERMINOLOGY:
# - PARAMETER: The variable name in the function definition: def greet(name)
# - ARGUMENT:  The actual value you pass when calling: greet("John")
# - RETURN:    The value the function sends back to the caller
# - SCOPE:     Where a variable is visible/accessible
#
# TYPES OF ARGUMENTS:
# 1. Positional:  func(1, 2, 3)     → matched by position
# 2. Keyword:     func(a=1, b=2)    → matched by name
# 3. Default:     def func(a, b=10) → b has default value if not provided
# 4. *args:       def func(*args)   → accepts any number of positional args
# 5. **kwargs:    def func(**kwargs) → accepts any number of keyword args


# ───────────────────────���──────────────────────────────────────────────────────
# Q56: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet(greeting="Hey", name="Charlie"))

# ANSWER:
# Hello, Alice!
# Hi, Bob!
# Hey, Charlie!
#
# EXPLANATION:
# ────────────
# 1) greet("Alice") → name="Alice", greeting="Hello" (uses default)
# 2) greet("Bob", "Hi") → name="Bob", greeting="Hi" (positional override)
# 3) greet(greeting="Hey", name="Charlie") → keyword arguments (order doesn't matter!)
#
# DEFAULT PARAMETER RULES:
# → Parameters WITH defaults must come AFTER parameters WITHOUT defaults
# → def func(a, b=10): ✓  (non-default first, default second)
# → def func(a=10, b): ✗  SyntaxError! (default before non-default)
#
# KEYWORD ARGUMENT RULES:
# → You can pass arguments by name: greet(name="Alice")
# → Order doesn't matter with keyword args
# → You CAN'T put positional args AFTER keyword args:
#   greet(name="Alice", "Hello") → SyntaxError!


# ──────────────────────────────────────────────────────────────────────────────
# Q57: What is the output? (RETURN vs PRINT)
# ──────────────────────────────────────────────────────────────────────────────
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

result1 = add_print(3, 4)
result2 = add_return(3, 4)
print(f"result1 = {result1}")
print(f"result2 = {result2}")

# ANSWER:
# 7                        ← printed by add_print
# result1 = None           ← add_print has no return → returns None!
# result2 = 7              ← add_return returns the value
#
# CRITICAL DISTINCTION:
# ─────────────────────
# print() → DISPLAYS a value on screen. The function still returns None.
# return  → SENDS a value back to the caller. Nothing is displayed.
#
# This is one of the MOST COMMON beginner mistakes:
# → Using print() inside a function when you should use return
# → A function that print()s but doesn't return cannot be used in further calculations
#
# Example of why return matters:
# total = add_return(3, 4) + add_return(5, 6)  → 7 + 11 = 18 ✓
# total = add_print(3, 4) + add_print(5, 6)    → None + None → TypeError!


# ──────────────────────────────────────────────────────────────────────────────
# Q58: What is the output? (SCOPE — Local vs Global)
# ──────────────────────────────────────────────────────────────────────────────
x = 10  # GLOBAL variable

def my_func():
    x = 20  # LOCAL variable (different from global x!)
    print(f"Inside function: x = {x}")

my_func()
print(f"Outside function: x = {x}")

# ANSWER:
# Inside function: x = 20
# Outside function: x = 10
#
# SCOPE RULES (LEGB):
# ─────────────────────
# Python looks for variables in this order:
# L - Local:     Inside the current function
# E - Enclosing: Inside any enclosing (outer) function
# G - Global:    At the module level (top of the file)
# B - Built-in:  Python's built-in names (print, len, etc.)
#
# In my_func(), "x = 20" creates a NEW LOCAL variable.
# It does NOT change the global x = 10.
# They are COMPLETELY SEPARATE variables that happen to have the same name.
#
# EXAM TRAP: If you want to MODIFY the global variable from inside a function:
def modify_global():
    global x       # Declare that we want to use the GLOBAL x
    x = 20         # Now this modifies the global x!

# Before: x = 10
modify_global()
# After: x = 20

# WARNING: Using "global" is generally BAD PRACTICE.
# Better approach: return the new value and assign it.


# ──────────────────────────────────────────────────────────────────────────────
# Q59: What is the output? (SCOPE — Tricky!)
# ──────────────────────────────────────────────────────────────────────────────
x = 20  # Reset for this example

def func():
    print(x)  # Can we READ the global x without "global" keyword?

func()

# ANSWER: 20
#
# YES! You can READ global variables without "global" keyword.
# You only need "global" when you want to MODIFY (reassign) them.
#
# But THIS would fail:
# def func_fail():
#     print(x)     # Python sees x = ... below, so it thinks x is local
#     x = 30       # UnboundLocalError! Python decided x is local but it hasn't been assigned yet
#
# RULE: If a variable is ASSIGNED anywhere in a function, Python treats it as
# LOCAL throughout the ENTIRE function — even in lines BEFORE the assignment!


# ─────────────────────────────────────────────��────────────────────────────────
# Q60: What is the output? (*args and **kwargs)
# ──────────────────────────────────────────────────────────────────────────────
def show_args(*args):
    print(type(args))
    for arg in args:
        print(arg, end=" ")
    print()

show_args(1, 2, 3, 4, 5)

def show_kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}={value}", end=" ")
    print()

show_kwargs(name="Alice", age=25, city="NYC")

# ANSWER:
# <class 'tuple'>
# 1 2 3 4 5
# <class 'dict'>
# name=Alice age=25 city=NYC
#
# *args EXPLAINED:
# ────────────────
# → Collects any number of POSITIONAL arguments into a TUPLE
# → The name "args" is convention — you could use *anything
# → Inside the function, args is a regular tuple
#
# **kwargs EXPLAINED:
# ───────────────────
# → Collects any number of KEYWORD arguments into a DICTIONARY
# → The name "kwargs" is convention — you could use **anything
# → Inside the function, kwargs is a regular dict
#
# ORDER OF PARAMETERS:
# def func(regular, *args, **kwargs):  ← This order is required!
# 1. Regular positional parameters first
# 2. *args second
# 3. **kwargs last


# ──────────────────────────────────────────────────────────────────────────────
# Q61: What is the output? (MUTABLE DEFAULT ARGUMENT — CLASSIC TRAP!)
# ──────────────────────────────────────────────────────────────────────────────
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item("a"))
print(add_item("b"))
print(add_item("c"))

# ANSWER:
# ['a']
# ['a', 'b']          ← SURPRISE! Not ['b']!
# ['a', 'b', 'c']     ← SURPRISE! Not ['c']!
#
# THIS IS THE #1 PYTHON GOTCHA ON EXAMS:
# ───────────────────────────────────────
# Default mutable arguments (lists, dicts, sets) are created ONCE when the
# function is defined, NOT each time the function is called!
#
# So all calls share the SAME list object. Each call appends to the same list.
#
# THE FIX:
def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []       # Create a NEW list each time
    lst.append(item)
    return lst

print(add_item_fixed("a"))  # ['a']
print(add_item_fixed("b"))  # ['b']  ← Now correct!
print(add_item_fixed("c"))  # ['c']  ← Now correct!

# RULE: NEVER use mutable objects as default parameters!
# Use None as default, then create the object inside the function.


# ──────────────────────────────────────────────────────────────────────────────
# Q62: What is the output? (RECURSION)
# ──────────────────────────────────────────────────────────────────────────────
def factorial(n):
    if n <= 1:      # BASE CASE: stop recursion
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE: call itself

print(factorial(5))

# ANSWER: 120
#
# RECURSION: A function that calls ITSELF.
# Every recursive function MUST have:
# 1. BASE CASE: when to STOP (if n <= 1: return 1)
# 2. RECURSIVE CASE: how to get CLOSER to the base case (n-1)
#
# TRACE:
# factorial(5) = 5 * factorial(4)
#              = 5 * (4 * factorial(3))
#              = 5 * (4 * (3 * factorial(2)))
#              = 5 * (4 * (3 * (2 * factorial(1))))
#              = 5 * (4 * (3 * (2 * 1)))
#              = 5 * (4 * (3 * 2))
#              = 5 * (4 * 6)
#              = 5 * 24
#              = 120
#
# DANGER: Without a base case → INFINITE RECURSION → RecursionError!
# Python has a default recursion limit of 1000.


# ──────────────────────────────────────────────────────────────────────────────
# Q63: What is the output? (LAMBDA — Anonymous Functions)
# ──────────────────────────────────────────────────────────────────────────────
square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

# Using lambda with sorted():
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

# ANSWER:
# 25
# 7
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
#
# LAMBDA EXPLAINED:
# ────��────────────
# lambda parameters: expression
# → Creates a small, one-line function WITHOUT a name
# → Can only have ONE expression (no statements, no assignments)
# → Returns the result of the expression automatically
#
# lambda x: x ** 2  is the same as:
# def square(x):
#     return x ** 2
#
# WHERE LAMBDA IS COMMONLY USED:
# → sorted(key=lambda ...)  → Custom sorting
# → map(lambda ...)         → Transform each element
# → filter(lambda ...)      → Filter elements
#
# sorted() FUNCTION:
# → sorted(iterable) → Returns a new sorted list
# → sorted(iterable, key=function) → Sort by function's result
# → sorted(iterable, reverse=True) → Sort in descending order
# → The "key" parameter says: "Use this function to extract a comparison value"
# → In our example: key=lambda student: student[1] means "sort by the grade (index 1)"


# ──────────────────────────────────────────────────────────────────────────────
# Q64-Q70: RAPID FIRE — Functions
# ──────────────────────────────────────────────────────────────────────────────

# Q64: What is the output?
def func(a, b, c=10):
    return a + b + c

print(func(1, 2))        # 13 → a=1, b=2, c=10(default)
print(func(1, 2, 3))     # 6  → a=1, b=2, c=3(override default)
print(func(c=5, a=1, b=2))  # 8 → keyword args, order doesn't matter

# Q65: What is the output?
def func():
    return 1, 2, 3  # Returns a TUPLE!

result = func()
print(result)        # (1, 2, 3)
print(type(result))  # <class 'tuple'>

a, b, c = func()    # UNPACKING the tuple
print(a, b, c)       # 1 2 3

# Q66: What is the output?
def outer():
    x = "outer"
    def inner():
        # x = "inner"  # ← If uncommented, this would shadow outer's x
        print(x)       # Uses ENCLOSING scope (the 'E' in LEGB)
    inner()

outer()  # "outer"

# Q67: What happens?
def greet(name):
    """This function greets someone."""
    print(f"Hello, {name}!")

print(greet.__doc__)
# Output: This function greets someone.
# __doc__ stores the docstring. This is how help() works.

# Q68: What is the output?
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# map(function, iterable):
# → Applies function to EVERY element in iterable
# → Returns a map object (need list() to see results)
# → Think: "transform each element"

# Q69: What is the output?
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# filter(function, iterable):
# → Keeps elements where function returns True
# → Removes elements where function returns False
# → Returns a filter object (need list() to see results)
# → Think: "keep only matching elements"

# Q70: What is the output?
def apply(func, value):
    return func(value)

print(apply(lambda x: x ** 2, 5))   # 25
print(apply(len, "hello"))           # 5
print(apply(str.upper, "hello"))     # HELLO

# Functions are FIRST-CLASS OBJECTS in Python:
# → They can be passed as arguments to other functions
# → They can be stored in variables
# → They can be returned from other functions


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 6: STRINGS
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY:
# ───────
# Strings are IMMUTABLE sequences of characters.
# IMMUTABLE = once created, CANNOT be changed. Any "modification" creates a new string.
#
# INDEXING:     "Python"[0] = 'P',  "Python"[-1] = 'n'
# SLICING:      "Python"[1:4] = 'yth'
# LENGTH:       len("Python") = 6
# MEMBERSHIP:   'th' in "Python" → True
# CONCATENATION: "Hello" + " " + "World" = "Hello World"
# REPETITION:    "ha" * 3 = "hahaha"
#
# SLICING SYNTAX: string[start:stop:step]
# → start: where to begin (inclusive, default=0)
# → stop: where to end (exclusive, default=end)
# → step: how to move (default=1, -1=backwards)


# ──────────────────────────────────────────────────────────────────────────────
# Q71: What is the output? (INDEXING)
# ──────────────────────────────────────────────────────────────────────────────
s = "Python"
# Index:    0  1  2  3  4  5
# Char:     P  y  t  h  o  n
# Neg idx: -6 -5 -4 -3 -2 -1

print(s[0])     # P
print(s[5])     # n
print(s[-1])    # n (last character)
print(s[-2])    # o (second to last)
# print(s[6])   # IndexError! Index out of range (max is 5 for length 6)

# RULE: Valid indices for string of length n: 0 to n-1 (or -n to -1)


# ──────────────────────────────────────────────────────────────────────────────
# Q72: What is the output? (SLICING)
# ──────────────────────────────────────────────────────────────────────────────
s = "Python Programming"
#     0123456789...

print(s[0:6])      # "Python"     → index 0 to 5 (6 is excluded!)
print(s[7:])        # "Programming" → from index 7 to end
print(s[:6])        # "Python"     → from start to index 5
print(s[::2])       # "Pto rgamn" → every 2nd character
print(s[::-1])      # "gnimmargorP nohtyP" → reversed!
print(s[7:11])      # "Prog"      → index 7, 8, 9, 10
print(s[-11:])      # "Programming" → last 11 characters

# SLICING NEVER RAISES IndexError!
print(s[0:100])     # "Python Programming" → just goes to the end
print(s[100:200])   # "" → empty string (start is beyond the string)

# EXAM STRATEGY FOR SLICING:
# ──────────────────────────
# 1. If start >= len(string): result is ""
# 2. If stop > len(string): stops at the end
# 3. If start > stop (with positive step): result is ""
# 4. s[::-1] ALWAYS reverses the string
# 5. Slicing creates a NEW string (strings are immutable)


# ──────────────────────────────────────────────────────────────────────────────
# Q73: What is the output? (STRING METHODS)
# ──────────────────────────────────────────────────────────────────────────────
s = "  Hello, World!  "

print(s.strip())        # "Hello, World!"    → removes leading/trailing whitespace
print(s.lstrip())       # "Hello, World!  "  → removes leading (left) whitespace only
print(s.rstrip())       # "  Hello, World!"  → removes trailing (right) whitespace only
print(s.strip().upper())  # "HELLO, WORLD!" → chaining: strip first, then uppercase
print(s.strip().lower())  # "hello, world!" → chaining: strip first, then lowercase

# METHOD CHAINING:
# → Since each method returns a NEW string, you can chain them:
# → s.strip().upper().replace(",", "")
# → Each method works on the RESULT of the previous one
# → Read left to right: strip → then uppercase → then replace

# IMPORTANT: These methods return NEW strings. They don't modify the original!
original = "hello"
result = original.upper()
print(original)    # "hello" → unchanged!
print(result)      # "HELLO" → new string


# ──────────────────────────────────────────────────────────────────────────────
# Q74: What is the output? (SPLIT and JOIN)
# ──────────────────────────────────────────────────────────────────────────────
sentence = "Python is awesome"

# .split(separator) → Splits string into a LIST of substrings
words = sentence.split()        # Default: split by whitespace
print(words)                     # ['Python', 'is', 'awesome']

csv_data = "apple,banana,cherry"
items = csv_data.split(",")     # Split by comma
print(items)                     # ['apple', 'banana', 'cherry']

# .join(iterable) → Joins list elements into a STRING
result = " ".join(words)        # Join with space
print(result)                    # "Python is awesome"

result2 = "-".join(items)       # Join with dash
print(result2)                   # "apple-banana-cherry"

result3 = "".join(["H","e","l","l","o"])  # Join with nothing
print(result3)                   # "Hello"

# SPLIT AND JOIN ARE INVERSES:
# "a,b,c".split(",")  → ['a', 'b', 'c']    (string → list)
# ",".join(['a','b','c']) → "a,b,c"          (list → string)
#
# COMMON USE: Reverse words in a sentence
reversed_words = " ".join(sentence.split()[::-1])
print(reversed_words)  # "awesome is Python"
# Step 1: split() → ['Python', 'is', 'awesome']
# Step 2: [::-1]  → ['awesome', 'is', 'Python']
# Step 3: join()  → "awesome is Python"


# ──────────────────────────────────────────────────────────────────────────────
# Q75: What is the output? (FIND, REPLACE, COUNT)
# ──────────────────────────────────────────────────────────────────────────────
s = "Hello World Hello Python Hello"

# .find(substring) → Returns INDEX of first occurrence, or -1 if not found
print(s.find("Hello"))      # 0  (first occurrence at index 0)
print(s.find("Python"))     # 18
print(s.find("Java"))       # -1 (not found!)

# .index(substring) → Same as find, but raises ValueError if not found!
# Use find() when not-found is a normal case. Use index() when not-found is an error.

# .replace(old, new) → Replaces ALL occurrences
print(s.replace("Hello", "Hi"))     # "Hi World Hi Python Hi"
print(s.replace("Hello", "Hi", 1))  # "Hi World Hello Python Hello" → only first 1

# .count(substring) → Counts occurrences
print(s.count("Hello"))     # 3
print(s.count("o"))          # 4


# ──────────────────────────────────────────────────────────────────────────────
# Q76: What is the output? (STRING CHECKING METHODS)
# ──────────────────────────────────────────────────────────────────────────────
print("hello123".isalnum())     # True  → all alphanumeric (letters + digits)
print("hello".isalpha())        # True  → all alphabetic (letters only)
print("12345".isdigit())        # True  → all digits
print("hello".islower())        # True  → all lowercase
print("HELLO".isupper())        # True  → all uppercase
print("Hello World".istitle())  # True  → title case (first letter of each word caps)
print("   ".isspace())          # True  → all whitespace
print("hello world".startswith("hello"))  # True
print("hello world".endswith("world"))    # True

# These return BOOL (True/False) and are useful for validation:
user_input = "12345"
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid number: {number}")


# ──────────────────────────────────────────────────────────────────────────────
# Q77: What is the output? (F-STRINGS — Formatted String Literals)
# ──────────────────────────────────────────────────────────────────────────────
name = "Alice"
age = 25
height = 1.756

# Basic f-string
print(f"My name is {name} and I'm {age} years old.")
# "My name is Alice and I'm 25 years old."

# Expressions inside {}
print(f"Next year I'll be {age + 1}.")
# "Next year I'll be 26."

# Format specifiers
print(f"Height: {height:.2f}")     # "Height: 1.76"    → 2 decimal places
print(f"{'hello':>20}")            # "               hello" → right-align, width 20
print(f"{'hello':<20}")            # "hello               " → left-align, width 20
print(f"{'hello':^20}")            # "       hello        " → center-align, width 20
print(f"{1000000:,}")              # "1,000,000"  → thousand separator
print(f"{0.75:.0%}")               # "75%"  → percentage format

# OTHER STRING FORMATTING (older methods):
print("My name is {} and I'm {} years old.".format(name, age))
print("My name is %s and I'm %d years old." % (name, age))
# f-strings are the MOST MODERN and RECOMMENDED way.


# ──────────────────────────────────────────────────────────────────────────────
# Q78: What is the output? (STRING IMMUTABILITY)
# ──────────────────────────────────────────────────────────────────────────────
s = "Hello"
# s[0] = "h"   # TypeError: 'str' object does not support item assignment!

# To "change" a string, you must CREATE A NEW ONE:
s = "h" + s[1:]     # "h" + "ello" = "hello"
print(s)              # "hello"

# Or use replace:
s = "Hello"
s = s.replace("H", "h")
print(s)              # "hello"

# IMMUTABILITY means:
# → You cannot change individual characters
# → Every string method returns a NEW string
# → The original string is never modified
# → This is why s.upper() doesn't change s — it returns a new string


# ──────────────────────────────────────────────────────────────────────────────
# Q79-Q85: RAPID FIRE — Strings
# ──────────────────────────────────────────────────────────────────────────────

# Q79: What is the output?
print("abc" * 3)           # "abcabcabc"
print("abc" + "def")       # "abcdef"
print(len("Hello\n"))      # 6 → \n is ONE character (newline)
print(len("Hello\\n"))     # 7 → \\ is ONE character (backslash), n is another

# Q80: What is the output?
s = "Python"
print(s[1:4])     # "yth" → index 1,2,3
print(s[::2])     # "Pto" → every 2nd: index 0,2,4
print(s[1::2])    # "yhn" → starting at 1, every 2nd: index 1,3,5
print(s[::-2])    # "nhy" → reversed, every 2nd: index 5,3,1

# Q81: What is the output?
print("Hello World".title())     # "Hello World" → First letter of each word capitalized
print("Hello World".swapcase())  # "hELLO wORLD" → Swap upper↔lower
print("hello".capitalize())     # "Hello" → Only FIRST character capitalized
print("hello".center(11, "*"))  # "***hello***" → Center with * padding

# Q82: Escape characters
print("Hello\tWorld")     # "Hello    World" → \t = tab
print("Hello\nWorld")     # "Hello" (newline) "World" → \n = newline
print("He said \"Hi\"")   # He said "Hi" → \" = literal quote
print("C:\\Users\\name")  # C:\Users\name → \\ = literal backslash
print(r"C:\Users\name")   # C:\Users\name → r"..." = raw string (no escape processing)

# Q83: What is the output?
print("Python"[100:200])   # "" → Slicing out of range returns empty string (no error!)
# print("Python"[100])     # IndexError! Indexing out of range IS an error!
# KEY: Slicing = safe (empty string), Indexing = unsafe (error)

# Q84: What is the output?
print(ord("A"))     # 65    → ord() returns the Unicode/ASCII code of a character
print(ord("a"))     # 97    → lowercase letters have higher codes
print(chr(65))      # "A"   → chr() returns the character for a Unicode code
print(chr(97))      # "a"
# ord() and chr() are INVERSES: chr(ord("A")) = "A", ord(chr(65)) = 65

# Q85: What is the output?
print("hello" > "Hello")  # True! Because 'h' (104) > 'H' (72)
print("abc" < "abd")      # True! 'c' (99) < 'd' (100)
print("apple" < "banana") # True! 'a' (97) < 'b' (98)
# String comparison is LEXICOGRAPHIC (character by character, using Unicode values)
# Uppercase letters (65-90) come BEFORE lowercase (97-122) in Unicode


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 7: LISTS & TUPLES
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# LISTS: Ordered, MUTABLE, allow duplicates. Created with []
# TUPLES: Ordered, IMMUTABLE, allow duplicates. Created with ()
#
#             | List            | Tuple
# ─────────── ──────────────── ─────────────────
# Syntax      | [1, 2, 3]      | (1, 2, 3)
# Mutable?    | YES             | NO
# Methods     | Many (append,   | Few (count, index)
#             |  insert, etc.)  |
# Speed       | Slower          | Faster
# Use case    | Data that       | Data that shouldn't
#             |  changes        |  change (coordinates,
#             |                 |  database records)


# ──────────────────────────────────────────────────────────────────────────────
# Q86: What is the output? (LIST METHODS)
# ──────────────────────────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

# .append(x) → Add x to END of list
fruits.append("date")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# .insert(index, x) → Insert x at specific position
fruits.insert(1, "blueberry")
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date']

# .remove(x) → Remove FIRST occurrence of x (ValueError if not found!)
fruits.remove("banana")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# .pop(index) → Remove and RETURN item at index (default: last item)
last = fruits.pop()
print(last)     # 'date'
print(fruits)   # ['apple', 'blueberry', 'cherry']

first = fruits.pop(0)
print(first)    # 'apple'
print(fruits)   # ['blueberry', 'cherry']

# ALL LIST METHODS THAT MODIFY THE LIST RETURN None!
# EXCEPT .pop() which returns the removed item
result = fruits.append("fig")
print(result)  # None! A very common mistake: x = my_list.append(item)


# ──────────────────────────────────────────────────────────────────────────────
# Q87: What is the output? (SORTING)
# ──────────────────────────────────────────────────────────────────────────────
nums = [5, 2, 8, 1, 9]

# .sort() → Sorts IN PLACE, returns None
result = nums.sort()
print(nums)     # [1, 2, 5, 8, 9]
print(result)   # None! .sort() returns None because it modifies in place.

# sorted() → Returns a NEW sorted list, original unchanged
nums = [5, 2, 8, 1, 9]
new_list = sorted(nums)
print(new_list)  # [1, 2, 5, 8, 9]
print(nums)      # [5, 2, 8, 1, 9] → original is UNCHANGED!

# Descending order:
print(sorted(nums, reverse=True))  # [9, 8, 5, 2, 1]

# THE CRITICAL DIFFERENCE:
# .sort()   → modifies original, returns None → for when you don't need the original
# sorted()  → keeps original, returns new list → for when you need both


# ──────────────────────────────────────────────────────────────────────────────
# Q88: What is the output? (LIST SLICING & COPYING)
# ──────────────────────────────────────────────────────────────────────────────
original = [1, 2, 3, 4, 5]

# Slicing creates a NEW list (shallow copy)
copy1 = original[:]        # Full slice copy
copy2 = original.copy()    # .copy() method
copy3 = list(original)     # list() constructor

# All three are equal but independent:
copy1.append(6)
print(original)  # [1, 2, 3, 4, 5] → unchanged!
print(copy1)     # [1, 2, 3, 4, 5, 6]

# BUT THIS IS NOT A COPY:
not_a_copy = original      # This just creates another reference!
not_a_copy.append(99)
print(original)  # [1, 2, 3, 4, 5, 99] → CHANGED! Both point to same list!

# EXAM TRAP:
# a = b → BOTH variables point to SAME list (alias, not copy)
# a = b[:] → a is a COPY (independent)


# ──────────────────────────────────────────────────────────────────────────────
# Q89: What is the output? (LIST COMPREHENSION — VERY IMPORTANT!)
# ──────────────────────────────────────────────────────────────────────────────

# Basic: [expression for variable in iterable]
squares = [x**2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]

# With condition: [expression for variable in iterable if condition]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# With transformation:
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Nested:
matrix = [[i*3+j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# With if-else (note: the if-else goes BEFORE the for):
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
# SYNTAX: [true_val if condition else false_val for x in iterable]
# ≠ [x for x in iterable if condition]  ← this has no else!


# ──────────────────────────────────────────────────────────────────────────────
# Q90: What is the output? (TUPLES)
# ──────────────────────────────────────────────────────────────────────────────

# Creating tuples
t1 = (1, 2, 3)
t2 = 1, 2, 3          # Parentheses are optional!
t3 = (1,)              # Single-element tuple NEEDS the comma!
t4 = (1)               # This is just the integer 1, NOT a tuple!
t5 = tuple([1, 2, 3])  # Convert list to tuple

print(type(t3))  # <class 'tuple'>
print(type(t4))  # <class 'int'>  ← TRAP!

# Tuple indexing and slicing (same as lists)
t = (10, 20, 30, 40, 50)
print(t[0])      # 10
print(t[-1])     # 50
print(t[1:4])    # (20, 30, 40) → slicing returns a NEW tuple

# Tuple methods (only 2!)
print(t.count(30))  # 1 → How many times 30 appears
print(t.index(30))  # 2 → At what index is 30?

# Tuple is IMMUTABLE:
# t[0] = 99  → TypeError: 'tuple' object does not support item assignment

# BUT! If a tuple contains a mutable object:
tricky = (1, 2, [3, 4])
tricky[2].append(5)        # The LIST inside the tuple CAN be modified!
print(tricky)               # (1, 2, [3, 4, 5])
# The tuple itself didn't change (still has 3 elements).
# But the list at index 2 was modified in place.


# ──────────────────────────────────────────────────────────────────────────────
# Q91: What is the output? (UNPACKING)
# ──────────────────────────────────────────────────────────────────────────────

# Basic unpacking
a, b, c = [1, 2, 3]          # List unpacking
print(a, b, c)                # 1 2 3

x, y, z = (10, 20, 30)       # Tuple unpacking
print(x, y, z)                # 10 20 30

# Extended unpacking with *
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# EXAM TRAP:
# a, b = [1, 2, 3]  → ValueError: too many values to unpack
# a, b, c = [1, 2]  → ValueError: not enough values to unpack
# a, *b = [1]        → a=1, b=[] (empty list — this is valid!)


# ──────────────────────────────────────────────────────────────────────────────
# Q92-Q105: RAPID FIRE — Lists & Tuples
# ──────────────────────────────────────────────────────────────────────────────

# Q92: What is the output?
nums = [1, 2, 3]
nums.extend([4, 5])    # .extend() adds EACH element from another list
print(nums)             # [1, 2, 3, 4, 5]

nums2 = [1, 2, 3]
nums2.append([4, 5])   # .append() adds the WHOLE list as ONE element!
print(nums2)            # [1, 2, 3, [4, 5]]
# BIG DIFFERENCE: extend unpacks, append treats as single item

# Q93: What is the output?
print([1, 2] + [3, 4])    # [1, 2, 3, 4] → concatenation
print([0] * 5)             # [0, 0, 0, 0, 0] → repetition
print(len([1, [2, 3], 4])) # 3 → the inner list counts as ONE element!

# Q94: What is the output?
nums = [3, 1, 4, 1, 5, 9]
print(nums.count(1))     # 2  → 1 appears twice
print(nums.index(4))     # 2  → 4 is at index 2
# .index(x) returns FIRST occurrence. ValueError if not found!

# Q95: What is the output?
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  ← a was also modified! Because b IS a (same object)
print(a is b)  # True → they ARE the same object

# Q96: What is the output?
a = [1, 2, 3]
b = a[:]        # This IS a copy
b.append(4)
print(a)  # [1, 2, 3]  ← a is NOT modified! Because b is a separate copy.
print(a is b)  # False → they are different objects

# Q97: What is del?
nums = [10, 20, 30, 40, 50]
del nums[1]        # Delete by INDEX
print(nums)         # [10, 30, 40, 50]
del nums[1:3]      # Delete a SLICE
print(nums)         # [10, 50]
# del vs .remove(): del uses INDEX, .remove() uses VALUE
# del vs .pop(): del doesn't return the value, .pop() does

# Q98: Nested list access
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])        # [1, 2, 3]  → first row
print(matrix[1][2])     # 6          → row 1, column 2
print(matrix[-1][-1])   # 9          → last row, last column

# Q99: What is the output?
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30]    # Replace slice with different-length list!
print(nums)              # [1, 20, 30, 5]  → indices 1,2,3 replaced with 20,30

# Q100: What is the output?
print(list("Hello"))     # ['H', 'e', 'l', 'l', 'o'] → string → list of chars
print(tuple("Hello"))    # ('H', 'e', 'l', 'l', 'o') → string → tuple of chars
print("".join(['H', 'e', 'l', 'l', 'o']))  # "Hello" → list of chars → string

# Q101: Tuple packing and unpacking
coords = (3, 4)           # Packing
x, y = coords              # Unpacking
print(f"x={x}, y={y}")     # x=3, y=4

# Q102: What can tuples be used for that lists can't?
# Tuples can be DICTIONARY KEYS because they're immutable (hashable)!
locations = {(40.7, -74.0): "New York", (51.5, -0.1): "London"}
print(locations[(40.7, -74.0)])  # "New York"
# Lists CANNOT be dict keys: {[1,2]: "value"} → TypeError: unhashable type: 'list'

# Q103: What is the output?
t = (1, 2, 3) + (4, 5)    # Tuple concatenation
print(t)                    # (1, 2, 3, 4, 5)
t = (1, 2) * 3             # Tuple repetition
print(t)                    # (1, 2, 1, 2, 1, 2)

# Q104: What is the output?
nums = [4, 2, 7, 1, 9]
print(min(nums))      # 1
print(max(nums))      # 9
print(sum(nums))      # 23
print(sorted(nums))   # [1, 2, 4, 7, 9] → new sorted list
print(nums)           # [4, 2, 7, 1, 9] → original unchanged

# Q105: What is the output?
print(3 in [1, 2, 3])          # True  → membership test
print(3 not in [1, 2, 3])      # False
print([1, 2] in [1, 2, 3])     # False → looking for [1,2] as single element!
print([1, 2] in [[1, 2], 3])   # True  → [1,2] IS an element of this list


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 8: DICTIONARIES & SETS
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# DICTIONARIES: Key-Value pairs. Unordered (Python 3.7+: insertion ordered).
#   Keys must be IMMUTABLE (str, int, float, tuple — NOT list!)
#   Keys must be UNIQUE (duplicate keys → last value wins)
#   Lookup is O(1) — constant time!
#
# SETS: Unordered collection of UNIQUE elements.
#   Elements must be IMMUTABLE
#   No duplicates allowed
#   Lookup is O(1) — constant time!
#   Good for: membership testing, removing duplicates, set operations


# ──────────────────────────────────────────────────────────────────────────────
# Q106: What is the output? (DICTIONARIES)
# ──────────────────────────────────────────────────────────────────────────────
student = {"name": "Alice", "age": 25, "grade": "A"}

# Accessing values
print(student["name"])              # "Alice"
print(student.get("age"))           # 25
print(student.get("email", "N/A"))  # "N/A" → key not found, return default
# print(student["email"])           # KeyError! → key not found, raises error!

# IMPORTANT DIFFERENCE:
# dict["key"]      → KeyError if key doesn't exist!
# dict.get("key")  → Returns None if key doesn't exist (no error)
# dict.get("key", default) → Returns default if key doesn't exist

# Adding / Updating
student["email"] = "alice@test.com"   # Add new key
student["age"] = 26                    # Update existing key

# Removing
del student["email"]                   # Delete by key
removed = student.pop("grade")         # Remove and return value
print(removed)                          # "A"
print(student)                          # {'name': 'Alice', 'age': 26}


# ──────────────────────────────────────────────────────────────────────────────
# Q107: What is the output? (ITERATING OVER DICTS)
# ──────────────────────────────────────────────────────────────────────────────
person = {"name": "Bob", "age": 30, "city": "NYC"}

# Iterating over KEYS (default)
for key in person:
    print(key, end=" ")
print()  # name age city

# Iterating over VALUES
for value in person.values():
    print(value, end=" ")
print()  # Bob 30 NYC

# Iterating over KEY-VALUE PAIRS
for key, value in person.items():
    print(f"{key}={value}", end=" ")
print()  # name=Bob age=30 city=NYC

# .keys()   → returns all keys (dict_keys object)
# .values() → returns all values (dict_values object)
# .items()  → returns (key, value) tuples (dict_items object)


# ──────────────────────────────────────────────────────────────────────────────
# Q108: What is the output? (DICT COMPREHENSION)
# ───────────���──────────────────────────────────────────────────────────────────
# Dict comprehension: {key_expr: value_expr for variable in iterable}
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition:
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values:
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}


# ──────────────────────────────────────────────────────────────────────────────
# Q109: What is the output? (SETS)
# ──────────────────────────────────────────────────────────────────────────────
# Creating sets
s1 = {1, 2, 3, 3, 4, 4, 5}
print(s1)           # {1, 2, 3, 4, 5} → duplicates removed!

s2 = set([1, 2, 2, 3, 3, 3])
print(s2)           # {1, 2, 3} → convert list to set removes duplicates

# EMPTY SET:
empty_set = set()    # Correct!
empty_dict = {}      # This is an EMPTY DICT, not a set!
print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>  ← TRAP!

# Adding and removing
s1.add(6)            # Add element
s1.discard(3)        # Remove element (no error if not found)
s1.remove(4)         # Remove element (KeyError if not found!)
print(s1)            # {1, 2, 5, 6}


# ──────────────────────────────────────────────────────────────────────────────
# Q110: What is the output? (SET OPERATIONS)
# ──────────────────────────────────────────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union: elements in EITHER set (combine all)
print(a | b)           # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))      # Same result

# Intersection: elements in BOTH sets (common elements)
print(a & b)           # {4, 5}
print(a.intersection(b))  # Same result

# Difference: elements in a but NOT in b
print(a - b)           # {1, 2, 3}
print(a.difference(b)) # Same result

# Symmetric Difference: elements in EITHER but NOT BOTH
print(a ^ b)                      # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))  # Same result

# Subset and Superset
print({1, 2} <= {1, 2, 3})       # True → {1,2} is subset of {1,2,3}
print({1, 2}.issubset({1, 2, 3}))  # True
print({1, 2, 3} >= {1, 2})       # True → {1,2,3} is superset of {1,2}

# WHEN TO USE SETS:
# → Remove duplicates: list(set(my_list))
# → Fast membership testing: if item in my_set  (O(1) instead of O(n) for lists!)
# → Finding common elements between collections
# → Checking if all required items are present


# ──────────────────────────────────────────────────────────────────────────────
# Q111-Q120: RAPID FIRE — Dicts & Sets
# ──────────────────────────────────────────────────────────────────────────────

# Q111: What is the output?
d = {"a": 1, "b": 2, "a": 3}   # Duplicate key "a"!
print(d)                          # {'a': 3, 'b': 2}
# RULE: Duplicate keys → LAST value wins. No error raised.

# Q112: What is the output?
d = {1: "one", True: "true", 1.0: "one_float"}
print(d)   # {1: 'one_float'}
# WHY? Because 1 == True == 1.0 in Python!
# They're all considered the SAME key. Last value ("one_float") wins.
# MIND-BLOWING EXAM TRAP!

# Q113: What is the output?
d = {"x": 10, "y": 20}
d.update({"y": 30, "z": 40})
print(d)   # {'x': 10, 'y': 30, 'z': 40}
# .update() merges another dict into this one. Existing keys are updated.

# Q114: What is the output?
print("x" in {"x": 10, "y": 20})   # True → "in" checks KEYS, not values!
print(10 in {"x": 10, "y": 20})    # False → 10 is a VALUE, not a key
print(10 in {"x": 10, "y": 20}.values())  # True → now checking values

# Q115: What is the output?
d = dict(name="Alice", age=25)  # Creating dict with keyword syntax
print(d)   # {'name': 'Alice', 'age': 25}

d2 = dict([("a", 1), ("b", 2)])  # Creating dict from list of tuples
print(d2)  # {'a': 1, 'b': 2}

# Q116: What is the output?
d = {"a": 1, "b": 2, "c": 3}
keys_list = list(d.keys())
print(keys_list)  # ['a', 'b', 'c']

values_list = list(d.values())
print(values_list)  # [1, 2, 3]

# Q117: What is the output? (Set comprehension)
s = {x**2 for x in range(5)}
print(s)  # {0, 1, 4, 9, 16} (order may vary — sets are unordered!)

# Q118: What is the output?
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(nums))
print(sorted(unique))  # [1, 2, 3, 4]
# COMMON PATTERN: Remove duplicates by converting to set, then back to list

# Q119: frozenset — IMMUTABLE set
fs = frozenset([1, 2, 3])
# fs.add(4)  → AttributeError! frozenset is immutable
# frozenset can be used as a DICTIONARY KEY (because it's hashable)
d = {fs: "my frozen set"}
print(d[fs])  # "my frozen set"

# Q120: What is the output?
s = {3, 1, 4, 1, 5, 9, 2, 6}
print(s)                # {1, 2, 3, 4, 5, 6, 9} (deduped, order may vary)
print(sorted(s))        # [1, 2, 3, 4, 5, 6, 9] → sorted() returns a LIST!
print(min(s), max(s))   # 1 9
print(sum(s))           # 30
print(len(s))           # 7


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 9: ERROR HANDLING — try / except
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# THEORY:
# ───────
# Errors (Exceptions) crash your program. Error handling lets you catch and
# deal with them gracefully.
#
# SYNTAX:
# try:
#     risky_code
# except ExceptionType:
#     what_to_do_if_error
# else:
#     runs_if_NO_error
# finally:
#     ALWAYS_runs_no_matter_what
#
# COMMON EXCEPTION TYPES:
# ValueError    → Wrong value:  int("hello")
# TypeError     → Wrong type:   "5" + 3
# IndexError    → Bad index:    [1,2,3][5]
# KeyError      → Bad key:      {"a":1}["b"]
# ZeroDivisionError → Divide by zero: 5/0
# NameError     → Undefined variable: print(xyz)
# AttributeError → Wrong method: (1).append(2)
# FileNotFoundError → File doesn't exist: open("xyz.txt")


# ──────────────────────────────────────────────────────────────────────────────
# Q121: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("This always runs.")

# ANSWER:
# Cannot divide by zero!
# This always runs.
#
# TRACE:
# 1. try: 10/0 → raises ZeroDivisionError
# 2. except ZeroDivisionError: → CATCHES the error → prints message
# 3. else: → SKIPPED because an error occurred
# 4. finally: → ALWAYS runs → prints "This always runs."
#
# EXECUTION ORDER:
# → No error:  try → else → finally
# → Error caught: try (until error) → except → finally
# → Error NOT caught: try (until error) → finally → error propagates up!


# ──────────────────────────────────────────────────────────────────────────────
# Q122: What is the output?
# ──────────────────────────────────────────────────────────────────────────────
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")
finally:
    print("Done.")

# ANSWER:
# Result: 5.0
# Done.
#
# No error occurred → except is SKIPPED → else RUNS → finally RUNS


# ──────────────────────────────────────────────────────────────────────────────
# Q123: What is the output? (MULTIPLE EXCEPT BLOCKS)
# ──────────────────────────────────────────────────────────────────────────────
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Invalid types for division!"
    else:
        return result

print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Cannot divide by zero!
print(safe_divide("10", 2))    # Invalid types for division!

# MULTIPLE EXCEPT: You can have as many except blocks as you want.
# Python checks them TOP to BOTTOM. First matching one handles the error.
# Only ONE except block runs (like if/elif).


# ──────────────────────────────────────────────────────────────────────────────
# Q124: What is the output? (CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK)
# ──────────────────────────────────────────────────────────────────────────────
try:
    num = int("hello")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# ANSWER: Error: invalid literal for int() with base 10: 'hello'
#
# You can catch multiple exception types with a TUPLE: (Type1, Type2)
# The "as e" captures the error message in variable "e"


# ──────────────────────────────────────────────────────────────────────────────
# Q125: What is the output? (EXCEPTION HIERARCHY)
# ──────────────────────────────────────────────────────────────────────────────
try:
    x = 1 / 0
except ArithmeticError:  # Parent class of ZeroDivisionError
    print("Caught!")

# ANSWER: Caught!
#
# EXCEPTION HIERARCHY (simplified):
# BaseException
# └── Exception
#     ├── ArithmeticError
#     │   ├── ZeroDivisionError
#     │   ├── OverflowError
#     │   └── FloatingPointError
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     ├── ValueError
#     ├── TypeError
#     └── ... many more
#
# Catching a PARENT class catches all CHILD classes too!
# "except Exception:" catches almost everything (but avoid this — too broad!)


# ──────────────────────────────────────────────────────────────────────────────
# Q126-Q130: RAPID FIRE — Error Handling
# ──────────────────────────────────────────────────────────────────────────────

# Q126: What exception does this raise?
# print(undefined_variable)
# ANSWER: NameError → variable was never defined

# Q127: What exception does this raise?
# my_list = [1, 2, 3]
# my_list[10]
# ANSWER: IndexError → index out of range

# Q128: What exception does this raise?
# my_dict = {"a": 1}
# my_dict["b"]
# ANSWER: KeyError → key doesn't exist

# Q129: What is the output?
def func():
    try:
        return 1
    finally:
        return 2

print(func())
# ANSWER: 2
# TRAP! "finally" ALWAYS runs, even if there's a return in try!
# The finally block's return OVERRIDES the try block's return.

# Q130: Raising your own exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return f"Age {age} is valid."

try:
    print(check_age(25))    # "Age 25 is valid."
    print(check_age(-5))    # Raises ValueError!
except ValueError as e:
    print(f"Error: {e}")    # "Error: Age cannot be negative!"

# "raise" keyword: manually trigger an exception
# Used for: input validation, enforcing rules, signaling errors


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 10: ALGORITHM THINKING & PROBLEM SOLVING
# ██████████████████████████████████████████████████████████████████████████████
# ══════════════════════════════════════════════════════════════════════════════
#
# This section teaches you HOW TO THINK when you see a problem.
# For each pattern, I explain:
# → When to recognize it
# → Which data structure to use
# → The algorithm template
# → A worked example


# ──────────────────────────────────────────────────────────────────────────────
# Q131-Q133: PATTERN — FREQUENCY COUNTING
# ──────────────────────────────────────────────────────────────────────────────
# WHEN TO USE: "How many times does X appear?" / "What is the most common?"
# DATA STRUCTURE: Dictionary (key=item, value=count)

# Q131: Count character frequency in a string
def char_frequency(s):
    """
    Algorithm: FREQUENCY COUNTER
    ─────────────────────────────
    1. Create empty dict
    2. For each character:
       → If already in dict: increment count
       → If not in dict: set count to 1
    3. Return the dict
    
    .get(key, default) method:
    → Returns value if key exists, otherwise returns default
    → freq.get(char, 0) → if char exists, return its count; otherwise return 0
    → Then we add 1 to it
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        # Same as:
        # if char in freq:
        #     freq[char] += 1
        # else:
        #     freq[char] = 1
    return freq

print(char_frequency("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Q132: Find the most frequent element in a list
def most_frequent(lst):
    """Uses frequency counting + max with key function."""
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    
    # max() with key parameter:
    # max(iterable, key=function)
    # → Returns the item that gives the HIGHEST value when function is applied
    # → freq.get gives us the count for each key
    # → So max(freq, key=freq.get) returns the key with highest count
    return max(freq, key=freq.get)

print(most_frequent([1, 2, 3, 2, 2, 3, 1, 2]))  # 2

# Q133: Are two strings anagrams?
def is_anagram(s1, s2):
    """
    Anagram: same characters, different order. "listen" ↔ "silent"
    
    Approach: If both strings have the same character frequencies → anagram!
    
    METHOD 1: Using frequency counting (O(n))
    """
    if len(s1) != len(s2):
        return False
    
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        freq[char] = freq.get(char, 0) - 1
    
    # If all counts are 0, they're anagrams
    return all(v == 0 for v in freq.values())
    # all() returns True if ALL elements are True

# Shortcut method:
def is_anagram_short(s1, s2):
    return sorted(s1) == sorted(s2)  # Sort both and compare

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False


# ──────────────────────────────────────────────────────────────────────────────
# Q134-Q136: PATTERN — TWO POINTER
# ────────────────────────────────────────────────────────────��─────────────────
# WHEN TO USE: Palindromes, pair finding in sorted arrays, reversing
# DATA STRUCTURE: Array/String with two index variables

# Q134: Check if a list is a palindrome
def is_palindrome_list(lst):
    """
    Algorithm: TWO POINTER
    ──────────────────────
    1. One pointer at the START (left = 0)
    2. One pointer at the END (right = len-1)
    3. Compare elements at both pointers
    4. If different → not palindrome
    5. Move pointers toward center
    6. If they meet without mismatch → palindrome!
    
    Time: O(n/2) = O(n) → check half the elements
    Space: O(1) → only two variables
    """
    left = 0
    right = len(lst) - 1
    
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1       # Move left pointer right →
        right -= 1      # Move right pointer left ←
    
    return True

print(is_palindrome_list([1, 2, 3, 2, 1]))   # True
print(is_palindrome_list([1, 2, 3, 4, 5]))   # False

# Q135: Remove duplicates from sorted list (in-place)
def remove_duplicates(nums):
    """
    Two pointers: slow (write position) and fast (scan position)
    
    [1, 1, 2, 2, 3] → we want [1, 2, 3, ...]
    
    slow=0 (write here), fast scans ahead.
    When fast finds a new value → write it at slow+1, advance slow.
    """
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1   # Number of unique elements

nums = [1, 1, 2, 2, 3, 3, 3, 4]
k = remove_duplicates(nums)
print(nums[:k])  # [1, 2, 3, 4]

# Q136: Two Sum on a SORTED array (Two Pointer approach)
def two_sum_sorted(nums, target):
    """
    If the array is SORTED, we can use two pointers instead of a hash map.
    
    Left pointer at start, right at end.
    → Sum too small? Move left right (increase sum)
    → Sum too big? Move right left (decrease sum)
    → Sum equals target? Found it!
    
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1       # Need bigger sum → move left forward
        else:
            right -= 1      # Need smaller sum → move right backward
    
    return []

print(two_sum_sorted([1, 2, 4, 7, 11], 9))  # [1, 3] → nums[1]+nums[3] = 2+7 = 9


# ──────────────────────────────────────────────────────────────────────────────
# Q137-Q139: PATTERN — HASH MAP LOOKUP
# ──────────────────────────────────────────────────────────────────────────────
# WHEN TO USE: "Have we seen this before?" / "Find complement"
# DATA STRUCTURE: Dictionary or Set
# TIME: O(1) lookup instead of O(n) scanning

# Q137: Find first non-repeating character
def first_unique_char(s):
    """
    Step 1: Count frequency of each character → dict
    Step 2: Find first character with count 1
    
    WHY dict? Because counting with dict is O(1) per lookup.
    WHY two passes? First pass counts, second pass finds.
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

print(first_unique_char("leetcode"))      # 0 → 'l' is first unique
print(first_unique_char("aabb"))          # -1 → no unique character

# Q138: Group anagrams together
def group_anagrams(strs):
    """
    KEY INSIGHT: All anagrams have the same sorted form!
    "eat", "tea", "ate" → sorted → "aet", "aet", "aet"
    
    Use sorted form as DICTIONARY KEY, group originals as VALUES.
    
    tuple(sorted(word)): We use tuple because lists can't be dict keys!
    """
    groups = {}
    for word in strs:
        key = tuple(sorted(word))   # "eat" → ('a','e','t')
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Q139: Two Sum (Hash Map — from your course!)
def two_sum(nums, target):
    """
    PATTERN: Complement Lookup
    ──────────────────────────
    For each number: complement = target - number
    "Have we seen the complement before?"
    → Yes: return indices
    → No: store current number and its index
    
    This converts O(n²) brute force to O(n) with a dict!
    """
    seen = {}   # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]


# ──────────────────────────────────────────────────────────────────────────────
# Q140-Q142: PATTERN — STACK
# ──────────────────────────────────────────────────────────────────────────────
# WHEN TO USE: Matching pairs, nested structures, undo operations, expression evaluation
# DATA STRUCTURE: List used as stack (.append = push, .pop = pop)

# Q140: Valid Parentheses (from your course!)
def is_valid_parens(s):
    """
    PATTERN: Stack for Matching
    ───────────────────────────
    Opening bracket → push to stack
    Closing bracket → check if stack top matches
    End → stack should be empty
    
    WHY STACK? Because brackets follow LIFO order.
    The most recent opening bracket must be closed first.
    """
    bracket_map = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for char in s:
        if char in bracket_map:   # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:                      # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

print(is_valid_parens("()[]{}"))   # True
print(is_valid_parens("(]"))       # False
print(is_valid_parens("([])"))     # True

# Q141: Reverse a string using stack
def reverse_with_stack(s):
    """Push all chars, then pop all — LIFO gives reverse order."""
    stack = []
    for char in s:
        stack.append(char)      # Push
    
    result = ""
    while stack:
        result += stack.pop()   # Pop (last in, first out)
    
    return result

print(reverse_with_stack("Hello"))  # "olleH"

# Q142: Evaluate simple expressions with stack
def eval_postfix(expression):
    """
    Postfix notation: "3 4 + 2 *" means (3 + 4) * 2 = 14
    
    Algorithm:
    → Number: push to stack
    → Operator: pop two numbers, apply operator, push result
    """
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()     # Second operand (popped first!)
            a = stack.pop()     # First operand
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            elif token == "/": stack.append(int(a / b))
    
    return stack[0]

print(eval_postfix("3 4 + 2 *"))   # 14 → (3+4)*2


# ──────────────────────────────────────────────────────────────────────────────
# Q143-Q145: PATTERN — SLIDING WINDOW / SIMULATION
# ──────────────────────────────────────────────────────────────────────────────

# Q143: Time to Buy Tickets (from your course!)
from collections import deque

def time_required(tickets, k):
    """
    PATTERN: Queue Simulation
    ─────────────────────────
    Simulate the exact process described:
    → Front person buys 1 ticket
    → If they need more → go to back
    → If done → leave
    → Count seconds until person k finishes
    
    deque (double-ended queue): O(1) for both append and popleft
    Regular list: O(n) for pop(0)! That's why we use deque.
    """
    queue = deque()
    for i, t in enumerate(tickets):
        queue.append((i, t))    # (original_index, tickets_needed)
    
    time = 0
    while queue:
        idx, remaining = queue.popleft()
        remaining -= 1
        time += 1
        
        if idx == k and remaining == 0:
            return time
        
        if remaining > 0:
            queue.append((idx, remaining))
    
    return time

print(time_required([2, 3, 2], 2))      # 6
print(time_required([5, 1, 1, 1], 0))   # 8

# Q144: Maximum sum of subarray of size k
def max_sum_subarray(nums, k):
    """
    PATTERN: SLIDING WINDOW (Fixed Size)
    ─────────────────────────────────────
    Instead of recalculating sum for each window → 
    SLIDE the window: subtract the leaving element, add the entering element.
    
    Window of size k slides from left to right:
    [1, 4, 2, 10, 2, 3, 1, 0, 20] with k=3
    [1, 4, 2]                      sum=7
       [4, 2, 10]                  sum=7-1+10=16
          [2, 10, 2]               sum=16-4+2=14
             ...
    
    Time: O(n) instead of O(n*k)
    """
    # Calculate sum of first window
    window_sum = sum(nums[:k])     # sum(nums[0:k]) → sum of first k elements
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i]       # Add new element (entering window)
        window_sum -= nums[i - k]   # Remove old element (leaving window)
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 3))  # 23 → [1, 0, 20]... wait
# Actually: [1,0,20] → sum=21. Let me retrace: max is actually [3,1,0] no...
# [1,4,2]=7, [4,2,10]=16, [2,10,2]=14, [10,2,3]=15, [2,3,1]=6, [3,1,0]=4, [1,0,20]=21
# Answer: 16? No wait. Let me check: [4,2,10]=16 is max before last window.
# [1,0,20]=21. So answer is 21.
# Actually: sum(nums[-3:]) = 1+0+20 = 21. 21 > 16. So max_sum = 21.
# I need to recheck: The answer is 21.

# Q145: Destination City (from your course!)
def dest_city(paths):
    """
    PATTERN: SET LOOKUP
    ───────────────────
    1. Collect all SOURCE cities in a set
    2. Check each DESTINATION city — if it's not a source → it's the answer
    
    WHY set? Because "in" check is O(1) for sets, O(n) for lists.
    """
    sources = {path[0] for path in paths}    # Set comprehension
    
    for path in paths:
        if path[1] not in sources:
            return path[1]
    
    return None

print(dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
# "Sao Paulo"


# ──────────────────────────────────────────────────────────────────────────────
# Q146-Q150: MIXED ALGORITHM PROBLEMS
# ──────────────────────────────────────���───────────────────────────────────────

# Q146: Fibonacci sequence (Iteration vs Recursion)
def fibonacci_iterative(n):
    """
    Generate first n Fibonacci numbers.
    Fib: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    Each number = sum of two previous numbers.
    
    ITERATIVE approach: O(n) time, O(1) space
    """
    if n <= 0: return []
    if n == 1: return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])   # fib[-1] = last, fib[-2] = second-to-last
    return fib

print(fibonacci_iterative(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Q147: Binary search (O(log n))
def binary_search(nums, target):
    """
    REQUIREMENT: Array must be SORTED!
    
    Algorithm:
    1. Look at middle element
    2. If target = middle → found!
    3. If target < middle → search LEFT half
    4. If target > middle → search RIGHT half
    5. Repeat until found or range is empty
    
    Time: O(log n) — halves the search space each time!
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2    # Find middle index
        
        if nums[mid] == target:
            return mid               # Found!
        elif nums[mid] < target:
            left = mid + 1           # Target is in right half
        else:
            right = mid - 1          # Target is in left half
    
    return -1                        # Not found

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3 (index of 7)
print(binary_search(nums, 6))    # -1 (not found)

# Q148: Bubble Sort (Understanding sorting)
def bubble_sort(nums):
    """
    Compare adjacent elements. If out of order, swap.
    Repeat until no swaps needed.
    
    Time: O(n²), Space: O(1)
    Not efficient, but simple and commonly tested.
    """
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):    # n-i-1: already sorted part at end
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap!
                swapped = True
        if not swapped:
            break    # If no swaps → already sorted → early exit!
    return nums

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# [11, 12, 22, 25, 34, 64, 90]

# Q149: Flatten a nested list
def flatten(nested_list):
    """
    [[1, 2], [3, [4, 5]], 6] → [1, 2, 3, 4, 5, 6]
    
    Uses RECURSION: if element is a list → flatten it. Otherwise, add it.
    
    isinstance(item, list): checks if item is a list.
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursively flatten sublists
        else:
            result.append(item)
    return result

print(flatten([[1, 2], [3, [4, 5]], 6]))  # [1, 2, 3, 4, 5, 6]

# Q150: Matrix rotation — rotate a 2D list 90° clockwise
def rotate_90(matrix):
    """
    Original:       Rotated 90° clockwise:
    1 2 3           7 4 1
    4 5 6    →      8 5 2
    7 8 9           9 6 3
    
    TRICK: Transpose (swap rows/columns) then reverse each row.
    
    zip(*matrix): Unpacks matrix rows and zips columns together.
    * operator unpacks: zip(*[[1,2,3],[4,5,6],[7,8,9]])
                      = zip([1,2,3], [4,5,6], [7,8,9])
                      = [(1,4,7), (2,5,8), (3,6,9)]  ← transposed!
    """
    return [list(row[::-1]) for row in zip(*matrix)]
    # zip(*matrix) transposes
    # row[::-1] reverses each row

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate_90(matrix)
for row in rotated:
    print(row)
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]


# ══════════════════════════════════════════════════════════════════════════════
# ██████████████████████████████████████████████████████████████████████████████
# SECTION 11: FULL MOCK EXAM (40 Questions)
# ██████████████████████████████████████████████████████████████████████████████
# ═════════════════════════════════���════════════════════════════════════════════
#
# PCEP-30-02 Format:
# → 40 questions
# → 45 minutes
# → 70% to pass (28/40)
# → Mix of: single-choice, multiple-choice, fill-in-blank, code output
#
# Below is a realistic mock exam. Try to solve WITHOUT looking at answers first!
# Time yourself: 45 minutes.


print("\n" + "=" * 70)
print("MOCK EXAM — 40 QUESTIONS")
print("=" * 70)

# ────────────── MOCK EXAM Q1 ──────────────
# What is the output of the following code?
print(2 ** 3 ** 2)
# A) 64    B) 512    C) 256    D) 12
# ANSWER: B) 512
# WHY: ** is right-associative → 2 ** (3 ** 2) = 2 ** 9 = 512

# ────────────── MOCK EXAM Q2 ──────────────
# What is the output?
x = 17
print(x // 3, x % 3)
# A) 5 2    B) 5.67 2    C) 6 -1    D) 5 3
# ANSWER: A) 5 2
# WHY: 17 // 3 = 5 (floor), 17 % 3 = 2 (remainder: 17 - 5*3 = 2)

# ────────────── MOCK EXAM Q3 ──────────────
# What is the output?
print(type(10 / 2))
# A) <class 'int'>    B) <class 'float'>    C) <class 'str'>    D) Error
# ANSWER: B) <class 'float'>
# WHY: / ALWAYS returns float. Even 10/2 = 5.0 (not 5)

# ────────────── MOCK EXAM Q4 ──────────────
# What is the output?
print(bool(0), bool(""), bool([]), bool("0"))
# A) False False False False
# B) False False False True
# C) False True False True
# D) True False False True
# ANSWER: B) False False False True
# WHY: "0" is a non-empty string → truthy! Only "" is falsy.

# ────────────── MOCK EXAM Q5 ──────────────
# What is the output?
x = 5
y = 10
x, y = y, x + y
print(x, y)
# A) 10 15    B) 10 20    C) 15 10    D) 5 15
# ANSWER: A) 10 15
# WHY: Right side evaluated first with OLD values: y=10, x+y=5+10=15
#      Then assign: x=10, y=15

# ────────────── MOCK EXAM Q6 ──────────────
# What is the output?
for i in range(5, 0, -2):
    print(i, end=" ")
print()
# A) 5 3 1    B) 5 3 1 -1    C) 5 4 3 2 1    D) 0 2 4
# ANSWER: A) 5 3 1
# WHY: range(5, 0, -2) → 5, 3, 1 (next would be -1, but -1 < stop=0... wait)
# Actually range stops when value would pass stop. -1 < 0 so it's not included.
# Wait: range(5, 0, -2): 5, 3, 1. Next: -1, but -1 < 0? range with negative step
# stops when value <= stop. 1 > 0 so it's included. -1 <= 0 so STOP.
# Answer: 5 3 1

# ────────────── MOCK EXAM Q7 ──────────────
# What is the output?
word = "Python"
print(word[1:4])
print(word[::-1])
# A) "Pyt" and "nohtyP"
# B) "yth" and "nohtyP"
# C) "yth" and "Python"
# D) "ytho" and "nohtyP"
# ANSWER: B) "yth" and "nohtyP"
# WHY: [1:4] → indices 1,2,3 → 'y','t','h' → "yth"
#      [::-1] → reverse → "nohtyP"

# ────────────── MOCK EXAM Q8 ──────────────
# What is the output?
nums = [1, 2, 3, 4, 5]
print(nums[1:4])
nums[1:4] = [20, 30]
print(nums)
# ANSWER:
# [2, 3, 4]
# [1, 20, 30, 5]
# WHY: Slice assignment can replace with different number of elements

# ────────────── MOCK EXAM Q9 ──────────────
# What is the output?
def func(a, b=5, c=10):
    return a + b + c

print(func(1))
print(func(1, 2))
print(func(1, c=20))
# ANSWER:
# 16  (1 + 5 + 10)
# 13**
