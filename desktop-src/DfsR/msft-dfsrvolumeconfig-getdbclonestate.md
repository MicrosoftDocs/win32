---
title: GetDBCloneState method of the MSFT\_DfsrVolumeConfig class
description: Returns the current state of the database export or import process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14C2A87E-38D6-46A9-AB56-2A156EAFC832
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDBCloneState method Distributed File System Replication
- GetDBCloneState method Distributed File System Replication , MSFT_DfsrVolumeConfig interface
- MSFT_DfsrVolumeConfig interface Distributed File System Replication , GetDBCloneState method
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig.GetDBCloneState
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetDBCloneState method of the MSFT\_DfsrVolumeConfig class

Returns the current state of the database export or import process.This is a static method.

## Syntax


```mof
uint32 GetDBCloneState();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>

**Shut down** (0)
</dt> <dt>

**Ready** (1)
</dt> <dt>

**Started DB Export** (2)
</dt> <dt>

**Started DB Import** (3)
</dt> <dt>

**Processing DB Export** (4)
</dt> <dt>

**Processing DB Import** (5)
</dt> <dt>

**Resetting** (6)
</dt> <dt>

**Shutting down** (7)
</dt> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrVolumeConfig**](msft-dfsrvolumeconfig.md)
</dt> </dl>

 

 





