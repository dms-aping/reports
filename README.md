# Production Order Reports / 生产订单报表系统

这个仓库包含生产订单的JSON模板和结构，用于生成PDF和HTML报表。
This repository contains JSON templates and structures for production orders, designed for generating PDF and HTML reports.

## 文件说明 / File Description

### JSON Sample Files / JSON示例文件

1. **`sample_production_order.json`** - 基础生产订单JSON模板
   - Basic production order JSON template with standard structure
   - Contains all required fields and sections

2. **`production_order_detailed_sample.json`** - 详细生产订单JSON示例  
   - Detailed production order JSON sample with realistic data
   - Includes comprehensive examples for all sections

### Documentation / 文档

3. **`JSON_SCHEMA_DOCUMENTATION.md`** - JSON结构文档
   - Complete documentation of the JSON schema
   - Field descriptions in both Chinese and English
   - Usage examples and validation rules

### Tools / 工具

4. **`validate_json.py`** - JSON验证脚本
   - Python script to validate JSON files
   - Displays order summaries and statistics
   - Usage: `python3 validate_json.py`

5. **`generate_html_report.py`** - HTML报表生成器
   - Generates HTML reports from JSON data matching PDF layout
   - Replicates the styling and structure of Report1.pdf
   - Usage: `python3 generate_html_report.py`

6. **`demo_generate_report.py`** - HTML生成演示脚本
   - Demo script showing how to generate HTML reports
   - Bilingual output and easy to use
   - Usage: `python3 demo_generate_report.py`

### HTML Reports / HTML报表

7. **`production_order_report.html`** - 生成的HTML报表
   - HTML report generated from JSON data
   - Matches the layout and styling of Report1.pdf
   - Responsive design for web and print use

8. **`report_template.html`** - HTML模板
   - Static HTML template for reference
   - Can be customized for different layouts
   - Shows the basic structure and CSS styling

9. **`HTML_REPORT_README.md`** - HTML报表文档
   - Detailed documentation for HTML report generation
   - Explains the structure, styling, and usage

## JSON Structure Overview / JSON结构概览

The production order JSON includes these main sections:

1. **主订单数据 (mainOrder)** - Company info, order numbers, QR code, important notes
2. **订单明细 (orderDetails)** - Product specifications and quantities  
3. **原材 (rawMaterials)** - Raw material requirements and specifications
4. **出版 (publishing)** - Publishing and layout requirements
5. **印刷 (printing)** - Printing specifications and color requirements
6. **后工序 (postProcessing)** - Post-production workflow steps
7. **辅材 (auxiliaryMaterials)** - Auxiliary materials and supplies
8. **页脚信息 (footer)** - Approval and review information
9. **元数据 (metadata)** - System and document metadata

## Usage / 使用方法

1. **Validate JSON files / 验证JSON文件:**
   ```bash
   python3 validate_json.py
   ```

2. **Use as template / 作为模板使用:**
   ```bash
   # Copy the detailed sample as starting point
   cp production_order_detailed_sample.json my_order.json
   # Edit with your specific order data
   ```

3. **Integration / 集成使用:**
   - Import JSON into your PDF generation system
   - Use the structure for database schema design
   - Adapt for your specific printing workflow requirements

## Features / 特性

- ✅ Complete bilingual documentation (中文/English)
- ✅ Realistic sample data based on actual form
- ✅ JSON validation and verification tools
- ✅ Comprehensive schema covering all form sections
- ✅ Ready for PDF report generation integration

## Next Steps / 后续步骤

这些JSON模板和HTML生成工具可以用于：
These JSON templates and HTML generation tools can be used for:

- PDF报表生成系统 / PDF report generation systems
- HTML网页报表 / HTML web reports  
- 数据库设计 / Database schema design  
- API接口定义 / API interface definitions
- 工作流管理 / Workflow management systems
- 打印友好的网页版本 / Print-friendly web versions

## HTML Report Features / HTML报表特性

✅ **PDF结构复制** - Faithful reproduction of Report1.pdf layout
✅ **响应式设计** - Works on desktop, tablet, and mobile devices  
✅ **打印优化** - Optimized for professional printing
✅ **QR码集成** - Dynamic QR code generation from order data
✅ **中文字体支持** - Proper SimSun font rendering for Chinese text
✅ **表格布局** - Accurate table structure matching the PDF
✅ **数据绑定** - Automatic population from JSON data
