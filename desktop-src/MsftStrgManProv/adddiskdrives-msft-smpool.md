---
title: AddDiskDrives method of the MSFT\_SMPool class
description: Adds disk drives to a concrete pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8fc7f9e6-2685-4e86-ad80-4f4f923ff368
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddDiskDrives method
- AddDiskDrives method, MSFT_SMPool class
- MSFT_SMPool class, AddDiskDrives method
topic_type:
- apiref
api_name:
- MSFT_SMPool.AddDiskDrives
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddDiskDrives method of the MSFT\_SMPool class

Adds disk drives to a concrete pool.

## Syntax


```mof
uint32 AddDiskDrives(
  [in]            String                DiskDriveObjectIds[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMPool       REF Pool,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*DiskDriveObjectIds* \[in\]
</dt> <dd>

An array of strings containing ObjectIds of disk drives.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

Reference to the created [**MSFT\_SMPool**](msft-smpool.md).

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**StorageService: Unable To Wait For Job Completion** (40055)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Concrete Pool Expansion is not supported** (40813)
</dt> <dt>

**StorageService: Cannot expand a Primordial Pool. Only Concrete Pools can be expanded** (40814)
</dt> <dt>

**StorageService: Provider job completed with errors** (41000)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMPool**](msft-smpool.md)
</dt> </dl>

 

 





