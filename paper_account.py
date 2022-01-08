import yfinance as yf

class paper_account:

    def __init__(self, account_name, balance):
        self.name = account_name
        self.balance = balance
        self.stocks = []

    def calculate_stock_worth(self):
        assets = 0
        for stock in self.stocks:
            ticker = yf.Ticker(stock)
            assets += ticker.info["regularMarketPrice"]
        return assets

    def buy(self, stock):
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]
        self.balance -= price
        self.stocks.append(stock)

    def sell(self, stock):
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]
        self.balance += price
        self.stocks.remove(stock)

    def __repr__(self):
        assets = self.calculate_stock_worth();
        return 'Account %s has: $%s \nis worth $%s \nand is invested in %s' % (self.name, self.balance, assets, self.stocks)
