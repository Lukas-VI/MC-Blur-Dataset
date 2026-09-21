## MC-Blur: A Comprehensive Benchmark for Image Deblurring
## Kaihao, Zhang and Tao, Wang and Wenhan,Luo and Boheng, Chen and Wenqi, Ren and Stenger, Bjorn and Wei, Liu and Hongdong, Li and Ming-Hsuan, Yang
## https://arxiv.org/abs/2112.00234

## Download MC-Blur for image deblurring
## 说明：本脚本用于一键下载并解压 MC-Blur 数据集的各个子集。
## 它既不是训练脚本，也不是数据生成/处理工具，而是一个简单的“数据集下载与解压”工具。
## 核心流程：用 gdown 从 Google Drive 按文件 ID 下载 zip 压缩包 → 用 shutil 解压到 Datasets/ 目录 → 删除压缩包。

import os          # 标准库：提供与操作系统交互的功能，这里用来删除下载后的 zip 压缩包（os.remove）
import gdown       # 第三方库：可以从 Google Drive 直接通过文件 ID 下载文件（google-drive 下载器）
import shutil      # 标准库：高级文件操作，这里用 shutil.unpack_archive 解压 zip 压缩包

import argparse    # 标准库：用于解析命令行参数（让用户可以通过 --data 指定要下载哪些数据集）

parser = argparse.ArgumentParser()                    # 创建命令行参数解析器
parser.add_argument('--data', type=list,              # 定义名为 --data 的命令行参数
                    default=['RHM_250_Test', 'RHM_500_Test', 'RHM_1000_Test', 'RHM_250_500_1000_train_test',
                             'UHDM_train_test', 'LSD_train_test', 'RMBQ'])
                    # default 是默认值：如果运行脚本时不带 --data 参数，就默认下载上述全部 7 个子集。
                    # 注：type=list 在此处比较特殊。argparse 会用该类型（函数）转换输入值，
                    # 当用户传入像 "UHDM_train_test" 这样的字符串时，list() 会把它拆成单个字符组成的列表，
                    # 导致后续 if 判断无一匹配而上文默认值不受影响；因此这里给默认值生效其实是安全的，
                    # 但若用 --data 传参则可能达不到预期（理解存疑：官方写法本身的可达性）。
args = parser.parse_args()                            # 真正解析命令行参数，结果存到 args 对象；args.data 即要下载的数据集列表

### Google drive IDs for MC-Blur dataset
### 下面定义的是各个子集文件在 Google Drive 上的文件 ID（用于 gdown 按 ID 下载）

## For RHM dataset
RHM_250_Test = '1hoCFNeP1GOszaJfLABBw35hCQQKWPMhV'  ## https://drive.google.com/file/d/1hoCFNeP1GOszaJfLABBw35hCQQKWPMhV
# RHM 250fps 测试集对应的 Google Drive 文件 ID。
# RHM = Real high-fps based Motion-blurred subset（基于高帧率真实视频合成的运动模糊子集）

RHM_500_Test = '13payJmIY6mssFXMSuOwf1aosA3n6bXb6'  ## https://drive.google.com/file/d/13payJmIY6mssFXMSuOwf1aosA3n6bXb6
# RHM 500fps 测试集对应的 Google Drive 文件 ID

RHM_1000_Test = '1HJqV6Ogve-G6YGYJDH7MD5nKAQOTnVMG'  ## https://drive.google.com/file/d/1HJqV6Ogve-G6YGYJDH7MD5nKAQOTnVMG
# RHM 1000fps 测试集对应的 Google Drive 文件 ID

RHM_250_500_1000_train_test = '1V9Ac0Bw9wdoo50y8JM0F4VVh1jNGTP6m '  ## https://drive.google.com/file/d/1V9Ac0Bw9wdoo50y8JM0F4VVh1jNGTP6m
# RHM 250/500/1000fps 合并的训练+测试集文件 ID。
# 注意：该字符串末尾（引号闭合前）有一个多余空格，原始代码即如此，为保持行为不变故保留原样。
# 它会影响 gdown 匹配该 ID，可能导致下载失败，属官方脚本自带的潜在问题（理解存疑）。

## For UHDM

UHDM_train_test = '1qToTBej21VC7n49L_36FjmuQisjM3xPf'  ## https://drive.google.com/file/d/1qToTBej21VC7n49L_36FjmuQisjM3xPf
# UHDM = large-kernel UHD Motion-blurred subset（超高清、大卷积核运动模糊子集），这里为其训练+测试集 ID

