# monitor_ftp

  主程序为monitor.py，可配置crontab定时执行此程序，其功能：

    1. 程序可通过环境变量CFG_FILE定义配置文件位置
    2. 从配置文件中获取数据库（db）以及ftp（prefix ftp）信息
    3. 初始化数据库
    4. 递归获取ftp目录下面的文件信息，然后写入Oracle对应的表中

# config

  cfg/config.ini：db为oracle数据库信息，而ftp_{N}为监控的ftp主机信息

# lib

  - lib/mycfg.py：从config配置文件中获取ftp与db元数据
  - lib/myftp.py：walk方法模拟os.walk方法，其返回根目录，子目录元组，文件字典
  - lib/myora.py：将获取到的ftp文件信息插入到对应的表中，初始化时将使用truncate清空表

# require

  程序需要安装oracle客户端并配置LD_LIBRARY_PATH环境变量
