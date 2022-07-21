import sys
import getopt
import os.path
from compress import compress
from decompress import decompress

def main(argv):
    inputfile = ''
    outputfile = ''
    decompressfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:d:", ["help", "ifile=", "ofile="])
    except getopt.GetoptError:
        print('sc.py -i <inputfile> -o <outputfile>')
        print('sc.py -d <decompressfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('sc.py -i <inputfile> -o <outputfile>')
            print('sc.py -d <decompressfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--dfile"):
            decompressfile = arg

    i = ''
    o = ''

    if inputfile != '':
        i = open(inputfile, 'r')
        if outputfile == '':
            outputfile = inputfile + '.curlyc'
        while os.path.isfile(outputfile):
            break
        print('Input file is', inputfile)
    elif decompressfile != '':
        i = open(decompressfile, 'r')
        if outputfile == '':
            outputfile = decompressfile.replace('.curlyc', '')
        print('Decompress file is', decompressfile)

    ix = 1
    origoutputfile = outputfile
    while True:
        if not os.path.isfile(outputfile):
            break
        else:
            outputfile = origoutputfile + str(ix)
            ix = ix + 1

    o = open(outputfile, 'x')

    if inputfile != '':
        compress(i, o)
    elif decompressfile != '':
        decompress(i, o)
    print('Output file is', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
