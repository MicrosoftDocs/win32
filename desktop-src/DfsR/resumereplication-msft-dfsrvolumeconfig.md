---
title: ResumeReplication method of the MSFT\_DfsrVolumeConfig class
description: Resumes replication for the volume. In order to resume replication, the volume must be in the auto recovery state and replication me be stopped on the volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c1be4eaf-e39c-47ba-97f5-185245593a18'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ResumeReplication method Distributed File System Replication", "ResumeReplication method Distributed File System Replication , MSFT_DfsrVolumeConfig class", "MSFT_DfsrVolumeConfig class Distributed File System Replication , ResumeReplication method"]
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig.ResumeReplication
api_location:
- DfsRWmiV2.dll
api_type:
- COM
---

# ResumeReplication method of the MSFT\_DfsrVolumeConfig class

Resumes replication for the volume. In order to resume replication, the volume must be in the auto recovery state and replication me be stopped on the volume.

## Syntax


```mof
uint32 ResumeReplication();
```



## Parameters

This method has no parameters.

## Return value

This method returns a system error code.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrVolumeConfig**](msft-dfsrvolumeconfig.md)
</dt> </dl>

 

 





