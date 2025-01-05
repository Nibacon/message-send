import socket

def start_server():
    host = socket.gethostname()  # 自動獲取本機的電腦名稱
    port = 443  # 設定端口號為 443（您可以根據需要改為其他端口）

    # 創建並綁定 socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"伺服器正在 {host} 上監聽端口 {port}...")

    while True:
        # 等待客戶端連接
        client_socket, client_address = server_socket.accept()
        print(f"已連接: {client_address}")
        
        while True:
            # 等待接收訊息
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("等待對方回覆中...")  # 如果沒有收到訊息，顯示等待訊息
                continue  # 重新檢查是否有新的訊息

            print(f"收到訊息: {message}")

            # 等待伺服器回應
            response = input("請輸入回覆訊息: ")  # 伺服器輸入回覆訊息
            client_socket.send(response.encode('utf-8'))  # 發送回覆給客戶端

        # 關閉連接
        client_socket.close()

if __name__ == "__main__":
    start_server()
