---
title: ResumeReplication method of the DfsrVolumeConfig class
description: Resumes replication for the volume. In order to resume replication, the volume must be in the auto recovery state and replication me be stopped on the volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86e16a4c-ff81-4cd6-ac54-8aa70ba540a8
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ResumeReplication method Distributed File System Replication
- ResumeReplication method Distributed File System Replication , DfsrVolumeConfig class
- DfsrVolumeConfig class Distributed File System Replication , ResumeReplication method
topic_type:
- apiref
api_name:
- DfsrVolumeConfig.ResumeReplication
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResumeReplication method of the DfsrVolumeConfig class

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>Dfsrprovs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrVolumeConfig**](dfsrvolumeconfig.md)
</dt> </dl>

 

 





