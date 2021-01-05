---
description: Copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks.
ms.assetid: D374F14D-24C7-4771-AD40-3AC37E7A2D2F
title: RtlMoveMemory function (Wdm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlMoveMemory
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlMoveMemory function

Copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks.

## Syntax


```C++
VOID RtlMoveMemory(
  _Out_       VOID UNALIGNED *Destination,
  _In_  const VOID UNALIGNED *Source,
  _In_        SIZE_T         Length
);
```



## Parameters

<dl> <dt>

*Destination* \[out\]
</dt> <dd>

A pointer to the destination memory block to copy the bytes to.

</dd> <dt>

*Source* \[in\]
</dt> <dd>

A pointer to the source memory block to copy the bytes from.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

The number of bytes to copy from the source to the destination.

</dd> </dl>

## Return value

None

## Remarks

The source memory block, which is defined by *Source* and *Length*, can overlap the destination memory block, which is defined by *Destination* and *Length*.

The [**RtlCopyMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopymemory) routine runs faster than **RtlMoveMemory**, but **RtlCopyMemory** requires that the source and destination memory blocks do not overlap.

Callers of **RtlMoveMemory** can be running at any IRQL if the source and destination memory blocks are in nonpaged system memory. Otherwise, the caller must be running at IRQL <= APC\_LEVEL.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| Header<br/>                   | <dl> <dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt> </dl>                   |
| Library<br/>                  | <dl> <dt>Ntdll.lib</dt> </dl>                                                    |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**RtlCopyMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopymemory)
</dt> </dl>

 

 
