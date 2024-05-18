# make event pics sprites code
import os
import glob

dir_name = os.getcwd()
mod_prefix = 'hfe_'
pics_dir = os.path.join(dir_name, 'gfx', 'event_pictures')
gfx_name = os.path.join(dir_name, 'interface', mod_prefix + 'eventpictures.gfx')

pics = glob.glob(pics_dir + '/*.dds')

with open(gfx_name, 'w') as f:
    f.write('spriteTypes = {\n')
    for pic in pics:
        pic_name = os.path.splitext(os.path.basename(pic))[0]
        f.write(f'\tspriteType = {{\n\t\tname = "GFX_evt_{pic_name}"\n\t\ttexturefile = "gfx/event_pictures/{pic_name}.dds"\n\t\tanimation = {{\n\t\t\tanimationmaskfile = "gfx/event_pictures/style/{pic_name}.dds"\n\t\t\tanimationtime = 10.0\n\t\t\tanimationblendmode = "overlay"\n\t\t\tanimationtype = "pulsing"\n\t\t}}\n\t}}\n')
    f.write('}')