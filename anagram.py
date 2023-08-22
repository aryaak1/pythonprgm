#anagram

word = "earth"
inpt = "heart"
w =list(word)
i =list(inpt)

w.sort()
i.sort()
if w == i:
    print("anagram")
else:
    print("not anagram")


    

# srt_word=sorted(word)
# srt_out=sorted(out)
# print(srt_word)
# print(srt_out)
#print("anagram" if srt_word==srt_out else "not anagram")
