---
title: MSFT\_DedupVolumeStatus class
description: Represents the data deduplication status for a volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CC4B759D-1236-4C87-BEF2-577E2DF8BAD6
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupVolumeStatus class Data Deduplication API
- MSFT_DedupVolumeStatus class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupVolumeStatus
- MSFT_DedupVolumeStatus.VolumeId
- MSFT_DedupVolumeStatus.Volume
- MSFT_DedupVolumeStatus.Capacity
- MSFT_DedupVolumeStatus.FreeSpace
- MSFT_DedupVolumeStatus.UsedSpace
- MSFT_DedupVolumeStatus.SavedSpace
- MSFT_DedupVolumeStatus.SavingsRate
- MSFT_DedupVolumeStatus.OptimizedFilesCount
- MSFT_DedupVolumeStatus.OptimizedFilesSize
- MSFT_DedupVolumeStatus.InPolicyFilesCount
- MSFT_DedupVolumeStatus.InPolicyFilesSize
- MSFT_DedupVolumeStatus.LastOptimizationTime
- MSFT_DedupVolumeStatus.LastGarbageCollectionTime
- MSFT_DedupVolumeStatus.LastScrubbingTime
- MSFT_DedupVolumeStatus.LastOptimizationResult
- MSFT_DedupVolumeStatus.LastGarbageCollectionResult
- MSFT_DedupVolumeStatus.LastScrubbingResult
- MSFT_DedupVolumeStatus.LastOptimizationResultMessage
- MSFT_DedupVolumeStatus.LastGarbageCollectionResultMessage
- MSFT_DedupVolumeStatus.LastScrubbingResultMessage
- MSFT_DedupVolumeStatus.UnoptimizedSize
- MSFT_DedupVolumeStatus.OptimizedFilesSavingsRate
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DedupVolumeStatus class

Represents the data deduplication status for a volume.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupVolumeStatus
{
  String   VolumeId;
  String   Volume;
  uint64   Capacity;
  uint64   FreeSpace;
  uint64   UsedSpace;
  uint64   SavedSpace;
  uint32   SavingsRate;
  uint64   OptimizedFilesCount;
  uint64   OptimizedFilesSize;
  uint64   InPolicyFilesCount;
  uint64   InPolicyFilesSize;
  datetime LastOptimizationTime;
  datetime LastGarbageCollectionTime;
  datetime LastScrubbingTime;
  uint32   LastOptimizationResult;
  uint32   LastGarbageCollectionResult;
  uint32   LastScrubbingResult;
  string   LastOptimizationResultMessage;
  string   LastGarbageCollectionResultMessage;
  string   LastScrubbingResultMessage;
  uint64   UnoptimizedSize;
  uint32   OptimizedFilesSavingsRate;
};
```

## Members

The **MSFT\_DedupVolumeStatus** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DedupVolumeStatus** class has these methods.



| Method                                          | Description                                                                                                                                                                     |
|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Update**](msft-dedupvolumestatus-update.md) | Scans the specified volumes to compute fresh data deduplication savings information and returns a deduplication status object containing fresh metadata, not cached.<br/> |



 

### Properties

The **MSFT\_DedupVolumeStatus** class has these properties.

<dl> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The capacity of the volume, in bytes.

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of free space on the volume, in bytes.

</dd> <dt>

**InPolicyFilesCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of files that currently qualify for optimization. This number will stay relatively constant between optimization jobs.

</dd> <dt>

**InPolicyFilesSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The aggregate size of all files that currently qualify for optimization. This number will stay relatively constant between optimization jobs.

</dd> <dt>

**LastGarbageCollectionResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code from when a garbage collection job was run last on the volume. A value of zero means the job ran successfully.

</dd> <dt>

**LastGarbageCollectionResultMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message from when a garbage collection job was run last on the volume. A null value or empty string means the job ran successfully.

</dd> <dt>

**LastGarbageCollectionTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a garbage collection job was run last on the volume. This date and time will stay constant between garbage collection jobs.

</dd> <dt>

**LastOptimizationResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code from when an optimization job was run last on the volume. A value of zero means the job ran successfully.

</dd> <dt>

**LastOptimizationResultMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message from when an optimization job was run last on the volume. A null value or empty string means the job ran successfully.

</dd> <dt>

**LastOptimizationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The data and time when an optimization job was run last on the volume. This date and time will stay constant between optimization jobs.

</dd> <dt>

**LastScrubbingResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code from when a scrubbing job was run last on the volume. A value of zero means the job ran successfully.

</dd> <dt>

**LastScrubbingResultMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message from when a scrubbing job was run last on the volume. A null value or empty string means the job ran successfully.

</dd> <dt>

**LastScrubbingTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The data and time when a scrubbing job was run last on the volume. This date and time will stay constant between scrubbing jobs.

</dd> <dt>

**OptimizedFilesCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of optimized files on the volume. Note that this number will remain steady (instead of decrease) as users delete files from, or add files to, the volume until you run a garbage collection job. This count is most accurate after a garbage collection job runs.

</dd> <dt>

**OptimizedFilesSavingsRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ratio of deduplication saved space to the logical size of all optimized files on the volume, expressed as a percentage. Note that this number will remain steady as users delete files from, or add new files to, the volume-until you run an optimization job or execute the Update method of the **MSFT\_DedupVolumeStatus** class. This number is most accurate after an optimization job runs or the Update method is executed.

</dd> <dt>

**OptimizedFilesSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The aggregate size of all optimized files on the volume. Note that this number will remain steady (instead of decrease) as users delete files from, or add new files to, the volume until you run a garbage collection job. This number is most accurate after a garbage collection job runs.

</dd> <dt>

**SavedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Saved space is the difference between the logical size of the optimized files and the logical size of the store (the deduplicated user data plus deduplication metadata). Note that this number will remain steady as users delete files from, or add new files to, the volume until you run an optimization job or execute the [**Update**](msft-dedupvolumestatus-update.md) method. This number is most accurate after an optimization job runs or the **Update** method is executed.

</dd> <dt>

**SavingsRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ratio of deduplication saved space to the logical size of all of the files on the volume and is expressed in percentage. Note that this number will remain steady as users delete files from, or add new files to, the volume until you run an optimization job or execute the [**Update**](msft-dedupvolumestatus-update.md) method. This number is most accurate after an optimization job runs or the **Update** method is executed.

</dd> <dt>

**UnoptimizedSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total logical size of all files on the volume, in bytes. This includes all files, optimized and non-optimized. Note that this number will remain steady as users delete optimized files from the volume-until you run an optimization job or execute the Update method of the **MSFT\_DedupVolumeStatus** class. This number is most accurate after an optimization job runs or the Update method is executed.

</dd> <dt>

**UsedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of used space on the volume, in bytes.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A drive letter (for example, D:) or volume GUID path for the volume.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A volume GUID path for the volume. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



 

 





