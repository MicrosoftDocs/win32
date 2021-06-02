---
description: Process_V0_TypeGroup1 class - This class is the event type class for process events. The following syntax is simplified from MOF code.
ms.assetid: fcf2897d-32b4-42b9-892c-f0106687d3c2
title: Process_V0_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Process_V0_TypeGroup1
- Process_V0_TypeGroup1.ProcessId
- Process_V0_TypeGroup1.ParentId
- Process_V0_TypeGroup1.UserSID
- Process_V0_TypeGroup1.ImageFileName
api_type: 
- NA
api_location: 
---

# Process\_V0\_TypeGroup1 class

This class is the event type class for process events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 2, 3, 4}, EventTypeName{"Start", "End", "DCStart", "DCEnd"}]
class Process_V0_TypeGroup1 : Process_V0
{
  uint32 ProcessId;
  uint32 ParentId;
  object UserSID;
  string ImageFileName;
};
```

## Members

The **Process\_V0\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Process\_V0\_TypeGroup1** class has these properties.

<dl> <dt>

ImageFileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), StringTermination("NullTerminated")
</dt> </dl>

Path to the executable file of the process.

</dd> <dt>

ParentId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Unique identifier of the process that creates a process. Process identifier numbers are reused, so they only identify a process for the lifetime of that process. It is possible that the process identified by ParentProcessId is terminated, so ParentProcessId may not refer to a running process. It is also possible that ParentProcessId incorrectly refers to a process that reuses a process identifier.

</dd> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Global process identifier that you can use to identify a process. The value is valid from the time a process is created until it is terminated.

</dd> <dt>

UserSID
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Extension("Sid")
</dt> </dl>

Security identifier (SID) for the user context under which the event happens.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Process\_V0**](process-v0.md)
</dt> </dl>

 

 




