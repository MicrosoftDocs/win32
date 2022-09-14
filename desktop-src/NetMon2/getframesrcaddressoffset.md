---
description: The GetFrameSrcAddressOffset function returns the offset of the frames source address.
ms.assetid: 1c5408d7-cf66-4887-93ee-134c0b8c5eff
title: GetFrameSrcAddressOffset function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameSrcAddressOffset
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameSrcAddressOffset function

The **GetFrameSrcAddressOffset** function returns the offset of the frame's source address.

## Syntax


```C++
DWORD WINAPI GetFrameSrcAddressOffset(
   HFRAME  hFrame,
   DWORD   AddressType,
   LPDWORD AddressLength
);
```



## Parameters

<dl> <dt>

*hFrame* 
</dt> <dd>

Handle to the frame.

</dd> <dt>

*AddressType* 
</dt> <dd>

Source address type. The parameter value can be one of the following:

-   ADDRESS\_TYPE\_ETHERNET
-   ADDRESS\_TYPE\_IP
-   ADDRESS\_TYPE\_IPX
-   ADDRESS\_TYPE\_TOKENRING
-   ADDRESS\_TYPE\_FDDI
-   ADDRESS\_TYPE\_XNS
-   ADDRESS\_TYPE\_VINES\_IP
-   ADDRESS\_TYPE\_ATM

</dd> <dt>

*AddressLength* 
</dt> <dd>

Pointer to a **DWORD**, which on return, contains the length of the address, in bytes.

</dd> </dl>

## Return value

If the function is successful, the return value is the offset to the source address.

If the function is unsuccessful, the return value is minus one (-1).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




