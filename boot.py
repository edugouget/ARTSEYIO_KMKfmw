import board
import storage
from kmk.bootcfg import bootcfg

storage.enable_usb_drive()
storage.remount("/", readonly=False, disable_concurrent_write_protection=True)
m = storage.getmount("/")
m.label = "ARTSEYIO"

bootcfg(
    sense =  board.GP2,  # column
    source = board.GP6,  # row
    cdc=True,
    keyboard=True,
    midi=False,
    mouse=False,
    storage=False,
    consumer_control=True,
    nkro=True,
    usb_id=('KMK Gouget 2023', 'ARTSEYIO KBD kmk'),
)
