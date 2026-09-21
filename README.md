# GrowthCalc

A financial planning suite built with [Netlify].

## What it does

GrowthCalc is four independent calculators in one app:

### 1. Investment Calculator
Models compound growth on a starting amount plus monthly contributions over time, using standard monthly-compounding math. Shows the ending balance and a growth curve.

### 2. Retirement Checker
Projects your savings to a target retirement age, then checks the result against the **4% rule** — a common guideline stating you can safely withdraw ~4% of your savings per year in retirement without running out of money.

### 3. Tax-Advantaged vs. Taxable Comparison
Runs two growth simulations side by side: one that taxes investment growth every year (a taxable brokerage account), and one that grows untouched and is only taxed once at withdrawal (like a 401(k) or IRA). Shows the real dollar impact taxes have on long-term growth.

### 4. Loan Payoff Calculator
Calculates a fixed monthly payment using the standard loan amortization formula, then simulates the loan paying down month by month — splitting each payment into interest and principal, and tracking cumulative interest paid over the life of the loan.

## Tech stack

- Netlify
- No database, no backend framework — all calculations run client-side in the Netlify script itself


## What I learned building this

- How Netlify/ Streamlit rerun model works — the whole script re-executes top to bottom on every interaction
- Compound interest math, amortization formulas, and the 4% retirement rule
- Streamlit quirks: `$` triggers LaTeX math mode in Markdown-rendering functions (`st.write`, `st.error`, `st.success`) but not in `st.metric`, which renders plain text 
- netlify commands and software setup.
- Why indentation in Python is control flow, not just style. Several bugs in this project came directly from misplaced indentation

## AI

I used AI as a helper to explain certain concepts to me, however all code was written by me. AI showed me mistakes and I implemented the fixes.



# BIG CHANGES

- Completely revamped the entire software and reaplace almost all python lines for HTML and Javascript.
- Changed the deployment software from Streamlit to netlify (via Stardance's rules).