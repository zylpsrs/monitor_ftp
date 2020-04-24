import os
from ftplib import FTP
from dateutil import parser

class myftp (object):
    ''' ref https://docs.python.org/2/library/ftplib.html '''
    def __init__(self, host, user, passwd, port=21):
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, passwd)

    def listdir(self, path):
        file_list, dirs, nondirs = [], [], {} 
        try:
            self.ftp.cwd(path)
        except Exception as exp:
            print("the current path is : ", self.ftp.pwd(), exp.__str__(), path)
            return [], {}
        else:
            self.ftp.retrlines('LIST', lambda x: file_list.append(x.split()))
            for info in file_list:
                file_info = {}
                ls_type, size, name = info[0], info[4], info[-1]
                mdtm = str(parser.parse(info[5] + " " + info[6] + " " + info[7]))

                file_info['size'] = size
                file_info['mdtm'] = mdtm

                if ls_type.startswith('d'):
                    dirs.append(name)
                else:
                    #nondirs.append(name)
                    nondirs[name] = file_info
            return dirs, nondirs

    def walk(self, top):
        dirs, nondirs = self.listdir(top)
        top = self.ftp.pwd()
        yield top, dirs, nondirs
        for dirname in dirs:
            new_path = os.path.join(top, dirname)
            for x in self.walk(new_path):
                yield x

    def close(self):
        self.ftp.close()