## For LSD

LSD_train_test = '19C56VIxChcvcCylKpAlK1pqYo16c0D_k'  ## https://drive.google.com/file/d/19C56VIxChcvcCylKpAlK1pqYo16c0D_k
# LSD = large-scale heavy defocus blurred subset（大规模重度散焦模糊子集），这里为其训练+测试集 ID

## For RMBQ

RMBQ = '1ydAuaPy8uh_s3yk0G9raEYyC7z8BGvMl'  ## https://drive.google.com/file/d/1ydAuaPy8uh_s3yk0G9raEYyC7z8BGvMl
# RMBQ = Real Mixed Blurry Qualitative subset（真实混合模糊的定性评估子集）的文件 ID

for data in args.data:                    # 遍历命令行指定的每个子集名称（默认是上方那 7 个）
    if data == 'RHM_250_Test':
        print('RHM 250 fps Testing Data!')
        gdown.download(id=RHM_250_Test, output='Datasets/', quiet=False)
        # 用 gdown 按文件 ID 下载，保存到 Datasets/ 目录下；quiet=False 表示打印下载进度
        print('Extracting RHM 250 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_250fps.zip', 'Datasets')
        # 把下载的 zip 解压到 Datasets/ 目录（第二个参数是解压目标目录）
        os.remove('Datasets/motion_avg_250fps.zip')
        # 解压完成后删除 zip 压缩包，节省磁盘空间

    if data == 'RHM_500_Test':
        print('RHM 500 fps Testing Data!')
        gdown.download(id=RHM_500_Test, output='Datasets/', quiet=False)
        print('Extracting RHM 500 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_500fps.zip', 'Datasets')
        os.remove('Datasets/motion_avg_500fps.zip')
        # 与上面类似：RHM 500fps 测试集的下载→解压→删除压缩包

    if data == 'RHM_1000_Test':
        print('RHM 1000 fps Testing Data!')
        gdown.download(id=RHM_1000_Test, output='Datasets/', quiet=False)
        print('Extracting RHM 1000 fps Testing data...')
        shutil.unpack_archive('Datasets/motion_avg_1000fps.zip', 'Datasets')
        os.remove('Datasets/motion_avg_1000fps.zip')
        # RHM 1000fps 测试集的下载→解压→删除压缩包

    if data == 'RHM_250_500_1000_train_test':
        print('RHM_250_500_1000 training and Testing Data!')
        gdown.download(id=RHM_250_500_1000_train_test, output='Datasets/', quiet=False)
        print('Extracting RHM training and Testing data...')
        shutil.unpack_archive('Datasets/motion_avg.zip', 'Datasets')
        os.remove('Datasets/motion_avg.zip')
        # 三个帧率合并的训练+测试集，压缩包名为 motion_avg.zip

    if data == 'UHDM_train_test':
        print('UHDM training and Testing Data!')
        gdown.download(id=UHDM_train_test, output='Datasets/', quiet=False)
        print('Extracting UHDM training and Testing data...')
        shutil.unpack_archive('Datasets/Conv.zip', 'Datasets')
        os.remove('Datasets/Conv.zip')
        # UHDM 子集，压缩包名为 Conv.zip

    if data == 'LSD_train_test':
        print('LSD training and Testing Data!')
        gdown.download(id=LSD_train_test, output='Datasets/', quiet=False)
        print('Extracting LSD training and Testing data...')
        shutil.unpack_archive('Datasets/defocus_crop.zip', 'Datasets')
        os.remove('Datasets/defocus_crop.zip')
        # LSD 子集，压缩包名为 defocus_crop.zip（聚焦 defocus 散焦模糊）

    if data == 'RMBQ':
        print('RMBQ Data!')
        gdown.download(id=LSD_train_test, output='Datasets/', quiet=False)
        print('Extracting RMBQ data...')
        shutil.unpack_archive('Datasets/real.zip', 'Datasets')
        os.remove('Datasets/real.zip')
        # RMBQ 子集，压缩包名为 real.zip。
        # 注意：此处 gdown 传的是 id=LSD_train_test（LSD 的 ID）而非 RMBQ 的 ID，
        # 与 'RMBQ Data!' 的意图不符，疑似官方脚本笔误（理解存疑：大概率是 bug，但按规范不改动逻辑）。

print('Download completed successfully!')
# 全部选中的子集下载并解压完成后，打印完成提示。