# ProgrammingAssignment2Algos

Nihar Devireddy (78990160)
Mukul Vinod (65024528)

From ProgrammingAssignment2Algos directory, run command "python3 src/cache.py tests/example.in" or "python src/cache.py tests/example.in" if not using python 3. Based on what file you are testing, change the test file name by referring to it as tests/filehere. 

Input file is formatted as
k m
r1 r2 r3 ... rm

Solution is generated in a .out file. 



Written componenet solutions:
1.Yes, OPTFF have the fewest misses. This is because OPTFF evicts the one whose next request occurs farthest in the future. FIFO and LRU basically had the same number of misses, which shows how as the number of requests increases, FIFO and LRU perform the same and OPTFF performs much better.


Input File
k
m
FIFO
LRU
OPTFF
File1
3
60
58
59
38
File2
4
56
55
55
37
File3
3
56
56
56
38




2. For a cache size k = 3, there is a request sequence where OPTFF has fewer misses than LRU and FIFO. One example sequence is:
1 2 3 4 1 2 5 1 2 3 4 5
When this sequence is run using the provided program with k = 3, the miss counts are:
FIFO : 9
LRU : 10
OPTFF : 7
This means OPTFF has fewer misses than both FIFO and LRU for this sequence.
The reason this happens is because OPTFF knows the future requests, while FIFO and LRU only use past information. When the cache is full and something needs to be removed, OPTFF evicts the item that will be used farthest in the future or never used again. This is usually the best possible choice because it avoids removing something that will be needed soon. FIFO just removes the item that has been in the cache the longest, and LRU removes the item that has not been used recently. Because these algorithms do not know what requests are coming later, they sometimes remove items that will be needed again soon. That leads to extra misses, which is why OPTFF performs better on this sequence.


3. We want to show that OPTFF (Belady’s Farthest-in-Future algorithm) will never have more cache misses than any other offline algorithm A on the same request sequence. An offline algorithm means the algorithm already knows the full request sequence ahead of time.
Assume we have some offline algorithm A that may make different eviction choices than OPTFF. Consider a moment when the cache is full and a miss happens, so an item must be removed. OPTFF removes the item whose next use is farthest in the future, or an item that never appears again. Suppose algorithm A removes a different item. Let x be the item OPTFF removes and let y be the item removed by algorithm A.
Because of how OPTFF works, the next request for x must happen later than the next request for y, or maybe x is never used again. Now imagine we change algorithm A slightly so that at this step it removes x instead of y. After this change, the only difference between the two algorithms is that one keeps y in the cache while the other keeps x.
If we look ahead in the request sequence, the first time we see either x or y again must be a request for y, because y appears earlier. When that request happens, algorithm A will have a miss because it removed y, but the modified version will have a hit because it kept y. So replacing y with x does not increase the number of misses.
We can repeat this same idea every time algorithm A makes a different choice than OPTFF. Each time we adjust it so it matches OPTFF without increasing the number of misses. After repeating this enough times, algorithm A will behave exactly like OPTFF.
Because of this, OPTFF cannot have more misses than any other offline algorithm. This shows that OPTFF is optimal.


