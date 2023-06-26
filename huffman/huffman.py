import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heapq.heappop(heap)[1:]#, key=lambda p: (len(p[-1]), p))


data = "saadhvikka"
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")

code=[]
alpha=[]
flen=len(frequency)
for l in data:
    for r in range(flen):
        if huff[r][0]==l:
            alpha.append(huff[r][0])
            code.append(huff[r][1])
            
        
        
print(alpha)
print(code)

#bi=[]
#
#for i in range(len(code)):
#    c=int(code[i])
#    decimal = int(code[i], 2);
#    bi.append(decimal)
#    
#print(bi)

print(huff)
for i in range(len(code)):
    print(alpha[i],code[i])
#
#for p in huff:
##    print (p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
#    if frequency[p[0]]==1:
#        print(p[1])
#    else:
#        for r in range(frequency[p[0]]):
#            print(p[1])