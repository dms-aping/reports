# Production Order Reports / 生产订单报表系统

这个仓库包含生产订单的JSON模板和结构，用于生成PDF报表。
This repository contains JSON templates and structures for production orders, designed for generating PDF reports.

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

这些JSON模板可以用于：
These JSON templates can be used for:

- PDF报表生成系统 / PDF report generation systems
- 数据库设计 / Database schema design  
- API接口定义 / API interface definitions
- 工作流管理 / Workflow management systems
