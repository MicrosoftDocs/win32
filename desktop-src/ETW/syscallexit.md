---
description: This class is the event type class for system call exit events. The following syntax is simplified from MOF code.
ms.assetid: bb9a2770-f37b-4055-8811-59ba117adf82
title: SysCallExit class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SysCallExit
- SysCallExit.SysCallNtStatus
api_type: 
- NA
api_location: 
---

# SysCallExit class

This class is the event type class for system call exit events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{52}, EventTypeName{"SysClExit"}]
class SysCallExit : PerfInfo
{
  uint32 SysCallNtStatus;
};
```

## Members

The **SysCallExit** class has these types of members:

-   [Properties](#properties)

### Properties

The **SysCallExit** class has these properties.

<dl> <dt>

**SysCallNtStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

Status code returned by the NT system call.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




