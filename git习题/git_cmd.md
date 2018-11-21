# 1.2 git习题



1. ##### git add和git stage的区别是什么

   git add 增加文件到暂存区，

   git stage 也是增加文件到暂存区，

2. ##### git rm --cached 和git rm -f的区别是什么

   git rm --cached  文件任然存在工作区，从暂存区删除，删除后文件不会被版本控制了

   git rm -f 删除工作区和暂存区的文件，删除后文件不存在了

3. #####  git和svn的区别是什么

   git 是分布式版本管理软件，svn不是

4. ##### 筛选出 2018.10.1 到 2018.10.20之间的日志,并且输出为地理图,并且没有做过合并

   git log --since '2018.10.1' --after '2018.10.20' --graph

5. ##### git init和git clone的区别

   git clone ， 从远程仓库中克隆版本到工作区

   git init ，新建工作区初始化，代表该目录需要用git进行版本管理

6. ##### 每次提交都忽略.idea文件夹里面的东西怎么办

   创建 .gitignore

   echo .idea/*  > .gitignore

7. ##### 如果编辑一个文件之后并且加入了暂存区,但是你后悔了,想把文件恢复到没有修改之前的样子,怎么办

   git reset head filename

   git checkout -- filename

8. ##### 如何检出标签?

   git show tagname

9. ##### git fetch 和 git pull的区别

   git fetch 从远程获取最新到本地，不会自动merge

   git pull 从远程获取最新版本并merge到本地

10. ##### 如何添加远程仓库

    git remote add <shortname> <url>

