## 房产信息爬虫（HouseInfoSpider）

--- 

## 项目概述  

本项目旨在通过自动化爬虫技术，从房天下(https://xm.esf.fang.com)网站抓取房产信息，包括房屋户型、建筑面积、单价、朝向、楼层、装修情况、小区名称和房屋总价等数据。抓取的数据将保存为CSV文件，便于后续分析和处理。

---

### 原始代码来源
本项目基于 [jimmy0k/Xiamen-siming-house](https://github.com/jimmy0k/Xiamen-siming-house) 的代码进行改进和扩展。原始代码提供了基础的房产数据爬取功能。

---

## 功能模块
### 1. 数据爬取模块：
- 从指定房产网站抓取房屋详细信息。

- 支持分页爬取，自动处理多页数据。

- 支持随机延迟，避免频繁请求导致IP被封禁。

### 2. 数据处理模块：

- 将抓取的数据存储为CSV文件。

- 支持数据清洗和去重。

### 3. 数据存储模块：

- 自动生成带时间戳的CSV文件，便于区分不同批次的数据。

---

## 使用须知
### 环境要求
- Python版本：3.8+
- 依赖库：
```bash
pip install requests pandas beautifulsoup4
```
### 配置文件
- 无需额外配置文件，直接运行即可。

### 运行步骤
### 1. 安装依赖：
```bash
pip install -r requirements.txt
```
### 2. 运行爬虫：
```bash
python 2_request.py
```
### 3.查看结果：
- 爬取的数据将保存为house_information_X.csv文件，其中X为页码。
- 文件路径为当前目录。

### 参数说明
- 分页爬取：  
  + 修改for i in range(1, 2):中的range(1, 2)，调整爬取的页码范围。
  + 例如，range(1, 101)表示爬取前100页数据。

- 延迟设置：
  + 修改time.sleep(5)中的5，调整每次请求的延迟时间（单位为秒）。

### 注意事项

### 1. 反爬机制：
- 网站可能有反爬虫机制，建议合理设置延迟时间，避免频繁请求。
- 如果IP被封禁，可以使用代理IP或更换网络环境。

### 2. 数据完整性：
- 由于网站页面结构可能变化，部分字段可能无法正确抓取，需定期检查代码适配性。
### 3. 法律合规：
- 本项目仅供学习和研究使用，禁止用于商业用途或未经授权的数据抓取。
- 使用前请确保遵守目标网站的robots.txt协议和相关法律法规。

--- 

### 文件结构
```
HouseInfoSpider/
├── 2_request.py            # 主程序，包含数据爬取和存储逻辑
├── house_information_X.csv # 爬取的数据文件（X为页码）
├── requirements.txt        # 依赖库列表
└── README.md               # 项目说明文档
```

--- 

## 示例运行
### 1. 爬取单页数据:
```bash
python 2_request.py
```
+ 默认爬取第1页数据，保存为`house_information_1.csv`。
### 2. 爬取多页数据：
- 修改for i in range(1, 2):为for i in range(1, 101):，爬取前100页数据。
- 每爬取1页数据，生成一个CSV文件。

---

## 联系方式
如有问题或建议，请联系：

邮箱：commonboeotian@gmail.com

---

## 未来计划

    1. 支持更多房产网站：扩展爬虫支持更多房产平台。
    2. 数据可视化：集成数据可视化功能，生成图表分析报告。
    3. 自动化通知：添加邮件通知功能，定时发送爬取结果。

--- 

