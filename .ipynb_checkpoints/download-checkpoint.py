import os
# 修改为镜像源
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'


from huggingface_hub import snapshot_download

snapshot_download(
  repo_id="stable-diffusion-v1-5/stable-diffusion-v1-5",
  repo_type="model",
  local_dir="checkpoints/stable-diffusion-v1-5",
  allow_patterns=["model_index.json",
                    "v1-5-pruned.ckpt",
                    "feature_extractor/preprocessor_config.json",
                    "safety_checker/config.json",
                    "scheduler/scheduler_config.json",
                    "text_encoder/config.json",
                    "text_encoder/model.fp16.safetensors",
                    'text_encoder/model.safetensors',
                    'tokenizer/merges.txt',
                    'tokenizer/special_tokens_map.json',
                    'tokenizer/tokenizer_config.json',
                    'tokenizer/vocab.json',
                    'unet/config.json',
                    'unet/diffusion_pytorch_model.bin',
                    'vae/config.json',
                    'vae/diffusion_pytorch_model.bin',],
  local_dir_use_symlinks=False,
  resume_download=False,
#   proxies={"https": "http://localhost:7890"}, # clash default port
  max_workers=8
)
