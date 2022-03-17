import os
import gzip
import datetime
print("By CitingNutria")
# create a folder in user documents folder
def create_folder(folder_name):
    # get the user documents folder
    user_documents = os.path.expanduser('~') + '/Documents'
    # is not exist create the folder
    if not os.path.exists(user_documents + '/' + folder_name):
        os.makedirs(user_documents + '/' + folder_name)
    return user_documents + '/' + folder_name




cache_path = create_folder('Kedama Logs Reader')

if not os.path.exists(cache_path+ '\\logs.txt'):
    print('输入.minecraft目录下的logs文件夹路径，如：D:\Game\MultiMC\instances\\1.18.2_YASMP_v1.0.220308\.minecraft\logs\n只有第一次要输')
    logs_path = input('logs文件夹路径:')
    #create a file in the cache folder
    with open(cache_path+ '\\logs.txt', 'w') as f:
        f.write(logs_path)
else:
    with open(cache_path+ '\\logs.txt', 'r') as f:
        logs_path = f.read()


while True:
    # create a logs list
    logs_list = []
    gz_list = []
    # create a list of files with .gz in the logs folder
    for file in os.listdir(logs_path):
        if file.endswith(".gz"):
            try:
                with gzip.open(logs_path + "\\" + file, 'rt', encoding='utf-8') as f:
                    file_content = f.read()
                    for line in file_content.splitlines():
                        if '您收到了' in line:
                            info = file[0:-9] + ' ' + line[0:11] + line[39:]
                            logs_list.append(info)
            except:
                with gzip.open(logs_path + "\\" + file, 'rt', encoding='gbk') as f:
                    file_content = f.read()
                    for line in file_content.splitlines():
                        if '您收到了' in line:
                            info = file[0:-9] + ' ' + line[0:11] + line[39:]
                            logs_list.append(info)

    latest_log = logs_path + "\\latest.log"

    # get now date
    now = datetime.datetime.now()

    # read the latest log file
    with open(latest_log, 'r') as f:
        for line in f:
            if "您收到了" in line:
                logs_list.append(str(now)[0:10] + ' ' + line[0:11] + line[39:])

    # print the logs list line by line
    for line in logs_list:
        print(line)

    exit = input('按回车刷新')





