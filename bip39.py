import random
import hashlib

def getBip39WordList():
    wordList = []
    with open('bip39_wordlist.txt','r') as fo:
        while True:
            word = fo.readline()
            if word == '':
                break
            wordList.append(word.strip())
    return wordList

def generateBip39Mnemonic(words=24):
    '''

    :param words:
    :return:
    '''

    '''
    cs will be list of tuple [(Entropy, checksum size, 11-bit words)]
    [(32, 1, 3), (64, 2, 6), (96, 3, 9), (128, 4, 12), (160, 5, 15), (192, 6, 18), (224, 7, 21), (256, 8, 24)]
    '''
    cs = [(x,int(x/32),int((x+x/32)/11)) for x in list(range(32,256+1,32))]

    curr_set = [v for v in cs if v[2] == words]

    if curr_set == []: #if invalid word size is given than return None
        return None

    '''generating random number of 8 bit integers based on entropy'''
    entropy = ''.join(['{:08b}'.format(random.randint(0,255)) for x in range(int(curr_set[0][0]/8))])

    sha256 = hashlib.sha256(entropy.encode('utf-8')).hexdigest()
    cs = '{:08b}'.format(int(sha256[:2],16))[:curr_set[0][1]]

    wordList = getBip39WordList()

    ent_cs = entropy+cs

    mnemonics = [wordList[int(ent_cs[x*11:x*11+11],2)] for x in range(curr_set[0][2])]

    print(' '.join(mnemonics))
    x=1

if __name__ == '__main__':
    generateBip39Mnemonic(3)
    # getBip39WordList()
