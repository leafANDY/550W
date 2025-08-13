# ASCII艺术标题 ，使用颜色标记美化显示
texts = '''[white]
███████╗███████╗ ██████╗ [red]██╗    ██╗[/red]
██╔════╝██╔════╝██╔═████╗[red]██║    ██║[/red]
███████╗███████╗██║██╔██║[red]██║ █╗ ██║[/red]
╚════██║╚════██║████╔╝██║[red]██║███╗██║[/red]
███████║███████║╚██████╔╝[red]╚███╔███╔╝[/red]
╚══════╝╚══════╝ ╚═════╝  [red]╚══╝╚══╝[/red]
                                   '''
# 导入必要的库
import time  # 时间相关功能 ，如延时操作
import hashlib  # 哈希算法 ，用于数据加密和校验
import os  # 操作系统接口 ，用于文件和目录操作
import sys  # 系统相关参数和函数 ，用于与Python解释器交互
import random  # 随机数生成 ，用于生成随机值
import shutil  # 高级文件操作 ，如文件复制和移动
from datetime import datetime  # 日期和时间处理 ，用于获取和处理时间信息
from rich.console import Console  # 终端输出美化 ，用于美化控制台输出

# 定义加载动画列表 ，包含多种风格的加载动画
spinnerlist = ['aesthetic',  # 美学风格加载动画
               'arc',  # 弧形加载动画
               'arrow',  # 箭头加载动画
               'arrow2',  # 箭头2加载动画
               'arrow3',  # 箭头3加载动画
               'balloon',  # 气球加载动画
               'balloon2',  # 气球2加载动画
               'betaWave',  # β波加载动画
               'bounce',  # 弹跳加载动画
               'bouncingBall',  # 弹跳球加载动画
               'bouncingBar',  # 弹跳条加载动画
               'boxBounce',  # 方块弹跳加载动画
               'boxBounce2',  # 方块弹跳2加载动画
               'christmas',  # 圣诞节加载动画
               'circle',  # 圆形加载动画
               'circleHalves',  # 半圆加载动画
               'circleQuarters',  # 四分之一圆加载动画
               'clock',  # 时钟加载动画
               'dots',  # 点加载动画
               'dots2',  # 点2加载动画
               'dots3',  # 点3加载动画
               'dots4',  # 点4加载动画
               'dots5',  # 点5加载动画
               'dots6',  # 点6加载动画
               'dots7',  # 点7加载动画
               'dots8',  # 点8加载动画
               'dots8Bit',  # 8位点加载动画
               'dots9',  # 点9加载动画
               'dots10',  # 点10加载动画
               'dots11',  # 点11加载动画
               'dots12'  # 点12加载动画
               ]

# 初始化用户名
name = "???"  # 默认用户名

# 初始化设置变量
isfirstlaunch = ""  # 是否首次启动标志
isloggedin = ""  # 登录状态标志
style = ""  # 显示样式
spinner=""  # 加载动画类型

# 尝试读取密码文件，如果不存在则创建
try:
    passf = open('pass.json', 'r',encoding="utf-8")  # 尝试打开密码文件
    passdic = eval(passf.read())  # 读取密码字典
    passf.close()  # 关闭文件
except:
    passf = open('pass.json', 'w',encoding="utf-8")  # 如果文件不存在，创建新文件
    passf.write("{}")  # 写入空字典
    passf.close()  # 关闭文件
# 尝试读取设置文件，如果不存在则创建默认设置
try:
    f = open('setting.json','r',encoding="utf-8")  # 尝试打开设置文件 #  尝试打开名为'setting.json'的文件，以只读模式
    settingdic = eval(f.read())  # 读取设置字典 #  读取文件内容并使用eval函数将其转换为字典
    f.close()  # 关闭文件
    for i in settingdic:  # 遍历设置字典 #  遍历设置字典中的每个键值对
        exec(i + "=" + str(settingdic[i]))  # 执行设置语句 #  使用exec函数执行设置语句，将字典中的键设置为变量，值为变量的值
    #print(type(isfirstlaunch),type(isloggedin)) #  调试代码，打印isfirstlaunch和isloggedin变量的类型（已注释）
