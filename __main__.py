# -*- coding: utf-8 -*-
# @File : md2zhihu.py
import re


def replace (file_name, output_file_name):
    #注意md文本中不含其它$，例如代码段出现$会有问题！
    pattern1 = r"\$\$\n*((.|\n)*?)\n*\$\$"
    # 上句代码优于注释句
    # pattern1 = r"\$\$\n*([\s\S]*?)\n*\$\$"
    # 知乎中，公式末尾插入\\可以实现公式居中
    new_pattern1 = r'\n<img src="https://www.zhihu.com/equation?tex=\1\\\\" alt="\1\\\\" class="ee_img tr_noresize" eeimg="1">\n'
    pattern2 = r"\$\n*((.|\n)*?)\n*\$"
    #上句代码优于注释句
    #pattern2 = r"\$\n*(.*?)\n*\$"
    new_pattern2 = r'\n<img src="https://www.zhihu.com/equation?tex=\1" alt="\1" class="ee_img tr_noresize" eeimg="1">\n'

    with open(file_name, 'r', encoding='utf-8') as f:
        all_lines = f.read()
    f.close()

    new_lines1 = re.sub(pattern1, new_pattern1, all_lines)
    new_lines2 = re.sub(pattern2, new_pattern2, new_lines1)

    with open(output_file_name, 'w', encoding='utf-8') as f_output:
        # for line in all_lines:
        #     new_line1 = re.sub(pattern1, new_pattern1, line)
        #     new_line2 = re.sub(pattern2, new_pattern2, new_line1)
        #     f_output.write(new_line2)
        f_output.write(new_lines2)
    f_output.close()


if __name__ == '__main__':
    file_name = 'my_blog.md'
    file_name_pre = file_name.split(".")[0]
    output_file_name = file_name_pre + "_zhihu.md"
    replace(file_name, output_file_name)
