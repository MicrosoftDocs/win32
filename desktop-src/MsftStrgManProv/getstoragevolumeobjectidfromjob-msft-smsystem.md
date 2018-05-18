---
title: GetStorageVolumeObjectIdFromJob method of the MSFT\_SMSystem class
description: Returns a storage volume object id based on a Job reference.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cc073eba-305d-40c8-bedc-9c5f08f05dfd'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetStorageVolumeObjectIdFromJob method", "GetStorageVolumeObjectIdFromJob method, MSFT_SMSystem class", "MSFT_SMSystem class, GetStorageVolumeObjectIdFromJob method"]
topic_type:
- apiref
api_name:
- MSFT_SMSystem.GetStorageVolumeObjectIdFromJob
api_location:
- StorageService.dll
api_type:
- COM
---

# GetStorageVolumeObjectIdFromJob method of the MSFT\_SMSystem class

Returns a storage volume object id based on a Job reference.

## Syntax


```mof
uint32 GetStorageVolumeObjectIdFromJob(
  [in]            MSFT_SMJob        REF Job,
  [out]           string                StorageVolumeObjectId,
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Job* \[in\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance.

</dd> <dt>

*StorageVolumeObjectId* \[out\]
</dt> <dd>

Storage Volume ObjectId.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





