# 1.1  linux习题集

1. ls -lah /home/d*
2. ls -d s*/
3. rm -i *.log
4. -n 不要覆盖已存在的文件，-u 当把文件从一个目录复制到另一个目录时，仅复制 目标目录中不存在的文件，或者是文件内容新于目标目录中已经存在的文件。
5. ls ~ -la |grep *.py > test1.txt
6. ls -w 25
7. ps -ef | tail -3
8. 文件夹已经被mount过了，或者之前mount的文件夹正在使用
9. port 22，ssh-keygen 使用ssh-keygen生成一对公钥私钥对,交换公钥
10. 文件所有者读写执行权限，文件用户组有读执行权限，其他用户对文件读执行权限，chmod  555