# -*- coding: utf-8 -*-
from os import listdir,mkdir
from os.path import exists
from shutil import copy
from cv2 import imread,namedWindow,imshow,waitKey,destroyAllWindows
# mpimg 用于读取图片


    
           
if __name__=='__main__':
    listall=listdir('.')
    
    if not(exists('accept')):
        mkdir('accept')
    if not(exists('reject')):
        mkdir('reject')
    
    reject_key='c'
    quit_key='q'
    list_ac=listdir('./accept/')
    list_re=listdir('./reject/')
    
    i=0
    n_all=0
    n_towork=0
    for file in listall:
        filetype=file.split('.')[-1]
        if filetype in ['jpg','png']:
            n_all=n_all+1
            if (file not in list_ac) and (file not in list_re):
                n_towork=n_towork+1
				
    for file in listall:
        if (file not in list_ac) and (file not in list_re):
            filetype=file.split('.')[-1]
            if filetype in ['jpg','png']:
                img = imread(file)
                print(file)
                i=i+1
                print([i,'------',n_towork,'------',n_all])
                namedWindow("Cat")
                imshow("Cat",img) # 只使用imshow的时候，在IDLE窗口不会显示出图片。需要其后面接waitKey()配合使用。
                key = waitKey(0) # 显示1s，然后关闭显示。
                destroyAllWindows() 

                #key=input('how do you think about the pic,press c if you want to diss it!!')
                if key== ord(quit_key):
                    break
                if key==ord(reject_key):
                    copy(file,'./reject/'+file)
                elif key>0:
                    copy(file,'./accept/'+file)
    a=input('program end')
                
                    