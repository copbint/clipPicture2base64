# 介绍
自动读取剪贴板图片，使用base64编码为文本，发送回剪贴板。

主要是用于在markdown中插入base64编码的图片。请参考：<br>
[在markdown中直接插入base64编码的图片](https://blog.csdn.net/qq_31567335/article/details/82322858)

# 构建
使用pip下载依赖的三方库
```
 pip install base64
 pip install pyperclip
 pip install Pillow
 pip install pyinstaller
```
然后使用pyinstaller构建exe文件<br>
`pyinstaller -F -w clipPicture2base64.py`

# 其他
不知道为什么exe文件执行过之后就无法删除，可以在cmd中使用如下命令强制删除:<br>
`del /F /S /Q clipPicture2base64.exe`

# License
Just use it as you like.
