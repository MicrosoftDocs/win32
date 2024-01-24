---
description: The MacTypeToAddressType function converts a given MAC type to an address type.
ms.assetid: 7ede39a8-9a71-4c7a-8d2d-84a4ea2173bb
title: MacTypeToAddressType function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MacTypeToAddressType
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# MacTypeToAddressType function

The **MacTypeToAddressType** function converts a given MAC type to an address type.

## Syntax


```C++
DWORD WINAPI MacTypeToAddressType(
  _In_ DWORD MacType
);
```



## Parameters

<dl> <dt>

*MacType* \[in\]
</dt> <dd>

MAC type to be converted. Specify one of the following values:

MAC\_TYPE\_ETHERNET MAC\_TYPE\_TOKENRING MAC\_TYPE\_FDDI

</dd> </dl>

## Return value

If the function is successful, the return value is one of the following address types.

ADDRESS\_TYPE\_ETHERNET ADDRESS\_TYPE\_TOKENRING ADDRESS\_TYPE\_FDDI

If the function is unsuccessful, the MAC type is unknown, the return value is -1.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **MacTypeToAddressType** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




