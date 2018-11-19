# 1.2 git习题



1. git add 增加文件到暂存区，

   git stage 也是增加文件到暂存区，

2. git rm --cached  文件任然存在工作区，从暂存区删除，删除后文件不会被版本控制了

   git rm -f 删除工作区和暂存区的文件，删除后文件不存在了

3. git 是分布式版本管理软件，svn不是

4. git log --since '2018.10.1' --after '2018.10.20' --graph

5. git clone ， 从远程仓库中克隆版本到工作区

   git init ，新建工作区初始化，代表该目录需要用git进行版本管理

6. 创建 .gitignore

   echo .idea/*  > .gitignore

7. git reset head filename

   git checkout -- filename

8. git show tagname

9. git fetch 从远程获取最新到本地，不会自动merge

   git pull 从远程获取最新版本并merge到本地

10. git remote add <shortname> <url>

