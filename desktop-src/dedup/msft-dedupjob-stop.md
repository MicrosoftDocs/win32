---
title: Stop method of the MSFT\_DedupJob class
description: Cancels the data deduplication job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5DECE113-62F2-4D8C-BB88-2575205CE95B
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Stop method Data Deduplication API
- Stop method Data Deduplication API , MSFT_DedupJob interface
- MSFT_DedupJob interface Data Deduplication API , Stop method
topic_type:
- apiref
api_name:
- MSFT_DedupJob.Stop
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Stop method of the MSFT\_DedupJob class

Cancels the data deduplication job.

## Syntax


```mof
uint32 Stop();
```



## Parameters

This method has no parameters.

## Return value

This method returns either a WMI return code or a system error code.

## Examples

For an example that uses the **Stop** method, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

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

[**MSFT\_DedupJob::Start**](msft-dedupjob-start.md)
</dt> </dl>

 

 





