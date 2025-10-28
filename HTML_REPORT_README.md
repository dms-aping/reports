# HTML Report Generator / HTML 报表生成器

This directory contains tools to generate HTML reports that replicate the PDF structure and styling.

## Generated Files / 生成的文件

### HTML Reports / HTML 报表
- `production_order_report.html` - Generated HTML report from JSON data / 从JSON数据生成的HTML报表
- `report_template.html` - Static HTML template for reference / 静态HTML模板供参考

### Tools / 工具
- Python script for PDF analysis and HTML generation / PDF分析和HTML生成的Python脚本

## Features / 特性

✅ **PDF Structure Analysis** - Analyzes Report1.pdf structure and layout
✅ **JSON Data Integration** - Uses existing production order JSON data  
✅ **Faithful HTML Reproduction** - Replicates PDF styling and layout in HTML
✅ **Responsive Design** - Works on desktop and mobile devices
✅ **Print-friendly** - Optimized for printing
✅ **QR Code Support** - Dynamic QR code generation
✅ **Chinese Font Support** - Proper SimSun font rendering

## Layout Structure / 布局结构

The HTML report maintains the same structure as the PDF:

1. **Company Header** / 公司标题 - Large centered title
2. **Order Information** / 订单信息 - Date, order numbers, QR code  
3. **Product Details Table** / 产品详情表 - Product specifications and quantities
4. **Important Notes** / 重要说明 - Highlighted important information
5. **Business Sections** / 业务部分:
   - Raw Materials / 原材
   - Publishing / 出版  
   - Printing / 印刷
   - Post Processing / 后工序
   - Auxiliary Materials / 辅材
6. **Footer** / 页脚 - Staff and approval information

## Styling / 样式

- Font: SimSun (宋体) for proper Chinese character rendering
- Page Size: 595px × 842px (A4 proportions)
- Border styles matching the PDF tables
- Responsive design for different screen sizes
- Print optimization for professional output

## Usage / 使用方法

The HTML report can be:
- Viewed in any web browser / 在任何网页浏览器中查看
- Printed directly from browser / 直接从浏览器打印  
- Integrated into web applications / 集成到网页应用中
- Used as email attachments / 用作电子邮件附件
- Served from web servers / 从网络服务器提供