"""
Create CSV file of below format
Year,Month,Company A, Company B,Company C, .............Company N

1990, Jan, 10, 15, 20, , ..........,50

1990, Feb, 10, 15, 20, , ..........,50
.
.
2013, Sep, 50, 10, 15............500

Solve below exercise with Generated CSV File
a) List for each Company year and month in which the share price was highest.

b) Submit a unit test with sample data to support your solution.
author: Vikas Kumar
"""
from random import randint
import csv
import logging
logging.basicConfig(filename='error.log',level=logging.ERROR)

class MaxSharePrice:
    def generate_csv(self, no_of_companies=10, filename="data.csv",
                            year_range=(1990,2005), data_range=(10,50)):
        """
        generate problem csv file depending upon parameters
        """
        months = ['January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September', 'October', 'November',
        'December']

        with open(filename, "wb") as f:
            writer = csv.writer(f)
            header = ["year", "month"]
            for comp in range(0, no_of_companies):
                header.append("company_" + str(comp))
            writer.writerow(header)

            for year in range(*year_range):
                for month in months:
                    row = [year, month]
                    for comp in range(0, no_of_companies):
                        row.append(randint(*data_range))
                    writer.writerow(row)
        return filename

    def _validate_data(self,data,comp_names):
        """
            Validate Data Row from empty data and negative Values
            skiping those rows having invalid data
        """
        ## if year/month is not valid name
        if len(data['year'].strip()) == 0: raise ValueError("Year is Empty")
        if len(data['month'].strip()) == 0: raise ValueError("Month is Empty")
        for company in comp_names:
            if len(data[company].strip()) == 0: raise ValueError("price is Empty")
            if float(data[company]) < 0 : raise ValueError("price is -ve")

    def maximum_of_each_company(self, filename="data.csv"):
        """
        function will return a list having each element as dictionary
        {year:value, month:value, max_share_value=value}
        """
        with open(filename) as f:
            dict_reader = csv.DictReader(f)
            companies = {}
            comp_names = []
            for comp in  dict_reader.fieldnames[2:]:
                companies[comp] = {'year':'', 'month':'',
                                        'max_value':-1}
                comp_names.append(comp)

            for row in dict_reader:
                try:
                    self._validate_data(row,comp_names)
                    for comp in  dict_reader.fieldnames[2:]:

                        if float(row[comp]) > float(companies[comp]['max_value']):
                            companies[comp]['year'] = row['year']
                            companies[comp]['month'] = row['month']
                            companies[comp]['max_value'] = row[comp]
                except ValueError,e:
                    logging.error("ValueError %s:\n %s\n"%(e,row))

                except Exception as e:
                    logging.error("Exception %s:\n%s\n"%(e,row))
            print "Please check error.log for checking errors in file"
            return companies

if __name__ == "__main__":
    filename = "testdata/data.csv"
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    ex = MaxSharePrice()
    #filename = ex.generate_csv(data_range=(0,50))
    companies = ex.maximum_of_each_company(filename=filename)
    for key,value in companies.items():
        print key," : ",value

