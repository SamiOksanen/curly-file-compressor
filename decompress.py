import re

def decompress(d, o):
    print('Decompressing...')
    content = d.read()
    actualContent = content

    if '{;' in content:
        if '{;' not in content:
            print('Nothing to decompress for the file.')
        if len(re.findall('{;', content)) > 1:
            raise Exception('File containing more than one "{;". Can not decompress.')
        else:
            contents = re.split('{;', content)
            if len(contents[0]) > 1:
                actualContent = contents[1]
                replacements = re.split('{', contents[0])

                if '}:' in contents[0]:
                    replacementsByBracketDirection = re.split('}:', contents[0])
                    if len(replacementsByBracketDirection[0]) > 1:
                        replacements = re.split('}', replacementsByBracketDirection[0])
                        replacements.pop(0)
                        actualContent = replaceCurlies(replacements, actualContent, '}', False)
                        if any(rep in actualContent for rep in replacements):
                            print('Rerunning replacement of the curlies due to some curlies still being in the content.')
                            actualContent = replaceCurlies(replacements, actualContent, '}', False)
                    replacements = re.split('{', replacementsByBracketDirection[1])

                replacements.pop(0)
                actualContent = replaceCurlies(replacements, actualContent, '{', True)
                if any(rep in actualContent for rep in replacements):
                    print('Rerunning replacement of the curlies due to some curlies still being in the content.')
                    actualContent = replaceCurlies(replacements, actualContent, '{', False)
            print('Decompressed.')

    o.write(actualContent)

def replaceCurlies(replacements, actualContent, curly, validate):
    for r in replacements:
        if validate and curly + r[:1] not in actualContent:
            raise Exception('Didn´t find anything to decompress for ' + curly + r[:1])
        else:
            actualContent = actualContent.replace(curly + r[:1], r[1:])
    return actualContent