# Webpage Screenshot Tool

一个用 Python 编写的自动化网页截图工具，适用于开源项目、文档存档等场景。

## 功能
- 输入网址后自动截取全屏截图
- 无需手动操作，适合批量处理

## 如何使用
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
2.运行程序：
python screenshot.py
3.截图会保存在 screenshots/ 目录下。
贡献
欢迎提交 Issues 或 Pull Requests！

3. 点击 **Commit changes**  

---

### **2. 添加自动测试（GitHub Actions）**
1. 点击 **Add file → Create new file**  
2. 文件名输入 `.github/workflows/test.yml`（注意最前面有个点）  
3. 内容区复制以下代码：  

```yaml
name: Run Screenshot Test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run screenshot test
        run: python screenshot.py
