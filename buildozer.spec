[app]
title = TrashClassifier
package.name = trashclassifier
package.domain = org.fengxian.school

source.dir = .
source.main = app_android.py

version = 1.0

# 显式指定 hostpython3 与 python3 版本一致，避免 p4a 跟随系统 Python
requirements = hostpython3==3.11.0,python3==3.11.0,kivy==2.3.0

source.include_exts = py,json,otf,ttf
source.include_patterns = NotoSansCJKsc-Regular.otf

orientation = landscape

android.minapi = 21
android.api = 33
android.ndk = 25b

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
