# 项目介绍

本项目旨在利用LangChain和大语言模型（如ZhipuAI）开发一个智能数据库问答系统。

该系统能够通过自然语言理解用户的查询请求，自动生成相应的SQL语句并执行，最后将查询结果以自然语言形式返回户。

# 环境依赖

import os

from dotenv import load_dotenv

from langchain_community.chat_models import ChatZhipuAI

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from langchain.prompts import PromptTemplate

from utils import *

# 目录结构描述
```
llm+sql
├── .gitignore           # Git忽略文件，忽略了环境变量（'ZHIPUAI_API_KEY'和 DB_KEY')）
├── .env                 # 环境变量文件，存储API密钥和数据库连接信息
├── ChatBI.ipynb         # Jupyter Notebook文件，包含项目的代码和说明
├── README.md            # 项目说明文件，介绍项目背景、安装和使用方法
├── requirements.txt     # Python依赖文件，列出项目所需的所有Python包及其版本
├── utils.py             # 自定义工具模块，包含数据库连接和查询函数等
└── zhipuai.py           # 主要脚本文件，使用ZhipuAI进行自然语言处理和数据库交互
```

# 使用说明
1. 本项目是与MySQL数据库进行连接，如果你使用别的数据库，请自行修改utilis.py中的连接数据库的function，以及prompt里的提示词
2. 本项目用的大模型是ZHIPU AI，如果你想使用别的大模型请手动更改LLM接口。
3. 大模型首先进行word2sql之后在数据库中运行sql代码，把结果作为promp上传大模型得到最终的nlp结果。
4. 如果有表格中具有数字代表类别的数据(比如0代表男性，1代表女性)，请在数据库新创一个"notation",notation表格有两列，一列是table_name,一列是mapping。把数据库中所有表格中的映射关系都列在notation中。

