import yfinance as yf
import stock as st


class paper_account:

    def __init__(self, account_name, balance):
        self.name = account_name
        self.balance = balance
        self.stocks = {}

    def calculate_stock_worth(self):
        # Initialize stock names, quantity and total asset price
        assets = 0

        # Pull ticker info
        tickers = yf.Tickers(list(self.stocks.keys()))

        # Sum up assets
        for stock in self.stocks:
            assets += tickers.tickers[stock].info["regularMarketPrice"] * \
                int(self.stocks.get(stock).quantity)
        return assets

    def buy(self, stock, quantity):
        # Pull ticker info
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]

        if stock in self.stocks:
            self.stocks[stock].add_position(price, quantity)
        else:
            self.stocks[stock] = st.stock(price, quantity)

        # Take money
        self.balance -= price * quantity

    def sell(self, stock, quantity):
        # Pull ticker info
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]

        if stock in self.stocks:
            if self.stocks[stock].quantity > quantity:
                self.stocks[stock].remove_position(quantity)
            elif self.stocks[stock].quantity == quantity:
                self.stocks.pop(stock)
            else:
                print("Oversold")
                return

            # Give money
            self.balance += price * quantity

    def __repr__(self):
        assets = self.calculate_stock_worth()
        quantity = []
        stocks = list(self.stocks.keys())
        for stock in self.stocks:
            quantity.append(self.stocks.get(stock).quantity)
        return f'Account {self.name} has: {self.balance} \nis worth ${assets} \nand is invested in {stocks} \nat {quantity} quantity'
