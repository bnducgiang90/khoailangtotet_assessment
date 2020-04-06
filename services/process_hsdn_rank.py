import sys
sys.path.append('.') # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác
import logging
# define top level module logger
logger = logging.getLogger(__name__)
from typing import List

from utils.constants import *
from services.crmsservices import *
from datamodels.crms.qlt_params import *

class process_rank_hsdn:
    def __init__(self, _lstHSDNs : [], _params_hsdn : {}):
        self._hsdn_params = _params_hsdn
        self._HSDNs = _lstHSDNs

