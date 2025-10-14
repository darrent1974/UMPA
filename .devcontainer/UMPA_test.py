import UMPA
from UMPA.model import UMPAModelNoDF

from UMPA import match, match_unbiased
from UMPA import utils as u

s = UMPA.utils.prep_simul()
s = u.prep_simul()
T = s["T"]
dx = s["dx"]
dy = s["dy"]
positions = s["pos_sample"]
ref = s["ref"]
meas = s["meas"]

result_1 = match(meas, ref, Nw=1, step=10)

result_2 = match_unbiased(meas, ref, Nw=1, step=10)
