---
description: PageFault_TransitionFault class - This class is the event type class for page fault events. The following syntax is simplified from MOF code.
ms.assetid: cc2b7a93-6974-4872-98f3-d6cb81861ae5
title: PageFault_TransitionFault class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PageFault_TransitionFault
- PageFault_TransitionFault.VirtualAddress
- PageFault_TransitionFault.ProgramCounter
api_type: 
- NA
api_location: 
---

# PageFault\_TransitionFault class

This class is the event type class for page fault events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10, 11, 12, 13, 14}, EventTypeName{"TransitionFault", "DemandZeroFault", "CopyOnWrite", "GuardPageFault", "HardPageFault"}]
class PageFault_TransitionFault : PageFault_V2
{
  uint32 VirtualAddress;
  uint32 ProgramCounter;
};
```

## Members

The **PageFault\_TransitionFault** class has these types of members:

-   [Properties](#properties)

### Properties

The **PageFault\_TransitionFault** class has these properties.

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

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**PageFault\_V2**](pagefault-v2.md)
</dt> </dl>

 

 




