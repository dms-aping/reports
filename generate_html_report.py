#!/usr/bin/env python3
"""
HTML Report Generator
Generates HTML report from JSON data matching the PDF layout
"""

import json
import os
from datetime import datetime
from pathlib import Path

def load_json_data(json_path):
    """Load production order data from JSON file"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return None

def generate_qr_code_url(data):
    """Generate QR code URL for the work order number"""
    work_order = data.get('mainOrder', {}).get('workOrderNumber', '')
    if work_order:
        return f"https://api.qrserver.com/v1/create-qr-code/?size=80x80&data={work_order}"
    return "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAiIGhlaWdodD0iODAiIHZpZXdCb3g9IjAgMCA4MCA4MCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjgwIiBoZWlnaHQ9IjgwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSJibGFjayIvPgo8dGV4dCB4PSI0MCIgeT0iNDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSI4Ij5RUiBDb2RlPC90ZXh0Pgo8L3N2Zz4K"

def generate_product_rows(order_details):
    """Generate HTML table rows for product details"""
    rows = []
    for idx, item in enumerate(order_details, 1):
        product_name = item.get('productName', '')
        description = item.get('productDescription', '')
        specification = item.get('specification', '')
        quantity = item.get('orderQuantity', 0)
        
        # Combine product name and description
        full_description = f"{product_name}"
        if description:
            full_description += f"<br>{description}"
        if specification:
            full_description += f"<br>{specification}"
        
        row = f"""
        <tr>
            <td>{idx}</td>
            <td>{item.get('materialCode', '')}</td>
            <td>{full_description}</td>
            <td>自定义成品</td>
            <td>{quantity}</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_raw_materials_rows(raw_materials):
    """Generate HTML table rows for raw materials"""
    rows = []
    specifications = raw_materials.get('specifications', [])
    
    for spec in specifications:
        row = f"""
        <tr>
            <td>{spec.get('partName', '')}</td>
            <td>{spec.get('materialDescription', '')}</td>
            <td>{spec.get('orderSpec', '')}</td>
            <td>{spec.get('quantity', '')}</td>
            <td>{spec.get('workingSize', '')}</td>
            <td></td>
            <td>{spec.get('totalQuantity', '')}</td>
            <td></td>
            <td>{spec.get('totalSheets', '')}</td>
            <td></td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_publishing_rows(publishing):
    """Generate HTML table rows for publishing details"""
    rows = []
    details = publishing.get('details', [])
    
    for detail in details:
        row = f"""
        <tr>
            <td>{detail.get('partName', '')}</td>
            <td>{detail.get('total', '')}</td>
            <td>{detail.get('requirement', '')}</td>
            <td>{detail.get('version', '')}</td>
            <td>{detail.get('total', '')}</td>
            <td>{detail.get('size', '')}</td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_printing_rows(printing):
    """Generate HTML table rows for printing details"""
    rows = []
    details = printing.get('details', [])
    
    for detail in details:
        row = f"""
        <tr>
            <td>{detail.get('partName', '')}</td>
            <td>{detail.get('total', '')}</td>
            <td>{detail.get('frontColor', '')}</td>
            <td>{detail.get('backColor', '')}</td>
            <td></td>
            <td></td>
            <td>HP-INDIGO120K</td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_post_processing_rows(post_processing):
    """Generate HTML table rows for post processing details"""
    rows = []
    processes = post_processing.get('processes', [])
    
    for process in processes:
        row = f"""
        <tr>
            <td>{process.get('partName', '')}</td>
            <td>{process.get('process', '')}</td>
            <td></td>
            <td>{process.get('requirements', '')}</td>
            <td></td>
            <td></td>
            <td></td>
            <td>{process.get('supervisor', '')}</td>
            <td></td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_auxiliary_materials_rows(auxiliary_materials):
    """Generate HTML table rows for auxiliary materials"""
    rows = []
    materials = auxiliary_materials.get('materials', [])
    
    for material in materials:
        row = f"""
        <tr>
            <td>{material.get('partName', '')}</td>
            <td>{material.get('materialCode', '')}</td>
            <td>{material.get('materialName', '')}</td>
            <td>{material.get('specification', '')}</td>
            <td>{material.get('unit', '')}</td>
            <td>{material.get('quantity', '')}</td>
            <td>{material.get('remarks', '')}</td>
            <td>{material.get('unitArea', '')}</td>
            <td></td>
        </tr>"""
        rows.append(row)
    
    return '\n'.join(rows)

