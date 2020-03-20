import sys, getopt, os
from PIL import Image
from resizeimage import resizeimage

androidSizes = {
    "-android-432x432": [432,432],
    "-android-324x324": [324,324],
    "-android-216x216":[216,216],
    "-android-162x162":[162,162],
    "-android-108x108":[108,108],
    "-android-81x81":[81,81],
    "-android-192x192":[192,192],
    "-android-144x144":[144,144],
    "-android-96x96":[96,96],
    "-android-72x72":[72,72],
    "-android-48x48":[48,48],
    "-android-36x36":[36,36]    
}

def scale(inputfile, outputfile):
    print('Input file ', inputfile)
    print('Ouput file prefix', outputfile)
    if inputfile == '':
        print("Inputfile is empty")
        sys.exit()
    if outputfile == '':
        print("Outpufile is empty")
        sys.exit()    
    img = Image.open(inputfile)
    for name, res in androidSizes.items():
        icon = resizeimage.resize_thumbnail(img, res)
        fname = outputfile + '-' + name + '.png'
        if os.path.exists(fname):
            os.remove(fname)
        icon.save(fname, img.format)
        print("Created file "+fname)
    

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('-i <inputfile>')
        print ('-o <outputfile prefix>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-i <inputfile> -o <ouputfile prefix>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    scale(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
