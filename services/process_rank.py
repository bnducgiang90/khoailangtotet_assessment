import sys
sys.path.append('.') # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác
import logging
# define top level module logger
logger = logging.getLogger(__name__)

from services.crmsservices import *
from services.process_hsdn_rank import *
from services.process_hsvp_rank import *
from utils.constants import *
from datamodels.crms.qlt_xhdn import QLT_XEPHANGDN_20, QLT_LYDOXEPHANG_HSDN_DIEMTC


class process_rank:
    def __init__(self):
        self._srvcrms = crmsservice()
        self._qlt_xephangs: List[QLT_XEPHANGDN_20] = []
        self._lst_lydo_diem_tc: List[QLT_LYDOXEPHANG_HSDN_DIEMTC] = []
        self._hsdn_rowIdmin = 0
        self._hsdn_rowIdmax = 0
        self._params_qltxephang = self._srvcrms.get_params_plxephangs()
        self._dict_qlt_hsvp_xhdns = {}

    ## tính toán xhdn
    def qlt_xhdn(self):
        try:
            _ID_TH = self._srvcrms.get_XHDN_TH_GetID()
            if _ID_TH is None or _ID_TH == 0:
                logger.warning("Chưa có thông tin tổng hợp doanh nghiệp!")
                logger.warning("Kết thúc đánh giá xếp hạng!")
                return

            # 0. Lấy Phiên bản và id_lydo:
            _ID_PHIENBAN = self._srvcrms.get_id_phienban(0)
            _ID_LYDOXEPHANG = self._srvcrms.get_next_id_lydoxephang()
            if _ID_PHIENBAN is None or _ID_PHIENBAN == 0 or _ID_LYDOXEPHANG is None or _ID_LYDOXEPHANG == 0:
                logger.warning("Lỗi khởi tạo ID_PHIENBAN  và ID_LYDOXEPHANG  !")
                logger.warning("Kết thúc đánh giá xếp hạng!")
                return

            # 1. tính toán XHDN HSVP
            ### lấy danh sách params HSVP:
            _hsvp_params: {} = self._srvcrms.get_hsvp_params()
            print("_hsvp_params : {}".format(len(_hsvp_params)))
            ### lấy danh sách HSVP cần đánh giá:
            _lstHSVPs = self._srvcrms.get_hsvps()
            print("_lstHSVPs : {}".format(len(_lstHSVPs)))

        except Exception as ex:
            logger.exception("Lỗi :")
        finally:
            logger.info("------Kết thúc đánh giá RANK ---------")


# hiển thị biểu  đồ
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()
