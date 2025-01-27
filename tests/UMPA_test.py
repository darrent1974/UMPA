"""
Testing UMPA
"""

import pytest
from UMPA import match, match_unbiased
from UMPA import utils as u


@pytest.fixture()
def s():
    yield u.prep_simul()


class TestUMPA:

    def test_UMPA(self, s):
        result = match(s["meas"], s["ref"], Nw=1, step=10)

        assert result

    def test_UMPA_unbiased(self, s):
        result = match_unbiased(s["meas"], s["ref"], Nw=1, step=10)

        assert result
