---
Description: The Win32\_NamedJobObjectLimitSetting WMI class represents the limit settings for a job object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b70a2c27-e4a2-458d-949f-f7e957289a94
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_NamedJobObjectLimitSetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_NamedJobObjectLimitSetting class

The **Win32\_NamedJobObjectLimitSetting** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the limit settings for a job object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("NamedJobObjectLimitSettingProv"), UUID("{F2D96E32-2A34-475b-878D-B0AE7657519F}"), AMENDMENT]
class Win32_NamedJobObjectLimitSetting : CIM_Setting
{
  string Caption;
  string Description;
  uint32 ActiveProcessLimit;
  uint32 Affinity;
  uint32 JobMemoryLimit;
  uint32 LimitFlags;
  uint32 MaximumWorkingSetSize;
  uint32 MinimumWorkingSetSize;
  uint64 PerJobUserTimeLimit;
  uint64 PerProcessUserTimeLimit;
  uint32 PriorityClass;
  uint32 ProcessMemoryLimit;
  uint32 SchedulingClass;
  string SettingID;
};
```

## Members

The **Win32\_NamedJobObjectLimitSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectLimitSetting** class has these properties.

<dl> <dt>

**ActiveProcessLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Active process limit for a job. If associating a process with a job causes the active process count to exceed the limit, the process is terminated and the association fails. This property is ignored unless the **LimitFlags** property specifies the Active Process Limit value.

</dd> <dt>

**Affinity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Processor affinity for all of the processes associated with a job. The affinity of each thread is set to this value, but threads are free to set the affinity subsequently, when it is a subset of the specified affinity mask. Processes cannot set an affinity mask. This property is ignored unless **LimitFlags** specifies the Limit Affinity value.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**JobMemoryLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Per-job memory limit in kilobytes. This property is ignored unless **LimitFlags** specifies the Limit Job Memory value.

</dd> <dt>

**LimitFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitValues**](https://msdn.microsoft.com/library/aa393650) ("Limit Working Set", "Limit Process Time", "Limit Job Time", "Active Process Limit", "Limit Affinity", "Limit Priority Class", "Limit Preserve Job Time", "Limit Scheduling Class", "Limit Process Memory", "Limit Job Memory", "Limit Die On Unhandled Exception", "Limit Breakaway OK", "Silent Breakaway OK")
</dt> </dl>

Bitmap that represents the job limits. One or more of the limits can be in effect at the same time.

<dt>

1 (0x1)
</dt> <dd>

Limit Working Set

Causes all of the processes associated with the job to use the same minimum and maximum working set sizes.

</dd> <dt>

2 (0x2)
</dt> <dd>

Limit Process Time

Establishes a user-mode execution time limit for each currently active process and all of the future processes associated with a job.

</dd> <dt>

4 (0x4)
</dt> <dd>

Limit Job Time

Establishes a user-mode execution time limit for the job. This flag cannot be used with Limit Preserve Job Time.

</dd> <dt>

8 (0x8)
</dt> <dd>

Active Process Limit

Establishes a maximum number of simultaneously active processes associated with the job.

</dd> <dt>

16 (0x10)
</dt> <dd>

Limit Affinity

Causes all of the processes associated with the job to use the same processor affinity.

</dd> <dt>

32 (0x20)
</dt> <dd>

Limit Priority Class

Causes all of the processes associated with a job to use the same priority class.

</dd> <dt>

64 (0x40)
</dt> <dd>

Limit Preserve Job Time

Preserves any job time limits you set previously. When this flag is set, you can establish a per-job time limit one time, then alter other limits in subsequent calls. This flag cannot be used with Limit Job Time.

</dd> <dt>

128 (0x80)
</dt> <dd>

Limit Scheduling Class

Causes all of the processes in a job to use the same scheduling class.

</dd> <dt>

256 (0x100)
</dt> <dd>

Limit Process Memory

Causes all of the processes associated with a job to limit their committed memory. When a process attempts to commit memory that exceeds the perprocess limit, it fails. If the job object is associated with a completion port, a **JOB\_OBJECT\_MSG\_PROCESS\_MEMORY\_LIMIT** message is sent to the completion port.

</dd> <dt>

512 (0x200)
</dt> <dd>

Limit Job Memory

Causes all of the processes associated with a job to limit the job-wide sum of the committed memory. When a process attempts to commit memory that exceeds the job-wide limit, it fails. If the job object is associated with a completion port, a **JOB\_OBJECT\_MSG\_JOB\_MEMORY\_LIMIT** message is sent to the completion port.

</dd> <dt>

1024 (0x400)
</dt> <dd>

Limit Die On Unhandled Exception

Forces a call to the [**SetErrorMode**](https://msdn.microsoft.com/library/windows/desktop/ms680621) function with the **SEM\_NOGPFAULTERRORBOX** flag for each process associated with a job.

</dd> <dt>

2048 (0x800)
</dt> <dd>

Limit Breakaway OK

If any of the process associated with a job creates a child process using the **CREATE\_BREAKAWAY\_FROM\_JOB** flag while this limit is in effect, the child process is not associated with the job.

</dd> <dt>

4096 (0x1000)
</dt> <dd>

Silent Breakaway OK

Allows any process associated with a job to create child processes that are not associated with the job.

</dd> </dl>

</dd> <dt>

**MaximumWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum working set size for all of the processes associated with a job. This property is ignored unless **LimitFlags** specifies the Limit Working Set value.

</dd> <dt>

**MinimumWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum working set size for all of the processes associated with a job. This property is ignored unless **LimitFlags** specifies the Limit Working Set value.

</dd> <dt>

**PerJobUserTimeLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Per-job user-mode execution time limit, in 100 nanosecond units. The system adds the current time of the processes associated with the job to this limit. For example, if you set this limit to 1 minute, and the job has a process that has accumulated 5 minutes of user mode time, the limit actually enforced is 6 minutes.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**PerProcessUserTimeLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("100 nanoseconds")
</dt> </dl>

Per-process user-mode execution time limit, in 100-nanosecond units. This property is ignored unless **LimitFlags** specifies Limit Process Time. The system periodically checks to determine whether or not each process associated with the job has accumulated more user-mode time than the set limit. If it has, the process is terminated.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**PriorityClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Priority class for all of the processes associated with the job. Processes and threads cannot modify their priority class. This property is ignored unless **LimitFlags** specifies the Limit Priority value.

</dd> <dt>

**ProcessMemoryLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("kilobytes")
</dt> </dl>

Per-process memory limit in kilobytes. This property is ignored unless **LimitFlags** specifies the Limit Process Memory value.

</dd> <dt>

**SchedulingClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scheduling class for all of the processes associated with the job. The valid values are 0 (zero) to 9 (nine). Use 0 (zero) for the least favorable scheduling class relative to other threads, and 9 (nine) for the most favorable scheduling class relative to other threads. This property is ignored unless **LimitFlags** specifies the Limit Scheduling Class value.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SettingID), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Job object limit setting instance. Because they are kernel objects, job object names are case-sensitive. However, Windows Management Instrumentation (WMI) keys are case-insensitive and must be decorated to distinguish case. To indicate a capital letter, precede the letter by a backslash. For example, "A" and "a" are lowercase and "\\A" and "\\a" are uppercase.

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectLimitSetting** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

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

[**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




