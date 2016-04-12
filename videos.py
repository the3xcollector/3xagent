import math
import os

import imageio

def get_meta(mov):
    reader = imageio.get_reader(mov)
    meta = reader.get_meta_data()
    meta['path'] = mov
    meta['file'] = os.path.basename(mov)
    meta['size'] = os.path.getsize(mov)
    return meta


def extract_frames(video_file):
    reader = imageio.get_reader(video_file, print_info=False)

    # pprint(reader.get_meta_data())
    nframes = reader.get_length()
    print("frames:", nframes)
    for i in range(0, nframes, math.floor(nframes / 4)):  # get 4 pictures
        image_file = "./scr." + str(i) + ".jpg"
        print("writing frame", i, "to", image_file)
        frame = reader.get_data(i)
        imageio.imwrite(image_file, frame, 'jpg')
