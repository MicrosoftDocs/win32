---
description: The AddressToString function converts an address into a string.
ms.assetid: 999a6142-1423-4006-a489-63895dd19ce3
title: AddressToString function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddressToString
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# AddressToString function

The **AddressToString** function converts an address into a string.

## Syntax


```C++
LPSTR WINAPI AddressToString(
  _Out_ LPSTR string,
  _In_  BYTE  *lpAddress
);
```



## Parameters

<dl> <dt>

*string* \[out\]
</dt> <dd>

String that the address is converted to.

</dd> <dt>

*lpAddress* \[in\]
</dt> <dd>

The address that is printed.

</dd> </dl>

## Return value

The return value is a pointer to the converted string.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




