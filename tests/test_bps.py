import unittest

from src.co_data.bps import parse_bps_text


COUNTY_FIXTURE = """Survey,FIPS,FIPS,Region,Division,County,,1-unit,,,2-units,,,3-4 units,,,5+ units,,,1-unit rep,,,2-units rep,,,3-4 units rep,,, 5+units rep
Date,State,County,Code,Code,Name,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value
2025,08,107,4,8,Routt County                ,196,196,291811809,0,0,0,0,0,0,1,3,5800000,196,196,291811809,0,0,0,0,0,0,1,3,5800000
"""

PLACE_FIXTURE = """Survey,State,6-Digit,County,Census Place,FIPS Place,FIPS MCD,Pop,CSA,CBSA,Footnote,Central,Zip,Region,Division,Number of,Place,,1-unit,,,2-units,,,3-4 units,,,5+ units,,,1-unit rep,,,2-units rep,,,3-4 units rep,,,5+ units rep
Date,Code,ID,Code,Code,Code,Code,  ,Code,Code,Code,City,Code,Code,Code,Months Rep,Name,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value
2025,08,559000,107,6115,73825,00000,13000,999,44460,,2,80487,4,8,12,Steamboat Springs,10,10,1000000,0,0,0,0,0,0,1,20,3000000,10,10,1000000,0,0,0,0,0,0,1,20,3000000
"""


class TestBPSParser(unittest.TestCase):
    def test_parse_bps_text(self) -> None:
        rows = parse_bps_text(COUNTY_FIXTURE)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["survey_date"], "2025")
        self.assertEqual(rows[0]["fips_state"], "08")
        self.assertEqual(rows[0]["fips_county"], "107")
        self.assertEqual(rows[0]["county_name"], "Routt County")

    def test_parse_place_headers(self) -> None:
        rows = parse_bps_text(PLACE_FIXTURE)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["state_code"], "08")
        self.assertEqual(rows[0]["county_code"], "107")
        self.assertEqual(rows[0]["fips_place_code"], "73825")
        self.assertEqual(rows[0]["place_name"], "Steamboat Springs")


if __name__ == "__main__":
    unittest.main()
