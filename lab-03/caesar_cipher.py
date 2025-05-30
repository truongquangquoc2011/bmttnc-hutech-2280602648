import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests  # dùng để gửi HTTP request đến API Flask

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()           # khởi tạo giao diện từ file caesar.py
        self.ui.setupUi(self)              # gắn giao diện lên cửa sổ chính
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)  # khi bấm nút Encrypt → gọi hàm
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)  # khi bấm nút Decrypt → gọi hàm

    def call_api_encrypt(self):  # Hàm xử lý khi người dùng bấm nút Encrypt
        url = "http://127.0.0.1:5000/api/caesar/encrypt"  # URL API mã hóa từ Flask backend
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),  # lấy nội dung nhập từ ô plain_text
            "key": self.ui.txt_key.text()                         # lấy giá trị khóa từ ô key
        }

        try:
            response = requests.post(url, json=payload)           # gửi POST request với payload
            if response.status_code == 200:                       # kiểm tra nếu mã phản hồi OK
                data = response.json()                            # chuyển kết quả từ JSON → dict
                self.ui.txt_cipher_text.setText(data["encrypted_message"])  # hiển thị kết quả

                # Hiện thông báo popup
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")  # lỗi nếu status code khác 200
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)  # bắt ngoại lệ nếu không kết nối được API
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),  
            "key": self.ui.txt_key.text()
        } 
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])  # Gán kết quả giải mã vào ô plain text

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")  # Hiển thị thông báo popup nếu thành công
                msg.exec_()
            else:
                print("Error while calling API")  # Thông báo nếu server trả về mã lỗi
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)  # Thông báo nếu không kết nối được API

if __name__ == "__main__":  # Kiểm tra nếu chạy trực tiếp file này
    app = QApplication(sys.argv)  # Khởi tạo ứng dụng Qt
    window = MyApp()              # Tạo cửa sổ chính với lớp MyApp đã định nghĩa
    window.show()                 # Hiển thị cửa sổ
    sys.exit(app.exec_())         # Bắt đầu vòng lặp sự kiện chính của Qt

        
