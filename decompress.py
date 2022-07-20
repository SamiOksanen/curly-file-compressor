import re

def decompress(d, o):
    print('Decompressing...')
    content = d.read()
    
    if len(re.findall('{;', content)) > 0:
        if len(re.findall('{;', content)) > 1:
            raise Exception('File containing more than one "{;". Can not decompress.')
        else:
            contents = re.split('{;', content)
            if len(contents[0]) > 1:
                replacements = re.split('{', contents[0])
                replacements.pop(0)
                actualContent = contents[1]
                for r in replacements:
                    if len(re.findall('{' + r[:1], actualContent)) == 0:
                        raise Exception('Didn´t find anything to decompress for {' + r[:1])
                    else:
                        actualContent = actualContent.replace('{' + r[:1], r[1:])

    o.write(actualContent)
    print('Decompressed.')