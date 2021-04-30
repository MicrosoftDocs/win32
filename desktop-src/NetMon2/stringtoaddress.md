---
description: The StringToAddress function converts a string to an address.
ms.assetid: b1ada88d-04bb-4869-87c6-99f5046356c5
title: StringToAddress function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StringToAddress
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# StringToAddress function

The **StringToAddress** function converts a string to an address.

## Syntax


```C++
LPBYTE WINAPI StringToAddress(
  _Out_ BYTE  *lpAddress,
  _In_  LPSTR string
);
```



## Parameters

<dl> <dt>

*lpAddress* \[out\]
</dt> <dd>

Pointer to the address the string is converted to.

</dd> <dt>

*string* \[in\]
</dt> <dd>

String that is converted to an address.

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



 

 




