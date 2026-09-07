def classify_logistics_feature(feature_name):
    feature = feature_name.lower()

    if "đã lấy hàng" in feature or "quét mã vạch" in feature or "in phiếu cước" in feature:
        return "TPS"

    if "báo cáo" in feature or "thống kê" in feature:
        return "MIS"

    if "dự báo" in feature or "phân tích" in feature or "quá tải" in feature:
        return "DSS"

    return "Không xác định"


features = [
    "Tài xế bấm nút Đã lấy hàng",
    "Nhân viên kho quét mã vạch nhập kho",
    "In phiếu cước giao hàng",
    "Báo cáo tổng hợp doanh thu tháng",
    "Thống kê số lượng đơn giao tuần trước",
    "Công cụ phân tích dự báo điểm nóng quá tải đơn hàng"
]

for feature in features:
    print(f"{feature} -> {classify_logistics_feature(feature)}")