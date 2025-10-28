# Production Order JSON Schema Documentation

## 生产订单JSON数据结构说明

This document describes the JSON schema for the production order system based on the Chinese printing company form template.

## Structure Overview / 结构概览

### 1. Main Order Data / 主订单数据 (`mainOrder`)

Contains the primary order information including company details, order numbers, and important notes.

**Fields:**
- `companyName` (string): 公司名称 - Company name
- `companyLogo` (string): 公司标识 - Company logo placeholder
- `orderNumber` (string): 订单号 - Order number with date/time
- `workOrderNumber` (string): 工单号 - Work order number
- `customerOrderNumber` (string): 客户订单号 - Customer order number
- `qrcode` (string): 二维码 - QR code URL or data
- `importantNotes` (string): 重要说明 - Important notes and instructions
- `specialRemarks` (string): 特别备注 - Special remarks and requirements
- `createdDate` (string): 创建日期 - Creation date (YYYY-MM-DD)
- `createdTime` (string): 创建时间 - Creation time (HH:MM)
- `status` (string): 状态 - Order status
- `priority` (string): 优先级 - Priority level

### 2. Order Details / 订单明细 (`orderDetails`)

Array of product items with specifications and quantities.

**Fields per item:**
- `sequence` (number): 序号 - Sequence number
- `materialCode` (string): 物料编码 - Material code
- `productName` (string): 产品名称 - Product name
- `productDescription` (string): 产品描述 - Product description
- `specification` (string): 规格 - Specification details
- `orderQuantity` (number): 订单数量 - Order quantity
- `productCode` (string): 产品代码 - Product code
- `unitPrice` (number): 单价 - Unit price
- `totalAmount` (number): 总金额 - Total amount
- `unit` (string): 单位 - Unit of measurement

### 3. Raw Materials / 原材 (`rawMaterials`)

Information about raw materials required for production.

**Structure:**
- `summary`: Header definitions for the materials table
- `specifications`: Array of material specifications
  - `partName` (string): 部件名称 - Part name
  - `materialDescription` (string): 材料描述 - Material description
  - `orderSpec` (string): 订单规格 - Order specification
  - `quantity` (number): 数量 - Quantity
  - `workingSize` (string): 上机尺寸 - Working size
  - `thickness` (string): 厚度 - Thickness
  - `materialType` (string): 原料类型 - Material type
  - `grammage` (string): 克重 - Grammage
  - `totalSheets` (number): 总张数 - Total sheets
  - `totalQuantity` (number): 总数量 - Total quantity

### 4. Publishing / 出版 (`publishing`)

Publishing and layout requirements.

**Structure:**
- `summary`: Header definitions for publishing table
- `details`: Array of publishing specifications
  - `partName` (string): 部件名称 - Part name
  - `quantity` (number): 数量 - Quantity
  - `requirement` (string): 工艺要求 - Process requirements
  - `version` (number): 版本数 - Version number
  - `total` (number): 总数 - Total count
  - `size` (string): 拼版尺寸 - Layout size
- `remarks` (string): 备注 - Remarks
- `layoutRequirements` (string): 拼版要求 - Layout requirements

### 5. Printing / 印刷 (`printing`)

Printing specifications and color requirements.

**Structure:**
- `summary`: Header definitions for printing table
- `details`: Array of printing specifications
  - `partName` (string): 部件名称 - Part name
  - `quantity` (number): 数量 - Quantity
  - `frontColor` (string): 正面颜色 - Front side colors
  - `backColor` (string): 反面颜色 - Back side colors
  - `unitPrice` (number): 应产数 - Expected production
  - `total` (number): 总数 - Total count
- `specialRequirements` (string): 特殊要求 - Special requirements
- `colorRequirements` (string): 色彩要求 - Color requirements
- `qualityStandards` (string): 质量标准 - Quality standards

### 6. Post-processing / 后工序 (`postProcessing`)

Post-production workflow and finishing processes.

**Structure:**
- `summary`: Header definitions for post-processing table
- `processes`: Array of post-processing steps
  - `partName` (string): 部件名称 - Part name
  - `process` (string): 工序 - Process name
  - `quantity` (number): 数量 - Quantity
  - `requirements` (string): 工艺要求 - Process requirements
  - `isOutsourced` (boolean): 是否外发 - Is outsourced
  - `unitPrice` (number): 应产 - Expected production
  - `actualProduction` (number): 实产 - Actual production
  - `supervisor` (string): 机长 - Supervisor/operator
  - `total` (number): 总数 - Total count

### 7. Auxiliary Materials / 辅材 (`auxiliaryMaterials`)

Additional materials and supplies needed for production.

**Structure:**
- `summary`: Header definitions for auxiliary materials table
- `materials`: Array of auxiliary materials
  - `partName` (string): 部件名称 - Part name
  - `materialCode` (string): 物料编码 - Material code
  - `materialName` (string): 物料名称 - Material name
  - `specification` (string): 规格 - Specification
  - `unit` (string): 单位 - Unit
  - `quantity` (number): 数量 - Quantity
  - `remarks` (string): 备注 - Remarks
  - `unitArea` (number): 单耗（㎡）- Unit consumption (square meters)
  - `total` (number): 总数 - Total amount

### 8. Footer / 页脚信息 (`footer`)

Approval and review information.

**Fields:**
- `approver` (string): 制单 - Document creator
- `reviewer` (string): 文件制作 - Document reviewer
- `businessUnit` (string): 业务员 - Business representative
- `customer` (string): 顾客 - Customer
- `supervisor` (string): 主管 - Supervisor
- `approvalDate` (string): 审批日期 - Approval date
- `reviewDate` (string): 审核日期 - Review date

### 9. Metadata / 元数据 (`metadata`)

System and document metadata.

**Fields:**
- `version` (string): 版本 - Schema version
- `createdBy` (string): 创建者 - Created by
- `lastModified` (string): 最后修改时间 - Last modified timestamp
- `documentType` (string): 文档类型 - Document type
- `language` (string): 语言 - Language code
- `currency` (string): 币种 - Currency code

## Usage Examples / 使用示例

1. **Basic Order Creation / 基础订单创建:**
   ```json
   {
     "mainOrder": {
       "companyName": "佛山智冠彩印包装有限公司",
       "orderNumber": "2025/8/22 13:44",
       "workOrderNumber": "250220000017505"
     }
   }
   ```

2. **Adding Product Details / 添加产品详情:**
   ```json
   {
     "orderDetails": [
       {
         "sequence": 1,
         "productName": "覆亮膜【高光尺寸】357x392-300g",
         "orderQuantity": 3
       }
     ]
   }
   ```

## Validation Rules / 验证规则

1. All quantities must be positive numbers
2. Dates must be in YYYY-MM-DD format
3. Times must be in HH:MM format
4. QR codes should be valid URLs or base64 encoded data
5. Material codes should follow company naming conventions
6. Color specifications should follow printing industry standards

## File Structure / 文件结构

- `sample_production_order.json` - Basic sample with template structure
- `production_order_detailed_sample.json` - Detailed sample with realistic data
- `README.md` - This documentation file
