---
description: The CompareFrameDestAddress function compares an address to the destination address of a frame.
ms.assetid: 739b3b9f-f989-459d-ac3e-6be7769adc06
title: CompareFrameDestAddress function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CompareFrameDestAddress
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CompareFrameDestAddress function

The **CompareFrameDestAddress** function compares an address to the destination address of a frame.

## Syntax


```C++
BOOL WINAPI CompareFrameDestAddress(
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

For the **CompareFrameDestAddress** function to return successfully, the destination address type must match the type of address specified in the *lpAddress* parameter.

Network Monitor provides two other functions, [CompareFrameSourceAddress](compareframesourceaddress.md) and [CompareAddresses](compareaddresses.md), which you can use to compare addresses. The **CompareFrameSourceAddress** function compares a given address to the frame's source address, and the **CompareAddress** function compares two given addresses.

[*Experts*](e.md) and [*parsers*](p.md) can call the **CompareFrameDestAddress** function.

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

[CompareFrameSourceAddress](compareframesourceaddress.md)
</dt> </dl>

 

 




