import json
import os
import time
import random
import Sunny as SyNet
import sqlite3
from datetime import datetime


# 验证函数
def yanzheng():
    # 定义字符映射表
    codeMap = {"fc":"[re]","ep":"[Af]","rj":"[M_]","sp":"[sW]","ws":"[Pj]","mb":"[^~]","ww":"[Dp]","wh":"[ZH]","ph":"[b+]","hk":"[3b]","mc":"[%)]","fm":"[$4]","nm":"[T!]","ei":"[J3]","pd":"[(A]","ef":"[%t]","xf":"[n_]","na":"[W6]","mr":"[dn]","km":"[b*]","aw":"[#*]","sj":"[~6]","ry":"[t#]","sd":"[$R]","eh":"[!!]","wp":"[TE]","fy":"[s6]","ex":"[EE]","ce":"[PS]","xr":"[~z]","cj":"[xh]","am":"[(G]","kw":"[Nr]","hj":"[p@]","ia":"[jO]","mp":"[75]","py":"[6C]","hc":"[46]","sk":"[(8]","hp":"[SB]","my":"[pq]","wk":"[Xd]","bk":"[Q^]","ak":"[)J]","cw":"[ai]","ym":"[Te]","yh":"[Cd]","xb":"[R5]","yy":"[#H]","nt":"[4)]","bc":"[#J]","fe":"[2+]","ni":"[f@]","bb":"[!k]","jc":"[$Q]","an":"[m$]","ee":"[RH]","nn":"[n$]","jr":"[5F]","pp":"[JQ]","fx":"[86]","2":"[)h]","3":"[iL]","4":"[r2]","5":"[Ys]","6":"[7p]","7":"[!5]","8":"[@A]","A":"[_W]","B":"[Kt]","C":"[m#]","D":"[A!]","E":"[M!]","F":"[xG]","G":"[k@]","H":"[_!]","J":"[rP]","K":"[z#]","M":"[r$]","N":"[rN]","P":"[t$]","Q":"[3(]","R":"[fF]","S":"[H)]","T":"[J@]","W":"[83]","X":"[t5]","Y":"[T_]","Z":"[CT]","a":"[Jt]","b":"[Ks]","c":"[yn]","d":"[2r]","e":"[#2]","f":"[yM]","h":"[)m]","i":"[mx]","j":"[YV]","k":"[$j]","m":"[Xy]","n":"[Bk]","p":"[5$]","r":"[EH]","s":"[Pw]","t":"[j(]","w":"[p7]","x":"[a+]","y":"[B2]","z":"[4n]","~":"[~C]","!":"[iw]","@":"[SK]","#":"[Pf]","$":"[de]","%":"[3t]","^":"[H_]","&":"[WA]","*":"[!A]","(":"[z*]",")":"[)n]","_":"[&k]","+":"[*F]","{":"[3k]",'"':"[t]",":":"[j7]","}":"[8u]","0":"[2]","1":"[k6]"}


    # 随机数生成函数
    def random_num(min_num, max_num):
        return random.randint(min_num, max_num)

    # 替换函数
    def owo_replace_all(string, s1, s2):
        while s1 in string:
            string = string.replace(s1, s2)
        return string

    # 解码函数
    def owo_decode(item_str):
        for item in codeMap:
            item_str = owo_replace_all(item_str, codeMap[item], item)
        while ']' in item_str:
            item_str = owo_decode(item_str)
        return item_str

    # 文件存储与读取函数
    def read_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        return None

    def write_to_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content)
    owomm = read_from_file('C:\WINDOWS\Temp\owomm.txt')
    if owomm and (len(owomm) > 20):
        try:
            data = owo_decode(owomm)
            data = json.loads(data)
            if data['time'] > int(time.time() * 1000):
                # print('登陆成功')
                return True
            else:
                sqm = str(random_num(1000, 9999))
                write_to_file('C:\WINDOWS\Temp\owomm.txt', sqm)
        except Exception as error:
            write_to_file("C:\WINDOWS\Temp\owomm.txt", "")
    sqm = read_from_file('C:\WINDOWS\Temp\owomm.txt')
    if not sqm:
        sqm = str(random_num(1000, 9999))
        write_to_file('C:\WINDOWS\Temp\owomm.txt', sqm)
    res_input = input(f'您是ID为[{sqm}]，请向客服索要密码:')
    if res_input:
        # 判断是否是离线码
        if len(res_input) > 30:
            data = owo_decode(res_input)
            data = json.loads(data)
            if data['time'] > int(time.time() * 1000) and sqm == data['code']:
                print('使用成功')
                write_to_file("C:\WINDOWS\Temp\owomm.txt", res_input)
                return True
        else:
            import requests
            headers = {
                "Content-Type": "application/json"
            }
            payload = json.dumps({"path": "cdk/" + res_input})
            response = requests.post(
                "https://service-hnqivk8b-1251887489.sh.apigw.tencentcs.com/release/read", 
                headers=headers, data=payload
            )
            result = response.text
            if result == 'Fail':
                print('密码错误')
                return False
            
            data = owo_decode(result)
            # print(data)
            data = json.loads(data)
            if data['time'] > int(time.time() * 1000) and sqm == data['code']:
                print('使用成功')
                write_to_file("C:\WINDOWS\Temp\owomm.txt", result)
                return True

    return False


