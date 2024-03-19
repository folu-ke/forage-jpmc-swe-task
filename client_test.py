import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2))


  """ ------------ Add more unit tests ------------ """
  
  # get price with bid less than ask
  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quotes = [
      {'top_ask': {'price': 129.1, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 170.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 189.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 200.98, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2))
  
  # get price and ask are equal to zero
  def test_getDataPoint_calculatePriceBidAskEqualZero(self):
    quotes = [
      {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2))
  
  # get price when size is zero
  def test_getDataPoint_calculatePriceWithZeroSize(self):
    quotes = [
      {'top_ask': {'price': 109.1, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 170.48, 'size': 0}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 189.0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 90.98, 'size': 0}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2))


if __name__ == '__main__':
    unittest.main()
