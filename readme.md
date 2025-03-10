# 学习强国文章爬虫

一个用于批量下载学习强国文章的爬虫工具，支持多线程下载并将文章保存为 Word 文档格式。

## 功能特点

- 支持多线程并发下载，提高爬取效率
- 自动将文章保存为规范的 Word 文档格式
- 支持按专题批量下载文章
- 内置错误重试机制
- 实时显示下载进度
- 支持自定义线程数量

## 环境要求

- Python 3.7+
- 依赖包：
  - playwright
  - beautifulsoup4
  - python-docx
  - tqdm

## 安装说明

1. 克隆项目到本地
2. 安装依赖包：
```bash
pip install -r requirements.txt
```
3. 安装 Playwright 浏览器(谷歌)：
```bash
playwright install chromium
```

## 使用方法
1. 直接运行主程序：
```bash
python xuexiqiangguo_crawler.py
```
2. 按提示输入：
   - 线程数量（默认为4）
   - 专题信息（两种方式）：
     - 直接输入字段（即JSON文件名）和专题名称（用英文逗号分隔）
     ![mage.png](./images/1741575605123.png)
     - 或从配置文件中选择主题关键字
## 文件说明
- xuexiqiangguo_crawler.py : 主程序文件
- tools_json.py : JSON 工具类
## 注意事项
- 请合理设置线程数，建议不要超过8个
- 下载的文章将按专题分类保存
- 确保网络连接稳定
- 遵守网站使用规则，合理设置爬取间隔
## 更新日志
### v1.0.0
- 实现基础爬虫功能
- 支持多线程下载
- 添加进度条显示
- 实现 Word 文档格式化保存