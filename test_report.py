import pytest
from test_data import parsed_report
from sprint import parse_report
import json

def test_report():
    with open("train/report1.json") as file:
        report = json.load(file)
        assert parse_report(report) == parsed_report
        

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
