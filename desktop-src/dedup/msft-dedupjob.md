---
title: MSFT\_DedupJob class
description: Represents a currently active data deduplication job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88365623-DABC-45D2-8C15-C8381F76F257
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupJob class Data Deduplication API
- MSFT_DedupJob class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupJob
- MSFT_DedupJob.Id
- MSFT_DedupJob.ProcessId
- MSFT_DedupJob.Volume
- MSFT_DedupJob.VolumeId
- MSFT_DedupJob.Type
- MSFT_DedupJob.ScheduleType
- MSFT_DedupJob.StopWhenSystemBusy
- MSFT_DedupJob.Priority
- MSFT_DedupJob.Memory
- MSFT_DedupJob.Cores
- MSFT_DedupJob.InputOutputThrottle
- MSFT_DedupJob.InputOutputThrottleLevel
- MSFT_DedupJob.State
- MSFT_DedupJob.Progress
- MSFT_DedupJob.StartTime
- MSFT_DedupJob.Full
- MSFT_DedupJob.ReadOnly
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DedupJob class

Represents a currently active data deduplication job.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupJob
{
  String   Id;
  uint32   ProcessId;
  String   Volume;
  String   VolumeId;
  uint32   Type;
  uint32   ScheduleType;
  boolean  StopWhenSystemBusy;
  uint32   Priority;
  uint32   Memory;
  uint32   Cores;
  uint32   InputOutputThrottle;
  uint32   InputOutputThrottleLevel;
  uint32   State;
  uint32   Progress;
  datetime StartTime;
  boolean  Full;
  boolean  ReadOnly;
};
```

## Members

The **MSFT\_DedupJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DedupJob** class has these methods.



| Method                               | Description                                                                                     |
|:-------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Start**](msft-dedupjob-start.md) | Queues a new data deduplication job of the specified type for the specified volumes.<br/> |
| [**Stop**](msft-dedupjob-stop.md)   | Cancels the specified data deduplication job or jobs.<br/>                                |



 

### Properties

The **MSFT\_DedupJob** class has these properties.

<dl> <dt>

**Cores**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

The maximum percentage of physical machine cores that the job can use.

</dd> <dt>

**Full**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the job runs in a more thorough and resource intensive mode. This property applies to garbage collection and scrubbing jobs.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A string that uniquely identifies the job.

</dd> <dt>

**InputOutputThrottle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

The amount of I/O throttling of the job to ensure that it does not interfere with other heavy I/O processes on the system. This value can range from "0" to "100".

</dd> <dt>

**InputOutputThrottleLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The level of I/O throttling of the job to ensure that it does not interfere with other heavy I/O processes on the system.

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

Access type: Read-only
</dt> </dl>

The maximum percentage of physical machine memory that can be consumed by this job. For optimization jobs, a range from 15-50 is suggested with lower memory consumption for jobs that are scheduled to run when the **StopWhenSystemBusy** property is set to **false**. For garbage collection and scrubbing jobs, which are typically run at off hours, a higher memory consumption can be safely specified for example, 50.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The CPU and I/O priority for the deduplication job. For jobs that are scheduled to run when the **StopWhenSystemBusy** property is set to **false**, setting this property to **Low** might make sense. For most other optimization jobs, setting this property to **Normal** is the most efficient.

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

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process ID of the process in which the deduplication job is running.

</dd> <dt>

**Progress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of the job that is completed so far.

</dd> <dt>

**ReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the job runs in read-only mode. This property only applies to scrubbing jobs.

</dd> <dt>

**ScheduleType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manual jobs are given priority over scheduled jobs.

<dt>

<span id="Scheduled"></span><span id="scheduled"></span><span id="SCHEDULED"></span>

**Scheduled** (1)


</dt> <dd></dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time to start this job. By default, this property is set to 1:45 A. M. Type the date in a format that is standard for the system locale, such as dd-MM-yyyy (German \[Germany\]) or MM/dd/yyyy (English \[United States\]).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The execution state of the job.

<dt>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>

**Queued** (1)


</dt> <dd></dd> <dt>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>

**Initializing** (2)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (3)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (4)


</dt> <dd></dd> <dt>

<span id="PendingCancel"></span><span id="pendingcancel"></span><span id="PENDINGCANCEL"></span>

**PendingCancel** (5)


</dt> <dd></dd> <dt>

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>

**Canceled** (6)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

**Failed** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**StopWhenSystemBusy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the job stops running when the system is busy and retries later. If the schedule is for high priority jobs, then set this property to **false**.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data deduplication job.

<dt>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>**Optimization** (1)


</dt> <dd>

This job performs both deduplication and compression of files according data deduplication policy for the volume. After initial optimization of a file, if that file is then modified and again meets the data deduplication policy threshold for optimization, the file is optimized again.

</dd> <dt>

<span id="GarbageCollection"></span><span id="garbagecollection"></span><span id="GARBAGECOLLECTION"></span>

<span id="GarbageCollection"></span><span id="garbagecollection"></span><span id="GARBAGECOLLECTION"></span>**GarbageCollection** (2)


</dt> <dd>

This job processes previously deleted or logically overwritten optimized content to create usable volume free space. When an optimized file is deleted or overwritten by new data, the old data in the chunk store is not deleted right away. By default, garbage collection is scheduled to run weekly. We recommend to run it manually only after large deletions have occurred.

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

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A drive letter (for example, D:) or volume GUID path for the volume. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A volume GUID path for the volume.

</dd> </dl>

## Examples

For an example that uses the **MSFT\_DedupJob** class, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[Data Deduplication Management WMI API Reference](data-deduplication-management-wmi-api-reference.md)
</dt> </dl>

 

 





