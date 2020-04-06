import sys
sys.path.append('.') # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác
import logging
# define top level module logger
logger = logging.getLogger(__name__)

from datamodels.crms.qlt_params import *
from datamodels.crms.qlt_thongtins import QLT_THONGTINVIPHAM
from typing import List
from services.crmsservices import *
from utils.constants import *

class process_rank_hsvp:
    def __init__(self, _lstHSVPs: [], _params_hsvp: {}):
        self._hsvp_params = _params_hsvp
        self._HSVPs: List[QLT_THONGTINVIPHAM] = _lstHSVPs
