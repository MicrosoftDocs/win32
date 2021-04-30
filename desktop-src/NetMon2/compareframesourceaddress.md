---
description: The CompareFrameSourceAddress function compares an address to the source address of a frame.
ms.assetid: 7221c0cc-d6c1-4ec9-bf11-3ba1fefb35da
title: CompareFrameSourceAddress function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CompareFrameSourceAddress
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CompareFrameSourceAddress function

The **CompareFrameSourceAddress** function compares an address to the source address of a frame.

## Syntax


```C++
BOOL WINAPI CompareFrameSourceAddress(
  _In_ HFRAME    hFrame,
  _In_ LPADDRESS lpAddress
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to a frame.

</dd> <dt>

*lpAddress* \[in\]
</dt> <dd>

Pointer to an address.

</dd> </dl>

## Return value

If the addresses are the same, the return value is **TRUE**.

If the addresses are not the same, the return value is **FALSE**.

## Remarks

For the **CompareFrameSourceAddress** function to succeed, the source address type must match the type of address specified in the *lpAddress* parameter.

Network Monitor provides two other functions for comparing addresses: [CompareFrameDestAddress](compareframedestaddress.md) and [CompareAddresses](compareaddresses.md). The **CompareFrameDestAddress** function compares a given address to the frame's destination address, and the **CompareAddress** function compares two given addresses.

[*Experts*](e.md) and [*parsers*](p.md) can call the **CompareFrameSourceAddress** function.

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

[CompareAddresses](compareaddresses.md)
</dt> <dt>

[CompareFrameDestAddress](compareframedestaddress.md)
</dt> </dl>

 

 




