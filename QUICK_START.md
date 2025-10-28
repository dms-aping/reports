# 快速开始指南 / Quick Start Guide

## 生成HTML报表 / Generate HTML Report

### 方法1：使用演示脚本 / Method 1: Use Demo Script
```bash
python3 demo_generate_report.py
```

### 方法2：使用主生成器 / Method 2: Use Main Generator  
```bash
python3 generate_html_report.py
```

### 方法3：集成到您的代码中 / Method 3: Integrate into Your Code
```python
from generate_html_report import generate_html_report, load_json_data

# Load your JSON data
data = load_json_data("your_order_data.json")

# Generate HTML report
html_path = generate_html_report(data, "output_report.html")
print(f"Report generated: {html_path}")
```

## 文件说明 / File Descriptions

| 文件 / File | 说明 / Description |
|-------------|-------------------|
| `production_order_report.html` | 完整的HTML报表 / Complete HTML report |
| `report_template.html` | 静态模板参考 / Static template reference |
| `generate_html_report.py` | 核心生成器脚本 / Core generator script |
| `demo_generate_report.py` | 简单演示脚本 / Simple demo script |
| `HTML_REPORT_README.md` | 详细文档 / Detailed documentation |

## 特性 / Features

✅ **PDF布局复制** - Faithful PDF layout reproduction  
✅ **数据驱动** - Driven by JSON production order data  
✅ **响应式设计** - Responsive design for all devices  
✅ **打印优化** - Print-optimized styling  
✅ **QR码集成** - Integrated QR code generation  
✅ **中文支持** - Full Chinese language support

## 技术要求 / Requirements

- Python 3.6+
- PyPDF2 (for PDF analysis)
- pdfplumber (for PDF processing)  
- Modern web browser for viewing

## 支持 / Support

查看 `HTML_REPORT_README.md` 获取详细信息。
See `HTML_REPORT_README.md` for detailed information.