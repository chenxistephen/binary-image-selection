import os
import os.path as osp
import sys
import json

jsonFile = './annotations/bison_annotations.cocoval2014.json'
imgPath = '/media/data/chnxi/coco/val2014/'

d = json.load(open(jsonFile,'rb'))

imglistFile = './annotations/bison_coco_imglist.txt'
trueIdFile = './annotations/true_image_ids2.txt'

print ("len(data) = {}".format(len(d['data'])))

with open(imglistFile,'w') as fout, open(trueIdFile,'w') as ftrue:
    fout.write('bison_id\timage_id_0\timage_id_1\n')
    for ix, x in enumerate(d['data']):
        imgNames = []
        bisonId = x['bison_id']
        trueId = x['true_image_id']
        for im in x['image_candidates']:
            img_id = im['image_id']
            #print (img_id)
            imgName = 'COCO_val2014_{0:012d}.jpg'.format(img_id)
            if not osp.exists(osp.join(imgPath, imgName)):
                print ("{} not exists!".format(imgName))
            #imgNames.append(imgName)
            imgNames.append(str(img_id))
            #print ("{}:{}".format(img_id, imgName))
        fout.write('{:d}\t{:s}\t{:s}\n'.format(bisonId, imgNames[0], imgNames[1]))
        ftrue.write('{}\n'.format(trueId))

