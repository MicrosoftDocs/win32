---
title: CmFree function
description: Frees a memory block allocated from a heap by the CmMalloc function.
ms.assetid: 962bfc33-a8b3-4598-aabf-94de26d1fdb5
keywords:
- CmFree function RAS
topic_type:
- apiref
api_name:
- CmFree
api_location:
- CmUtil.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CmFree function

The **CmFree** function frees a memory block allocated from a heap by the [**CmMalloc**](cmmalloc.md) function.

## Syntax


```C++
void* CmFree(
   void *pvPtr
);
```



## Parameters

<dl> <dt>

*pvPtr* 
</dt> <dd>

Previously allocated memory block to be freed.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **CmFree** function deallocates a memory block that was previously allocated by a call to the [**CmMalloc**](cmmalloc.md) function. The number of freed bytes is equivalent to the number of bytes requested when the block was allocated.

If *pvPtr* is **NULL**, the pointer is ignored and **CmFree** immediately returns.

Attempting to **CmFree** a pointer to a memory block that was not allocated by [**CmMalloc**](cmmalloc.md) may affect subsequent allocation requests and cause errors.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>CmUtil.dll</dt> </dl> |



## See also

<dl> <dt>

[**CmMalloc**](cmmalloc.md)
</dt> </dl>

 

 





