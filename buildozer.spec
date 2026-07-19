[app]

# (str) Title of your application
title = My Converted App

# (str) Package name
package.name = mytermuxapp

# (str) Package domain (needed for android packaging)
package.domain = org.yourname

# (str) Source code directory where main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3==3.10.12,kivy==2.3.0,cython==0.29.36

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# ==========================================
# Android Configurations
# ==========================================

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android Build-Tools version to use
android.build_tools_version = 33.0.2

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
