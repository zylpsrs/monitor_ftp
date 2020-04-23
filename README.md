# monitor_ftp

  程序递归获取ftp目录下面的文件信息，然后写入到Oracle对应的表中
  程序可通过环境变量CFG_FILE获取配置文件
  程序可通过境变量FTP_DIR获取需要递归抓取FTP文件元数据目录

# config

  cfg/config.ini：db为oracle数据库信息，而ftp_{N}为监控的ftp主机信息

# lib

  lib/mycfg.py：从config配置文件中获取ftp与db元数据
  lib/myftp.py：walk方法模拟os.walk方法，其返回根目录，子目录元组，文件字典
  lib/myora.py：将获取到的ftp文件信息插入到对应的表中，每次插入会将表truncate

# require

  程序需要安装oracle客户端并配置LD_LIBRARY_PATH环境变量
