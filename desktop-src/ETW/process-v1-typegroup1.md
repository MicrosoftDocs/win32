---
description: Process_V1_TypeGroup1 class - This class is the event type class for process events. The following syntax is simplified from MOF code.
ms.assetid: b114d7fd-c308-4f21-8f1a-ab27dc93abc5
title: Process_V1_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Process_V1_TypeGroup1
- Process_V1_TypeGroup1.PageDirectoryBase
- Process_V1_TypeGroup1.ProcessId
- Process_V1_TypeGroup1.ParentId
- Process_V1_TypeGroup1.SessionId
- Process_V1_TypeGroup1.ExitStatus
- Process_V1_TypeGroup1.UserSID
- Process_V1_TypeGroup1.ImageFileName
api_type: 
- NA
api_location: 
---

# Process\_V1\_TypeGroup1 class

This class is the event type class for process events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 2, 3, 4}, EventTypeName{"Start", "End", "DCStart", "DCEnd"}]
class Process_V1_TypeGroup1 : Process_V1
{
  uint32 PageDirectoryBase;
  uint32 ProcessId;
  uint32 ParentId;
  uint32 SessionId;
  sint32 ExitStatus;
  object UserSID;
  string ImageFileName;
};
```

## Members

The **Process\_V1\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Process\_V1\_TypeGroup1** class has these properties.

<dl> <dt>

ExitStatus
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Exit status of the stopped process.

</dd> <dt>

ImageFileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), StringTermination("NullTerminated")
</dt> </dl>

Path to the executable file of the process.

</dd> <dt>

PageDirectoryBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Reserved.

</dd> <dt>

ParentId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Unique identifier of the process that creates this process. Process identifier numbers are reused, so they only identify a process for the lifetime of that process. It is possible that the process identified by ParentProcessId is terminated, so ParentProcessId may not refer to a running process. It is also possible that ParentProcessId incorrectly refers to a process that reuses a process identifier.

**Windows Server 2003:** Includes the Format("x") qualifier.

</dd> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Global process identifier that you can use to identify a process. The value is valid from the time a process is created until it is terminated.

**Windows Server 2003:** Includes the Format("x") qualifier.

</dd> <dt>

SessionId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Unique identifier that an operating system generates when it creates a new session. A session spans a period of time from log on until log off from a specific system.

</dd> <dt>

UserSID
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Extension("Sid")
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

[**Process\_V1**](process.md)
</dt> <dt>

[**Process\_V1**](process-v1.md)
</dt> </dl>

 

 




