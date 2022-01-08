import yfinance as yf
import stock as st

class paper_account:

    def __init__(self, account_name, balance):
        self.name = account_name
        self.balance = balance
        self.stocks = []

    def calculate_stock_worth(self):

        #Initialize stock names, quantity and total asset price
        assets = 0
        stock_names = []
        stock_qty = []

        #Build list
        for stock in self.stocks:
            stock_names.append(stock.ticker)
            stock_qty.append(stock.quantity)

        #Pull ticker info
        tickers = yf.Tickers(stock_names)

        #Sum up assets
        for stock, quantity in zip(tickers.tickers, stock_qty):
            assets += tickers.tickers[stock].info["regularMarketPrice"] * int(quantity)
        return assets

    def buy(self, stock, quantity):

        #Pull ticker info
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]

        #Take money
        self.balance -= price * int(quantity)

        #Check for pre-existing stock
        is_in_list = False

        for stocks in self.stocks:
            if stock == stocks.ticker:
                stocks.add_position(price, quantity)
                is_in_list = True

        #If it is not in the list append
        if not is_in_list:
            obj_stock = st.stock(stock, price, quantity)
            self.stocks.append(obj_stock)

    def sell(self, stock):

        #Pull ticker info
        ticker = yf.Ticker(stock)
        price = ticker.info["regularMarketPrice"]

        #Give money
        self.balance += price

        #Remove stock
        self.stocks.remove(stock)

    def __repr__(self):
        assets = self.calculate_stock_worth()
        stock_names = []
        stock_qty = []
        for stock in self.stocks:
            stock_names.append(stock.ticker)
            stock_qty.append(stock.quantity)
        return 'Account %s has: $%s \nis worth $%s \nand is invested in %s \nat %s quantity' % (self.name, self.balance, assets, stock_names, stock_qty)
