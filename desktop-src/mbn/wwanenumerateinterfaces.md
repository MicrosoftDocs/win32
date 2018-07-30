---
Description: The WwanEnumerateInterfaces function enumerates all of the mobile broadband interfaces currently enabled on the local computer.
ms.assetid: C51F2837-9654-4231-AD96-2EF20E090BD3
title: WwanEnumerateInterfaces function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WwanEnumerateInterfaces
api_type: 
- DllExport
api_location: 
- WwApi.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-1.dll
---

# WwanEnumerateInterfaces function

The **WwanEnumerateInterfaces** function enumerates all of the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md) currently enabled on the local computer.

> [!Note]  
> The **WwanEnumerateInterfaces** function may be altered or unavailable for releases after Windows 8.1. Instead, use the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md).

 

## Syntax


```C++
DWORD WwanEnumerateInterfaces(
  _In_     HANDLE                   hClientHandle,
  _In_opt_ DWORD                    *pdwReserved,
  _Out_    WWAN_INTERFACE_INFO_LIST **ppInterfaceList
);
```



## Parameters

<dl> <dt>

*hClientHandle* \[in\]
</dt> <dd>

The client's session handle that was obtained by a previous call to [**WwanOpenHandle**](wwanopenhandle.md).

</dd> <dt>

*pdwReserved* \[in, optional\]
</dt> <dd>

Reserved for future use. This pointer must be **NULL**.

</dd> <dt>

*ppInterfaceList* \[out\]
</dt> <dd>

A pointer to a memory block that receives an array of [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md) in a [**WWAN\_INTERFACE\_INFO\_LIST**](wwan-interface-info-list.md) structure.

The memory block for the [**WWAN\_INTERFACE\_INFO\_LIST**](wwan-interface-info-list.md) returned is allocated by **WwanEnumerateInterfaces** if the call succeeds.

</dd> </dl>

## Return value

Returns **ERROR\_SUCCESS** if the operation was successful; otherwise, an error value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| DLL<br/>                      | <dl> <dt>WwApi.dll</dt> </dl> |



 

 




