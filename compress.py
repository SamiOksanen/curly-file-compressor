import re

def compress(i, o):
    print('Compressing...')
    content = i.read()
    if len(re.findall('{;', content)) > 0:
        print('File containing "{;". Can not compress.')
        raise
    suppressions = ''
    dups = re.findall(r'\b(\S+)\b(?=.*\b\1\b.*)', content)
    replacements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#%&*+,-./:<=>?@]_`|}~ ¡¢£¤¥¦§¨©ª«¬	®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſ&ƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄɅɆɇɈɉɊɋɌɍɎɏḂḃḊḋḞḟṀṁṖṗṠṡṪṫẀẁẂẃẄẅẛỲỳəɼʒ'
    print(dups)
    for dup in dups:
        if len(dup) > 2:
            sdup = dup + ' '
            if len(re.findall(sdup, content)) > 2:
                for r in replacements:
                    rep = '{' + r
                    try:
                        if len(re.findall(rep, content)) == 0:
                            content = content.replace(sdup, rep)
                            suppressions += rep + sdup
                            break
                    except Exception:
                        raise Exception('Char', r, 'causing trouble')
            if len(re.findall(dup, content)) > 2:
                for r in replacements:
                    rep = '{' + r
                    try:
                        if len(re.findall(rep, content)) == 0:
                            content = content.replace(dup, rep)
                            suppressions += rep + dup
                            break
                    except Exception:
                        raise Exception('Char', r, 'causing trouble')
    content = suppressions + '{;' + content
    o.write(content)
    print('Compressed')