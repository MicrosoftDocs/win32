---
title: Determining Growth Patterns Using Allocation Times
description: Determining Growth Patterns Using Allocation Times
ms.assetid: '0adf2ba2-181b-40a3-a978-933d0971b464'
---

# Determining Growth Patterns Using Allocation Times

Sorting this data by AllocTime as shown in **Allocation size and lifetime pattern that indicates an initial sizing issue** reveals a pattern of growth that indicates the initial size is too small. Undersized data structures lead to additional costs incurred when copying of previously inserted elements needed during array growth. Further, indications that the initial size is a problem can be discerned from the extremely short lifetime of the allocations, typically less than 30 microseconds, displayed in the Selection Lifetime column.

In the screen shot below the data suggests an exponential growth policy is used. For example in pseudocode: cbNew = cbOld + cbOld/2. This is a scalable pattern, reaching the final size with log(n) reallocs. A common problem is growing each allocation by a fixed size, which asymptotically has O(n^2) cpu time due to the overhead of copying buffers.

![screen shot of a table listing the allocation size and lifetime pattern that indicates an initial sizing issue](images/he-img19.png)

Selecting the ReallocAlloc column provides a means to separate the reallocations associated with data structure growth from new allocations.

 

 




