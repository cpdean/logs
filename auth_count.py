
import os

mainlogs = "/var/log/"
subject = "auth.log"

log_path = os.path.join(mainlogs, subject)

with open(log_path, "rb") as f:
    print len(f.readlines())
