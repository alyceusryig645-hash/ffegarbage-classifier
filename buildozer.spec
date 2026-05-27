[app]
title = TrashClassifier
package.name = trashclassifier
package.domain = org.fengxian.school

source.dir = .
source.main = app_android.py

version = 1.0

requirements = python3,kivy==2.3.0

source.include_exts = py,json,otf,ttf
source.include_patterns = NotoSansCJKsc-Regular.otf

# 横屏（适合平板展示）
orientation = landscape

# Android 版本设置
# 华为平板 MatePad 系列支持 Android 10+ (API 29+)
android.minapi = 21
android.api = 33
android.ndk = 25b

# 权限（读写数据，保存学生训练记录）
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 只打 arm64（华为平板主流架构，比同时打两个快一倍）
android.archs = arm64-v8a

# 自动接受 SDK 许可证
android.accept_sdk_license = True

# 不使用 Google 服务（华为设备无需）
# android.services =

[buildozer]
log_level = 2
warn_on_root = 1
