import os
import shutil
from tqdm import tqdm

def move_files_in_chunks(source_dir, dest_dir, chunk_size=50):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get the list of files in the source directory
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Process files in chunks
    for i in range(0, len(files), chunk_size):
        chunk_files = files[i:i+chunk_size]
        for file in tqdm(chunk_files, desc="Moving files", unit="file"):
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
        print(f"Moved {len(chunk_files)} files.")

if __name__ == "__main__":
    SOURCE_DIR = "/Users/alex/PycharmProjects/scrapy-project-v1/downloads"
    DEST_DIR = "/Users/alex/Library/CloudStorage/Dropbox-Team/TeamSynergix/Datasets/Capture One/sd-mega-image-repo/Capture"
    move_files_in_chunks(SOURCE_DIR, DEST_DIR)
