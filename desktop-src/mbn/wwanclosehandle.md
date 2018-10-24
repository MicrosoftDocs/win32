---
Description: The WwanCloseHandle function closes a handle to the mobile broadband service.
ms.assetid: 671F7A5F-B67B-4C5A-8422-AC07D7F3F555
title: WwanCloseHandle function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WwanCloseHandle
api_type: 
- DllExport
api_location: 
- wwapi.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-0.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-1.dll
---

# WwanCloseHandle function

The **WwanCloseHandle** function closes a handle to the mobile broadband service.

> [!Note]  
> The **WwanCloseHandle** function may be altered or unavailable for releases after Windows 8.1. Instead, use the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md).

 

## Syntax


```C++
DWORD WwanCloseHandle(
  _In_       HANDLE hClientHandle,
  _Reserved_ VOID   *pReserved
);
```



## Parameters

<dl> <dt>

*hClientHandle* \[in\]
</dt> <dd>

A handle to the mobile broadband service that [**WwanOpenHandle**](wwanopenhandle.md) returned.

</dd> <dt>

*pReserved* 
</dt> <dd>

Reserved

</dd> </dl>

## Return value

Returns **ERROR\_SUCCESS** if the operation was successful; otherwise, an error value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| DLL<br/>                      | <dl> <dt>Wwapi.dll</dt> </dl> |



 

 




