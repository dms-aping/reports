#!/usr/bin/env python3
"""
Demo Script - Generate HTML Report
演示脚本 - 生成HTML报表

This script demonstrates how to generate an HTML report from the JSON production order data.
此脚本演示如何从JSON生产订单数据生成HTML报表。

Usage / 使用方法:
    python3 demo_generate_report.py
"""

import os
import sys
import json
from pathlib import Path

# Add current directory to path so we can import the generator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from generate_html_report import generate_html_report, load_json_data
except ImportError:
    print("Error: Could not import generate_html_report module")
    print("Make sure generate_html_report.py is in the same directory")
    sys.exit(1)

def main():
    print("=== HTML Report Generation Demo ===")
    print("HTML报表生成演示")
    print()
    
    # File paths
    base_dir = Path(__file__).parent
    json_file = base_dir / "production_order_detailed_sample.json"
    output_file = base_dir / "demo_report.html"
    
    # Check if JSON file exists
    if not json_file.exists():
        print(f"Error: JSON file not found: {json_file}")
        print(f"错误：未找到JSON文件：{json_file}")
        return
    
    print(f"📄 Loading JSON data from: {json_file}")
    print(f"📄 从以下位置加载JSON数据：{json_file}")
    
    # Load and validate JSON data
    data = load_json_data(json_file)
    if not data:
        print("❌ Failed to load JSON data")
        print("❌ 加载JSON数据失败")
        return
    
    print("✅ JSON data loaded successfully")
    print("✅ JSON数据加载成功")
    
    # Display some key information
    main_order = data.get('mainOrder', {})
    company_name = main_order.get('companyName', 'N/A')
    work_order = main_order.get('workOrderNumber', 'N/A')
    order_count = len(data.get('orderDetails', []))
    
    print(f"   Company / 公司: {company_name}")
    print(f"   Work Order / 工单号: {work_order}")
    print(f"   Products / 产品数量: {order_count}")
    print()
    
    print(f"🔄 Generating HTML report: {output_file}")
    print(f"🔄 生成HTML报表：{output_file}")
    
    try:
        # Generate the HTML report
        result_path = generate_html_report(data, str(output_file))
        
        # Get file size
        file_size = os.path.getsize(result_path)
        
        print("✅ HTML report generated successfully!")
        print("✅ HTML报表生成成功！")
        print(f"   📁 File: {result_path}")
        print(f"   📁 文件：{result_path}")
        print(f"   📏 Size: {file_size:,} bytes")
        print(f"   📏 大小：{file_size:,} 字节")
        print()
        print("💡 To view the report:")
        print("💡 查看报表的方法：")
        print(f"   • Open in browser: file://{os.path.abspath(result_path)}")
        print(f"   • 在浏览器中打开：file://{os.path.abspath(result_path)}")
        print("   • Or start a local server and navigate to the file")
        print("   • 或启动本地服务器并导航到该文件")
        
    except Exception as e:
        print(f"❌ Error generating HTML report: {e}")
        print(f"❌ 生成HTML报表时出错：{e}")

if __name__ == "__main__":
    main()