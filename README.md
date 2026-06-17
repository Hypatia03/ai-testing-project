# AI Testing Project

## UI Automation Testing với Selenium, Pytest, Selenium Grid, Jenkins và Allure Report

---

# 1. Giới thiệu đề tài

Đây là dự án kiểm thử tự động (UI Automation Testing) được xây dựng bằng Python.

Dự án thực hiện kiểm thử luồng mua hàng End-to-End trên website:

https://www.saucedemo.com

Các chức năng được kiểm thử:

- Đăng nhập hệ thống
- Thêm sản phẩm vào giỏ hàng
- Thanh toán đơn hàng
- Data Driven Testing bằng CSV
- Screenshot khi test thất bại
- Báo cáo Allure
- Tích hợp Jenkins CI/CD
- Chạy Selenium Grid

---

# 2. Công nghệ sử dụng

| Công nghệ   | Mục đích                   |
| ------------- | ----------------------------- |
| Python 3.13   | Ngôn ngữ lập trình        |
| Selenium 4    | Tự động hóa trình duyệt |
| Pytest        | Framework kiểm thử          |
| Selenium Grid | Chạy test phân tán         |
| Jenkins       | CI/CD                         |
| Git           | Quản lý mã nguồn          |
| GitHub        | Lưu trữ source code         |
| Allure Report | Báo cáo kiểm thử          |
| Docker        | Khởi tạo Selenium Grid      |

---

# 3. Kiến trúc hệ thống

GitHub
↓
Jenkins
↓
Pytest
↓
Selenium Grid
↓
Chrome
↓
Allure Report

Mô tả:

1. Source code được lưu trên GitHub
2. Jenkins lấy source code từ GitHub
3. Jenkins thực thi Pytest
4. Pytest gọi Selenium
5. Selenium kết nối Selenium Grid
6. Selenium Grid mở Chrome
7. Kết quả test được lưu vào Allure Report

---

# 4. Cấu trúc project

```text
ai-testing-project
│
├── pages
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_add_cart.py
│   └── test_checkout.py
│
├── testdata
│   └── login_data.csv
│
├── screenshots
│
├── allure-results
│
├── conftest.py
│
├── requirements.txt
│
├── Jenkinsfile
│
└── docker-compose.yml
```

---

# 5. Mô hình Page Object Model (POM)

Dự án sử dụng Page Object Model.

## Login Page

File:

pages/login_page.py

Chức năng:

- Nhập username
- Nhập password
- Click Login
- Kiểm tra thông báo lỗi

---

## Inventory Page

File:

pages/inventory_page.py

Chức năng:

- Thêm sản phẩm vào giỏ hàng

---

## Cart Page

File:

pages/cart_page.py

Chức năng:

- Mở giỏ hàng
- Checkout

---

## Checkout Page

File:

pages/checkout_page.py

Chức năng:

- Nhập thông tin khách hàng
- Continue
- Finish Order

---

# 6. Data Driven Testing

File dữ liệu:

testdata/login_data.csv

Ví dụ:

```csv
username,password,expected
standard_user,secret_sauce,pass
standard_user,wrong_password,fail
wrong_user,secret_sauce,fail
```

Pytest sẽ tự động đọc dữ liệu CSV và chạy nhiều bộ test.

---

# 7. Chụp màn hình khi lỗi

File:

conftest.py

Khi testcase FAIL:

- Tự động chụp ảnh
- Lưu vào thư mục screenshots

Ví dụ:

```text
screenshots/
fail_test_login_20260614_001530.png
```

---

# 8. Cài đặt môi trường

## Bước 1: Clone source code

```bash
git clone https://github.com/Hypatia03/ai-testing-project.git

cd ai-testing-project
```

---

## Bước 2: Tạo môi trường ảo

```bash
python -m venv venv
```

Kích hoạt:

Windows:

```bash
venv\Scripts\activate
```

---

## Bước 3: Cài thư viện

```bash
pip install -r requirements.txt
```

---

# 9. Chạy Selenium Grid

Cài Docker Desktop trước.

Kiểm tra:

```bash
docker --version
```

Khởi động Grid:

```bash
docker-compose up -d
```

Kiểm tra:

```bash
http://localhost:4444
```

Nếu xuất hiện Selenium Grid Dashboard là thành công.

---

# 10. Chạy test bằng Pytest

## Chạy toàn bộ test

```bash
pytest -v
```

---

## Chạy test Login

```bash
pytest tests/test_login.py -v
```

---

## Chạy test Add Cart

```bash
pytest tests/test_add_cart.py -v
```

---

## Chạy test Checkout

```bash
pytest tests/test_checkout.py -v
```

---

# 11. Tạo Allure Report

Sinh kết quả:

```bash
pytest -v --alluredir=allure-results
```

---

Mở báo cáo:

```bash
allure serve allure-results
```

---

# 12. Cài đặt Jenkins

Cài:

- Java JDK 21
- Jenkins LTS

Kiểm tra:

```bash
java -version
```

```bash
jenkins --version
```

Mở:

```text
http://localhost:8080
```

---

# 13. Jenkins Pipeline

File:

Jenkinsfile

```groovy
pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v --alluredir=allure-results'
            }
        }

    }
}
```

---

---

# 14. Kết nối Jenkins với GitHub

Sau khi cài đặt Jenkins thành công, thực hiện các bước sau để Jenkins tự động lấy source code từ GitHub và chạy Pipeline.

## Bước 1: Truy cập Jenkins

Mở trình duyệt:

```text
http://localhost:8080
```

Đăng nhập bằng tài khoản Jenkins đã tạo.

