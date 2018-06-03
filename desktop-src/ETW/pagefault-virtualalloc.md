---
Description: This class is the event type class for virtual allocation events. The following syntax is simplified from MOF code.
ms.assetid: 037d33e0-da94-4834-bc02-814c1cae1d8d
title: PageFault\_VirtualAlloc class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PageFault\_VirtualAlloc class

This class is the event type class for virtual allocation events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{98, 99}, EventTypeName{"VirtualAlloc", "VirtualFree"}]
class PageFault_VirtualAlloc : PageFault_V2
{
  uint32 BaseAddress;
  object RegionSize;
  uint32 ProcessId;
  uint32 Flags;
};
```

## Members

The **PageFault\_VirtualAlloc** class has these types of members:

-   [Properties](#properties)

### Properties

The **PageFault\_VirtualAlloc** class has these properties.

<dl> <dt>

**BaseAddress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

The starting address at which memory was allocated or freed.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Format("x")
</dt> </dl>

The type of memory allocation that was performed. For possible values, see the *flAllocationType* parameter of the [**VirtualAllocEx**](https://msdn.microsoft.com/windows/desktop/ff0b6b79-40f5-499c-b797-b66797654164) function.

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

The process that owned the memory (can be different from the thread that performed the allocation).

</dd> <dt>

**RegionSize**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Extension("SizeT")
</dt> </dl>

The size, in bytes, of the memory that was allocated or freed.

</dd> </dl>

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**PageFault\_V2**](pagefault-v2.md)
</dt> </dl>

 

 




