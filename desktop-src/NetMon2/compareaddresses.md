---
description: The CompareAddresses function compares two addresses, indicating that one of the addresses is greater than, less than, or equal to the other address.
ms.assetid: 76ff37d2-714f-4bac-adcc-eab78c8f25d3
title: CompareAddresses function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CompareAddresses
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CompareAddresses function

The **CompareAddresses** function compares two addresses, indicating that one of the addresses is greater than, less than, or equal to the other address.

## Syntax


```C++
int WINAPI CompareAddresses(
  _In_ LPADDRESS lpAddress1,
  _In_ LPADDRESS lpAddress2
);
```



## Parameters

<dl> <dt>

*lpAddress1* \[in\]
</dt> <dd>

Pointer to the first address.

</dd> <dt>

*lpAddress2* \[in\]
</dt> <dd>

Pointer to the second address.

</dd> </dl>

## Return value

If the addresses are the same, the function returns zero.

If the *lpAddress1* parameter specifies an address that is less than the address that the *lpAddress2* parameter specifies, the return value is a negative number.

If the *lpAddress1* parameter specifies an address that is greater than the address that the *lpAddress2* parameter specifies, the return value is a positive number.

## Remarks

An address that is less than another address indicates a previous frame. An address that is greater than another address indicates a later frame.

Network Monitor provides two other functions, [CompareFrameDestAddress](compareframedestaddress.md) and [CompareFrameSourceAddress](compareframesourceaddress.md), which you can use to compare addresses. The **CompareFrameDestAddress** function compares a given address to the frame's destination address, and the **CompareFrameSourceAddress** function compares a given address to the frame's source address.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[CompareFrameDestAddress](compareframedestaddress.md)
</dt> <dt>

[CompareFrameSourceAddress](compareframesourceaddress.md)
</dt> </dl>

 

 




