import subprocess as sp

from bs4 import BeautifulSoup

import os
import sys
import traceback

version = "v1.0.0"

def mk_dir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            return directory
    except OSError:
        print('Error with creating directory ' + directory)
        return None

def readTxtFile():
    file = open("input.txt", 'r', encoding='utf-8')
    url = file.readline()
    lec_name = file.readline()
    return url, lec_name

def download_via_m3u8(url, video_name):
    # # ffmpeg -i "https://mszgmhihzdlo5752380.cdn.ntruss.com/hls/689ab1fb-3c5c-4a3c-bcf7-cbc23ddd1cef/mp4/689ab1fb-3c5c-4a3c-bcf7-cbc23ddd1cef.mp4/index.m3u8" -bsf:a aac_adtstoasc -c copy test.mp4
    cmd = ['ffmpeg', '-i']
    cmd.append(url)
    cmd.append("-bsf:a")
    cmd.append("aac_adtstoasc")
    cmd.append("-c")
    cmd.append("copy")
    file_name = os.path.join(video_name + ".mp4")
    cmd.append(file_name)
    print(cmd)
    try:
        sp.call(cmd)
    except:
        traceback.print_exc()

def find_info():
    with open("LearnUs.html", 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        url = soup.find("source", src=True)["src"]
        lec_name = soup.find("h1").text
        lec_name = lec_name[22:-18]
        return url, lec_name

def download_video():
    # url, lec_name = readTxtFile()
  
    # print("sumamry")
    # print("lecture name=",lec_name)

    try :
        url, lec_name = find_info()
        download_via_m3u8(url, lec_name)
        print('m3u8 url =', url)
        print('lecture name =', lec_name)
        print('Save complete')
    except Exception as e :
        print('-' * 20, 'Error occured', '-'*20)
        print(e)
        _, _ , tb = sys.exc_info() # tb -> traceback object 
        print ('file name = ', __file__)
        print ('error line No = {}'.format(tb.tb_lineno))
        traceback.print_exc()

if __name__ == "__main__":
    print("yonsei learn us video downloader", version)
    download_video()