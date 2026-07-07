# Stock Portfolio Tracker

## CodeAlpha Internship Task 2

A simple Python-based Stock Portfolio Tracker that allows users to enter their stock holdings, calculate the total investment value, display a portfolio summary, and save the report into a text file.

---

## Features

- Display available stocks with their current prices.
- Add multiple stocks to a personal portfolio.
- Validate stock names before adding.
- Accept and calculate share quantities.
- Calculate individual stock investment values.
- Calculate total portfolio investment value.
- Display a formatted investment summary.
- Save portfolio details into a text file.
- Handles invalid inputs gracefully.

---

## Technologies Used

- Python 3
- File Handling
- Dictionaries
- Functions
- User Input Handling
- Exception Handling

---

## How It Works

1. The program contains a predefined dictionary of stock symbols and their prices.

Example:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}
```

2. The user enters stock names and quantities.

3. The program calculates:

```
Investment Value = Stock Price × Number of Shares
```

4. A complete portfolio summary is displayed.

5. The user can save the report as:

```
portfolio_summary.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to Project Directory

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Program

```bash
python portfolio_tracker.py
```

---

## Usage Example

```
=== Stock Portfolio Tracker ===

Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT
Enter 'done' when finished.

Enter stock name: AAPL
Enter quantity of AAPL: 10

Added 10 shares of AAPL.

Enter stock name: TSLA
Enter quantity of TSLA: 5

Added 5 shares of TSLA.

Enter stock name: done
```

### Output:

```
----- Investment Summary -----
Stock     Qty     Price     Value
AAPL      10      180       1800
TSLA      5       250       1250
--------------------------------------
Total Investment Value: $3050
```

---

## File Output

If the user chooses to save the report, the program creates:

```
portfolio_summary.txt
```

Example:

```
Stock Portfolio Summary
======================================
Stock     Qty     Price     Value
AAPL      10      180       1800
TSLA      5       250       1250
--------------------------------------
Total Investment Value: $3050
```

---

## Project Structure

```
Stock-Portfolio-Tracker/
│
├── portfolio_tracker.py
├── README.md
└── portfolio_summary.txt
```

---

## Functions Overview

| Function | Description |
|----------|-------------|
| `get_user_portfolio()` | Takes stock names and quantities from the user |
| `calculate_investment()` | Calculates individual and total investment values |
| `display_summary()` | Displays portfolio details in formatted output |
| `save_to_file()` | Saves portfolio summary into a text file |
| `main()` | Controls the complete program execution |

---

## Error Handling

The program handles:

- Invalid stock symbols.
- Non-numeric quantities.
- Negative share quantities.
- Empty portfolios.

---

## Future Improvements

Possible enhancements:

- Connect with a live stock market API.
- Add stock price updates automatically.
- Create a graphical user interface (GUI).
- Add user accounts and authentication.
- Store multiple portfolios.
- Add profit/loss tracking.
- Export reports as CSV or Excel files.

---

## Author

Developed as part of the **CodeAlpha Internship Task 2**.
