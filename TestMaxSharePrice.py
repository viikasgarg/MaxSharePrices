import unittest
from max_share_price import MaxSharePrice
class MaxSharePriceTests(unittest.TestCase):
    """
    tested with attached data.csv
    """
    def testSharePrice(self):
        # manually verified Test cases
        # filename: result
        from testdata.testfile import tests
        ex = MaxSharePrice()
        for filename in tests.keys():
            companies = ex.maximum_of_each_company(filename=filename)
            try:
                self.failUnless(cmp(companies,tests[filename]) == 0)
            except:
                print "data File:",filename
                print "Calculated result:",companies
                print "Expected Result:",tests[filename]
                raise

if __name__ == "__main__":
    unittest.main()
