# GrowthCalc

A pure-Python financial planning suite built with [Streamlit] — all python.

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

- Python 3
- Streamlit — for the entire UI (sliders, tabs, charts, metrics), no separate frontend code
- No database, no backend framework — all calculations run client-side in the Streamlit script itself

## Running it locally

```bash
git clone https://github.com/Shashyster/growthcalc.git
cd growthcalc
pip install streamlit
streamlit run app.py
```

## What I learned building this

- How Streamlit's rerun model works — the whole script re-executes top to bottom on every interaction
- Compound interest math, amortization formulas, and the 4% retirement rule
- Streamlit quirks: `$` triggers LaTeX math mode in Markdown-rendering functions (`st.write`, `st.error`, `st.success`) but not in `st.metric`, which renders plain text
- Why indentation in Python is control flow, not just style — several bugs in this project came directly from misplaced indentation

## AI

I did use Claude (Anthropic) as a line-by-line teaching assistant — however all code was explained and typed by hand, and I understood every single line perfectly and what exactly it does. Claude pointed out errors and I implemented the fixes.