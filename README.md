# monitor_ftp

  主程序为monitor.py，其功能：

    1. 程序可通过环境变量CFG_FILE定义配置文件位置
    2. 程序可通过境变量FTP_DIR定义需通过FTP递归抓取文件元数据的目录
    3. 从配置文件中获取数据库（db）以及ftp（prefix ftp）信息
    4. 初始化数据库
    5. 递归获取ftp目录下面的文件信息，然后写入Oracle对应的表中

# config

  cfg/config.ini：db为oracle数据库信息，而ftp_{N}为监控的ftp主机信息

# lib

  - lib/mycfg.py：从config配置文件中获取ftp与db元数据
  - lib/myftp.py：walk方法模拟os.walk方法，其返回根目录，子目录元组，文件字典
  - lib/myora.py：将获取到的ftp文件信息插入到对应的表中，初始化时将使用truncate清空表

# require

  程序需要安装oracle客户端并配置LD_LIBRARY_PATH环境变量
