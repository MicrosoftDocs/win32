---
description: This class is the event type class for process counter events. The following syntax is simplified from MOF code.
ms.assetid: 7f1fa1c4-a2ff-4a1c-ac9d-e922a13c99a1
title: Process_V2_TypeGroup2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Process_V2_TypeGroup2
- Process_V2_TypeGroup2.ProcessId
- Process_V2_TypeGroup2.PageFaultCount
- Process_V2_TypeGroup2.HandleCount
- Process_V2_TypeGroup2.Reserved
- Process_V2_TypeGroup2.PeakVirtualSize
- Process_V2_TypeGroup2.PeakWorkingSetSize
- Process_V2_TypeGroup2.PeakPagefileUsage
- Process_V2_TypeGroup2.QuotaPeakPagedPoolUsage
- Process_V2_TypeGroup2.QuotaPeakNonPagedPoolUsage
- Process_V2_TypeGroup2.VirtualSize
- Process_V2_TypeGroup2.WorkingSetSize
- Process_V2_TypeGroup2.PagefileUsage
- Process_V2_TypeGroup2.QuotaPagedPoolUsage
- Process_V2_TypeGroup2.QuotaNonPagedPoolUsage
- Process_V2_TypeGroup2.PrivatePageCount
api_type: 
- NA
api_location: 
---

# Process\_V2\_TypeGroup2 class

This class is the event type class for process counter events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{32, 33}, EventTypeName{"PerfCtr", PerfCtrRundown"}]
class Process_V2_TypeGroup2 : Process_V2
{
  uint32 ProcessId;
  uint32 PageFaultCount;
  uint32 HandleCount;
  uint32 Reserved;
  object PeakVirtualSize;
  object PeakWorkingSetSize;
  object PeakPagefileUsage;
  object QuotaPeakPagedPoolUsage;
  object QuotaPeakNonPagedPoolUsage;
  object VirtualSize;
  object WorkingSetSize;
  object PagefileUsage;
  object QuotaPagedPoolUsage;
  object QuotaNonPagedPoolUsage;
  object PrivatePageCount;
};
```

## Members

The **Process\_V2\_TypeGroup2** class has these types of members:

-   [Properties](#properties)

### Properties

The **Process\_V2\_TypeGroup2** class has these properties.

<dl> <dt>

**HandleCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Count of used handles.

</dd> <dt>

**PageFaultCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Count of page faults.

</dd> <dt>

**PagefileUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(12), Extension("SizeT")
</dt> </dl>

Current page file usage.

</dd> <dt>

**PeakPagefileUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), Extension("SizeT")
</dt> </dl>

Largest page file size used.

</dd> <dt>

**PeakVirtualSize**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Extension("SizeT")
</dt> </dl>

Largest virtual page size used.

</dd> <dt>

**PeakWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Extension("SizeT")
</dt> </dl>

Largest working set size used.

</dd> <dt>

**PrivatePageCount**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(15), Extension("SizeT")
</dt> </dl>

Current private physical page count.

</dd> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

Global process identifier that you can use to identify a process. The value is valid from the time a process is created until it is terminated.

</dd> <dt>

**QuotaNonPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(14), Extension("SizeT")
</dt> </dl>

Current committed non-paged memory usage.

</dd> <dt>

**QuotaPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(13), Extension("SizeT")
</dt> </dl>

Current committed paged memory usage.

</dd> <dt>

**QuotaPeakNonPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9), Extension("SizeT")
</dt> </dl>

Largest committed non-paged memory used.

</dd> <dt>

**QuotaPeakPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8), Extension("SizeT")
</dt> </dl>

Largest committed paged memory used.

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Reserved.

</dd> <dt>

**VirtualSize**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10), Extension("SizeT")
</dt> </dl>

Current virtual page size.

</dd> <dt>

**WorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(11), Extension("SizeT")
</dt> </dl>

Current working set size.

</dd> </dl>

## Remarks

These events are logged when the process ends. The event indicates how a process handled memory usage.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Process\_V2**](process-v2.md)
</dt> </dl>

 

 




