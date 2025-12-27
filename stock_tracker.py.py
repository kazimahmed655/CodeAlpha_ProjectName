def stock_portfolio_tracker():
    # 1. Define hardcoded stock prices (Dictionary)
    # In a real application, these would be fetched from a live API.
    stock_prices = {
        "AAPL": 150.00,
        "GOOGL": 2800.00,
        "TSLA": 700.00,
        "AMZN": 3400.00,
        "MSFT": 300.00
    }
    
    portfolio = {}
    total_value = 0.0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks: AAPL, GOOGL, TSLA, AMZN, MSFT")
    
    # 2. Input Loop
    while True:
        symbol = input("\nEnter stock symbol to add (or 'exit' to finish): ").upper()
        
        if symbol == 'EXIT':
            break
            
        if symbol in stock_prices:
            try:
                # Get quantity from user
                quantity = int(input(f"Enter quantity for {symbol}: "))
                
                # Add to portfolio dictionary
                if symbol in portfolio:
                    portfolio[symbol] += quantity
                else:
                    portfolio[symbol] = quantity
                    
                print(f"Added {quantity} shares of {symbol}.")
                
            except ValueError:
                print("Invalid input! Please enter a number for quantity.")
        else:
            print("Stock not found in our list. Please choose from the available stocks.")

    # 3. Calculate and Display Report
    print("\n" + "="*30)
    print("📊 YOUR PORTFOLIO SUMMARY")
    print("="*30)
    print(f"{'Stock':<10} {'Price':<10} {'Qty':<10} {'Total':<10}")
    print("-" * 40)
    
    report_lines = [] # To store lines for file saving later
    
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        total_value += value
        
        # Display row
        row = f"{symbol:<10} ${price:<9} {qty:<10} ${value:,.2f}"
        print(row)
        report_lines.append(row)
        
    print("-" * 40)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")
    
    # 4. Optional: Save to File (File Handling)
    save_choice = input("\nDo you want to save this report to a file? (y/n): ").lower()
    if save_choice == 'y':
        try:
            with open("portfolio_report.txt", "w") as file:
                file.write("=== Portfolio Report ===\n")
                for line in report_lines:
                    file.write(line + "\n")
                file.write(f"\nTOTAL VALUE: ${total_value:,.2f}")
            print("Report saved as 'portfolio_report.txt'.")
        except IOError:
            print(" Error saving file.")

# Run the program
if __name__ == "__main__":
    stock_portfolio_tracker()