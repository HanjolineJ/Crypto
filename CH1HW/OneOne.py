ciphertext = "Ievmnse the sumvtsve of the lmssv yoeeyekts of qmtm ss the fovns and ymsteut of sehf ss the essekve of ymtsnlmtmshs utn qmumte do s shmhh tut to ehnvsdmte the yoeeyekts of the qmtm mvvoudsko to yt skteusuetmtsok lmsed ok foutt temus of stndt ssoksfsvmkve and soye ynst ueymsk nkeashmsked to osee m st ss kot mk emst tmsq to eashmsk emvh yoeeyekt and sts voyshete eashmkmtsok oke conhd hmee to le fnmhsfsed mká sksssued to snvh mk eatekt thmt he vonhd uemvh the stmte of ekhsohteked yskd vmsmlhe of uevooksgsko sonkdhess sonkd and shmsehess shmse s do kot deey ytsehf the fskmh mnthoustt lnt yt easeusekve csth qmtm hms heft ko donlt thmt the fohhocsko ss the suoseu msshsvmtsok and skteusuetmtsok s offeu yt theouses sk the hose thmt the essekve of oqskmcmk qmumte cshh ueymsk sktmvt"
oldcipher ="Irvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mká wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

key = {
    'a': 'I',
    'b': 't',
    'c': 'c',
    'd': 'd',
    'e': 'a',
    'f': 'g',
    'g': 'r',
    'h': 'u',
    'i': 's',
    'j': 'o',
    'k': 'n',
    'l': 'p',
    'm': 'a',
    'n': 'e',
    'o': 'w',
    'p': 'h',
    'q': 'd',
    'r': 'e',
    's': 'c',
    't': 'b',
    'u': 'y',
    'v': 'i',
    'w': 'f',
    'x': 'f',
    'y': 'v',
    'z': 'k'
}


keyy = {
    'b': 't',
    'p': 'h',
    'r': 'e',
    'j': 'o',
    'x': 'f',
    'm': 'a',
    'k': 'n',
    'd': 'd',
    'w': 'i',
    'i': 's',
    'q': 'd'
}

# The decrypted text is built character by character
decrypted_text = ""

# Iterate through the ciphertext
for char in oldcipher:
#for char in ciphertext:
    # If the character is in our key, replace it with the plaintext letter
    if char in key:
        decrypted_text += key[char]
    # If it's not a letter we've guessed, keep it as is
    else:
        decrypted_text += char

# Print the partially decrypted text to see your progress
print(decrypted_text)