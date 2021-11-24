# Addison Blog


## Introduction 简介
This project is a personal blog app built with Flask. To see the demo, please click <a href="https://addison-blog.herokuapp.com/" target="_blank">Demo Link</a>

这是一个使用 Flask 开发的个人博客，其部署的地址为：https://addison-blog.herokuapp.com/


## Installing 安装步骤

1. Install all requirements *安装所有必要的扩展

  - `pip install -r requirement.txt`

2. Add environment variables *导入坏境变量，需要导入以下两个变量

 - export DATABASE_URL=Your SQLAlchemy Database Url(SQLAlchemy数据库url)
 - export SECRET_KET=Your Flask WTForms Secret Key(Flask WTForms的秘钥)
3. Run app on local server *本地运行应用

  - `python main.py runserver`

4. open http://127.0.0.1:5000 to see the app up and running, press CTRL+C to quit *打开http://127.0.0.1:5000 端口查看, 按Ctrl+C退出程序。

## Screenshot 截图
<img alt="Demo" src="https://github.com/XindiShang/assets/blob/007951b6a256fbfeaea7aef01e11a87e4615aee5/blog_demo.png">
