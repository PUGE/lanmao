# -*- coding: utf-8 -*-
import os
import sqlite3
import subprocess
import requests
conn = sqlite3.connect('list.db')
cursor = conn.cursor()
fileInd = 0
def downMp4(url,title):
    global fileInd
    try:
        #url编码，防止url中存在特殊字

        #请求url
        res=requests.get(url, stream=True)
        #如果不存在mp4目录，则创建
        if not os.path.exists("./mp4"):
            os.mkdir("./mp4")
        fileInd += 1
        with open("./mp4/" + str(fileInd) + '-' +str(title)+".mp4", "wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        print(e)
        return False
    return True
def down():
    #查询list表中state为0的数据
    cursor.execute("select * from list where state=0")
    result = cursor.fetchall()
    size=len(result)
    index=1
    for row in result:
        retry_count= 0
        while True:
            retry_count+=1

            if retry_count>3:
                index+=1
                break
            id = row[0]
            url = row[1]
            uuid = row[2]
            name = row[3]
            #将Windows中不支持的文件符号过滤掉
            name=name.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
            if ".mp4" in url:
                print("正在下载" + str(index) + "/" + str(size) + "：" + name + "," + url)
                if downMp4(url,name):
                    print("下载成功")
                    index += 1
                    cursor.execute("delete from list where id=" + str(id))
                    conn.commit()
                    break
                else:
                    print("下载失败")
            else:
                command = [
                    ".\\N_m3u8DL-CLI_v3.0.2.exe",
                    "./m3u8/" + uuid + ".m3u8",
                    "--enableDelAfterDone",
                    "--saveName",
                    name,
                ]
                if retry_count>1:
                    print("重试下载"+str(index)+"/"+str(size)+"："+name+","+uuid)
                else:
                    # 使用 subprocess 运行命令
                    print("正在下载" + str(index) + "/" + str(size)+"："+name+","+uuid)
                process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
                # 获取输出内容
                out=process.stdout.decode("gbk")
                if "任务结束" in out:
                    print("下载成功")
                    index += 1
                    cursor.execute("delete from list where id="+str(id))
                    conn.commit()
                    break
                else:
                    print("下载失败")
    #查询list表中state为0的数据
    print("########################################################################")
    cursor.execute("select * from list where state=0")
    result = cursor.fetchall()
    size=len(result)
    for row in result:
        id = row[0]
        uuid = row[2]
        name = row[3]
        print(name+","+uuid)
    print("以上视频未下载，共"+str(size)+"个")
    print("1.下载")
    print("2.跳过")
    while True:
        choice = input("请输入你的选择：")
        if choice == "1":
            down()
        elif choice == "2":
            for row in result:
                id = row[0]
                cursor.execute("update list set state=2 where id=" + str(id))
                conn.commit()
            conn.close()
            break
        else:
            print("无效的选择，请重新输入。")
down()
#downMp4("https://cdn-sh-trans.dingtalk.com/playVideo/iAEIAqRmaWxlA6h5dW5kaXNrMATOIWbUOgXNEscGzgABEqQHzmaBaT0IzQKI/0/iAEIAqRmaWxlA6h5dW5kaXNrMATOIWbUOgXNEscGzgABEqQHzmaBaT0IzQKI.mp4?Expires=1721595506&OSSAccessKeyId=LTAIjmWpzHta71rc&Signature=ULOBe5l%2FpdFhRVAFts9Ja1m3kQE%3D&auth_key=1721595506-31f3469583c04d0ebb6bc5af158b9c9c-0-79026e92d0569dfc2fe4e32ed1d26860",123)