def generate_html_report(data, output_path):
    """Generate complete HTML report from JSON data"""
    
    # Extract main order information
    main_order = data.get('mainOrder', {})
    company_name = main_order.get('companyName', '佛山智冠彩印包装有限公司')
    order_number = main_order.get('orderNumber', '')
    work_order_number = main_order.get('workOrderNumber', '')
    important_notes = main_order.get('importantNotes', '')
    special_remarks = main_order.get('specialRemarks', '')
    
    # Extract footer information
    footer = data.get('footer', {})
    
    # Generate QR code URL
    qr_code_url = generate_qr_code_url(data)
    
    # Generate table rows
    product_rows = generate_product_rows(data.get('orderDetails', []))
    raw_materials_rows = generate_raw_materials_rows(data.get('rawMaterials', {}))
    publishing_rows = generate_publishing_rows(data.get('publishing', {}))
    printing_rows = generate_printing_rows(data.get('printing', {}))
    post_processing_rows = generate_post_processing_rows(data.get('postProcessing', {}))
    auxiliary_materials_rows = generate_auxiliary_materials_rows(data.get('auxiliaryMaterials', {}))
    
    # Get printing special requirements
    printing_special = data.get('printing', {}).get('specialRequirements', '注意版面清洁')
    
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>生产订单报表 - {work_order_number}</title>
    <style>
        /* 基础样式 - 复制PDF的视觉效果 */
        body {{
            font-family: "SimSun", "MS Song", serif;
            margin: 0;
            padding: 20px;
            background: white;
            font-size: 10.5px;
            line-height: 1.2;
        }}
        
        .report-container {{
            width: 595px; /* PDF width in points */
            margin: 0 auto;
            background: white;
            min-height: 842px; /* PDF height in points */
            position: relative;
        }}
        
        /* 页眉 - 公司标题 */
        .header {{
            text-align: center;
            margin-bottom: 15px;
        }}
        
        .company-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }}
        
        /* 订单信息行 */
        .order-info-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 10.5px;
        }}
        
        .order-info-item {{
            display: inline-block;
        }}
        
        /* 客户信息行 */
        .customer-info {{
            margin-bottom: 15px;
            font-size: 10.5px;
        }}
        
        /* 表格样式 */
        .section-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
            font-size: 10.5px;
        }}
        
        .section-table th,
        .section-table td {{
            border: 1px solid #000;
            padding: 3px 5px;
            text-align: left;
            vertical-align: top;
        }}
        
        .section-table th {{
            background-color: #f5f5f5;
            font-weight: bold;
            text-align: center;
        }}
        
        /* 产品详情表格 */
        .product-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
            font-size: 9px;
        }}
        
        .product-table th,
        .product-table td {{
            border: 1px solid #000;
            padding: 2px 3px;
            text-align: center;
            vertical-align: middle;
        }}
        
        .product-table th {{
            background-color: #f0f0f0;
            font-weight: bold;
        }}
        
        /* 重要说明 */
        .important-notes {{
            margin: 10px 0;
            padding: 5px;
            background-color: #fff8dc;
            border: 1px solid #ddd;
            font-size: 9px;
        }}
        
        /* 各个业务部分 */
        .business-section {{
            margin-bottom: 15px;
        }}
        
        .section-header {{
            background-color: #f0f0f0;
            padding: 3px 5px;
            border: 1px solid #000;
            font-weight: bold;
            text-align: center;
            margin-bottom: 5px;
        }}
        
        .section-label {{
            writing-mode: vertical-lr;
            text-orientation: mixed;
            background-color: #f0f0f0;
            border: 1px solid #000;
            padding: 5px 3px;
            text-align: center;
            font-weight: bold;
            width: 20px;
        }}
        
        /* 脚注 */
        .footer {{
            position: absolute;
            bottom: 20px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-between;
            font-size: 9px;
            border-top: 1px solid #ccc;
            padding-top: 5px;
        }}
        
        /* 布局容器 */
        .section-container {{
            display: flex;
            margin-bottom: 10px;
        }}
        
        .section-content {{
            flex: 1;
        }}
        
        /* 特别备注 */
        .special-remarks {{
            margin: 8px 0;
            font-size: 9px;
            font-weight: bold;
        }}
        
        /* QR 码位置 */
        .qr-code {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 80px;
            height: 80px;
            border: 1px solid #ccc;
        }}
        
        /* 响应式调整 */
        @media screen and (max-width: 700px) {{
            .report-container {{
                width: 100%;
                padding: 10px;
            }}
            
            .footer {{
                position: relative;
                bottom: auto;
            }}
        }}
        
        @media print {{
            body {{
                margin: 0;
                padding: 0;
            }}
            
            .report-container {{
                width: 100%;
                margin: 0;
            }}
            
            .footer {{
                position: fixed;
                bottom: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="report-container">
        <!-- QR码 -->
        <div class="qr-code">
            <img src="{qr_code_url}" alt="QR Code" style="width: 100%; height: 100%;">
        </div>
        
        <!-- 页眉 -->
        <div class="header">
            <div class="company-title">{company_name}生产单</div>
        </div>
        
        <!-- 订单信息行 -->
        <div class="order-info-row">
            <span class="order-info-item">订单类型：</span>
            <span class="order-info-item">下单日期：{order_number}</span>
            <span class="order-info-item">工单编号：{work_order_number}</span>
        </div>
        
        <!-- 客户信息 -->
        <div class="customer-info">
            <span>广州至坚文化创意有限公司</span>
            <span style="margin-left: 50px;">订单号：</span>
            <span style="margin-left: 50px;">资料袋</span>
            <span style="margin-left: 50px;">旧单编号：</span>
        </div>
        
        <!-- 产品详情表格 -->
        <table class="product-table">
            <thead>
                <tr>
                    <th>序号</th>
                    <th>物料编码</th>
                    <th>产品名称</th>
                    <th>成品尺寸</th>
                    <th>订单数</th>
                    <th>备品</th>
                    <th>应产数</th>
                    <th>交期</th>
                </tr>
            </thead>
            <tbody>
                {product_rows}
            </tbody>
        </table>
        
        <!-- 重要说明 -->
        <div class="important-notes">
            <strong>重要说明：</strong>{important_notes}
        </div>
        
        <!-- 原材部分 -->
        <div class="business-section">
            <div class="section-container">
                <div class="section-label">原<br>材</div>
                <div class="section-content">
                    <table class="section-table">
                        <thead>
                            <tr>
                                <th>部件名称</th>
                                <th>物料编码及名称</th>
                                <th>订单规格</th>
                                <th>数量</th>
                                <th>上机尺寸</th>
                                <th>开度</th>
                                <th>发料数</th>
                                <th>模数</th>
                                <th>合计张数</th>
                                <th>损耗数</th>
                            </tr>
                        </thead>
                        <tbody>
                            {raw_materials_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- 出版部分 -->
        <div class="business-section">
            <div class="section-container">
                <div class="section-label">出<br>版</div>
                <div class="section-content">
                    <table class="section-table">
                        <thead>
                            <tr>
                                <th>部件名称</th>
                                <th>模数</th>
                                <th>拼版说明及工艺要求</th>
                                <th>版数</th>
                                <th>套数</th>
                                <th>拼版尺寸</th>
                            </tr>
                        </thead>
                        <tbody>
                            {publishing_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- 印刷部分 -->
        <div class="business-section">
            <div class="section-container">
                <div class="section-label">印<br>刷</div>
                <div class="section-content">
                    <table class="section-table">
                        <thead>
                            <tr>
                                <th>部件名称</th>
                                <th>模数</th>
                                <th>正面颜色</th>
                                <th>反面颜色</th>
                                <th>应产数</th>
                                <th>放数</th>
                                <th>机台</th>
                            </tr>
                        </thead>
                        <tbody>
                            {printing_rows}
                        </tbody>
                    </table>
                    <div class="special-remarks">特别备注：{printing_special}</div>
                </div>
            </div>
        </div>
        
        <!-- 后工序部分 -->
        <div class="business-section">
            <div class="section-container">
                <div class="section-label">后<br>工<br>序</div>
                <div class="section-content">
                    <table class="section-table">
                        <thead>
                            <tr>
                                <th>部件名称</th>
                                <th>工序</th>
                                <th>模数</th>
                                <th>工艺要求</th>
                                <th>外发</th>
                                <th>应产</th>
                                <th>实产</th>
                                <th>机长</th>
                                <th>放数</th>
                            </tr>
                        </thead>
                        <tbody>
                            {post_processing_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- 辅材部分 -->
        <div class="business-section">
            <div class="section-container">
                <div class="section-label">辅<br>材</div>
                <div class="section-content">
                    <table class="section-table">
                        <thead>
                            <tr>
                                <th>部件名称</th>
                                <th>物料编码</th>
                                <th>物料名称</th>
                                <th>规格</th>
                                <th>单位</th>
                                <th>数量</th>
                                <th>备注</th>
                                <th>面积（㎡）</th>
                                <th>配数</th>
                            </tr>
                        </thead>
                        <tbody>
                            {auxiliary_materials_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- 页脚 -->
        <div class="footer">
            <span>制单：{footer.get('businessUnit', '小陈')}</span>
            <span>文件制作：{footer.get('reviewer', '小莫')}</span>
            <span>业务员：小李</span>
            <span>跟单：小林</span>
            <span>审核：{footer.get('approver', '老杜')}</span>
        </div>
    </div>
</body>
</html>"""
    
    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    return output_path

def main():
    # Paths
    json_path = "/home/runner/work/reports/reports/production_order_detailed_sample.json"
    output_path = "/home/runner/work/reports/reports/production_order_report.html"
    
    # Load JSON data
    print("Loading JSON data...")
    data = load_json_data(json_path)
    
    if not data:
        print("Failed to load JSON data")
        return
    
    # Generate HTML report
    print("Generating HTML report...")
    generated_path = generate_html_report(data, output_path)
    
    print(f"HTML report generated successfully: {generated_path}")
    print(f"File size: {os.path.getsize(generated_path)} bytes")

if __name__ == "__main__":
    main()