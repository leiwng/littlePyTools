
import os, sys, datetime
from shutil import copyfile
from PIL import Image


if __name__ == '__main__':

  # Windows10 锁屏图片存储目录
  # src_dir = r'C:\Users\leiwn\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
  src_dir = r'C:\Users\Raymond.Wong\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

  # 目录下的文件名列表
  src_files = os.listdir(src_dir)

  # 图片转存目录
  # dest_dir = r'D:\OneDrive\图片\桌面背景'
  dest_dir = r'D:\oneDrive\bizOutlook\OneDrive\图片\桌面背景'

  # 打开记录已经转存文件的记录文件
  exist_file_list_file = open(os.path.join(dest_dir,'files_processed.txt'), 'r+')
  files_processed = exist_file_list_file.read().splitlines()
  files_processed = [x for x in files_processed if x != '']
  # print('files_processed: {}'.format(files_processed))

  file_copied_cnt = 0
  for src_file in src_files:
    src_file_fullpath = os.path.join(src_dir, src_file)
    file_size = os.path.getsize(src_file_fullpath)
    # 只处理大于400KB，和之前没有处理过的文件
    if (file_size > (1024 * 400)) and (src_file not in files_processed) :

      img = Image.open(src_file_fullpath)

      # 只处理分辨率中，宽超过或等于1920像素的图片
      if img.width >= 1920 :

        # used for file rename
        file_copied_cnt += 1
        # add newly processed file
        files_processed.append(src_file)

        # new filename
        new_filename = str(datetime.date.today())+'_'+ str(file_copied_cnt).zfill(4)+'.jpg'
        dest_file_fullpath = os.path.join(dest_dir, new_filename)

        try:
          copyfile(src_file_fullpath, dest_file_fullpath)
        except Exception as e:
          print('copy file error, src:{} ; dest:{}'.format(src_file_fullpath, dest_file_fullpath))
          print(e)

      img.close()

  if files_processed and file_copied_cnt > 0 :

    # 清空原文件处理记录文件
    exist_file_list_file.seek(0)
    exist_file_list_file.truncate()

    for item in files_processed:
      exist_file_list_file.write(item)
      exist_file_list_file.write(os.linesep)

  exist_file_list_file.close()
