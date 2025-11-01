import os
from datetime import datetime
filedest = "D:/testing"
for filename in os.listdir(filedest):
    path = os.path.join(filedest, filename)
    if os.path.isfile(path):
        mod_time = os.path.getmtime(filedest)
        data_str = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
        name, ext = os.path.splitext(filename)
        newname = f"{name}_{data_str}{ext}"
        os.rename(path, os.path.join(filedest, newname))
        print(f"{filename} - {newname} ")
