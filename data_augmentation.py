# -*- coding: utf-8 -*-
"""
========================================================================
PDCNN for DoFP image interpolation, Version 1.0
Copyright(c) 2018  Junchao Zhang, Jianbo Shao, Haibo Luo, Xiangyue Zhang,
Bin Hui, Zheng Chang, and Rongguang Liang
All Rights Reserved.

----------------------------------------------------------------------
Permission to use, copy, or modify this software and its documentation
for educational and research purposes only and without fee is here
granted, provided that this copyright notice and the original authors'
names appear on all copies and supporting documentation. This program
shall not be used, rewritten, or adapted as the basis of a commercial
software or hardware product without first obtaining permission of the
authors. The authors make no representations about the suitability of
this software for any purpose. It is provided "as is" without express
or implied warranty.
----------------------------------------------------------------------
Please cite the following paper when you use it:

Junchao Zhang, Jianbo Shao, Haibo Luo, Xiangyue Zhang, Bin Hui,
Zheng Chang, and Rongguang Liang, "Learning a convolutional demosaicing
network for microgrid polarimeter imagery," Optics Letters 43(18),
4534-4537 (2018). 
========================================================================
"""
import numpy as np

def data_augmentation(imagein, mode):
    image = np.transpose(imagein,(1,2,3,0))
    if mode == 0:
        # original
        return imagein
    elif mode == 1:
        # flip up and down
        image = np.flipud(image)
    elif mode == 2:
        # rotate counterwise 90 degree
        image = np.rot90(image)
    elif mode == 3:
        # rotate 90 degree and flip up and down
        image = np.rot90(image)
        image = np.flipud(image)
    elif mode == 4:
        # rotate 180 degree
        image = np.rot90(image, k=2)
    elif mode == 5:
        # rotate 180 degree and flip
        image = np.rot90(image, k=2)
        image = np.flipud(image)
    elif mode == 6:
        # rotate 270 degree
        image = np.rot90(image, k=3)
    elif mode == 7:
        # rotate 270 degree and flip
        image = np.rot90(image, k=3)
        image = np.flipud(image)
    imageout = np.transpose(image,(3,0,1,2))
    return imageout
