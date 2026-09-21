> 以下「中文导读」为学习用补充说明，由学习者撰写，置于原文之前；下方原有内容一字未改。

# 📘 中文导读 · MC-Blur 数据集工具

## 一句话定位
MC-Blur 是一个**大规模的「多成因图像去模糊（image deblurring）」基准数据集**；本仓库只是一个**数据下载/处理工具**：
用 `gdown` 从 Google Drive 按文件 ID 拉取 MC-Blur 各子集的 zip，再解压到本地，帮你快速拿到完整数据。

## 核心逻辑 / 怎么用
它不是训练脚本，也不生成数据。核心流程（见 `download_data.py` 注释）：
> gdown 按文件 ID 从 Google Drive 下载 zip → `shutil.unpack_archive` 解压到 `Datasets/` → `os.remove` 删除压缩包。

下载全部子集（默认）：
```bash
python download_data.py
```
只下载某一子集（`--data` 传子集名，如 README 示例）：
```bash
python download_data.py --data "UHDM_train_test"
```
可选的子集名在 `download_data.py` 中定义：`RHM_250_Test`、`RHM_500_Test`、`RHM_1000_Test`、`RHM_250_500_1000_train_test`、`UHDM_train_test`、`LSD_train_test`、`RMBQ`。
依赖：`python -m pip install gdown`；需要能访问 Google Drive（国内可能需代理）。

## 目录结构导读
- `download_data.py` —— 唯一的脚本：按 `args.data` 逐个下载→解压→删除 zip，末尾打印完成提示。
- `README.md` —— 数据集全貌：四种模糊（均匀模糊、连续帧平均运动模糊、重度散焦、真实世界模糊）；四类子集 RHM / UHDM / LSD / RMBQ；百度网盘直链与密码；以及各子集上的基准方法 PSNR/SSIM 对比表。
- `core_step_instruction/` —— 数据集人工合成步骤的说明（README）。
- `instruction/` —— 每个子集的视觉示例（README）。
- `examples/`、`imgs/` —— 示例图与示意图。

## 学习建议 / 易踩坑（依据注释与断点，如实记录）
- **`--data` 的 `type=list` 是个陷阱（代码注释已标注“理解存疑”）**：argparse 会用 `list()` 把传入字符串拆成字符列表，导致后续 `if data == ...` 无一匹配，可能下载落空；用默认全量下载最稳，逐个下载请手动核对子集名拼写。
- **`RHM_250_500_1000_train_test` 的文件 ID 末尾多了一个空格**（原始代码如此，为保持行为不变保留原样），可能影响 gdown 对该 ID 的匹配/下载。
- **`RMBQ` 分支疑似官方笔误**：它打印 “RMBQ Data!” 但下载用的是 `LSD_train_test` 的 ID（代码注释标注“大概率是 bug，但按规范不改动逻辑”）。如需 RMBQ 请注意甄别。
- 数据量很大（单个子集几 GB 到数百 GB），注意磁盘空间；百度网盘是替代通道。

# MC-Blur: A Comprehensive Benchmark for Image Deblurring


![](imgs/data1.png)

## Our propsoed MC-Blur Benchmark


We construct a large-scale multi-cause (MC-Blur) dataset for image deblurring.  It consists of four blur types: uniform blurs, motion blurs by averaging continuous frames, heavy defocus blurs, and real-world blurs. We collect these images from more than 1000 diverse scenes such as buildings, city scenes, vehicles, natural landscapes, people, animals, and sculptures. MC-Blur Benchmark consits of four different subsets, i.e., Real high-fps based Motion-blurred subset (RHM), large-kernel UHD Motion-blurred subset (UHDM),  large-scale heavy defocus blurred subset (LSD), and Real Mixed Blurry Qualitative subset (RMBQ).


## Downloads

The images of the dataset can be downloaded from the links below. 

