# Instructions
 # Coin Flip Streak Analysis

## Overview

This project explores a fascinating aspect of human psychology: our inability to generate truly random sequences. Through a simple coin flip experiment, we demonstrate how humans consistently fail to replicate the streak patterns that occur naturally in random data.

## The Experiment

### Human vs. True Randomness

When you flip a coin 100 times and record each result, you might get something like:

```
T T T T H H H H T T ...
```

However, when asked to *imagine* 100 random coin flips, humans typically produce alternating patterns like:

```
H T H T H H T H T T ...
```

While this looks "random" to us, it's mathematically not random at all. **Humans almost never write down streaks of six consecutive heads or tails**, even though such streaks are highly likely in truly random sequences.

## The Challenge

Write a program to determine how often a streak of six heads or six tails occurs in randomly generated coin flip sequences.

### Requirements

Your program should:

1. **Generate** a list of 100 randomly selected 'heads' and 'tails' values
2. **Check** if there is a streak of six consecutive identical results
3. **Repeat** this experiment 10,000 times
4. **Calculate** the percentage of sequences containing at least one streak

### Implementation Hint

Use `random.randint(0, 1)` to simulate coin flips:
- Returns `0` 50% of the time
- Returns `1` 50% of the time

## Expected Learning Outcomes

- Understanding probability and randomness
- Recognizing human biases in generating random data
- Practice with loops, conditionals, and statistical analysis
- Experience with Monte Carlo simulation methods

## Results

After running 10,000 simulations, you'll discover that streaks of six are far more common than most people intuitively expect, highlighting our predictable failure at being random.

---

*This exercise demonstrates the difference between perceived randomness and true statistical randomness.*