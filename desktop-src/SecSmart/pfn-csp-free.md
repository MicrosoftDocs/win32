---
title: PFN\_CSP\_FREE function pointer
description: Points to a function that frees a block of memory.
ms.assetid: fcf8130c-3e21-4fbe-b4db-070167d71fc0
keywords:
- PFN_CSP_FREE function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_FREE
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

# PFN\_CSP\_FREE function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_FREE** function pointer points to a function that frees a block of memory.

## Syntax


```C++
typedef VOID ( WINAPI *PFN_CSP_FREE)(
  _In_ LPVOID Address
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

A pointer to the address of the memory block to free.

</dd> </dl>

## Return value

This function pointer does not return a value.

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

[**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md)
</dt> <dt>

[**PFN\_CSP\_REALLOC**](pfn-csp-realloc.md)
</dt> </dl>

 

 