<!-- - ### Google Drive
<!-- - [RHM-250](https://drive.google.com/file/d/1hoCFNeP1GOszaJfLABBw35hCQQKWPMhV/view?usp=sharing) (6.2G for test)  -->
<!-- - [RHM-500](https://drive.google.com/file/d/13payJmIY6mssFXMSuOwf1aosA3n6bXb6/view?usp=sharing)  (7.1G for test)  -->
<!-- - [RHM-1000](https://drive.google.com/file/d/1HJqV6Ogve-G6YGYJDH7MD5nKAQOTnVMG/view?usp=sharing)  (9.3G for test)  -->
<!-- - [RHM-250-500-1000](https://drive.google.com/file/d/1V9Ac0Bw9wdoo50y8JM0F4VVh1jNGTP6m/view?usp=sharing) (117G total data) 
- [UHDM](https://drive.google.com/file/d/1qToTBej21VC7n49L_36FjmuQisjM3xPf/view?usp=sharing) (278G total data) 
- [LSD](https://drive.google.com/file/d/19C56VIxChcvcCylKpAlK1pqYo16c0D_k/view?usp=sharing) (34G total data)
- [RMBQ](https://drive.google.com/file/d/1ydAuaPy8uh_s3yk0G9raEYyC7z8BGvMl/view?usp=sharing) (110G total data)-->

### Baidu Cloud [(How to unzip?)](https://askubuntu.com/questions/31298/how-to-extract-and-join-files-xxx-zip-xxx-z01-and-xxx-z02)
- [RHM-250-500-1000](https://pan.baidu.com/s/18iwSYoERjPSLARlhxpbVzg) (117G total data) (password:ohzp)
- [UHDM](https://pan.baidu.com/s/1pG9kAo4v9n5LTMvmLpjZZg) (278G total data) (password:p78n)
- [LSD](https://pan.baidu.com/s/10-kLWGKJZQ5TQH5vUMcsyA) (34G total data) (password:sbtu) (Different from the TCSVT paper, the training set actually has 4,500 sharp–blurry pairs, the test set has 1,100 pairs, and the minimum resolution is 1,800 × 1,200. Please use this as the correct information)
- [RMBQ](https://pan.baidu.com/s/1_0drJkbIJ6X_GBseybHpeA) (110G total data) (password:nwq8)
### Download MC-Blur benchmark from the script, run

```
python download_data.py
```
**Note:** The above script will download all subsets of the MC-Blur. You can use "--data" to select. 
For example:
```
python download_data.py --data "UHDM_train_test"
```
## Some visual examples of MC-Blur Dataset

[Visual examples](instruction/README.md) for each subset of our MC-Blur Dataset.

## Some code steps in synthesizing dataset

See detail in [README](core_step_instruction/README.md).

## Benchmarking Study

## Methods

|Date|Publication|Title|Abbreviation|Code|Platform|
|---|---|---|---|---|---|
|2017|CVPR|Deep multi-scale convolutional neural network for dynamic scene deblurring [paper](http://zpascal.net/cvpr2017/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.pdf)|DeepDeblur|[Code](https://github.com/SeungjunNah/DeepDeblur_release)|Pytorch|
|2018|CVPR|Deblurgan: Blind motion deblurring using conditional adversarial networks [paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Kupyn_DeblurGAN_Blind_Motion_CVPR_2018_paper.html)|DeblurGAN|[Code](https://github.com/KupynOrest/DeblurGAN)|Pytorch|
|2018|CVPR|Scale-recurrent network for deep image deblurring [paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Tao_Scale-Recurrent_Network_for_CVPR_2018_paper.html)|SRN|[Code](https://github.com/jiangsutx/SRN-Deblur)|Tensorflow|
|2019|ICCV|DeblurGAN-v2: Deblurring (Orders-of-Magnitude) Faster and Better [paper](https://arxiv.org/abs/1908.03826)|DeblurGAN-v2|[Code](https://github.com/TAMU-VITA/DeblurGANv2)|Pytorch|
|2019|CVPR| Deep Stacked Hierarchical Multi-Patch Network for Image Deblurring [paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Zhang_Deep_Stacked_Hierarchical_Multi-Patch_Network_for_Image_Deblurring_CVPR_2019_paper.html)|DMPHN|[Code](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|Pytorch|
|2020|CVPR| Deblurring by Realistic Blurring [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Zhang_Deblurring_by_Realistic_Blurring_CVPR_2020_paper.pdf)|DBGAN|[Code](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|Pytorch|
|2021|CVPR|Multi-Stage Progressive Image Restoration [paper](https://arxiv.org/pdf/2102.02808.pdf)|MPRNet| [Code](https://github.com/swz30/MPRNet)|Pytorch|
|2022|CVPR|Restormer: Efficient Transformer for High-Resolution Image Restoration [paper](https://arxiv.org/pdf/2111.09881.pdf?ref=https://githubhelp.com)|Restormer| [Code](https://github.com/swz30/Restormer)|Pytorch|
|2021|ICCV|Rethinking Coarse-To-Fine Approach in Single Image Deblurring [paper](https://openaccess.thecvf.com/content/ICCV2021/html/Cho_Rethinking_Coarse-To-Fine_Approach_in_Single_Image_Deblurring_ICCV_2021_paper.html)|MIMO-UNet| [Code](https://github.com/chosj95/mimo-unet)|Pytorch|


## Metrics

|Abbreviation|Full-/Non-Reference|Platform|Code|
|---|---|---|---|
|PSNR (Peak Signal-to-Noise Ratio)|Full-Reference| | |
|SSIM (Structural Similarity Index Measurement)|Full-Reference|MATLAB|[Code](http://www.cns.nyu.edu/~lcv/ssim/ssim_index.m) |
|NIQE (Naturalness Image Quality Evaluator)|Non-Reference|MATLAB|[Code](https://github.com/utlive/niqe)|
|SSEQ (No-reference Image Quality Assessment Based on Spatial and Spectral Entropies)|Non-Reference|MATLAB|[Code](https://github.com/OaDsis/No-Reference-IQA)|


### Results for 250-fps images from RHM Set 

|Method|PSNR|SSIM|Parameter|
|-|-|-|-|
|[DeepDeblur](https://github.com/SeungjunNah/DeepDeblur_release)|30.38|0.8766|11.72 M|
|[DeblurGAN](https://github.com/KupynOrest/DeblurGAN)|24.89|0.6364|6.07 M|
|[SRN](https://github.com/jiangsutx/SRN-Deblur)|30.57|0.8799|6.88 M|
|[DeblurGAN-v2](https://github.com/TAMU-VITA/DeblurGANv2)|26.99|0.8061|7.84 M|
|[DMPHN](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|30.42|0.8768|21.69 M|
|[DBGAN](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|27.89|0.8191|11.59 M|
|[MPRNet](https://github.com/swz30/MPRNet)|31.52|0.9239|20.13 M|
|[Restormer](https://github.com/swz30/Restormer)|30.41|0.9106|26.10 M|
|[MIMO-UNet](https://github.com/chosj95/mimo-unet)|32.02|0.9285|6.81 M|

### Results for 500-fps images from RHM Set 

|Method|PSNR|SSIM|Parameter|
|-|-|-|-|
|[DeepDeblur](https://github.com/SeungjunNah/DeepDeblur_release)|31.08|0.8974|11.72 M|
|[DeblurGAN](https://github.com/KupynOrest/DeblurGAN)|24.66|0.6748|6.07 M|
|[SRN](https://github.com/jiangsutx/SRN-Deblur)|31.54|0.9051|6.88 MB|
|[DeblurGAN-v2](https://github.com/TAMU-VITA/DeblurGANv2)|27.67|0.8320|7.84 M|
|[DMPHN](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|31.43|0.9018|21.69 M|
|[DBGAN](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|28.36|0.8388|11.59 M|
|[MPRNet](https://github.com/swz30/MPRNet)|32.08|0.9300|20.13 M|
|[Restormer](https://github.com/swz30/Restormer)|30.98|0.9160|26.10 M|
|[MIMO-UNet](https://github.com/chosj95/mimo-unet)|32.89|0.9398|6.81 M|

### Results for 1000-fps images from RHM Set

|Method|PSNR|SSIM|Parameter|
|-|-|-|-|
|[DeepDeblur](https://github.com/SeungjunNah/DeepDeblur_release)|32.41|0.8966|11.72 M|
|[DeblurGAN](https://github.com/KupynOrest/DeblurGAN)|25.20|0.6535|6.07 M|
|[SRN](https://github.com/jiangsutx/SRN-Deblur)|32.69|0.0.9016|6.88 M|
|[DeblurGAN-v2](https://github.com/TAMU-VITA/DeblurGANv2)|29.81|0.8461|7.84 M|
|[DMPHN](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|32.41|0.9096|21.69 M|
|[DBGAN](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|29.66|0.8318|11.59 M|
|[MPRNet](https://github.com/swz30/MPRNet)|33.36|0.9332|20.13 M|
|[Restormer](https://github.com/swz30/Restormer)|32.77|0.9264|26.10 M|
|[MIMO-UNet](https://github.com/chosj95/mimo-unet)|33.75|0.9360|6.81 M|


### Results on UHDM Set

|Method|PSNR|SSIM|Parameter|
|-|-|-|-|
|[DeepDeblur](https://github.com/SeungjunNah/DeepDeblur_release)|22.23|0.6322|11.72 M|
|[DeblurGAN](https://github.com/KupynOrest/DeblurGAN)|20.39|0.5568|6.07 M|
|[SRN](https://github.com/jiangsutx/SRN-Deblur)|22.28|0.6346|6.88 M|
|[DeblurGAN-v2](https://github.com/TAMU-VITA/DeblurGANv2)|21.03|0.5839|7.84 M|
|[DMPHN](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|22.20|0.6378|21.69 M|
|[DBGAN](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|21.52|0.6025|11.59 M|
|[MPRNet](https://github.com/swz30/MPRNet)|23.70|0.7472|20.13 M|
|[Restormer](https://github.com/swz30/Restormer)|22.39|0.7356|26.10 M|
|[MIMO-UNet](https://github.com/chosj95/mimo-unet)|22.97|0.7317|6.81 M|

### Results on LSD Set

|Method|PSNR|SSIM|Parameter|
|-|-|-|-|
|[DeepDeblur](https://github.com/SeungjunNah/DeepDeblur_release)|20.73|0.7218|11.72 M|
|[DeblurGAN](https://github.com/KupynOrest/DeblurGAN)|20.04|0.6335|6.07 M|
|[SRN](https://github.com/jiangsutx/SRN-Deblur)|21.66|0.7664|6.88 M|
|[DeblurGAN-v2](https://github.com/TAMU-VITA/DeblurGANv2)|21.13|0.6964|7.84 M|
|[DMPHN](https://github.com/HongguangZhang/DMPHN-cvpr19-master)|21.23|0.7519|21.69 M|
|[DBGAN](https://github.com/HDCVLab/Deblurring-by-Realistic-Blurring)|21.56|0.7536|11.59 M|
|[MPRNet](https://github.com/swz30/MPRNet)|21.32|0.7897|20.13 M|
|[Restormer](https://github.com/swz30/Restormer)|22.35|0.8072|26.10 M|
|[MIMO-UNet](https://github.com/chosj95/mimo-unet)|22.56|0.7985|6.81 M|




## Citation
If you think this work is useful for your research, please cite the following paper.

```
@inproceedings{zhang2023benchmarking,
  title={MC-Blur: A Comprehensive Benchmark for Image Deblurring},
  author={Zhang, Kaihao and Wang, Tao and Luo, Wenhan and Chen, Boheng and Ren, Wenqi and Stenger, Bjorn and Liu, Wei and Li, Hongdong and Yang Ming-Hsuan},
  booktitle={IEEE Transactions on Circuits and Systems for Video Technology},
  year={2023}
}
```

### License

The MC-Blur dataset is released under [CC BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/) license.