except:
    f = open('setting.json','w',encoding="utf-8") #  如果发生异常（如文件不存在），则执行以下代码     以写入模式打开'setting.json'文件
    settingdic = {'isfirstlaunch': 'True', 'isloggedin': '{"?":False,"name":""}', 'style': "'bold green'", 'spinner': "'r'"} #  创建默认设置字典
    f.write("""{'isfirstlaunch': 'True', 'isloggedin': '{"?":False,"name":""}', 'style': "'bold green'", 'spinner': "'r'"}""") #  将默认设置字典写入文件
    f.close() #  关闭文件

# 检查spinner变量是否不在spinnerlist列表中
if spinner not in spinnerlist:
    # 如果spinner不在列表中，则从spinnerlist中随机选择一个元素赋值给spinner
    spinner = random.choice(spinnerlist)

commanddic = {"exit":"quit()", #  定义命令字典，将命令字符串映射到对应的函数或代码
              "quit":"quit()",
              "setting":"print(settingdic)",
              "info":"info()",
              "ls":"ls()",
              "clear":"os.system('cls')",
              "cls":"os.system('cls')",
              "help":"help()",
              "cd":"cd",
              "logout":"logout()", #  登出命令
              "reboot":"reboot()", #  重启命令
              "rm":"os.remove", #  删除文件命令
              "mv":"shutil.move", #  移动/重命名文件命令
              "cp":"shutil.copy", #  复制文件命令
              "chmod":"os.chmod", #  修改文件权限命令
              "mkdir":"os.mkdir", #  创建目录命令
              "makedirs":"os.makedirs", #  创建多级目录命令
              "rmdir":"os.rmdir", #  删除空目录命令
              "rmtree":"shutil.rmtree", #  递归删除目录命令
              "time":"time()", #  获取时间命令
              "useradd":"logon()", #  添加用户命令
              "userdel":"userdel", #  删除用户命令
              "":"" #  空命令，用于占位或特殊情况
              }

console = Console() #  创建一个控制台对象

运算符列表 = ["+", "-", "*", "/", "%", "**", "//","==", "!=", "<", ">", "<=", ">="] #  定义一个运算符列表，包含各种数学和比较运算符

def hash(x):
    return hashlib.sha512(hashlib.sha512(x.encode()).hexdigest().encode()).hexdigest()

#!
def sound():
    print('\a',end='')

def w(v_name,vaule,dic):
    exec(v_name + "=" + str(vaule))
    dic[str(v_name)] = vaule #  将变量值以字符串形式作为键存入字典

def reboot():
    with console.status('''正在重启...''',spinner=spinner): #"""    重启函数    使用进度条显示重启状态，保存密码和设置信息到JSON文件，然后重新执行程序    """
        time.sleep(1) #  暂停1秒
        passf = open('pass.json', 'w',encoding="utf-8") #  打开密码文件准备写入
        passf.write(str(passdic)) #  将密码字典转换为字符串并写入文件
        passf.close() #  关闭密码文件
        f = open('setting.json','w',encoding="utf-8") #  打开设置文件准备写入
        f.write(str(settingdic)) #  将设置字典转换为字符串并写入文件
        f.close() #  关闭设置文件
        python = sys.executable #  获取当前Python解释器的路径
        os.execl(python, python, *sys.argv)

def logout():
    with console.status('''正在登出...''',spinner=spinner): #"""    登出函数    使用进度条显示登出状态，将登录状态设置为未登录，然后调用重启函数    """
        time.sleep(1) #  暂停1秒
        w("isloggedin",{"?":False,"name":""},settingdic) #  更新登录状态为未登录
        reboot() #  调用重启函数

