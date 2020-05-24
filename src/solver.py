from extractor import extractKamus
from strMatcherAlgo import r_matcher, bm_matcher, kmp_matcher

def solve(inputText, algoOption, translationOption):
    if (translationOption=='indo-sunda'):
        return translateIndoToSunda(inputText, algoOption)
    else:
        return translateSundaToIndo(inputText, algoOption)

def doTranslate(inputText, algoOption, kamus):
    # fungsi untuk menerjemahkan kata sesuai opsi yang dipilih

    inputText = inputText.lower()
    for pairKata in kamus:
        if (len(pairKata[0])==len(inputText)):
            if (algoOption=='kmp'):
                if (kmp_matcher(pairKata[0],inputText)):
                    return pairKata[1]
            elif (algoOption=='boyerMoore'):
                if (bm_matcher(pairKata[0],inputText)):
                    return pairKata[1]
            else:   # regex
                if (r_matcher(pairKata[0],inputText)):
                    return pairKata[1]
    return inputText

def translateIndoToSunda(inputText, algoOption):
    # fungsi untuk menerjemahkan text indonesia ke sunda

    kamus = extractKamus('indo-sunda')

    subjekSunda = ['anjeun', 'anjeunna', 'maneh', 'manehna', 'urang', 'abdi', 'aing', 'ieu']    # kata subjek bahasa sunda
    isAlreadyUseTeh = False

    resultText = []
    listKata = inputText.split(' ')
    for kata in listKata:
        # jika di akhir kata ada simbol
        if (kata[-1].lower()==kata[-1].upper()):
            resultText.append(doTranslate(kata[:-1],algoOption,kamus) + kata[-1])
        else:
            temp = doTranslate(kata, algoOption, kamus)
            resultText.append(temp)
            print(temp)
            # jika subjek dan belum ada digunakan kata 'teh', maka ditambahkan 'teh'
            if ((not isAlreadyUseTeh) and (temp in subjekSunda)):
                isAlreadyUseTeh = True
                resultText.append("teh")
    return (" ".join(resultText))

def translateSundaToIndo(inputText, algoOption):
    # fungsi untuk menerjemahkan text sunda ke indo

    kamus = extractKamus('sunda-indo')

    notImportantStopWords = ['teh','mah','tea']     #stopwords bahasa sunda yang bisa diabaikan

    resultText = []
    listKata = inputText.split(' ')
    for kata in listKata:
        # jika di akhir kata ada simbol
        if (kata[-1].lower()==kata[-1].upper()):
            resultText.append(doTranslate(kata[:-1],algoOption,kamus) + kata[-1])
        else:
            if (kata not in notImportantStopWords):
                resultText.append(doTranslate(kata,algoOption,kamus))
    return (" ".join(resultText))
