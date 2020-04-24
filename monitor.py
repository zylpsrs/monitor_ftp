# coding:utf-8

import os
import datetime
import configparser

from lib.myftp import myftp
from lib.myora import myora
from lib.mycfg import mycfg

cfg_file = "cfg/config.ini" if (os.environ.get("CFG_FILE") is None) else os.environ.get("CFG_FILE")
ftp_dir  = "." if (os.environ.get("FTP_DIR") is None) else os.environ.get("FTP_DIR")

if __name__ == "__main__":
    # get ftp and db cfg 
    cfg = mycfg(cfg_file)
    ftp_cfg = cfg.get_ftp_cfg()
    db_url,table_name = cfg.get_db_cfg()

    # init ora instance
    db = myora(db_url,table_name)

    for ftp_h in ftp_cfg:
        curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # init ftp instance
        ftp = myftp(ftp_h['host'], ftp_h['username'], ftp_h['password'], int(ftp_h['port']))

        for root, dirs, files in ftp.walk(ftp_dir):
          rows = []
          for name,meta in files.items():
              row = ('%s:%s' % (ftp_h['host'],ftp_h['port']), 
                      root, name, meta['size'], meta['mdtm'], curr_time)
              if len(rows) < 500:
                  rows.append(row)
              else:
                  db.insert_table(rows)
                  rows = []
          db.insert_table(rows)

	ftp.close()

    db.close()
