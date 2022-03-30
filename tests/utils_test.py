
# this is the "tests/utils_test.py" file...

from app.utils import to_usd

def test_to_usd():

    # two decimal places
    assert to_usd(0.45555) == "$0.46"

    # thousands seperator
    assert to_usd(123456789.98) == "$123,456,789.98"

