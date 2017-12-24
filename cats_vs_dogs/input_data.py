# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os

#获取文件路径和标签
def get_files(file_dir):
    #file_dir : 文件夹路径
    #return 乱序后的图片和标签
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    
    # 载入数据路径并写入标签值
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0] == 'cat':
            cats.append(file_dir+file)
            label_cats.append(0)
        else:
            dogs.append(file_dir+file)
            label_dogs.append(1)
    print("There are %d cats\nThere are %d dogs" % (len(cats),len(dogs)))
    
    #打乱文件顺序
    image_list = np.hstack((cats,dogs))
    label_list = np.hstack((label_cats,label_dogs))
    temp = np.array([image_list,label_list])
    temp = temp.transpose()  #矩阵转置
    np.random.shuffle(temp)
    
    image_list = list(temp[:,0])
    label_list = list(temp[:,1])
    label_lsit = [int(i) for i in label_list]
    
    return image_list, label_list
    
#生成相同大小的批次
def get_batch(image,label,image_W,image_H,batch_size,capacity ):
    # image, label: 要生成batch的图像和标签list
    # image_W, image_H: 图片的宽高
    # batch_size: 每个batch有多少张图片
    # capacity: 队列容量
    # return: 图像和标签的batch
    
    # 将python.list类型转换成tf能够识别的格式
    image = tf.cast(image, tf.string)
    label = tf.cast(label, tf.int32)
    
    #生成队列
    input_queue = tf.train.slice_input_producer([image, label])
    image_contents = tf.read_file(input_queue[0])
    label = input_queue[1]
    image = tf.image.decode_jpeg(image_contents, channels = 3)
    
    #同一图片大小
    #视频方法
    #
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    