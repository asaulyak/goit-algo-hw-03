import os
import shutil
import sys
from pathlib import Path

def copy_content(source: Path, destination: Path):
    try:
        contents = os.listdir(source)

        for item in contents:
            path = Path(item)
            current_path = source / path

            if os.path.isfile(current_path):
                suffix = path.suffix
                extension = suffix if suffix else '(no extension)'

                destination_folder_path = destination / Path(extension)
                destination_file_path = destination_folder_path / path

                destination_folder_path.mkdir(parents=True, exist_ok=True)
                shutil.copy(current_path, destination_file_path)
                print(f'Copied {current_path} to {destination_file_path}')
            else:
                copy_content(current_path, destination)

    except Exception as e:
        print(f'Failed to copy files from {source} to {destination}: {e}')

def main():
    args = sys.argv

    if len(args) < 2:
        print('Provide source')
    else:
        source = args[1]
        destination = args[2] if len(args) > 2 else 'dist'
        copy_content(Path(source), Path(destination))


if __name__ == "__main__":
    main()