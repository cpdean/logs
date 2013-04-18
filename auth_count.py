import os
from glob import glob
import gzip

mainlogs = "/var/log/"
subject = "auth.log"

log_path = os.path.join(mainlogs, subject)

def log_files(log_file):
    """list of rotated log files"""
    return glob(log_file + "*")

with gzip.open(log_path + ".2.gz") as f:
    print len(f.readlines())
