import csv
def portfolio_cost(filename, errors="warn"):
    """
        This function returns total_cost : total_cost = shares * price
    """
    if errors not in {"warn", "raise", "ignore"}:
        raise ValueError("errors must be one of 'warn'/'ignore'/'raise'")
    total_cost = 0.0
    with open(filename, "r") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_no, row in enumerate(rows, 2):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == "warn":
                    print("Encountered error at line no.", row_no, "\nRow :", row)
                    print("Error:", err)
                elif errors == "raise":
                    raise
                continue
            total_cost += (row[2] * row[3])
        return total_cost


total = portfolio_cost("Data/portfolio.csv")
print("Total cost:", total)
# help(portfolio_cost)