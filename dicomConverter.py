import numpy
import os
import dicom
import PIL
from matplotlib import pyplot, cm
path = "C:/Users/asus/AppData/Local/Programs/Python/Python35"
os.chdir(path)
image = dicom.read_file("brain")
dms = (int(image.Rows), int(image.Columns), 1)
spacing = (float(image.PixelSpacing[0]), float(image.PixelSpacing[1]), float(image.SliceThickness))
AAD = numpy.zeros(dms, dtype = image.pixel_array.dtype)
AAD[:, :, 0] = image.pixel_array
pyplot.figure(dpi=300)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
x = numpy.arange(0.0, (dms[0])*spacing[0], spacing[0])
y = numpy.arange(0.0, (dms[1])*spacing[1], spacing[1])
pyplot.pcolormesh(x,y, numpy.flipud(AAD[:,:,0]))
pyplot.axis("off")
pyplot.savefig("brainconv.png", bbox_inches='tight', pad_inches = 0.0)
