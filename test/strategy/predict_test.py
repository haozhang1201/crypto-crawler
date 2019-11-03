import unittest
from src.common.app_util import get_system_milli
from src.strategy.predict import arima, create_crypto_file, arima_validation, earning_calculation


class SignalTest(unittest.TestCase):
    crypto_list = []
    price_milli = get_system_milli()

    def setUp(self):
        pass

    def testCreateTrainTest(self):
        create_crypto_file()
        self.assertTrue(True)

    # Returns True or False.
    def testPredictARIMA(self):
        arima()
        self.assertTrue(True)

    def testArimaValidation(self):
        pred = arima()
        arima_validation(pred)
        self.assertTrue(True)

    def testEarningCalculation(self):
        pred = arima()
        earning1 = earning_calculation(arima(), 0.0007)    # 0.07%
        earning2 = earning_calculation(arima(), 0.002)    # 0.2%
        self.assertTrue(earning1 > 1000)
        self.assertTrue(earning2 <= 0)


if __name__ == '__main__':
    unittest.main()
