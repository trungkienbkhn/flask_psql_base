import os
from datetime import datetime


def export_log(log):
    log_file = os.path.join('/tmp/logs', datetime.now().strftime("%d%m%Y") + '.log')
    if not os.path.isdir('/tmp/logs'):
        os.mkdir('/tmp/logs')
    with open(log_file, "a") as file:
        content = datetime.now().strftime("[%d/%a/%Y %H:%M:%S] ") + log
        file.write(content)
        file.write('\n')
