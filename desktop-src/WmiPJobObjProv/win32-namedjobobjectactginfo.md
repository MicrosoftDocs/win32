---
Description: The Win32\_NamedJobObjectActgInfo WMI class class represents the I/O accounting information for a job object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e974a16-e4f1-4183-98de-aa949363916b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_NamedJobObjectActgInfo class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_NamedJobObjectActgInfo class

The **Win32\_NamedJobObjectActgInfo** [WMI class](https://msdn.microsoft.com/library/aa393244) class represents the I/O accounting information for a job object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("NamedJobObjectActgInfoProv"), UUID("{486F2A44-D0BF-46c1-9543-68EF5D37F1F9}"), AMENDMENT]
class Win32_NamedJobObjectActgInfo : CIM_StatisticalInformation
{
  string Caption;
  string Description;
  uint32 ActiveProcesses;
  string Name;
  uint64 OtherOperationCount;
  uint64 OtherTransferCount;
  uint32 PeakJobMemoryUsed;
  uint32 PeakProcessMemoryUsed;
  uint64 ReadOperationCount;
  uint64 ReadTransferCount;
  uint64 ThisPeriodTotalKernelTime;
  uint64 ThisPeriodTotalUserTime;
  uint64 TotalKernelTime;
  uint32 TotalPageFaultCount;
  uint32 TotalProcesses;
  uint32 TotalTerminatedProcesses;
  uint64 TotalUserTime;
  uint64 WriteOperationCount;
  uint64 WriteTransferCount;
};
```

## Members

The **Win32\_NamedJobObjectActgInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectActgInfo** class has these properties.

<dl> <dt>

**ActiveProcesses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of processes associated with a job. When a process is associated with a job, but the association fails because of a limit violation, the value is temporarily incremented. When the terminated process exits and all references to the process are released, the value is decremented.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description for the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

Label by which the statistic or metric is known. When subclassed, this property can be overridden to be a key property. This property overrides the **Name** property in [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**OtherOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of I/O operations performed, other than read and write operations, by all of the processes that have been associated with the job including all of the processes currently associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**OtherTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes transferred during operations, other than read and write, by all of the processes that have been associated with the job including all of the processes currently associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**PeakJobMemoryUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("kilobytes")
</dt> </dl>

Peak memory in kilobyte usage of all of the processes associated with the job.

</dd> <dt>

**PeakProcessMemoryUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("kilobytes")
</dt> </dl>

The most process memory in kilobytes used by any process ever associated with the job.

</dd> <dt>

**ReadOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of read operations performed by all of the processes that have ever been associated with the job, in addition to all of the processes currently associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**ReadTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes read by all of the processes that have been associated with the job including all of the processes currently associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**ThisPeriodTotalKernelTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Total amount of kernel-mode execution time, in 100 nanosecond units, for all active processes associated with the job (and all terminated processes no longer associated with the job) after the last call that set a per-job kernel-mode time limit. This property is set to 0 (zero) when a job is created, and each time a per-job kernel-mode time limit is established.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**ThisPeriodTotalUserTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Total amount of user-mode execution time, in 100 nanosecond units, for all active processes associated with the job (and all terminated processes no longer associated with the job) since the last call that set a per-job user-mode time limit. This property is set to 0 (zero) when a job is created, and each time a per-job user-mode time limit is established.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**TotalKernelTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Total amount of kernel-mode execution time, in 100 nanosecond units, for all active processes associated with the job, as well as all terminated processes no longer associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**TotalPageFaultCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of page faults encountered by all of the active processes associated with the job, as well as all of the terminated processes no longer associated with the job.

</dd> <dt>

**TotalProcesses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of processes associated with the job during its lifetime, including those that are terminated. For example, when a process is associated with a job, but the association fails because of a limit violation, the value is incremented.

</dd> <dt>

**TotalTerminatedProcesses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of processes terminated because of a limit violation.

</dd> <dt>

**TotalUserTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Total amount of user-mode execution time, in 100 nanosecond units, for all active processes associated with a job, and all of the terminated processes not associated with a job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**WriteOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of write operations performed by all processes that have been associated with a job, and all of the processes currently associated with the job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**WriteTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes written by all of the processes that have been associated with a job, and all processes currently associated with a job.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectActgInfo** class is derived from the [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




