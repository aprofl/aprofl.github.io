import os
import filecmp
import shutil

def sync_directories(source_dir, target_dir, file_extension=".md"):
    copied_files = []
    deleted_files = []
    modified_files = []

    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Compare the two directories, ignoring . directories
    comparison = filecmp.dircmp(source_dir, target_dir, ignore=['.*'])

    # Update files that are new or have changed
    for file_name in comparison.left_only + comparison.diff_files:
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(target_dir, file_name)

        if os.path.isdir(source_file) and not os.path.basename(source_file).startswith('.'):
            if os.path.exists(target_file):
                shutil.rmtree(target_file)
            shutil.copytree(source_file, target_file, ignore=shutil.ignore_patterns('.*'))
            copied_files.append(target_file)
        elif source_file.endswith(file_extension):
            shutil.copy2(source_file, target_file)
            if file_name in comparison.diff_files:
                modified_files.append(target_file)
            else:
                copied_files.append(target_file)

    # Delete files that are no longer present in the source directory
    for file_name in comparison.right_only:
        target_file = os.path.join(target_dir, file_name)
        if os.path.isdir(target_file):
            shutil.rmtree(target_file)
            deleted_files.append(target_file)
        elif target_file.endswith(file_extension):
            os.remove(target_file)
            deleted_files.append(target_file)

    # Delete non .md files and . directories in the target directory
    for root, dirs, files in os.walk(target_dir):
        for dir_name in dirs:
            if dir_name.startswith('.'):
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                deleted_files.append(dir_path)
        dirs[:] = [d for d in dirs if not d.startswith('.')]  # Exclude . directories from further walk

        for file_name in files:
            if not file_name.endswith(file_extension):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                deleted_files.append(file_path)

    # Recursively sync subdirectories
    for subdir in comparison.common_dirs:
        if not subdir.startswith('.'):
            sub_copied, sub_deleted, sub_modified = sync_directories(
                os.path.join(source_dir, subdir),
                os.path.join(target_dir, subdir),
                file_extension
            )
            copied_files.extend(sub_copied)
            deleted_files.extend(sub_deleted)
            modified_files.extend(sub_modified)

    return copied_files, deleted_files, modified_files

def main():
    source_content_dir = r'D:\Obsidian\DocFlow'
    target_content_dir = r'D:\Obsidian\Aprofl_Hugo\content\docs'
    source_static_dir =r'D:\Obsidian\DocFlow\Resources'
    target_static_dir = r'D:\Obsidian\Aprofl_Hugo\static\Resources'

    copied, deleted, modified = sync_directories(source_content_dir, target_content_dir)

    # Print the results
    print("Copied Files:")
    print("\n".join(copied))
    print("\nDeleted Files:")
    print("\n".join(deleted))
    print("\nModified Files:")
    print("\n".join(modified))

    # Sync the static directory without file extension filter
    sync_directories(source_static_dir, target_static_dir, file_extension="")

if __name__ == "__main__":
    main()
