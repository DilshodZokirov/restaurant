import cv2
import numpy as np
from os.path import join as join_path
from pathlib import Path
import qrcode

BASE_DIR = Path(__file__).parent
file = join_path(BASE_DIR, 'static_file_qrcode')


def qrcode_write_file(name, fill_color='black', back_color='white'):
    g_file = join_path(file, name)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=50,
        border=10
    )
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(g_file)
