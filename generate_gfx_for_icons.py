# make icon pics sprites code
import os
import glob

dir_name = os.getcwd()
mod_prefix = 'hfe_'
pics_dir = os.path.join(dir_name, 'gfx', 'interface', 'icons', 'other')
gfx_name = os.path.join(dir_name, 'interface', mod_prefix + 'icons_other.gfx')

pics = glob.glob(pics_dir + '/*.dds')

with open(gfx_name, 'w') as f:
    f.write('spriteTypes = {\n')
    for pic in pics:
        pic_name = os.path.splitext(os.path.basename(pic))[0]
        f.write(f'\tspriteType = {{\n\t\tname = "GFX_{pic_name}"\n\t\ttexturefile = "gfx/interface/icons/other/{pic_name}.dds"\n\t}}\n')
    f.write('}')