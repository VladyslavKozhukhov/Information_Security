class RepeatedKeyCipher(object):

    def __init__(self, key=[0, 0, 0, 0, 0]):
        """Initializes the object with a list of integers between 0 and 255."""
        assert all(0 <= k <= 255 and isinstance(k, (int, long)) for k in key)
        self.key = key

    def encrypt(self, plaintext):
        cryptMsg = []
        for i in range(len(plaintext)):
            xorResult = ord(plaintext[i])^(self.key[i%len(self.key)])
            cryptChar = chr(xorResult)
            cryptMsg+=[cryptChar]
        return "".join(cryptMsg) 

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)


class BreakerAssistant(object):

    def plaintext_score(self, plaintext):
        score = 0
        counter = 0
        total = 0
        top_letters = ['o','t','a','e',' ','i']#'n','N']
        for i in plaintext:
            if i in top_letters:
                if i =='e':
                    counter+=12.5
                if i=='t':
                    counter+=9.28
                if i=='a':
                   counter+=8.04
                else:
                    counter+=3

            elif (ord(i)>=97 and ord(i)<=122):
                counter = counter + 2
            elif(ord(i)>=65 and ord(i)<=90):
                counter = counter + 2
            elif(ord(i)>32 and ord(i)<=47):
                counter = counter + 1
            elif(ord(i)==63 or ord(i)==10 or ord(i)==32):#new line and ?
                counter = counter + 1
        totalScore = float(counter)
        return totalScore

    def brute_force(self, cipher_text, key_length):
        amount_of_keys = 256**key_length
        bestmatch=""
        bestcore=-1
        for i in range(0,amount_of_keys):
            newKey=self.key_order_creator(amount_of_keys,key_length)
            newWord=RepeatedKeyCipher(newKey).decrypt(cipher_text)
            score = self.plaintext_score(newWord)
            amount_of_keys-=1
            if score>bestcore:
                bestmatch=newWord
                bestcore=score
        return bestmatch


    def key_order_creator(self,index,key_length):
        arr=[]
        for i in range(0,key_length):
            arr.append(index%256)
            index=index/256
        return arr
            


    def smarter_break(self, cipher_text, key_length):
        #print("cioherTEXT is:")
        #print(cipher_text)
        keys= []
        txtLen = len(cipher_text)
        matrix=[[]for i in range(0,key_length)]
        #for j in range(key_length):#Move to another problem
           # print("Same bit word is")
            #print(matrix[j])
        for j in range (0,txtLen):#Move to 1 bit problem
            index = j%key_length
            matrix[index]+=[cipher_text[j]]
        for i in range (0,key_length):    
            string = self.brute_force("".join(matrix[i]),1)
            #print("best match")
            #print(string)
            key_index = ord(string[0])^ord(matrix[i][0])
            keys+=[key_index]
            #print(keys[j])

        #print("KEYS IS")    
        #print(keys)
        match = RepeatedKeyCipher(keys)
        return match.decrypt(cipher_text)