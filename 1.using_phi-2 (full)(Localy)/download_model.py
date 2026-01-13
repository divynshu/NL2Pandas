from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="microsoft/phi-2",
    local_dir="phi-2",
    local_dir_use_symlinks=False
)

print("Phi-2 downloaded to ./phi-2")
