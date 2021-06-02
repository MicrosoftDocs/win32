---
description: The GetFrameDstAddressOffset function returns the offset to the destination address of a given frame.
ms.assetid: 8922d7d0-1a23-47ac-886b-fcc0bcaa6ba7
title: GetFrameDstAddressOffset function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameDstAddressOffset
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameDstAddressOffset function

The **GetFrameDstAddressOffset** function returns the offset to the destination address of a given frame.

## Syntax


```C++
DWORD WINAPI GetFrameDstAddressOffset(
  _In_ HFRAME  hFrame,
  _In_ DWORD   AddressType,
  _In_ LPDWORD AddressLength
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

Type of the destination address. Specify one of the following values:

ADDRESS\_TYPE\_ETHERNET ADDRESS\_TYPE\_IP ADDRESS\_TYPE\_IPX ADDRESS\_TYPE\_TOKENRING ADDRESS\_TYPE\_FDDI ADDRESS\_TYPE\_XNS ADDRESS\_TYPE\_VINES\_IP ADDRESS\_TYPE\_ATM.

</dd> <dt>

*AddressLength* \[in\]
</dt> <dd>

Length of the destination address, in bytes.

</dd> </dl>

## Return value

If the function is successful, the return value is the offset (measured in bytes) to the requested address type.

If the function is unsuccessful, the return value is minus one (-1).

## Remarks

If the *AddressType* parameter is set to ADDRESS\_TYPE\_ETHERNET, the return value of the **GetFrameDstAddressOffset** function is always zero. The offset of an Ethernet address is always zero.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameDstAddressOffset** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




