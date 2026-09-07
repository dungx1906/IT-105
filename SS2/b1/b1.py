def process_revenue_report(order_list):
    total_revenue = 0
    successful_orders = 0

    for order in order_list:
        if order["status"] == "DELIVERED":
            total_revenue += order["fee"]
            successful_orders += 1

    average_revenue = total_revenue / successful_orders if successful_orders > 0 else 0

    return {
        "total_revenue": total_revenue,
        "successful_orders": successful_orders,
        "average_revenue": average_revenue
    }


order_data = [
    {"order_id": "01", "fee": 15000, "status": "DELIVERED"},
    {"order_id": "02", "fee": 20000, "status": "DELIVERED"},
    {"order_id": "03", "fee": 0, "status": "CANCELLED"},
    {"order_id": "04", "fee": -5000, "status": "RETURNED"},
    {"order_id": "05", "fee": 25000, "status": "DELIVERED"}
]

result = process_revenue_report(order_data)

print("==========================================")
print("     BAO CAO DOANH THU RIKKEIEXPRESS")
print("==========================================")
print(f"Tong doanh thu: {result['total_revenue']:,}d")
print(f"So don giao thanh cong: {result['successful_orders']}")
print(f"Doanh thu trung binh/don: {result['average_revenue']:,.0f}d")
print("==========================================")