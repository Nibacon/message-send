import socket
import time

def start_client():
    host = input("請輸入伺服器的主機名稱或 IP 地址: ")  # 輸入伺服器主機名稱或 IP 地址
    port = 443  # 設定端口號為 443（您可以根據需要改為其他端口）

    # 創建 socket 並連接伺服器
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # 請求用戶輸入要發送的訊息
        message = input("請輸入要發送的訊息: ")

        # 發送訊息到伺服器
        client_socket.send(message.encode('utf-8'))

        # 顯示等待回覆訊息
        print("等待對方回覆中...")

        # 等待接收端的回覆
        response = client_socket.recv(1024).decode('utf-8')

        if response:
            print(f"伺服器回覆: {response}")
        else:
            print("伺服器尚未回覆，等待中...")

        # 等待 1 秒鐘後繼續發送下一條訊息
        time.sleep(1)  # 等待 1 秒鐘

if __name__ == "__main__":
    start_client()
