---
title: PFN\_CSP\_ALLOC function pointer
description: Points to a function that allocates a block of memory.
ms.assetid: d8f5878a-0ebd-40cf-afde-07f334f2ce40
keywords:
- PFN_CSP_ALLOC function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_ALLOC
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PFN\_CSP\_ALLOC function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_ALLOC** function pointer points to a function that allocates a block of memory.

## Syntax


```C++
typedef LPVOID ( WINAPI *PFN_CSP_ALLOC)(
  _In_ SIZE_T Size
);
```



## Parameters

<dl> <dt>

*Size* \[in\]
</dt> <dd>

The size, in bytes, of the memory block to be allocated.

</dd> </dl>

## Return value

If the function succeeds, the function returns a pointer to the allocated block of memory.

If the function fails, it returns **NULL**.

## Remarks

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

[**PFN\_CSP\_FREE**](pfn-csp-free.md)
</dt> <dt>

[**PFN\_CSP\_REALLOC**](pfn-csp-realloc.md)
</dt> </dl>

 

 





