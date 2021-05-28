import os
import re
dirs = os.listdir()
for file in dirs:
    if re.findall(".wav",file):
        os.remove(file)
