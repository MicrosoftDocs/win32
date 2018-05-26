---
title: Whats New
description: Windows Server 2012 R2 introduces the following changes to the Data Deduplication API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3316A9B5-60A1-47DE-B361-5745514A944A
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Data Deduplication API Data Deduplication API , whats new
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# What's New

Windows Server 2012 R2 introduces the following changes to the Data Deduplication API.

## Changes in Requirements

Windows Server 2012 R2 adds support for Cluster shared volume file system (CSVFS) supporting virtual desktop infrastructure (VDI) workloads.

For more information about requirements, see [About Data Deduplication](about-data-deduplication.md).

## New Data Deduplication Classes

<dl>

[**MSFT\_DedupFileMetadata**](msft-dedupfilemetadata.md) class  
</dl>

## Existing Data Deduplication Class Modifications

<dl>

[**IDedupBackupSupport**](/windows/previous-versions/DdpBackup/nn-ddpbackup-idedupbackupsupport?branch=master) interface  
Changed methods:  
<dl>

[**RestoreFiles**](https://msdn.microsoft.com/library/hh449224) method  
The *FileResults* parameter can now have additional values:  

-   **DDP\_E\_JOB\_COMPLETED\_PARTIAL\_SUCCESS**
-   **DDP\_E\_VOLUME\_UNSUPPORTED**

</dl> </dd> [**MSFT\_DedupJob**](msft-dedupjob.md) class  
Added properties:  
<dl> **InputOutputThrottleLevel** property </dl> </dd> [**MSFT\_DedupJobSchedule**](msft-dedupjobschedule.md) class  
Changed methods:  
<dl>

[**Create**](msft-dedupjobschedule-create.md) method  
Added the *InputOutputThrottleLevel* parameter.  
</dl>

Added properties:

<dl> **InputOutputThrottleLevel** property  
</dl> </dd> [**MSFT\_DedupJob**](msft-dedupjob.md) class  
Changed methods:  
<dl>

[**Start**](msft-dedupjob-start.md) method  
Added the *InputOutputThrottleLevel* parameter.  
</dl> </dd> [**MSFT\_DedupVolume**](msft-dedupvolume.md) class  
Added methods:  
<dl>

[**ExpandFile**](msft-dedupvolume-expandfile.md) method </dl>

Changed methods:

<dl>

[**Enable**](msft-dedupvolume-enable.md) method  
Added the *UsageType* parameter  
</dl>

Added properties:

<dl> **OptimizeInUseFiles**  
**OptimizePartialFiles**  
**UsageType**  
**ExcludeFileTypeDefault**  
</dl> </dd> </dl>

 

 




