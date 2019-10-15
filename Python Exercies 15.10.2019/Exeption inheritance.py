"""
1. we’ve defined a CandleShop class for our new candle shop that we’ve named Here’s a Hot Tip: Buy Drip Candles. We want to define our own exceptions for when we run out of candles to sell.

Define your own exception called OutOfStock that inherits from the Exception class.

2. Have CandleShop raise your OutOfStock exception when CandleShop.buy() tries to buy a candle that’s out of stock.

"""

# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')
