import os
import time
import shutil
def get_subfolders(folder_path):
    """
    获取指定文件夹下的所有子文件夹路径。

    :param folder_path: 要获取子文件夹的文件夹路径
    :return: 包含子文件夹路径的列表
    """
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    return [os.path.join(folder_path, subfolder) for subfolder in subfolders]


HOMEWORK_PATH = "D:\\Document\\Study\\研二上_电路助教\\buaa_spoc_automation\\data\\第一次作业"
serial = "1"

subfolders = get_subfolders(os.path.join(HOMEWORK_PATH,'学生作业附件'))
for subfolder in subfolders:
    ID_str = subfolder.split("\\")[-1].split('-')[0]
    name = subfolder.split("\\")[-1].split('-')[1]
    
    source_file = os.listdir(subfolder)[0]
    source_file = os.path.join(subfolder,source_file)

    file_type = source_file.split('\\')[-1].split('.')[-1]
    

    new_file_name = serial+'-'+ID_str + '-' + name  + '.' + file_type

    destination_file = os.path.join(HOMEWORK_PATH,'批改前',new_file_name)
    shutil.copy2(source_file,destination_file)

    destination_file = os.path.join(HOMEWORK_PATH,'批改后',new_file_name)
    shutil.copy2(source_file,destination_file)
    # shutil.move(source_file,destination_file)


print(subfolders)

