import numpy as np
import pandas as pd

import yfinance as yf

import paper_account as acc

def read_input(command, account):

    #Split Command and inputs
    split = command.upper().split(' ')
    #Get first word
    command = split[0]
    match command:

        #Buy Action
        case 'BUY':
            bought_stock = split[1]
            quantity = split[2]
            account.buy(bought_stock, int(quantity))
            #print(account)

        #Sell Action
        case 'SELL':
            sold_stock = split[1]
            quantity = split[2]
            account.sell(sold_stock, int(quantity))
            #print(account)

        #Check account
        case 'CHECK':
            print(account)

        #No Command Found
        case _:
            print('Invalid Command \n')

def main():

    #Create wallet
    account = acc.paper_account('test', 0)

    #Command Loop
    while 1:
        print('Enter Command')
        command = input()
        read_input(command, account)

if __name__ == '__main__':
    main()