if (not yanzheng()):
    exit()

def BytesToStr(b):
    """ 将字节数组转为字符串 """
    try:
        return b.decode('utf-8')
    except:
        return b.decode('gbk')


def replace_bytes(byte_array, old_bytes, new_bytes):
    """ 字节数组替换 """
    start_pos = byte_array.find(old_bytes)
    if start_pos == -1:
        # 如果需要替换的字节数组不存在，返回原始字节数组
        return byte_array
    end_pos = start_pos + len(old_bytes)
    new_byte_array = bytearray(byte_array)
    new_byte_array[start_pos:end_pos] = new_bytes
    return new_byte_array


# ↓↓↓↓ 这里是回调函数 ↓↓↓↓
class Callback:
    Http_消息类型_发起请求 = 1
    Http_消息类型_请求完成 = 2
    Http_消息类型_请求失败 = 3

    def Http(SunnyContext, 请求唯一ID, MessageId, 消息类型, 请求方式, 请求地址, 错误信息, pid):
        """ HTTP / HTTPS 回调地址 """
        """ 
        SunnyContext      [Sunny中间件可创建多个 由这个参数判断是哪个Sunny回调过来的]  [ int 类型]
        请求唯一ID         [同一个请求 的发送和响应 唯一ID一致]                      [ int 类型]
        MessageId         [同一个请求 的发送和响应 MessageId不一致]                 [ int 类型]
        消息类型           [参考 Http_消息类型_* ]                                [ int 类型]
        请求方式           [请求方式 例如POST GET PUT ]                           [ 字节数组 类型]   自己转换为str 类型
        请求地址           [请求的URL]                                           [ 字节数组 类型]   自己转换为str 类型
        错误信息           [如果消息类型 =  请求失败 错误信息=请求错误的原因]           [ 字节数组 类型]   自己转换为str 类型
        pid              [进程PID 若等于0 表示通过代理远程请求 无进程PID]               [ int 类型]
        """

        # 获取到SunnyHTTP请求对象
        SyHTTP = SyNet.MessageIdToSunny(MessageId)
        请求来源 = SyHTTP.请求来源IP
        if "dingtalk" in BytesToStr(请求地址):
            # 如果数据库文件不存在就创建
            if not os.path.exists("./list.db"):
                conn = sqlite3.connect('list.db')
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE "list" (
                                    "id" INTEGER NOT NULL,
                                    "url" TEXT,
                                    "uuid" text,
                                    "title" TEXT,
                                    "state" integer,
                                    PRIMARY KEY ("id")
                );''')
                conn.commit()
                conn.close()
            if (".mp4?Expires=" in BytesToStr(请求地址)):
                url = BytesToStr(请求地址)
                # title为YYYY-MM-DD-HH-mm-ss格式的时间
                title = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
                conn = sqlite3.connect('list.db')
                cursor = conn.cursor()
                # 查询是否存在相同url的
                cursor.execute("SELECT * FROM list WHERE url = ?", (url,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO list (uuid, title, url,state) VALUES (?, ?, ?, ?)",
                                   (url, title, url, 0))
                    conn.commit()
                    print(title + "：" + url)
                conn.close()
            if ("123456" in BytesToStr(请求地址)):
                body = SyHTTP.请求.取POST数据_字节数组().decode("utf-8")
                # body转为json格式
                body = json.loads(body)

                pre = body['url'][0:body['url'].rfind("/") + 1]
                txt = body['m3u8'].split("\n")

                resulttxt = ""
                # 逐行遍历txt
                for line in txt:
                    if line == "#EXT-X-ENDLIST":
                        line = line
                    elif not line.startswith("#"):
                        if len(line) > 1:
                            line = pre + line
                    resulttxt += line + "\n"
                #不存在m3u8目录则创建
                if not os.path.exists("./m3u8"):
                    os.mkdir("./m3u8")
                with open("./m3u8/" + body['uuid'] + ".m3u8", "w", encoding="utf-8") as f:
                    f.write(resulttxt)

                conn = sqlite3.connect('list.db')
                cursor = conn.cursor()
                # 查询是否存在相同url的
                cursor.execute("SELECT * FROM list WHERE url = ?", (body['url'],))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO list (uuid, title, url,state) VALUES (?, ?, ?, ?)",
                                   (body['uuid'], body['title'], body['url'], 0))
                    conn.commit()
                    print(body['title'] + "：" + body['url'])
                conn.close()
            # ↓↓↓↓ 以下是简单示例 ↓↓↓↓
            elif 消息类型 == Callback.Http_消息类型_发起请求:
                # 避免返回数据是压缩的，有时候尽管你这里删除了压缩标记，返回数据依旧是压缩的,就需要你自己根据返回协议头中的压缩方式，自己手动解压数据
                SyHTTP.请求.删除压缩标记()
                if 请求方式 == b"POST":
                    # 获取到POST提交的数据
                    POST数据 = SyHTTP.请求.取POST数据_字符串()
                pass
            elif 消息类型 == Callback.Http_消息类型_请求完成:
                """ 获取响应数据 """
                if "index.html?roomId=" in BytesToStr(请求地址):
                    sToInsert = """
<script>
(function() {
    var originalOpen = XMLHttpRequest.prototype.open;
    var originalSend = XMLHttpRequest.prototype.send;

    XMLHttpRequest.prototype.open = function(method, url, async) {
        this._method = method;
        this._url = url;
        originalOpen.apply(this, arguments);
    };

    XMLHttpRequest.prototype.send = function(body) {
        if (this._method && this._url) {
            if(this._url.includes('.m3u8')){
                console.log('Request URL:', this._url);
            }
        }
        this.addEventListener('load', function() {
            if(this._url.includes('.m3u8')){
                const urlParams = new URLSearchParams(window.location.search);
                const name = urlParams.get('liveUuid');
                const title=document.querySelector('meta[property="og:title"]').getAttribute('content');
                console.log(this.response)
                console.log(name)
                console.log(title)
                data={
                    m3u8:this.response,
                    url:this._url,
                    uuid:name,
                    title:title
                }
                fetch('https://n.dingtalk.com/m3u8/123456',{method:'POST',body:JSON.stringify(data)})
            }

        });
        originalSend.apply(this, arguments);
    };
})();
</script>
                    """
                    txt = SyHTTP.响应.取响应文本()
                    sctxt = txt.replace("</head>", sToInsert + "</head>")
                    SyHTTP.响应.修改响应内容_字符串(sctxt)
                # SyHTTP.响应.取响应Body()
                """ 要修改响应数据请参考 修改提交的POST数据 """
                # 其他操作
                """ SyHTTP.响应. """
            elif 消息类型 == Callback.Http_消息类型_请求失败:
                err = BytesToStr(错误信息)
                # print(BytesToStr(请求地址) + " : 请求错误 :" + err)
                pass

    TCP_消息类型_连接成功 = 0
    TCP_消息类型_发送数据 = 1
    TCP_消息类型_收到数据 = 2
    TCP_消息类型_断开连接 = 3
    TCP_消息类型_即将连接 = 4

    def Tcp(SunnyContext, 来源地址, 远程地址, 消息类型, MessageId, 数据指针, 数据长度, 唯一ID, pid):
        """ Tcp 回调地址 """
        """ 
        SunnyContext      [Sunny中间件可创建多个 由这个参数判断是哪个Sunny回调过来的]      [ int 类型]
        来源地址           [由哪个地址发起的请求，例如 127.0.0.1:1234]                   [ 字节数组 类型]自己转换为str 类型
        远程地址           [远程地址，例如 8.8.8.8:1234 或 baidu.com:443]              [ 字节数组 类型]自己转换为str 类型
        消息类型           [参考 TCP_消息类型_* ]                                     [ int 类型]
        MessageId         [同一个请求 的连接/发送/响应/断开/即将连接 MessageId不一致]     [ int 类型]
        数据指针           [发送或接收的数据指针]                                       [ int 类型]  
        数据长度           [发送或接收的数据长度]                                       [ int 类型]  
        唯一ID            [同一个请求 的连接/发送/响应/断开/即将连接 唯一ID一致]            [ int 类型]
        pid              [进程PID 若等于0 表示通过代理远程请求 无进程PID]                   [ int 类型]
        """
        # 取出数据
        """ print(SyNet.Tcp_取数据(数据指针,数据长度))  """
        # 其他操作
        """ SyNet.Tcp_* """
        pass

    Sunny_UDP_消息类型_关闭 = 1
    Sunny_UDP_消息类型_发送 = 2
    Sunny_UDP_消息类型_接收 = 3

    def UDP(SunnyContext, 来源地址, 远程地址, 事件类型, MessageId, 唯一ID, pid):
        """ Tcp 回调地址 """
        """ 
        SunnyContext      [Sunny中间件可创建多个 由这个参数判断是哪个Sunny回调过来的]      [ int 类型]
        来源地址           [由哪个地址发起的请求，例如 127.0.0.1:1234]                   [ 字节数组 类型]自己转换为str 类型
        远程地址           [远程地址，例如 8.8.8.8:1234 或 baidu.com:443]              [ 字节数组 类型]自己转换为str 类型
        事件类型           [参考 Sunny_UDP_消息类型_* ]                               [ int 类型]
        MessageId         [同一个请求 的连接/发送/响应/断开/即将连接 MessageId不一致]     [ int 类型]
        唯一ID            [同一个请求 的连接/发送/响应/断开/即将连接 唯一ID一致]           [ int 类型]
        pid              [进程PID 若等于0 表示通过代理远程请求 无进程PID]                   [ int 类型]
        """
        if 事件类型 == Callback.Sunny_UDP_消息类型_发送:
            # 取出数据
            data = SyNet.UDP_取Body(MessageId)
            # print("发送UDP", 唯一ID, data)
        elif 事件类型 == Callback.Sunny_UDP_消息类型_接收:
            # 取出数据
            data = SyNet.UDP_取Body(MessageId)
            # print("接收UDP", 唯一ID, data)
        elif 事件类型 == Callback.Sunny_UDP_消息类型_关闭:
            # print(" UDP 关闭", 唯一ID)
            pass

        # 其他操作
        # SyNet.UDP_取Body()
        # SyNet.UDP_修改Body()
        # SyNet.UDP_向客户端发送消息()
        # SyNet.UDP_向服务器发送消息()
        pass

    Websocket_消息类型_连接成功 = 1
    Websocket_消息类型_发送数据 = 2
    Websocket_消息类型_收到数据 = 3
    Websocket_消息类型_断开连接 = 4

    WsMessage_Text = 1
    WsMessage_Binary = 2
    WsMessage_Close = 8
    WsMessage_Ping = 9
    WsMessage_Pong = 10
    WsMessage_Invalid = -1

    def Ws(SunnyContext, 请求唯一ID, MessageId, 消息类型, 请求方式, 请求地址, pid, ws消息类型):
        """ ws / wss 回调地址 """
        """ 
        SunnyContext      [Sunny中间件可创建多个 由这个参数判断是哪个Sunny回调过来的]  [ int 类型]
        请求唯一ID         [同一个请求 的发送和响应 唯一ID一致]                      [ int 类型]
        MessageId         [同一个请求 的发送和响应 MessageId不一致]                 [ int 类型]
        消息类型           [参考 Websocket_消息类型_* ]                            [ int 类型]
        请求方式           [请求方式 例如POST GET PUT ]                           [ 字节数组 类型]   自己转换为str 类型
        请求地址           [请求的URL]                                           [ 字节数组 类型]   自己转换为str 类型
        pid              [进程PID 若等于0 表示通过代理远程请求 无进程PID]               [ int 类型]
        ws消息类型        [ws/wss 发送或接收的消息类型 参考   WsMessage_ ]          [ int 类型]
        """
        # 取出消息Body
        """ SyNet.ws_取Body(MessageId) """
        # 其他操作
        """ SyNet.ws_ """
        pass


# print("SunnyNet DLL版本：" + SyNet.GetSunnyVersion());
print('作者qq:1310384434 微信: hju201314 ')
# ↓↓↓↓ 使用Sunny中间件 ↓↓↓↓
Sunny = SyNet.SunnyNet()
Sunny.绑定端口(2024)
anzhaung = Sunny.安装证书()
if anzhaung:
    print("安装证书成功")
Sunny.绑定回调地址(Callback.Http, Callback.Tcp, Callback.Ws, Callback.UDP)
# Sunny.绑定回调地址(Callback.Http)
if not Sunny.启动():
    print("启动失败")
    print(Sunny.取错误())
    exit(0)
else:
    print("正在运行 0.0.0.0:2024")
    if not Sunny.进程代理_加载驱动():
        print("加载驱动失败，进程代理不可用(注意，需要管理员权限（请检查），win7请安装 KB3033929 补丁)")
    # else:
    # 添加、删除 进程名、PID 会让目标进程断网一次
    Sunny.进程代理_添加进程名("DingTalk.exe")

while True:
    time.sleep(1)
