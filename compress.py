import re

def compress(i, o):
    print('Compressing...')
    content = i.read()
    if '{;' in content:
        print('File containing "{;". Can not compress.')
        raise

    contents = replaceToCurlies(content, '{')
    if len(contents[0]) > 0:
        suppressions = contents[0] + '{;'
        content = contents[1]

    if '}:' in content:
        print('File containing "}:". Can not compress.')
        raise

    contents = replaceToCurlies(content, '}')
    if len(contents[0]) > 0:
        suppressions = contents[0]+ '}:' + suppressions
        content = contents[1]

    content = suppressions + content

    o.write(content)
    print('Compressed')


def replaceToCurlies(content, curly):
    suppressions = ''
    replacements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#%&*+,-./<=>?@]_`|~ ¡¢£¤¥¦§¨©ª«¬	®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſ&ƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄɅɆɇɈɉɊɋɌɍɎɏḂḃḊḋḞḟṀṁṖṗṠṡṪṫẀẁẂẃẄẅẛỲỳəɼʒ'
    dups1 = re.findall(r'\b(\S+)\b(?=.*\b\1\b.*)', content)
    dups2 = re.findall(r'\b\w{5,}', content)
    dups3 = re.findall(r'(\w+)\1', content)
    dupsCombo = dups1 + dups2 + dups3
    dups = list(dict.fromkeys([x for x in dupsCombo if len(x) >= 1]))
    print(dups)
    for dup in dups:
        ssdup = ' ' + dup + ' '
        ssdupCount = len(re.findall(ssdup, content))
        if (len(ssdup) >= 3 and ssdupCount >= 6) or (len(ssdup) >= 4 and ssdupCount >= 4) or (len(ssdup) >= 5 and ssdupCount >= 3) or (len(ssdup) >= 7 and ssdupCount >= 2):
            for r in replacements:
                rep = curly + r
                try:
                    if rep not in content and rep not in suppressions:
                        content = content.replace(ssdup, rep)
                        suppressions = rep + ssdup + suppressions
                        break
                except Exception:
                    raise Exception('Char', r, 'causing trouble')

        sdup = dup + ' '
        sdupCount = len(re.findall(sdup, content))
        if (len(sdup) >= 3 and sdupCount >= 6) or (len(sdup) >= 4 and sdupCount >= 4) or (len(sdup) >= 5 and sdupCount >= 3) or (len(sdup) >= 7 and sdupCount >= 2):
            for r in replacements:
                rep = curly + r
                try:
                    if rep not in content and rep not in suppressions:
                        content = content.replace(sdup, rep)
                        suppressions = rep + sdup + suppressions
                        break
                except Exception:
                    raise Exception('Char', r, 'causing trouble')

        dupCount = len(re.findall(dup, content))
        if (len(dup) >= 3 and dupCount >= 6) or (len(dup) >= 4 and dupCount >= 4) or (len(dup) >= 5 and dupCount >= 3) or (len(dup) >= 7 and dupCount >= 2):
            for r in replacements:
                rep = curly + r
                try:
                    if rep not in content and rep not in suppressions:
                        content = content.replace(dup, rep)
                        suppressions = rep + dup + suppressions
                        break
                except Exception:
                    raise Exception('Char', r, 'causing trouble')

    if len(suppressions) > 0:
        return [suppressions, content]
    else:
        return ['', content]
