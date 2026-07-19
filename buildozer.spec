[app]
# (str) Title of your application
title = My Converted App

# (str) Package name
package.name = mytermuxapp

# (str) Package domain (needed for android packaging)
package.domain = org.yourname

# (str) Source code directory where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
