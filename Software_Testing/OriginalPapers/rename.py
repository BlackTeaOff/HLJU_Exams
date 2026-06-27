import os
import re

def batch_rename():
    # 获取当前脚本所在的文件夹路径
    directory = os.path.dirname(os.path.abspath(__file__))
    
    prefix = "夸克扫描王_元份_"
    total_files = 56
    
    # 匹配模式：前缀 + 数字 + 可选的后缀名（如 .pdf、.jpg 等）
    pattern = re.compile(rf"^{prefix}(\d+)(\..*)?$")
    
    # 找出所有匹配的文件
    matched_files = []
    for f in os.listdir(directory):
        match = pattern.match(f)
        if match:
            num = int(match.group(1))
            ext = match.group(2) if match.group(2) else ""
            matched_files.append((f, num, ext))
            
    if not matched_files:
        print("未在当前目录下找到符合命名规则的文件，请确认脚本是否放对了文件夹。")
        return

    print(f"共找到 {len(matched_files)} 个符合条件的文件。开始重命名...")
    
    # 第一步：重命名为临时文件名，防止发生同名覆盖冲突
    temp_files = []
    for f, num, ext in matched_files:
        new_num = total_files - num + 1
        temp_name = f"temp_rename_{new_num:03d}{ext}"
        
        old_path = os.path.join(directory, f)
        temp_path = os.path.join(directory, temp_name)
        
        os.rename(old_path, temp_path)
        temp_files.append((temp_path, new_num, ext))
        
    # 第二步：将临时文件名重命名为最终的目标名字
    for temp_path, new_num, ext in temp_files:
        final_name = f"{prefix}{new_num:03d}{ext}"
        final_path = os.path.join(directory, final_name)
        os.rename(temp_path, final_path)
        
    print("重命名完成！文件序号已成功倒过来。")

if __name__ == "__main__":
    batch_rename()