import os
import shutil

current_directory = os.getcwd()
buffer = []
lines = []
read_line = 0


def create_file(path, file_name):
    with open(os.path.join(path, file_name), 'w') as file:
        file.write('')


def delete_file(path):
    os.remove(path)


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def copy_file(src_path, dest_path):
    shutil.copy2(src_path, dest_path)


def move_file(src_path, dest_path):
    shutil.move(src_path, dest_path)


def display_file_contents(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


def edit_file_contents(file_path):
    global buffer, read_line
    print(f'edit "{file_path}" start by {read_line}')
    buffer.clear()
    read_line += 1
    while True:
        line = lines[read_line]
        if line == 'saveFile':
            with open(file_path, 'w') as f:
                f.write('\n'.join(buffer))
            break
        else:
            buffer.append(line)
            read_line += 1
            print(f'added "{line}" to buffer')


def search_files(directory_path, extension):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))


def use_directory(directory_path):
    global current_directory
    current_directory = directory_path


def execute_command(command):
    global current_directory, buffer
    args = command.split()
    print(f'"execute -> "{command}')
    if args[0] == 'createFile':
        if len(args) == 3:
            create_file(os.path.join(current_directory, args[1]), args[2])
        else:
            create_file(os.path.join(current_directory, ''), args[1])
    elif args[0] == 'deleteFile':
        delete_file(os.path.join(current_directory, args[1]))
    elif args[0] == 'createDirectory':
        create_directory(os.path.join(current_directory, args[1]))
    elif args[0] == 'copyFile':
        if len(args) == 3:
            copy_file(os.path.join(current_directory, args[1]), os.path.join(current_directory, args[2]))
        else:
            copy_file(os.path.join(current_directory, ''), os.path.join(current_directory, args[1]))
    elif args[0] == 'moveFile':
        if len(args) == 3:
            move_file(os.path.join(current_directory, args[1]), os.path.join(current_directory, args[2]))
        else:
            move_file(os.path.join(current_directory, ''), os.path.join(current_directory, args[1]))
    elif args[0] == 'displayFile':
        display_file_contents(os.path.join(current_directory, args[1]))
    elif args[0] == 'editFile':
        edit_file_contents(os.path.join(current_directory, args[1]))
    elif args[0] == 'searchFiles':
        if len(args) == 3:
            search_files(os.path.join(current_directory, args[1]), args[2])
        else:
            search_files(os.path.join(current_directory, ''), args[1])
    elif args[0] == 'use':
        use_directory(args[1])


# 設定ファイルを読み込む
if __name__ == '__main__':
    with open('config.txt') as f:
        for line in f:
            lines.append(line.strip())

    # コマンドを実行する
    while read_line < len(lines):
        line = lines[read_line].strip()
        execute_command(line)
        read_line += 1
