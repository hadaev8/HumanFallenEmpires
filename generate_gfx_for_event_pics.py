# make event pics sprites code
import os
import glob

dir_name = os.getcwd()
mod_name = os.path.basename(dir_name)
pics_dir = os.path.join(os.path.join(dir_name, 'gfx'), 'event_pictures')
gfx_name = os.path.join(os.path.join(dir_name, 'interface'), mod_name + '_eventpictures.gfx')

pics = glob.glob(pics_dir + '/*.dds')

if os.path.exists(gfx_name):
    os.remove(gfx_name)

with open(gfx_name, 'a') as f:
    f.write('spriteTypes = {\n')
    for pic in pics:
        f.write('\tspriteType = {{\n\t\tname = "GFX_evt_{0}"\n\t\ttexturefile = "gfx/event_pictures/{0}.dds"\n\t\tmasking_texture = "gfx/interface/situation_log/event_mask.dds"\n\t\talwaystransparent = yes\n\t}}\n'.format(os.path.splitext(os.path.basename(pic))[0]))
    f.write('}')