accelerate launch  train_pasd.py \
 	--pretrained_model_name_or_path="checkpoints/stable-diffusion-v1-5" \
	--output_dir="runs/pasd" \
	--resolution=512 \
	--learning_rate=5e-5 \
	--gradient_accumulation_steps=2 \
	--train_batch_size=4 \
	--num_train_epochs=5 \
    --max_train_samples=1005535 \
	--tracker_project_name="pasd" \
	--enable_xformers_memory_efficient_attention \
	--checkpointing_steps=10000 \
	--control_type="realisr" \
	--mixed_precision="fp16" \
	--dataloader_num_workers=8 \
    --train_shards_path_or_url="datasets/train_part_{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}.tar" 
    --logging_dir="log"
# --max_train_samples=10000000 \
#    --multi_gpu --num_processes=8 --gpu_ids '0,1,2,3,4,5,6,7' \

# accelerate launch --multi_gpu --num_processes=2 --gpu_ids '0,1'  train_pasd.py \
#  	--pretrained_model_name_or_path="checkpoints/stable-diffusion-v1-5" \
# 	--output_dir="runs/pasd" \
# 	--resolution=512 \
# 	--learning_rate=5e-5 \
# 	--gradient_accumulation_steps=2 \
# 	--train_batch_size=4 \
# 	--max_train_steps=100000 \
# 	--max_train_samples=32463 \
# 	--tracker_project_name="pasd_rs" \
# 	--enable_xformers_memory_efficient_attention \
# 	--checkpointing_steps=20000 \
# 	--control_type="realisr" \
# 	--mixed_precision="fp16" \
# 	--dataloader_num_workers=8 \
# 	--train_shards_path_or_url="{datasets/AID,datasets/DIOR}.tar" 
#     --output_dir="runs/pasd_rs"
#   # --multi_gpu --num_processes=8 --gpu_ids '0,1,2,3,4,5,6,7' \

