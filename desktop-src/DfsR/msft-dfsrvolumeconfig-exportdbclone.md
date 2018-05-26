---
title: ExportDBClone method of the MSFT\_DfsrVolumeConfig class
description: Starts the process of exporting the Distributed File System Replication (DFSR) database for the specified volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2C167CE6-7D8E-40C0-98C7-2BA97540C6F5
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExportDBClone method Distributed File System Replication
- ExportDBClone method Distributed File System Replication , MSFT_DfsrVolumeConfig interface
- MSFT_DfsrVolumeConfig interface Distributed File System Replication , ExportDBClone method
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig.ExportDBClone
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExportDBClone method of the MSFT\_DfsrVolumeConfig class

Starts the process of exporting the Distributed File System Replication (DFSR) database for the specified volume. This is a static method.

## Syntax


```mof
uint32 ExportDBClone(
  [in] string  Source,
  [in] string  Destination,
  [in] uint32  ValidationLevel,
  [in] boolean Overwrite
);
```



## Parameters

<dl> <dt>

*Source* \[in\]
</dt> <dd>

Specifies the volume path containing the database to export.

</dd> <dt>

*Destination* \[in\]
</dt> <dd>

Specifies the folder path of the location to store the exported Distributed File System Replication (DFSR) database and configuration file.

</dd> <dt>

*ValidationLevel* \[in\]
</dt> <dd>

Specifies the level of validation to perform on the export.

<dt>

<span id="No_validation"></span><span id="no_validation"></span><span id="NO_VALIDATION"></span>

<span id="No_validation"></span><span id="no_validation"></span><span id="NO_VALIDATION"></span>**No validation** (0)


</dt> <dd>

No file validation is performed.

</dd> <dt>

<span id="Basic_validation"></span><span id="basic_validation"></span><span id="BASIC_VALIDATION"></span>

<span id="Basic_validation"></span><span id="basic_validation"></span><span id="BASIC_VALIDATION"></span>**Basic validation** (1)


</dt> <dd>

Validate the size, last modified date and security setting for each replicated file.

</dd> <dt>

<span id="Full_validation"></span><span id="full_validation"></span><span id="FULL_VALIDATION"></span>

<span id="Full_validation"></span><span id="full_validation"></span><span id="FULL_VALIDATION"></span>**Full validation** (2)


</dt> <dd>

Validate the full DFSR file hash for each replicated file.

</dd> </dl> </dd> <dt>

*Overwrite* \[in\]
</dt> <dd>

Specifies whether to overwrite any previously exported files. Set to **True** to overwrite; otherwise **false**.

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

 

 





