import configparser

class mycfg (object):
    ''' ref https://docs.python.org/2/library/ftplib.html '''
    def __init__(self, cfg_file):
        self.config = configparser.ConfigParser()
        self.config.read(cfg_file)

    def get_ftp_cfg(self):
        ftp_info = []
        ftps = [section for section in self.config if section.startswith('ftp')]
        for host in ftps:
            ftp_info.append(dict(self.config.items(host, raw=True)))
        return ftp_info

    def get_db_cfg(self):
        db_cfg = dict(self.config.items('db', raw=True))
        url = "{}/{}@{}:{}/{}".format(db_cfg['username'], db_cfg['password'], 
			              db_cfg['host'], db_cfg['port'], db_cfg['service_name'])
        return url,db_cfg['table_name']
