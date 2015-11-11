'''
Used to download main images from html using wget.
'''
html_id_file_name = 'result.txt';
html_dir_list = []
with open(html_id_file_name) as f:
    html_dir_list = f.readlines()
for i in range(len(html_id_list)):
    html_dir_list[i] = html_id_list[i].replace("\n", "")+".html"



