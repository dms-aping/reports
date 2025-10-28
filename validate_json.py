#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Production Order JSON Validator and Pretty Printer
生产订单JSON验证和格式化工具

This script validates and displays the production order JSON structure.
"""

import json
import sys
from pathlib import Path

def validate_json_file(file_path):
    """Validate and pretty print a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ {file_path} is valid JSON")
        return data
    except json.JSONDecodeError as e:
        print(f"❌ {file_path} contains invalid JSON: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None

def display_order_summary(data):
    """Display a summary of the order data."""
    if not data:
        return
    
    print("\n" + "="*60)
    print("生产订单摘要 / Production Order Summary")
    print("="*60)
    
    # Main order info
    main_order = data.get('mainOrder', {})
    print(f"公司名称 / Company: {main_order.get('companyName', 'N/A')}")
    print(f"订单号 / Order No: {main_order.get('orderNumber', 'N/A')}")
    print(f"工单号 / Work Order: {main_order.get('workOrderNumber', 'N/A')}")
    
    # Order details count
    order_details = data.get('orderDetails', [])
    print(f"产品数量 / Product Count: {len(order_details)}")
    
    # Raw materials count
    raw_materials = data.get('rawMaterials', {}).get('specifications', [])
    print(f"原材料类型 / Raw Material Types: {len(raw_materials)}")
    
    # Post-processing steps
    post_processing = data.get('postProcessing', {}).get('processes', [])
    print(f"后工序步骤 / Post-processing Steps: {len(post_processing)}")
    
    # Auxiliary materials
    aux_materials = data.get('auxiliaryMaterials', {}).get('materials', [])
    print(f"辅助材料 / Auxiliary Materials: {len(aux_materials)}")
    
    print("="*60)

def main():
    """Main function to validate both JSON files."""
    current_dir = Path(__file__).parent
    
    # Validate basic sample
    basic_file = current_dir / "sample_production_order.json"
    print("Validating basic sample...")
    basic_data = validate_json_file(basic_file)
    
    if basic_data:
        display_order_summary(basic_data)
    
    print("\n" + "-"*60 + "\n")
    
    # Validate detailed sample
    detailed_file = current_dir / "production_order_detailed_sample.json"
    print("Validating detailed sample...")
    detailed_data = validate_json_file(detailed_file)
    
    if detailed_data:
        display_order_summary(detailed_data)
    
    # Check if both files are valid
    if basic_data and detailed_data:
        print("\n✅ All JSON files are valid and ready for use!")
        return 0
    else:
        print("\n❌ Some JSON files have validation errors.")
        return 1

if __name__ == "__main__":
    sys.exit(main())