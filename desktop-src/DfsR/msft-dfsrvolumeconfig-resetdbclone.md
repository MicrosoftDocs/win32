---
title: ResetDBClone method of the MSFT\_DfsrVolumeConfig class
description: Stops the current database export or import operation and returns the database to its previous state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 212B31C3-AEF5-42BB-8F58-AEB19BE0E31E
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ResetDBClone method Distributed File System Replication
- ResetDBClone method Distributed File System Replication , MSFT_DfsrVolumeConfig interface
- MSFT_DfsrVolumeConfig interface Distributed File System Replication , ResetDBClone method
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig.ResetDBClone
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResetDBClone method of the MSFT\_DfsrVolumeConfig class

Stops the current database export or import operation and returns the database to its previous state.

## Syntax


```mof
uint32 ResetDBClone();
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
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrVolumeConfig**](msft-dfsrvolumeconfig.md)
</dt> </dl>

 

 





