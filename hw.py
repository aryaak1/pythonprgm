words=["hello","good","aabbcccdef","morning"]
def get_len(w):
    return len(w)
print(sorted(words,key=get_len,reverse=True))

print(sorted(words,key=lambda w:len(w),reverse=True))





