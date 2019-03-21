import sys
import os
import os.path as osp
import json

cocoFile = '/media/data/chnxi/coco/annotations/captions_val2014.json'
bisonFile = './annotations/bison_annotations.cocoval2014.json'
outCapFile = './annotations/bison_coco_caps.txt'
outFile = './annotations/detail_bison_coco_caps.txt'

d = json.load(open(cocoFile,'rb'))

ann = d['annotations']

ids = [a['id'] for a in ann]

bison = json.load(open(bisonFile,'rb'))

with open(outCapFile,'w') as fout, open(outFile,'w') as f2:
    f2.write('{}\t{}\t{}\t{}\n'.format('true id', 'image_id1', 'image_id2', 'caption'))
    for data in bison['data']:
        capId = data['caption_id']
        trueId = data['true_image_id']
        id1 = data['image_candidates'][0]['image_id']
        id2 = data['image_candidates'][1]['image_id']

        if capId in ids:
            index = ids.index(capId)
            cap = ann[index]['caption'].strip('\n')
            image_id = ann[index]['image_id']
            #print ("{}: {}".format(image_id, cap))
            fout.write(cap + '\n')
            fout.write(cap + '\n')
            f2.write('{}\t{}\t{}\t{}\n'.format(trueId, id1, id2, cap)) 
        else:
            print ("capId {} not in coco val!".format(capId))
        
