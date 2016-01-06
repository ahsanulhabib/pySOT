try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from experimental_design import *
from rbf_interpolant import *
from rbf_surfaces import *
from rs_capped import *
from sampling_strategies import *
from test_problems import *
from sot_sync_strategies import *
from ensemble_surrogate import EnsembleSurrogate

try:
    from GUI import GUI
except ImportError:
    pass

try:
    from mars_interpolant import MARSInterpolant
except ImportError:
    pass

try:
    from kriging_interpolant import KrigingInterpolant
except ImportError:
    pass
