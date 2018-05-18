---
title: GetSizesInfo method of the MSFT\_SMPool class
description: Returns the possible sizes of child storage volumes that can be created or modified by using capacity from this storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff4fc260-0afd-4d7a-a633-e995849a36b7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSizesInfo method", "GetSizesInfo method, MSFT_SMPool class", "MSFT_SMPool class, GetSizesInfo method"]
topic_type:
- apiref
api_name:
- MSFT_SMPool.GetSizesInfo
api_location:
- StorageService.dll
api_type:
- COM
---

# GetSizesInfo method of the MSFT\_SMPool class

Returns the possible sizes of child storage volumes that can be created or modified by using capacity from this storage pool.

## Syntax


```mof
uint32 GetSizesInfo(
  [in, optional]  String                username,
  [in, optional]  String                password,
  [in]            String                PoolSettingObjectId,
  [out, optional] uint64                SupportedSizes[],
  [out, optional] uint64                MinimumVolumeSize,
  [out, optional] uint64                MaximumVolumeSize,
  [out, optional] uint64                VolumeSizeDivisor,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
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

*PoolSettingObjectId* \[in\]
</dt> <dd>

An **ObjectId** of a pool setting. This is the service level that the StoragePool is expected to provide. If **NULL**, the storage service will try to locate a default setting.

</dd> <dt>

*SupportedSizes* \[out, optional\]
</dt> <dd>

All the possible sizes of a storage volume.

</dd> <dt>

*MinimumVolumeSize* \[out, optional\]
</dt> <dd>

The minimum size an element can take as a result of either a creation or modification operation.

</dd> <dt>

*MaximumVolumeSize* \[out, optional\]
</dt> <dd>

The maximum size an element can take as a result of either a creation or modification operation.

</dd> <dt>

*VolumeSizeDivisor* \[out, optional\]
</dt> <dd>

A volume/pool size must be a multiple of this value which is specified in bytes.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Related Provider Methods not supported** (1)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Failed to get supported size** (40311)
</dt> <dt>

**StorageService: Failed to get supported size range** (40312)
</dt> <dt>

**StorageService CIM Error: Failed** (43001)
</dt> <dt>

**StorageService CIM Error: Access denied** (43002)
</dt> <dt>

**StorageService CIM Error: Invalid namespace** (43003)
</dt> <dt>

**StorageService CIM Error: Invalid parameter** (43004)
</dt> <dt>

**StorageService CIM Error: Invalid class** (43005)
</dt> <dt>

**StorageService CIM Error: Not found** (43006)
</dt> <dt>

**StorageService CIM Error: Not supported** (43007)
</dt> <dt>

**StorageService CIM Error: Class has children** (43008)
</dt> <dt>

**StorageService CIM Error: Class has instances** (43009)
</dt> <dt>

**StorageService CIM Error: Invalid superclass** (43010)
</dt> <dt>

**StorageService CIM Error: Already exists** (43011)
</dt> <dt>

**StorageService CIM Error: No such property** (43012)
</dt> <dt>

**StorageService CIM Error: Type mismatch** (43013)
</dt> <dt>

**StorageService CIM Error: Query language not supported** (43014)
</dt> <dt>

**StorageService CIM Error: Invalid query** (43015)
</dt> <dt>

**StorageService CIM Error: Method not available** (43016)
</dt> <dt>

**StorageService CIM Error: Method not found** (43017)
</dt> <dt>

**StorageService CIM Error: Unexpected response** (43018)
</dt> <dt>

**StorageService CIM Error: Invalid response destination** (43019)
</dt> <dt>

**StorageService CIM Error: Namespace not empty** (43020)
</dt> <dt>

**StorageService CIM Error: Invalid enumeration context** (43021)
</dt> <dt>

**StorageService CIM Error: Invalid operation timeout** (43022)
</dt> <dt>

**StorageService CIM Error: Pull has been abandoned** (43023)
</dt> <dt>

**StorageService CIM Error: Pull cannot be abandoned** (43024)
</dt> <dt>

**StorageService CIM Error: Filtered enumeration not supported** (43025)
</dt> <dt>

**StorageService CIM Error: Continuation on error not supported** (43026)
</dt> <dt>

**StorageService CIM Error: Server limits exceeded** (43027)
</dt> <dt>

**StorageService CIM Error: Server is shutting down** (43028)
</dt> <dt>

**StorageService CIM Error: Query feature not supported** (43029)
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMPool**](msft-smpool.md)
</dt> </dl>

 

 





