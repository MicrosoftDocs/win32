---
title: ImportDBClone method of the MSFT\_DfsrVolumeConfig class
description: Starts the process of importing the specified Distributed File System Replication (DFSR) volume database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09D0A7DE-9198-48C5-A955-29DFBB5A96E8
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportDBClone method Distributed File System Replication
- ImportDBClone method Distributed File System Replication , MSFT_DfsrVolumeConfig interface
- MSFT_DfsrVolumeConfig interface Distributed File System Replication , ImportDBClone method
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig.ImportDBClone
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ImportDBClone method of the MSFT\_DfsrVolumeConfig class

Starts the process of importing the specified Distributed File System Replication (DFSR) volume database. This is a static method.

## Syntax


```mof
uint32 ImportDBClone(
  [in] string Source,
  [in] string Destination
);
```



## Parameters

<dl> <dt>

*Source* \[in\]
</dt> <dd>

Specifies the folder path to stores the imported DFSR database and configuration file.

</dd> <dt>

*Destination* \[in\]
</dt> <dd>

Specifies the volume path containing the folders to import.

</dd> </dl>

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

 

 





