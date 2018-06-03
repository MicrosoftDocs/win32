---
title: PFN\_CSP\_REALLOC function pointer
description: Points to a function that changes the size of a previously allocated block of memory. The existing contents of the memory block are copied to the reallocated block.
ms.assetid: 6239e313-f62c-4375-96c7-eca0763b343f
keywords:
- PFN_CSP_REALLOC function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_REALLOC
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PFN\_CSP\_REALLOC function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_REALLOC** function pointer points to a function that changes the size of a previously allocated block of memory. The existing contents of the memory block are copied to the reallocated block.

## Syntax


```C++
typedef LPVOID ( WINAPI *PFN_CSP_REALLOC)(
  _In_ LPVOID Address,
  _In_ SIZE_T Size
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

A pointer to the address of the memory block to reallocate.

</dd> <dt>

*Size* \[in\]
</dt> <dd>

The size, in bytes, of the reallocated memory block.

</dd> </dl>

## Return value

If the function succeeds, the function returns a pointer to the reallocated block of memory.

If the function fails, it returns **NULL**.

## Remarks

The existing contents of the memory block are copied to the reallocated block. If the size of the reallocated block of memory is smaller than the size of the data to be copied, the data is truncated to the size of the reallocated block of memory.

This function pointer is passed to a card module in a [**CARD\_DATA**](card-data.md) structure when the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) calls the [**CardAcquireContext**](cardacquirecontext.md) function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md)
</dt> <dt>

[**PFN\_CSP\_FREE**](pfn-csp-free.md)
</dt> </dl>

 

 





