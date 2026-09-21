class Solution:
    def encode(self, strs: List[str]) -> str:
        #let us add the length of the str and a deleimiter like # that way we can decode by grabbing the len prior to 
        #the deleimter and add that length of str into our result array
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        #when decoding we will find the lenghth by having another pointer pointing at right before the delimter
        #when we grab the str from delimter + 1 to the length that we had calacuted
        res = []
        i = 0
        while i < len(s):
            #second pointer incase length is two digits we can't assume s[0] or later as well
            j = i
            while s[j] != "#":
                j += 1
            #Once we have reach the deleimter now we can get the length as an int
            length = int(s[i:j])
            #now that we have the length we know the start of the str and end 
            startString = j + 1
            endString = startString + length 
            #finally append the string into res
            res.append(s[startString:endString])
            #update the i to go to next length or out of bound /end
            i = endString
        return res
