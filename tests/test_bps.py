import unittest

from src.co_data.bps import parse_bps_text


COUNTY_FIXTURE = """Survey,FIPS,FIPS,Region,Division,County,,1-unit,,,2-units,,,3-4 units,,,5+ units,,,1-unit rep,,,2-units rep,,,3-4 units rep,,, 5+units rep
Date,State,County,Code,Code,Name,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value,Bldgs,Units,Value
2025,08,107,4,8,Routt County                ,196,196,291811809,0,0,0,0,0,0,1,3,5800000,196,196,291811809,0,0,0,0,0,0,1,3,5800000
"""


class TestBPSParser(unittest.TestCase):
    def test_parse_bps_text(self) -> None:
        rows = parse_bps_text(COUNTY_FIXTURE)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["survey_date"], "2025")
        self.assertEqual(rows[0]["fips_state"], "08")
        self.assertEqual(rows[0]["fips_county"], "107")
        self.assertEqual(rows[0]["county_name"], "Routt County")


if __name__ == "__main__":
    unittest.main()
