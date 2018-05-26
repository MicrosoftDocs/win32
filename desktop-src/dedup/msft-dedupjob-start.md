---
title: Start method of the MSFT\_DedupJob class
description: Queues a new data deduplication job of the specified type for the specified volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 001BBACD-B1E6-4138-8C17-552FC45925CB
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Start method Data Deduplication API
- Start method Data Deduplication API , MSFT_DedupJob class
- MSFT_DedupJob class Data Deduplication API , Start method
topic_type:
- apiref
api_name:
- MSFT_DedupJob.Start
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Start method of the MSFT\_DedupJob class

Queues a new data deduplication job of the specified type for the specified volumes.

## Syntax


```mof
uint32 Start(
  [in]  string        Volume[],
  [in]  uint32        Type,
  [in]  uint32        Priority,
  [in]  uint32        Memory,
  [in]  uint32        Cores,
  [in]  uint32        InputOutputThrottle,
  [in]  uint32        InputOutputThrottleLevel,
  [in]  boolean       StopWhenSystemBusy,
  [in]  boolean       Preempt,
  [in]  boolean       Wait,
  [in]  boolean       Full,
  [in]  boolean       ReadOnly,
  [in]  datetime      Timestamp,
  [out] MSFT_DedupJob DedupJob[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

A list of file system volumes for which to manually queue data deduplication jobs of the named type. Volumes can be specified by drive letter (for example, D:) or volume GUID path. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of data deduplication job.

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

*Priority* \[in\]
</dt> <dd>

Sets the CPU and I/O priority for the optimization job that is run by this schedule. For jobs that are scheduled to run when the *StopWhenSystemBusy* parameter is set to **false**, setting this parameter to **Low** might make sense. For most other optimization jobs, setting this parameter to **Normal** is the most efficient setting.

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

*Memory* \[in\]
</dt> <dd>

The maximum percentage of physical machine memory that can be consumed by this job. For optimization jobs, a range from 15-50 is suggested with lower memory consumption for jobs that are scheduled to run when the *StopWhenSystemBusy* parameter is set to **false**. For garbage collection and scrubbing jobs, which are typically run at off hours, a higher memory consumption can be safely specified for example, 50.

</dd> <dt>

*Cores* \[in\]
</dt> <dd>

The maximum percentage of physical machine cores that the job can use.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

*InputOutputThrottle* \[in\]
</dt> <dd>

The amount of I/O throttling of the job to ensure that it does not interfere with other heavy I/O processes on the system. This value can range from "0" to "100".

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

*InputOutputThrottleLevel* \[in\]
</dt> <dd>

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


</dt> <dd></dd> </dl> </dd> <dt>

*StopWhenSystemBusy* \[in\]
</dt> <dd>

If **True**, the job stops running when the system is busy and retries later. If the schedule is for high-priority jobs, then set this parameter to **false**.

</dd> <dt>

*Preempt* \[in\]
</dt> <dd>

If **True**, this job is moved to the top of the job queue and cancels the current job, if one is running on the specified volumes.

This parameter applies to manual jobs only and is ignored for scheduled jobs.

Even after canceling the current job, if there is not enough memory to run the preempting job, it does not run.

</dd> <dt>

*Wait* \[in\]
</dt> <dd>

If **True**, the method waits for the job to complete and provides progress information to the client.

</dd> <dt>

*Full* \[in\]
</dt> <dd>

This parameter applies to garbage collection and scrubbing jobs.

If **True**, garbage collection jobs free up all deleted or unreferenced data in the system freeing up the most space. If **false**, garbage collection only frees up space after a system threshold of deleted data is exceeded.

We recommend to run garbage collection regularly with this parameter set to **false** and once a month with it set to **True**. Garbage collection is scheduled by default on the host and runs in Full mode at regular intervals.

If **True**, scrubbing jobs validate the integrity of all data on the volume that has been deduplicated. Otherwise, the job only validates critical metadata and data integrity issues that were previously encountered by data deduplication. We recommend to run scrubbing regularly with this parameter set to **false** and once a month with this parameter set to **True**.

</dd> <dt>

*ReadOnly* \[in\]
</dt> <dd>

This parameter only applies to scrubbing jobs. Scrubbing jobs that run in read-only mode process and report on found corruptions but do not take any repair actions.

</dd> <dt>

*Timestamp* \[in\]
</dt> <dd>

This parameter only applies to unoptimization jobs. Only deduplicated files that have been optimized or reoptimized since the specified time will be unoptimized.

</dd> <dt>

*DedupJob* \[out\]
</dt> <dd>

Array of references to the started jobs.

</dd> </dl>

## Return value

This method returns either a Window Management Instrumentation (WMI) return code or a system error code.

## Examples

For an example that uses the **Start** method, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

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

[**MSFT\_DedupJob**](msft-dedupjob.md)
</dt> <dt>

[**MSFT\_DedupJob::Stop**](msft-dedupjob-stop.md)
</dt> </dl>

 

 





