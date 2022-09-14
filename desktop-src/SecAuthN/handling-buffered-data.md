---
description: Several of the network provider functions take the address and size of a buffer into which the function places a variable-sized data structure.
ms.assetid: 0029a04d-6cf2-40e1-ae1d-4c349a379ad7
title: Handling Buffered Data
ms.topic: article
ms.date: 05/31/2018
---

# Handling Buffered Data

Several of the network provider functions take the address and size of a buffer into which the function places a variable-sized data structure.

In each case, the mechanism used is the same. The caller allocates a buffer and passes its address to the function. It also passes the address of a **DWORD** that specifies the size of the buffer, in bytes.

The function then copies as much of the requested data structure as it can into the buffer. If all of the data fits into the buffer, the function returns WN\_SUCCESS. If the data does not fit into the buffer, the data may be left incomplete, and the function sets the WN\_MORE\_DATA error. In either case, the **DWORD** indicating the size of the buffer is set to the number of bytes actually required by the data structure. This way, if the buffer passed in was too small and the function failed, the caller may allocate a new buffer of the required size and call the function again.

When the data structures returned include variable-length strings, the individual data structures typically contain pointers to these strings. The strings themselves should also be placed within the buffer. However, it is important to place them at the end of the buffer. Otherwise, they will make indexing to the Nth structure impossible. In other words, all structures are located contiguously at the beginning of the buffer. Pointers to strings or variable length data must be actual pointers, not offsets into the buffer.

When a buffer is used to pass in and return data that consists only of strings, the **DWORD** specifying the size of the buffer should be set to the total number of characters that will fit in these strings, not to the number of bytes.

 

 



