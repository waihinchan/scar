import torch
import torch.nn as nn
import mydataprocess
from mydataprocess import dataset, mydataloader
import option
import model
from torchvision import transforms
from PIL import Image
import os
import matplotlib.pyplot as plt



myoption = option.opt()
# myoption.which_epoch = '40'
# myoption.mode = 'test'
# for name,value in vars(myoption).items():
#     print('%s=%s'%(name,value))
#
# mymodel = model.SCAR()
# mymodel.initialize(myoption)


def grabdata(opt,path):
    # path = os.path.join('./dataset',opt.name)
    # inputname = path + '/a.png'
    # print(inputname)
    input_image = Image.open(path)
    transforms_pipe = dataset.build_pipe(opt)
    return transforms_pipe(input_image)

# theinput = grabdata(myoption)

# imshow(mymodel.netG(theinput))

unloader = transforms.ToPILImage()  # reconvert into PIL image
def imshow(tensor,interval = 0.5):
    image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
    image = image.squeeze(0)      # remove the fake batch dimension
    image = unloader(image)
    plt.figure()
    plt.imshow(image)
    plt.show()
    # plt.pause(interval)
    # plt.close('all')
    # here remain to update
    # like how to inline the result



a = grabdata(myoption,'/Users/waihinchan/Documents/mymodel/scar/dataset/test/046-a.png')
imshow(a)