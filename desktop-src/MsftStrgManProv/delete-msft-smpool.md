---
title: Delete method of the MSFT\_SMPool class
description: Starts a job to delete a Pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6529b04-4273-4150-a756-d48917ecb748
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Delete method
- Delete method, MSFT_SMPool class
- MSFT_SMPool class, Delete method
topic_type:
- apiref
api_name:
- MSFT_SMPool.Delete
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Delete method of the MSFT\_SMPool class

Starts a job to delete a Pool. The freed space is returned to the source primordial Pool.

## Syntax


```mof
uint32 Delete(
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

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

**StorageService: Concrete Pool deletion is not supported** (40809)
</dt> <dt>

**StorageService: Cannot delete a Primordial Pool. Only Concrete Pools can be deleted** (40810)
</dt> <dt>

**StorageService: Cannot delete Concrete Pool - Concrete Pool has allocated StorageVolumes** (40811)
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

 

 





