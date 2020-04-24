import configparser

_default_table_name = "monitor_ftp_files"

class mycfg (object):
    ''' ref https://docs.python.org/2/library/ftplib.html '''
    def __init__(self, cfg_file):
        ''' init a ConfigParser instance and read the cfg file '''
        self.config = configparser.ConfigParser()
        self.config.read(cfg_file)

    def get_ftp_cfg(self):
        ''' return a dict, which include: ftp host info '''
        ftp_info = []
        ftps = [section for section in self.config if section.startswith('ftp')]
        for host in ftps:
            ftp_info.append(dict(self.config.items(host, raw=True)))
        return ftp_info

    def get_db_cfg(self):
        ''' return ora_db_url,monitor_table_name '''
        db_cfg = dict(self.config.items('db', raw=True))
        url = "{}/{}@{}:{}/{}".format(db_cfg['username'], db_cfg['password'], 
			              db_cfg['host'], db_cfg['port'], db_cfg['service_name'])
        return url,db_cfg.get('table_name', _default_table_name)
