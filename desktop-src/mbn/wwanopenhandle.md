---
Description: The WwanOpenHandle function opens a connection to the server.
ms.assetid: 9E412058-86DD-47C6-8195-9FFF6E32B523
title: WwanOpenHandle function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WwanOpenHandle
api_type: 
- DllExport
api_location: 
- WwApi.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-0.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-1.dll
---

# WwanOpenHandle function

The **WwanOpenHandle** function opens a connection to the server.

> [!Note]  
> The **WwanOpenHandle** function may be altered or unavailable for releases after Windows 8.1. Instead, use the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md).

 

## Syntax


```C++
DWORD WwanOpenHandle(
  _In_       DWORD  dwClientVersion,
  _Reserved_ VOID   *pReserved,
  _Out_      DWORD  *pdwNegotiatedVersion,
  _Out_      HANDLE *phClientHandle
);
```



## Parameters

<dl> <dt>

*dwClientVersion* \[in\]
</dt> <dd>

A 32-bit value that specifies the requested version of the wireless wide area network (WWAN) API.

</dd> <dt>

*pReserved* 
</dt> <dd>

Reserved

</dd> <dt>

*pdwNegotiatedVersion* \[out\]
</dt> <dd>

A pointer to a variable that receives a 32-bit value that specifies the negotiated version of the WWAN API.

</dd> <dt>

*phClientHandle* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle for the client to use in this session. This handle is used by other functions throughout the session.

</dd> </dl>

## Return value

Returns ERROR\_SUCCESS if the operation was successful; otherwise, an error value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| DLL<br/>                      | <dl> <dt>WwApi.dll</dt> </dl> |



 

 




