import os
import json
import re

ROOT_DIR = "/Users/gaia/MEETS"
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

def organize_images():
    manifest = []
    
    # Get all subdirectories and sort them
    subdirs = [d for d in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, d)) and not d.startswith('.')]
    subdirs.sort()
    
    for folder_name in subdirs:
        folder_path = os.path.join(ROOT_DIR, folder_name)
        folder_files = []
        
        print(f"Processing folder: {folder_name}")
        
        files = os.listdir(folder_path)
        # Sort files to ensure deterministic order if needed, though we are just renaming existing ones
        files.sort()
        
        for filename in files:
            if filename.startswith('.'):
                continue
                
            name, ext = os.path.splitext(filename)
            if ext.lower() not in IMAGE_EXTENSIONS:
                continue
            
            # Check if already renamed
            # We assume "Folder Name " prefix. 
            # If the folder name is "My Folder", we look for "My Folder " at the start.
            prefix = f"{folder_name} "
            
            if filename.startswith(prefix):
                new_filename = filename
            else:
                new_filename = f"{folder_name} {filename}"
                old_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Rename
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"  Renamed: {filename} -> {new_filename}")
                except OSError as e:
                    print(f"  Error renaming {filename}: {e}")
                    continue
            
            folder_files.append(new_filename)
        
        # Add to manifest
        # Create a simple slug for ID
        slug = re.sub(r'[^a-z0-9]+', '-', folder_name.lower()).strip('-')
        
        manifest.append({
            "id": slug,
            "title": folder_name,
            "path": f"./{folder_name}",
            "files": sorted(folder_files)
        })

    # Write manifest.json
    manifest_path = os.path.join(ROOT_DIR, "manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Created {manifest_path}")

    # Write index.md
    index_path = os.path.join(ROOT_DIR, "index.md")
    with open(index_path, 'w') as f:
        f.write("# Image Index\n\n")
        f.write(f"Total Folders: {len(manifest)}\n\n")
        
        for item in manifest:
            f.write(f"## {item['title']}\n")
            f.write(f"**ID**: `{item['id']}`\n\n")
            f.write(f"**Path**: `{item['path']}`\n\n")
            f.write("**Files**:\n")
            for file in item['files']:
                # Link to the file relative to the index.md
                # URL encode the path parts just in case, but simple replacement for spaces usually works for local markdown preview
                # We'll keep it simple: path/filename
                rel_path = f"{item['path']}/{file}"
                f.write(f"- [{file}]({rel_path})\n")
            f.write("\n---\n\n")
    print(f"Created {index_path}")

if __name__ == "__main__":
    organize_images()