def logon():
    global passdic #  声明使用全局变量passdic
    while True: #  无限循环，直到用户成功登录
        console.print('''用户名:''',end='',style = style) #  打印用户名提示
        name = console.input() #  获取用户输入的用户名
        console.print('''密码:''',end='',style = style) #  打印"密码:"提示，不换行，应用指定样式
        passw1 = console.input(password=True) #  获取用户输入的密码，隐藏输入内容
        console.print('''确认密码:''',end='',style = style) #  打印"确认密码:"提示，不换行，应用指定样式
        passw2 = console.input(password=True) #  再次获取用户输入的密码，隐藏输入内容
        if passw1 == passw2: #  检查两次输入的密码是否一致
            with console.status('''正在保存中...''',spinner = spinner): #  显示保存状态和加载动画
                passdic[name] = hash(passw1) #  将密码哈希后存储到字典中
                console.log('''[bold green]保存成功''',style = style) #  打印保存成功的绿色提示信息
        else:
            console.log('''[bold red]两次输入的密码不一致，请重新输入''') #  打印密码不一致的红色错误提示

def login():
    global passdic #  声明使用全局变量passdic
    global name #  声明使用全局变量name
    while True: #  无限循环，直到登录成功
            time.sleep(0.5) #  暂停0.5秒
            console.print('''用户名:''',end='',style = style) #  打印"用户名:"提示，不换行，应用指定样式
            name = console.input() #  获取用户输入的用户名
            console.print('''密码:''',end='',style = style) #  打印"密码:"提示，不换行，应用指定样式
            password = hash(console.input(password=True)) #  获取用户输入的密码并哈希
            #print(password) #  注释掉的调试输出
            with console.status("身份验证中...",spinner = spinner):
                time.sleep(1) #  模拟验证过程，暂停1秒
                if name in passdic:
                    if password == passdic[name]: #  验证密码哈希是否匹配
                        console.log(f'''身份验证通过，欢迎您，[bold bule]{name}[/bold bule]''',style = style) #  打印登录成功信息
                        w('isloggedin',f'{{"?":"True","name":"{name}"}}',settingdic)
                        sound() #  播放提示音
                        break #  跳出当前循环
                    else:
                        console.log('''[bold red]身份验证失败，请重新输入''') #  打印红色错误信息提示身份验证失败
                        sound() #  播放提示音
                else:
                    console.log('''[bold red]用户不存在''') #  打印红色错误信息提示用户不存在
                    sound() #  播放提示音

def quit():
    with console.status('''正在退出...''',spinner=spinner): #  显示退出状态和加载动画
        time.sleep(1) #  暂停1秒
        passf = open('pass.json', 'w',encoding="utf-8") #  以写入模式打开密码文件
        passf.write(str(passdic)) #  将密码字典写入文件
        passf.close() #  关闭密码文件
        f = open('setting.json','w',encoding="utf-8") #  以写入模式打开设置文件
        f.write(str(settingdic)) #  将设置字典写入文件
        f.close() #  关闭设置文件
        sys.exit(0) #  退出程序，返回状态码0

def ls():
    for i in os.listdir(): #  遍历当前目录下的所有文件和文件夹
        console.print(i,style = style) #  打印文件名，并应用样式

def info():
    console.print(os.name,style = style) #  打印操作系统名称，并应用样式
    console.print(os.getcwd(),style = style) #  打印当前工作目录，并应用样式

def help():
    for i in commanddic: #"""    显示所有可用命令的帮助信息    遍历命令字典并打印每个命令    """
        console.print(i,style = style)

def cd(path):
    normalized0_path = path.replace("\\","/") #  将反斜杠转换为正斜杠，确保路径格式统一
    os.chdir(normalized0_path)

def time():
    console.log(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),style = style) #  使用console.log输出格式化后的当前时间，style参数用于设置输出样式

