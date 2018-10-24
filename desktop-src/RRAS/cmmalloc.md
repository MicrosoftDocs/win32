---
title: CmMalloc function
description: Allocates a block of memory from a heap.
ms.assetid: 0a03b6e9-417d-4b31-9ddf-83534557d93b
keywords:
- CmMalloc function RAS
topic_type:
- apiref
api_name:
- CmMalloc
api_location:
- CmUtil.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CmMalloc function

The **CmMalloc** function allocates a block of memory from a heap.

## Syntax


```C++
void* CmMalloc(
   size_t nBytes
);
```



## Parameters

<dl> <dt>

*nBytes* 
</dt> <dd>

Number of bytes to allocate.

</dd> </dl>

## Return value

The **CmMalloc** function returns a void pointer to the allocated space or **NULL** if there is insufficient memory available or the function fails. If size is 0, a zero-length item is allocated in the heap and a valid pointer to it is returned.

To return a pointer to a type other than void, use a type cast on the return value. The storage space pointed to by the return value is guaranteed to be suitably aligned for storage of any type of object.

## Remarks

The **CmMalloc** function allocates a memory block of at least *nBytes* bytes. The block may be larger than *nBytes* bytes due to space required for alignment and maintenance information. **CmMalloc** initializes the allocated memory to zero.

The return from this function should always be checked before use, even if the amount of memory requested is small.

Memory allocated by this function is not movable. The address returned by **CmMalloc** is valid until the memory block is freed. The memory block does not need to be locked. Because the system cannot compact a private heap, it can become fragmented

To free a block of memory allocated by **CmMalloc**, use the [**CmFree**](cmfree.md) function.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>CmUtil.dll</dt> </dl> |



## See also

<dl> <dt>

[**CmFree**](cmfree.md)
</dt> </dl>

 

 





