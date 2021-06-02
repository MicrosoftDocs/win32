---
description: This class is the event type class for system call enter events. The following syntax is simplified from MOF code.
ms.assetid: 1ab32977-3f59-4816-b311-67142475dff2
title: SysCallEnter class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SysCallEnter
- SysCallEnter.SysCallAddress
api_type: 
- NA
api_location: 
---

# SysCallEnter class

This class is the event type class for system call enter events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{51}, EventTypeName{"SysClEnter"}]
class SysCallEnter : PerfInfo
{
  uint32 SysCallAddress;
};
```

## Members

The **SysCallEnter** class has these types of members:

-   [Properties](#properties)

### Properties

The **SysCallEnter** class has these properties.

<dl> <dt>

**SysCallAddress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Address of the NT function call that is being entered.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




