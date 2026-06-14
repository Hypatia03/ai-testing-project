import os
import pytest
from datetime import datetime
from selenium import webdriver

# ====================================================================
# 1. FIXTURE KHỞI TẠO TRÌNH DUYỆT (Để sửa lỗi "fixture 'driver' not found")
# ====================================================================
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    
    # Kết nối đến Selenium Grid đang chạy ngầm của bạn
    grid_url = "http://localhost:4444/wd/hub"
    
    # Khởi tạo driver từ xa thông qua Grid
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )
    
    yield driver  # Cung cấp driver này cho các bài test sử dụng
    
    driver.quit() # Tắt trình duyệt sau khi test xong để giải phóng bộ nhớ

# ====================================================================
# 2. HOOK TỰ ĐỘNG CHỤP ẢNH MÀN HÌNH KHI BÀI TEST BỊ LỖI (FAILED)
# ====================================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Kiểm tra nếu bài test chạy xong (when == "call") và kết quả là THẤT BẠI (failed)
    if report.when == "call" and report.failed:
        try:
            # Lấy đối tượng driver đang chạy trong bài test đó ra để chụp ảnh
            driver = item.funcargs["driver"]
            
            # Tự động tạo thư mục 'screenshots' nếu trên máy chưa có
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
                
            # Tạo tên file ảnh theo thời gian: năm tháng ngày_giờ phút giây
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/fail_{item.name}_{timestamp}.png"
            
            # Ra lệnh cho trình duyệt chụp ảnh màn hình và lưu lại
            driver.save_screenshot(screenshot_path)
            print(f"\n[INFO] Đã chụp ảnh màn hình lỗi tại: {screenshot_path}")
            
        except Exception as e:
            print(f"\n[ERROR] Không thể chụp ảnh màn hình: {e}")