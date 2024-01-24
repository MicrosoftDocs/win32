---
description: PageFault_TypeGroup1 class - This class is the event type class for page fault events. The following syntax is simplified from MOF code.
ms.assetid: 59cb1091-af21-4fe6-87b8-17a262cc4467
title: PageFault_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PageFault_TypeGroup1
- PageFault_TypeGroup1.VirtualAddress
- PageFault_TypeGroup1.ProgramCounter
api_type: 
- NA
api_location: 
---

# PageFault\_TypeGroup1 class

This class is the event type class for page fault events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10, 11, 12, 13, 14, 15}, EventTypeName{"TransitionFault", "DemandZeroFault", "CopyOnWrite", "GuardPageFault", "HardPageFault", "AccessViolation"}]
class PageFault_TypeGroup1 : PageFault_V2
{
  uint32 VirtualAddress;
  uint32 ProgramCounter;
};
```

## Members

The **PageFault\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **PageFault\_TypeGroup1** class has these properties.

<dl> <dt>

ProgramCounter
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Pointer to the current instruction being executed.

</dd> <dt>

VirtualAddress
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Virtual address of the page that caused the page fault.

</dd> </dl>

## Remarks

A page fault occurs when a page sought in the memory cache is not found there and must be retrieved from elsewhere in memory (a soft fault) or from disk (a hard fault).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**PageFault\_V2**](pagefault-v2.md)
</dt> </dl>

 

 




