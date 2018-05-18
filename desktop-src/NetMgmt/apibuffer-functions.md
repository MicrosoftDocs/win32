---
title: ApiBuffer Functions
description: The network management ApiBuffer functions are used to manage memory allocation used by an application with network management functions.
ms.assetid: 'bf2fe8aa-dda6-4f6b-9c52-d7a96b96da18'
---

# ApiBuffer Functions

The network management ApiBuffer functions are used to manage memory allocation used by an application with network management functions. However, in general, for other memory used by an application you should use the [memory management functions](https://msdn.microsoft.com/library/windows/desktop/aa366781) instead of these ApiBuffer functions.

The ApiBuffer functions are listed following.



| Function                                                 | Description                                                                                                               |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**NetApiBufferAllocate**](netapibufferallocate.md)     | Allocates memory from the heap. Call this function when you require compatibility with the **NetApiBufferFree** function. |
| [**NetApiBufferFree**](netapibufferfree.md)             | Frees memory allocated by the **NetApiBufferAllocate** function and other network management functions.                   |
| [**NetApiBufferReallocate**](netapibufferreallocate.md) | Changes the size of a buffer allocated by a call to the **NetApiBufferAllocate** function.                                |
| [**NetApiBufferSize**](netapibuffersize.md)             | Returns the size, in bytes, of a buffer allocated by a call to the **NetApiBufferAllocate** function.                     |



 

For remotable functions that return information to the caller, the RPC run-time library allocates the buffer containing the return information. When the caller has finished processing the information, it must call the [**NetApiBufferFree**](netapibufferfree.md) function to free the allocated buffer.

 

 




