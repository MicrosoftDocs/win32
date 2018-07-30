---
Description: The WwanFreeMemory function frees a block of memory.
ms.assetid: 4CF45F7F-3FEC-4AB9-9A4E-FE1151837B79
title: WwanFreeMemory function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WwanFreeMemory
api_type: 
- DllExport
api_location: 
- wwapi.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-0.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-1.dll
---

# WwanFreeMemory function

The **WwanFreeMemory** function frees a block of memory.

> [!Note]  
> The **WwanFreeMemory** function may be altered or unavailable for releases after Windows 8.1. Instead, use the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md).

 

## Syntax


```C++
VOID WwanFreeMemory(
  _In_ LPVOID pMem
);
```



## Parameters

<dl> <dt>

*pMem* \[in\]
</dt> <dd>

A pointer to the memory block to free.

</dd> </dl>

## Return value

None

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| DLL<br/>                      | <dl> <dt>Wwapi.dll</dt> </dl> |



 

 