---

## Bước 2: Tạo Pipeline Job mới

Tại màn hình chính Jenkins:

```text
New Item
```

Nhập tên project:

```text
AI-Testing-Project
```

Chọn:

```text
Pipeline
```

Nhấn:

```text
OK
```

---

## Bước 3: Cấu hình GitHub Repository

Kéo xuống phần:

```text
Pipeline
```

Tại mục:

```text
Definition
```

Chọn:

```text
Pipeline script from SCM
```

SCM:

```text
Git
```

Repository URL:

```text
https://github.com/Hypatia03/ai-testing-project.git
```

Branch:

```text
*/main
```

Script Path:

```text
Jenkinsfile
```

Ví dụ:

```text
Definition      : Pipeline script from SCM
SCM             : Git
Repository URL  : https://github.com/Hypatia03/ai-testing-project.git
Branch Specifier: */main
Script Path     : Jenkinsfile
```

---

## Bước 4: Lưu cấu hình

Nhấn:

```text
Save
```

Jenkins sẽ tạo Job mới.

---

## Bước 5: Chạy Pipeline

Tại giao diện Job:

```text
Build Now
```

Jenkins sẽ:

```text
1. Clone source code từ GitHub
2. Đọc file Jenkinsfile
3. Cài đặt dependencies
4. Chạy Pytest
5. Sinh kết quả Allure
```

---

## Bước 6: Kiểm tra Console Output

Chọn Build vừa chạy:

```text
#1
```

Sau đó:

```text
Console Output
```

Nếu thành công sẽ thấy:

```text
===================
7 passed
===================
```

---

# 15. Cấu hình Allure Report trên Jenkins

Allure giúp hiển thị báo cáo kiểm thử trực quan trên Jenkins.

---

## Bước 1: Cài Plugin Allure

Truy cập:

```text
Manage Jenkins
```

↓

```text
Plugins
```

↓

```text
Available Plugins
```

Tìm:

```text
Allure
```

Chọn:

```text
Allure
```

Nhấn:

```text
Install
```

Sau khi cài xong:

```text
Restart Jenkins
```

---

## Bước 2: Cấu hình Allure Commandline

Truy cập:

```text
Manage Jenkins
```

↓

```text
Tools
```

Kéo xuống:

```text
Allure Commandline installations
```

Nhấn:

```text
Add Allure Commandline
```

Điền:

```text
Name: allure
```

Tick:

```text
Install automatically
```

Version:

```text
Latest
```

Ví dụ:

```text
Name    : allure
Version : Latest
```

Nhấn:

```text
Apply
```

↓

```text
Save
```

---

## Bước 3: Kiểm tra Allure đã được Jenkins nhận diện

Vào:

```text
Manage Jenkins
```

↓

```text
Tools
```

Nếu thấy:

```text
Allure Commandline
 └── allure
```

thì cấu hình thành công.

---

## Bước 4: Cấu hình Jenkinsfile

Ví dụ Jenkinsfile:

```groovy
pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest --alluredir=allure-results'
            }
        }

    }

    post {
        always {
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            )
        }
    }
}
```

---

## Bước 5: Chạy lại Pipeline

Tại Jenkins Job:

```text
Build Now
```

Jenkins sẽ:

```text
GitHub
  ↓
Jenkins
  ↓
Pytest
  ↓
Selenium Grid
  ↓
Chrome Browser
  ↓
Allure Results
  ↓
Allure Report
```

---

## Bước 6: Xem Allure Report

Sau khi Build thành công:

```text
AI-Testing-Project
```

↓

```text
Build #1
```

↓

```text
Allure Report
```

Tại đây có thể xem:

* Tổng số Test Case
* Passed
* Failed
* Duration
* Trend
* Suites
* Screenshots lỗi

Ví dụ:

```text
Total: 7
Passed: 7
Failed: 0
Skipped: 0
```

---

## Kiến trúc CI/CD của Project

```text
GitHub Repository
        │
        ▼
      Jenkins
        │
        ▼
      Pytest
        │
        ▼
   Selenium Grid
        │
        ▼
   Chrome Browser
        │
        ▼
  Allure Results
        │
        ▼
   Allure Report
```

Ý nghĩa:

* GitHub lưu trữ source code.
* Jenkins tự động lấy source từ GitHub.
* Pytest thực thi Test Case.
* Selenium Grid điều khiển trình duyệt.
* Chrome thực hiện thao tác người dùng.
* Allure thu thập kết quả kiểm thử.
* Allure Report hiển thị báo cáo trực quan.

# 16. Kết quả hiện tại

Các testcase đã chạy thành công:

| Test Case            | Trạng thái |
| -------------------- | ------------ |
| Login thành công   | PASS         |
| Login sai password   | PASS         |
| Login sai username   | PASS         |
| Login username rỗng | PASS         |
| Login password rỗng | PASS         |
| Add to Cart          | PASS         |
| Checkout             | PASS         |

Tổng:

```text
7 PASSED
```

---

# 17. Hướng phát triển

- Tích hợp GitHub Actions
- Chạy song song nhiều trình duyệt
- Cross Browser Testing
- Tích hợp AI tự sinh Test Case
- Tích hợp AI tự phân tích lỗi
- Tích hợp Database Testing
- Tích hợp API Testing

---

# 18. Tác giả

Sinh viên thực hiện:

Nguyễn Thị Ngọc Hân

Chuyên ngành:

Công nghệ Phần mềm

Đề tài:

UI Automation Testing End-to-End sử dụng Selenium, Pytest, Selenium Grid, Jenkins và Allure Report.
