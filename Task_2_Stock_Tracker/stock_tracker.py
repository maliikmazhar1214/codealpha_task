# Stock Portfolio Tracker
# CodeAlpha Internship Task 2

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

def get_user_portfolio():
    portfolio = {}
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished.\n")

    while True:
        stock_name = input("Enter stock name: ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print(f"'{stock_name}' not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}.\n")

    return portfolio


def calculate_investment(portfolio):
    total = 0
    details = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        details.append((stock, qty, price, value))

    return details, total


def display_summary(details, total):
    print("\n----- Investment Summary -----")
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    for stock, qty, price, value in details:
        print(f"{stock:<10}{qty:<8}{price:<10}{value:<10}")
    print("-" * 38)
    print(f"Total Investment Value: ${total}")


def save_to_file(details, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 38 + "\n")
        f.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        for stock, qty, price, value in details:
            f.write(f"{stock:<10}{qty:<8}{price:<10}{value:<10}\n")
        f.write("-" * 38 + "\n")
        f.write(f"Total Investment Value: ${total}\n")
    print(f"\nSummary saved to '{filename}'")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_user_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    details, total = calculate_investment(portfolio)
    display_summary(details, total)

    save_choice = input("\nSave summary to file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_to_file(details, total)


if __name__ == "__main__":
    main()