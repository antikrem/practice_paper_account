import yfinance as yf

class paper_account:

    def __init__(self, account_name, balance):
        self.name = account_name
        self.balance = balance
        self.stocks = []

    def __repr__(self):
        assets = 0;
        for stock in self.stocks:
            ticker = yf.Ticker(stock)
            assets += ticker.info["regularMarketPrice"]

        return 'Account %s has: $%s \nis worth $%s \nand is invested in %s' % (self.name, self.balance, assets, self.stocks)

    def buy(self, stock):
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]
        self.balance -= price
        self.stocks.append(stock)
