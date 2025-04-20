import os
# 修改为镜像源
#os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'


from huggingface_hub import snapshot_download

snapshot_download(
  repo_id="LHRS/RS5M_512_2048",
  repo_type="model",
  local_dir="datasets",
  allow_patterns=["train_part_1.tar","train_part_2.tar","train_part_3.tar","train_part_4.tar","train_part_5.tar","train_part_6.tar","train_part_7.tar","train_part_8.tar","train_part_9.tar","train_part_10.tar","train_part_11.tar","train_part_12.tar","train_part_13.tar","train_part_14.tar","train_part_15.tar","train_part_16.tar","train_part_17.tar"],
  local_dir_use_symlinks=False,
  resume_download=False,
#   proxies={"https": "http://localhost:7890"}, # clash default port
  max_workers=8
)
