from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    print("Linux")
elif _platform == "darwin":
    # MAC OS X
    print("Mac")
elif _platform == "win32":
    # Windows
    print("Windows32")
elif _platform == "win64":
    # Windows 64-bit
    print("Windows64")