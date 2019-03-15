import os
import os.path as osp
import sys
import json

jsonFile = './bison_annotations.cocoval2014.json'
imgPath = '/media/data/chnxi/coco/val2014/'

d = json.load(open(jsonFile,'rb'))

imglistFile = './bison_coco_imglist.txt'

with open(imglistFile,'w') as fout:
    for ix, x in enumerate(d['data']):
        imgNames = []
        for im in x['image_candidates']:
            img_id = im['image_id']
            #print (img_id)
            imgName = 'COCO_val2014_{0:012d}.jpg'.format(img_id)
            if not osp.exists(osp.join(imgPath, imgName)):
                print ("{} not exists!".format(imgName))
            imgNames.append(imgName)
            #print ("{}:{}".format(img_id, imgName))
        fout.write('{:d}\t{:s}\t{:s}\n'.format(ix, imgNames[0], imgNames[1]))


