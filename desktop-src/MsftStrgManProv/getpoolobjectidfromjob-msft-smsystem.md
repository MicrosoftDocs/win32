---
title: GetPoolObjectIdFromJob method of the MSFT\_SMSystem class
description: Returns a pool ObjectId associated with a Job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2efdf4ed-ee8e-42f8-b632-23650b0df249
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPoolObjectIdFromJob method
- GetPoolObjectIdFromJob method, MSFT_SMSystem class
- MSFT_SMSystem class, GetPoolObjectIdFromJob method
topic_type:
- apiref
api_name:
- MSFT_SMSystem.GetPoolObjectIdFromJob
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPoolObjectIdFromJob method of the MSFT\_SMSystem class

Returns a pool ObjectId associated with a Job.

## Syntax


```mof
uint32 GetPoolObjectIdFromJob(
  [in]            MSFT_SMJob        REF Job,
  [out]           String                PoolObjectId,
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Job* \[in\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance.

</dd> <dt>

*PoolObjectId* \[out\]
</dt> <dd>

The pool ObjectId.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Not Found** (6)
</dt> <dt>

**StorageService: Generic Failure** (51000)
</dt> <dt>

**StorageService: Invalid connection credentials** (51005)
</dt> <dt>

**StorageService: SSL connection failure** (51010)
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

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





