---
description: Process_TypeGroup1 class - This class is the event type class for process events. The following syntax is simplified from MOF code.
ms.assetid: 4f06e1af-3f9a-4346-aa50-50f3ee82cd98
title: Process_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Process_TypeGroup1
- Process_TypeGroup1.UniqueProcessKey
- Process_TypeGroup1.ProcessId
- Process_TypeGroup1.ParentId
- Process_TypeGroup1.SessionId
- Process_TypeGroup1.ExitStatus
- Process_TypeGroup1.DirectoryTableBase
- Process_TypeGroup1.UserSID
- Process_TypeGroup1.ImageFileName
- Process_TypeGroup1.CommandLine
api_type: 
- NA
api_location: 
---

# Process\_TypeGroup1 class

This class is the event type class for process events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 2, 3, 4, 39}, EventTypeName{"Start", "End", "DCStart", "DCEnd", "Defunct"}]
class Process_TypeGroup1 : Process
{
  uint32 UniqueProcessKey;
  uint32 ProcessId;
  uint32 ParentId;
  uint32 SessionId;
  sint32 ExitStatus;
  uint32 DirectoryTableBase;
  object UserSID;
  string ImageFileName;
  string CommandLine;
};
```

## Members

The **Process\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Process\_TypeGroup1** class has these properties.

<dl> <dt>

CommandLine
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Full command line of the process.

</dd> <dt>

DirectoryTableBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Pointer
</dt> </dl>

The physical address of the page table of the process.

</dd> <dt>

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

Qualifiers: WmiDataId(8), StringTermination("NullTerminated")
</dt> </dl>

Path to the executable file of the process.

</dd> <dt>

ParentId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Format("x")
</dt> </dl>

Unique identifier of the process that creates this process. Process identifier numbers are reused, so they only identify a process for the lifetime of that process. It is possible that the process identified by ParentProcessId is terminated, so ParentProcessId may not refer to a running process. It is also possible that ParentProcessId incorrectly refers to a process that reuses a process identifier.

</dd> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

Global process identifier that you can use to identify a process. The value is valid from the time a process is created until it is terminated.

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

UniqueProcessKey
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

The address of the process object in the kernel.

</dd> <dt>

UserSID
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), Extension("Sid")
</dt> </dl>

Security identifier (SID) for the user context under which the event happens.

</dd> </dl>

## Remarks

The DCStart and DCEnd event types enumerate the process that are currently running, including idle and system process, at the time the kernel session starts and ends, respectively.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Process**](process.md)
</dt> </dl>

 

 




