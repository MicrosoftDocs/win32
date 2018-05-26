---
title: MSFT\_DedupJobSchedule class
description: Represents a data deduplication schedule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CDBBF9D4-5A94-4B97-B55A-76A64B8D26C2
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupJobSchedule class Data Deduplication API
- MSFT_DedupJobSchedule class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupJobSchedule
- MSFT_DedupJobSchedule.Name
- MSFT_DedupJobSchedule.ScheduledTask
- MSFT_DedupJobSchedule.Type
- MSFT_DedupJobSchedule.StopWhenSystemBusy
- MSFT_DedupJobSchedule.Priority
- MSFT_DedupJobSchedule.Memory
- MSFT_DedupJobSchedule.Cores
- MSFT_DedupJobSchedule.InputOutputThrottle
- MSFT_DedupJobSchedule.InputOutputThrottleLevel
- MSFT_DedupJobSchedule.Enabled
- MSFT_DedupJobSchedule.Start
- MSFT_DedupJobSchedule.DurationHours
- MSFT_DedupJobSchedule.Days
- MSFT_DedupJobSchedule.Full
- MSFT_DedupJobSchedule.ReadOnly
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DedupJobSchedule class

Represents a data deduplication schedule.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupJobSchedule
{
  string   Name;
  string   ScheduledTask;
  uint32   Type;
  boolean  StopWhenSystemBusy;
  uint32   Priority;
  uint32   Memory;
  uint32   Cores;
  uint32   InputOutputThrottle;
  uint32   InputOutputThrottleLevel;
  boolean  Enabled;
  datetime Start;
  uint32   DurationHours;
  sint32   Days[];
  boolean  Full;
  boolean  ReadOnly;
};
```

## Members

The **MSFT\_DedupJobSchedule** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DedupJobSchedule** class has these methods.



| Method                                         | Description                                                                                                                                                                                     |
|:-----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](msft-dedupjobschedule-create.md) | Creates a new data deduplication schedule, with default settings, if none are specified, and returns a deduplication schedule CIM object that can be used to customize the schedule.<br/> |



 

### Properties

The **MSFT\_DedupJobSchedule** class has these properties.

<dl> <dt>

**Cores**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum percentage of physical machine cores that the job can use.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**Days**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The day of the week on which this weekly schedule runs.

<dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

**Sunday** (0)


</dt> <dd></dd> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

**Monday** (1)


</dt> <dd></dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

**Tuesday** (2)


</dt> <dd></dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

**Wednesday** (3)


</dt> <dd></dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

**Thursday** (4)


</dt> <dd></dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

**Friday** (5)


</dt> <dd></dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

**Saturday** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**DurationHours**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of hours that this job should run before it is stopped if the job is not completed prior to the elapsed hours. All deduplication jobs can be safely stopped with no impact on the files in process. If this property is set to zero, the scheduled job runs until completed.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, this job runs when the system clock reaches the date and time specified by the **Start** property. If **false**, the schedule remains in a disabled state and does not run at the time specified by the **Start** property.

</dd> <dt>

**Full**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the job runs in a more thorough and resource intensive mode. This property only applies to garbage collection and scrubbing jobs.

</dd> <dt>

**InputOutputThrottle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The amount of I/O throttling of the job to ensure that it does not interfere with other heavy I/O processes on the system. This value can range from "0" to "100".

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**InputOutputThrottleLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Amount that the deduplication job throttles I/O to limit interference with other I/O intense processes.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (1)


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (2)


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** (3)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (4)


</dt> <dd></dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

**Maximum** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Memory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum percentage of physical machine memory that can be consumed by this job. For optimization jobs, a range from 15-50 is suggested with lower memory consumption for jobs that are scheduled to run when the **StopWhenSystemBusy** property is set to **false**. For garbage collection and scrubbing jobs, which are typically run at off hours, a higher memory consumption can be safely specified for example, 50.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The friendly name for the data deduplication job schedule.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Sets the CPU and I/O priority for the optimization job run by this schedule. For jobs that are scheduled to run when the *StopWhenSystemBusy* property is set to **false**, setting this property to **Low** might make sense. For most other optimization jobs, setting this property to **Normal** is the most efficient.

<dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (2)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the job runs in read-only mode.

</dd> <dt>

**ScheduledTask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for system use.

</dd> <dt>

**Start**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time to start this job. By default, this property is set to 1:45 A. M. Type the date in a format that is standard for the system locale, such as dd-MM-yyyy (German \[Germany\]) or MM/dd/yyyy (English \[United States\]).

</dd> <dt>

**StopWhenSystemBusy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the job stops running when the system is busy and retries later. If the schedule is for high priority jobs, then set this property to **false**.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data deduplication job to run when this schedule is triggered.

<dt>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>**Optimization** (1)


</dt> <dd>

This job performs both deduplication and compression of files according data deduplication policy for the volume. After initial optimization of a file, if that file is then modified and again meets the data deduplication policy threshold for optimization, the file is optimized again.

</dd> <dt>

<span id="GarbageCollection"></span><span id="garbagecollection"></span><span id="GARBAGECOLLECTION"></span>

<span id="GarbageCollection"></span><span id="garbagecollection"></span><span id="GARBAGECOLLECTION"></span>**GarbageCollection** (2)


</dt> <dd>

This job processes previously deleted or logically overwritten optimized content to create usable volume free space. When an optimized file is deleted or overwritten by new data, the old data in the chunk store is not deleted right away. By default, garbage collection is scheduled to run weekly. We recommend to run garbage collection only after large deletions have occurred.

</dd> <dt>

<span id="Scrubbing"></span><span id="scrubbing"></span><span id="SCRUBBING"></span>

<span id="Scrubbing"></span><span id="scrubbing"></span><span id="SCRUBBING"></span>**Scrubbing** (3)


</dt> <dd>

This job processes data corruptions found during data integrity validation, performs possible corruption repair, and generates a scrubbing report.

</dd> <dt>

<span id="Unoptimization"></span><span id="unoptimization"></span><span id="UNOPTIMIZATION"></span>

<span id="Unoptimization"></span><span id="unoptimization"></span><span id="UNOPTIMIZATION"></span>**Unoptimization** (4)


</dt> <dd>

This job undoes deduplication on all of the optimized files on the volume. At the end of a successful unoptimization job, all of the data deduplication metadata is deleted from the volume.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



 

 





