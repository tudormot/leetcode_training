from typing import List


def quicksort(s:List[int],l:int ,r:int): #sorting done in place
    print("l, r = ", l,r)
    if r-l < 1:
        return

    p = s[l]
    i = l+1
    j = r-1
    while True:
        while i<r and s[i]< p:
            i +=1
        while j>=l and s[j]>p:
            j -=1
        if i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        else:
            break
    s[l] = s[j]
    s[j] = p
    quicksort(s,l,j)
    quicksort(s,i,r)

if __name__ == "__main__":
    s = [10, 5, 21, 1, 17]
    quicksort(s,0,len(s))
    print(s)