def userdel(user):
    global passdic #  声明使用全局变量passdic
    if user in passdic: #  检查用户是否存在于passdic中
        password = hash(console.input('''[bold red]请输入密码以确认:''')) #  提示用户输入密码进行确认，输入的密码会被哈希处理
        if password == passdic[user]: #  验证输入的密码是否与存储的密码匹配
            console.log('''[bold red]用户已删除''') #  如果密码正确，输出用户已删除的消息，并从passdic中删除该用户
            del passdic[user]
        else:
            console.log('''[bold red]密码错误''') #  如果密码错误，输出密码错误的消息，并调用sound函数发出提示音
            sound()
    else:
        console.log('''[bold red]用户不存在''') #  如果用户不存在，输出用户不存在的消息，并调用sound函数发出提示音
        sound()

if __name__ == "__main__": #  当该脚本作为主程序运行时执行的代码块
    print('''\n''') #  打印两个换行符，用于增加输出间距
    console.log('''正在加载中...''',style = style) #  输出"正在加载中..."的提示信息，使用指定的样式
    time.sleep(1) #  暂停1秒，模拟加载过程
    console.log('''这里是''',style = style) #  输出"这里是"的提示信息，使用指定的样式
    time.sleep(0.5) #  暂停0.5秒，控制输出速度
    console.print(texts) #  打印传入的文本内容
    sound() #  调用sound函数，可能用于播放声音提示
    time.sleep(1) #  暂停1秒
    if isfirstlaunch: #  判断是否是首次启动
        console.log('''这是你的第一次启动，请设置你的用户名和密码''',style = style) #  如果是首次启动，提示用户设置用户名和密码
        logon() #  调用logon函数进行注册
        w('isfirstlaunch','False',settingdic) #  将isfirstlaunch的值更新为False，记录已不是首次启动
        console.log('''设置成功,正在重新启动''',style = style) #  提示设置成功，准备重新启动
        time.sleep(1) #  暂停1秒
        reboot() #  调用reboot函数重启程序
    elif isloggedin["?"] == 'False':       #  如果不是首次启动，检查是否已登录
        login() #  如果未登录，调用login函数进行登录
    else: #  如果已经登录
        name = isloggedin["name"] #  获取已登录用户名
        with console.status("身份验证中...",spinner = spinner): #  显示身份验证状态，使用指定的加载动画
            time.sleep(1) #  暂停1秒，模拟验证过程
            console.log(f'''身份验证通过，欢迎您，[bold bule]{name}[/bold bule]''',style = style) #  输出欢迎信息，显示用户名，使用加粗蓝色样式
    while True: #  进入主循环，持续接收用户命令
        current_dir = os.getcwd() #  获取当前工作目录
        command = console.input(f'''{current_dir}>''') #  接收用户输入的命令
        if command in commanddic: #  检查命令是否在命令字典中
            exec(commanddic[command]) #  如果命令存在，执行对应的代码
        elif command.split(' ')[0] in commanddic: #  检查命令是否在命令字典中
            try:
                command = command.split(' ') #  将命令分割成列表
                if command[0] == 'cd': #  处理cd命令
                    if command[1][1] == ':': #  检查是否是盘符路径
                        exec(f'''{command[0]}('{command[1]}\\')''') #  执行cd命令并添加反斜杠
                    else:
                        exec(f'''{command[0]}('{command[1]}')''') #  执行cd命令
                else:
                    if len(command) > 2: #  如果命令有多个参数
                        for i in range(1,len(command)): #  合并参数
                            command[1] = command[1] + ',' + command[i]
                    exec(f'''{command[0]}({command[1]})''') #  执行命令
            except:
                console.log('''[bold red]错误: 无法识别的命令''') #  输出错误信息
        elif (i in command for i in 运算符列表): #  检查是否是数学表达式
                try:
                    d = eval(command) #  计算表达式
                    console.print(d,style = style) #  输出结果
                except:
                    console.log('''[bold red]错误: 无法识别的表达式''') #  输出错误信息
                    sound() #  播放错误音效
        elif '.' in command: #  检查是否是文件路径
            try:
                os.startfile(command) #  打开文件
            except:
                console.log('''[bold red]错误: 无法识别的文件''') #  输出错误信息
                sound() #  播放错误音效
        else: #  其他情况
            console.log('''[bold red]错误: 无法识别的命令''') #  输出错误信息
            sound() #  播放错误音效
