# 1.1  linux习题集

1. ##### 以容易理解的格式列出/home 目录中所有以”d”开头的文件目录的大小

  ls -lah /home/d*

2. ##### 列出/home 目录中所有以”s”开头的目录。

  ls -d s*/

3. ##### 删除后缀名为.log 的所有，删除前逐一询问

   rm -i *.log

4. ##### cp 命令 —n 和 -u的区别

  -n 不要覆盖已存在的文件，-u 当把文件从一个目录复制到另一个目录时，仅复制 目标目录中不存在的文件，或者是文件内容新于目标目录中已经存在的文件

5. ##### 找你的用户目录下面的所有py文件,ls -l 查看他们的属性,然后把这些结果输入到一个文件之中

   ls ~ -la |grep *.py > test1.txt

6. ##### 使用ls查看根目录 并且每行显示3个信息

   ls -w 25

7. ##### 查看所有进程信息,只查看前3行

   ps -ef | tail -3

8. ##### 分析以下问题,并给出解决方案

   ##### Mount is denied because the NTFS volume is already exclusively opened.

   ##### The volume may be already mounted, or another software may use it which could be identified for example by the help of the 'fuser' command.

   文件夹已经被mount过了，或者之前mount的文件夹正在使用

9. ##### ssh 服务端口是多少,ssh免密登录方式的原理是什么

  port 22，ssh-keygen 使用ssh-keygen生成一对公钥私钥对,交换公钥

10. ##### 权限755代表什么权限,如果我想把所有的w权限去除应该使用什么命令

    文件所有者读写执行权限，文件用户组有读执行权限，其他用户对文件读执行权限，chmod  555