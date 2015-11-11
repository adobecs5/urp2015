'''
Used to download main images from html using wget.
'''
from bs4 import BeautifulSoup
import subprocess

def execute(line):
    p = subprocess.Popen(line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    status = p.wait()
    return err

html_id_file_name = 'result.txt'
html_dir_list = []
with open(html_id_file_name) as f:
    html_dir_list = f.readlines()

url = 'http://www.amazon.com/dp/'
count = 0
count_limit = 1
for a_HTML in html_dir_list:
    a_HTML = a_HTML.strip()
    with open("html/"+a_HTML+".html") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        main_image_tag = soup.find(id = "imgTagWrapperId")
        img_url = main_image_tag.contents[1].attrs["src"]
        img_extension = img_url.split(".")[-1]
        for i in range(10):
            err = execute("wget %s -O html/images/%s.%s" % (img_url, a_HTML, img_extension))
            print(err)
            if "200 OK" in err:
                break
    count += 1
    print("%d/%d" % (count, count_limit))
    if count == count_limit: break;
