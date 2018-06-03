---
title: Create method of the MSFT\_DedupJobSchedule class
description: Creates a new data deduplication schedule (with default settings, if none are specified) and returns a deduplication schedule CIM object that can be used to customize the schedule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: EAC90495-BDDE-40AF-8A46-58F1C6F8E97A
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Create method Data Deduplication API
- Create method Data Deduplication API , MSFT_DedupJobSchedule class
- MSFT_DedupJobSchedule class Data Deduplication API , Create method
topic_type:
- apiref
api_name:
- MSFT_DedupJobSchedule.Create
api_location:
- DdpWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create method of the MSFT\_DedupJobSchedule class

Creates a new data deduplication schedule (with default settings, if none are specified) and returns a deduplication schedule CIM object that can be used to customize the schedule.

## Syntax


```mof
uint32 Create(
  [in]  string                Name,
  [in]  uint32                Type,
  [in]  boolean               Disable,
  [in]  datetime              Start,
  [in]  uint32                DurationHours,
  [in]  sint32                Days[],
  [in]  boolean               StopWhenSystemBusy,
  [in]  uint32                Memory,
  [in]  uint32                Cores,
  [in]  uint32                Priority,
  [in]  uint32                InputOutputThrottle,
  [in]  uint32                InputOutputThrottleLevel,
  [in]  boolean               Full,
  [in]  boolean               ReadOnly,
  [out] MSFT_DedupJobSchedule DedupJobSchedule
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A friendly name for the data deduplication job schedule that will be created.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of data deduplication job to run when this schedule is triggered.

<dt>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>

<span id="Optimization"></span><span id="optimization"></span><span id="OPTIMIZATION"></span>**Optimization** (1)


</dt> <dd>

This job performs both deduplication and compression of files according data deduplication policy for the volume. After initial optimization of a file, if that file is then modified and again meets the data deduplication policy threshold for optimization, the file will be optimized again.

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

</dd> </dl> </dd> <dt>

*Disable* \[in\]
</dt> <dd>

Creates this new job schedule, but immediately disables it so that it does not run when the system clock reaches the date and time specified by the *Start* parameter. To re-enable the job schedule after it has been disabled, modify the **Enabled** property of the CIM object instance.

</dd> <dt>

*Start* \[in\]
</dt> <dd>

The time to start this job. By default, this parameter is set to 1:45 A. M. Type the date in a format that is standard for the system locale, such as dd-MM-yyyy (German \[Germany\]) or MM/dd/yyyy (English \[United States\]).

</dd> <dt>

*DurationHours* \[in\]
</dt> <dd>

The number of hours that this job should run before it is stopped if the job is not completed prior to the elapsed hours. All deduplication jobs can be safely stopped with no impact on the files in process. If this parameter is set to zero, the scheduled job runs until completed.

</dd> <dt>

*Days* \[in\]
</dt> <dd>

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


</dt> <dd></dd> </dl> </dd> <dt>

*StopWhenSystemBusy* \[in\]
</dt> <dd>

If **True**, the job stops running when the system is busy and retries later. If the schedule is for high-priority jobs, then set this parameter to **false**.

</dd> <dt>

*Memory* \[in\]
</dt> <dd>

The maximum percentage of physical machine memory that can be consumed by this job. For optimization jobs, a range from 15-50 is suggested with lower memory consumption for jobs that are scheduled to run when the *StopWhenSystemBusy* parameter is set to **false**. For garbage collection and scrubbing jobs, which are typically run at off hours, a higher memory consumption can be safely specified for example, 50.

</dd> <dt>

*Cores* \[in\]
</dt> <dd>

The maximum percentage of physical machine cores that the job can use.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Sets the CPU and I/O priority for the optimization job run by this schedule. For jobs that are scheduled to run when the *StopWhenSystemBusy* parameter is set to **false**, setting this parameter to **Low** might make sense. For most other optimization jobs, setting this parameter to **Normal** is the most efficient.

<dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (2)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*InputOutputThrottle* \[in\]
</dt> <dd>

The amount of I/O throttling of the job to ensure that it does not interfere with other heavy I/O processes on the system. This value can range from "0" to "100".

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

*InputOutputThrottleLevel* \[in\]
</dt> <dd>

Amount that the dedupliction job throttles I/O to limit interference with other I/O intense processes.

**Windows Server 2012:** This parameter is not supported until Windows Server 2012 R2.

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


</dt> <dd></dd> </dl> </dd> <dt>

*Full* \[in\]
</dt> <dd>

If **True**, the job runs in a more thorough and resource intensive mode. This parameter applies to garbage collection and scrubbing jobs.

</dd> <dt>

*ReadOnly* \[in\]
</dt> <dd>

If **True**, the job runs in read-only mode. This parameter only applies to scrubbing jobs.

</dd> <dt>

*DedupJobSchedule* \[out\]
</dt> <dd>

Array of references to the newly created deduplication jobs.

</dd> </dl>

## Return value

This method returns either a Windows Management Instrumentation (WMI) return code or a system error code.

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

[**MSFT\_DedupJobSchedule**](msft-dedupjobschedule.md)
</dt> </dl>

 

 





