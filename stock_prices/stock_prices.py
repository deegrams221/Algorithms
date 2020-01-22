#!/usr/bin/python

import argparse

def find_max_profit(prices):
# return the maximum profit that can be made from a single buy and sell
# you must buy first before selling; no shorting is allowed here

    # set the current min price equal to first price in the list
    current_min_price_so_far = prices[0]
    # set the max profit equal to first price subtracted from max price in the list
    max_profit_so_far = prices[1] - prices[0]

    # loop through the index in range(starting at 1, comparing to len of prices list)
    for i in range(1, len(prices)):
        # if the index of prices is less than the current min prices, then the
        # current min price is equal to the index of prices
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
        # else if the diff between the index of prices and the current min price is
        # greater than the current max profit, then the max profit is equal to the
        # diff between the min and max prices
        elif prices[i] - current_min_price_so_far > max_profit_so_far:
            max_profit_so_far = prices[i] - current_min_price_so_far
    # retrun the max profit
    return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))