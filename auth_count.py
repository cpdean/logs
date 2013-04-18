import os
from glob import glob
import gzip

mainlogs = "/var/log/"
subject = "auth.log"

log_path = os.path.join(mainlogs, subject)

def log_files(log_file):
    """list of rotated log files"""
    return glob(log_file + "*")

def opener(filename):
    if l.endswith(".gz"):
        o = gzip.open
    else:
        o = open
    return o(filename,"rb")


total_count = 0
for l in log_files(log_path):
    with opener(l) as f:
        total_count += len(f.readlines())
print total_count

for l in log_files(log_path):
    with opener(l) as f:
        print l, len(f.readlines())

