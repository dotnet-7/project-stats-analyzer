import os
from project_stats.file_utils import load_ignore_patterns, should_ignore
from project_stats.text_processor import count_characters_in_project
from project_stats.config import DEFAULT_IGNORE_FILE,DEFAULT_ANALYZE_DIR

def main():
    # 指定项目目录和忽略规则文件
    project_directory = DEFAULT_ANALYZE_DIR
    ignore_file = DEFAULT_IGNORE_FILE

    # 检查路径是否存在
    if not os.path.exists(project_directory):
        print(f"Project directory '{project_directory}' does not exist.")
        return

    # 调用统计函数
    char_counts = count_characters_in_project(project_directory, ignore_file)

    # 打印统计结果
    for char, count in sorted(char_counts.items()):
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
