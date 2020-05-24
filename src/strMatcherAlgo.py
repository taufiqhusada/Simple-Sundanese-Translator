import re

def r_matcher(text, pattern):
    return re.match(text.lower(), pattern.lower())

def kmp_matcher(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)

    lps = compute_lps(pattern)
    
    i = 0
    j = 0

    while(i < len_text):
        if (text[i].lower() == pattern[j].lower()):
            if (j == len_pattern-1):
                return True
            else:
                j = j+1
            i = i+1
        elif (j > 0):
            j = lps[j-1]
        else:
            i = i+1 

    return False

def compute_lps(pattern):
    len_pattern = len(pattern)
    lps = [0 for i in range(len_pattern)]
    i = 1
    j = 0
    while(i < len_pattern):
        if (pattern[i].lower() == pattern[j].lower()):
            lps[i] = j+1
            i+=1
            j+=1
        elif (j > 0):
            j = lps[j-1]
        else:
            lps[i] = 0
            i+=1

    return lps

def bm_matcher(text, pattern):
    last = compute_last(pattern)
    len_text = len(text)
    len_pattern = len(pattern)
    i = len_pattern - 1

    if (i <= len_text - 1):
        j = len_pattern - 1
        isOk = True
        while(isOk):
            if (pattern[j].lower() == text[i].lower()):
                if (j == 0):
                    return True
                else:
                    i-=1
                    j-=1
            else:
                lo = last[ord(text[i])]
                i += len_pattern - min(j, 1 + lo)
                j = len_pattern - 1
            if (i > len_text - 1):
                isOk = False

    return False

def compute_last(pattern):
    last = [-1 for i in range(128)]
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last