class Cipher:
    def __init__(self, codestring):
        self.codestring = codestring.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__code = {a: b for (a, b) in zip(self.alphabet, codestring)}
        self.__inverse = {a: b for (a, b) in zip(codestring, self.alphabet)}
        self.__code[" "] = "-"
        self.__inverse["-"] = " "


    def encode(self, plaintext):
        plaintext = "".join(self.__code[l] if l in self.__code else l for l in plaintext.upper())
        return plaintext

    def decode(self, ciphertext):
        ciphertext = "".join(self.__inverse[l] if l in self.__inverse else l for l in ciphertext.upper())
        return ciphertext

    def give_code(self):
        return self.__code

    def give_inverse(self):
        return self.__inverse

test = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
result_encode = test.encode("Ab3c, De1::6")
result_decode = test.decode(result_encode)
print(result_encode)
print(result_decode)
print(test.give_code)
print(test.decode("--Ap4s#$!"))
