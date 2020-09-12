import sys
# import tkinter.messagebox
import base64
from PIL import Image
from PIL import ImageGrab
import pyperclip
from io import BytesIO

# png是无损压缩格式。jpeg有损格式。针对PNG格式，quality参数无效
# 有文章介绍说，在软件界面截图这种场景，PNG效果更好。但是实测，jpeg生成的文件确实要小一些
picture_format = 'png'


# picture_format = 'jpeg'


def encode_image_from_clip():
    image = ImageGrab.grabclipboard()
    if not isinstance(image, Image.Image):
        # tkinter.messagebox.showinfo("picture2base64", "not a image in clipboard.")
        print("not a image in clipboard.")
        sys.exit(1)
    img_buffer = BytesIO()
    image.save(img_buffer, format=picture_format, optimize=True, quality=40)
    byte_data = img_buffer.getvalue()
    base64_byte = base64.b64encode(byte_data)
    # 去除首尾多余字符
    base64_str = (str(base64_byte))[2:-1]
    msg = 'data:image/' + picture_format + ';base64,' + base64_str
    pyperclip.copy(msg)
    print("send base64 to clipboard succeed! len: " + str(len(msg)))


if __name__ == "__main__":
    encode_image_from_clip()
    sys.exit(0)
