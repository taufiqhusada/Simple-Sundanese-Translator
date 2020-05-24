def extractKamus(optTranslation):
    if (optTranslation=="indo-sunda"):
        listTranslate = open("../data/indonesia.txt", "r").readlines()
    else:
        listTranslate = open("../data/sunda.txt", "r").readlines()

    kamus = []

    for translation in listTranslate:
        pairWord = translation.split(' = ')
        if (pairWord[1][-1]=='\n'):
            pairWord[1] = pairWord[1][:-1]

        kamus.append((pairWord[0].lower(),pairWord[1].lower()))
    
    return kamus