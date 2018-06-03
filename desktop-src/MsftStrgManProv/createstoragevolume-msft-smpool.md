---
title: CreateStorageVolume method of the MSFT\_SMPool class
description: Starts a job to create a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b53d17a1-6232-4819-9606-583cda18ea21
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateStorageVolume method
- CreateStorageVolume method, MSFT_SMPool class
- MSFT_SMPool class, CreateStorageVolume method
topic_type:
- apiref
api_name:
- MSFT_SMPool.CreateStorageVolume
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateStorageVolume method of the MSFT\_SMPool class

Starts a job to create a storage volume.

## Syntax


```mof
uint32 CreateStorageVolume(
  [in, optional]      string                   ElementName,
  [in, out, optional] uint64                   Size,
  [in, optional]      boolean                  UseMaximumSize,
  [in, optional]      String                   PoolSettingObjectId,
  [in, optional]      boolean                  NoSinglePointOfFailure,
  [in, optional]      uint16                   PackageRedundancyGoal,
  [in, optional]      uint16                   DataRedundancyGoal,
  [in, optional]      uint16                   ParityLayout,
  [in, optional]      boolean                  ThinlyProvisioned,
  [in, optional]      String                   username,
  [in, optional]      String                   password,
  [out, optional]     MSFT_SMStorageVolume REF CreatedStorageVolume,
  [out]               MSFT_SMJob           REF Job,
  [out, optional]     MSFT_SMExtendedStatus    ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ElementName* \[in, optional\]
</dt> <dd>

End-user relevant name for the storage volume. If **NULL**, then a system supplied name is used.

</dd> <dt>

*Size* \[in, out, optional\]
</dt> <dd>

As an input parameter, the desired size. As an output parameter, the size achieved.

</dd> <dt>

*UseMaximumSize* \[in, optional\]
</dt> <dd>

If **True**, requests the provider to create a storage volume with the maximum possible size.

</dd> <dt>

*PoolSettingObjectId* \[in, optional\]
</dt> <dd>

The ObjectId of a pool setting the defines the service level that the storage volume is expected to provide. If **NULL** the storage service will try to locate a default setting.

**Windows Server 2012:  **

This parameter is not supported.

</dd> <dt>

*NoSinglePointOfFailure* \[in, optional\]
</dt> <dd>

This parameter is not supported.

**Windows Server 2012:  **

Whether to specify no single point of failure.

**True** specifies no single point of failure; **False** specifies a single point of failure.

</dd> <dt>

*PackageRedundancyGoal* \[in, optional\]
</dt> <dd>

This parameter is not supported.

**Windows Server 2012:  **

The desired number of redundant packages to be used.

Range: 0 = *value*

</dd> <dt>

*DataRedundancyGoal* \[in, optional\]
</dt> <dd>

This parameter is not supported.

**Windows Server 2012:  **

The desired number of complete copies of data to maintain.

Range: 1 = *value*

</dd> <dt>

*ParityLayout* \[in, optional\]
</dt> <dd>

This parameter is not supported.

**Windows Server 2012:  **

Whether a parity-based storage organization is using rotated or non-rotated parity.

The possible values are.

<dt>

<span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>

**Non-rotated Parity** (1)


</dt> <dd></dd> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>

**Rotated Parity** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*ThinlyProvisioned* \[in, optional\]
</dt> <dd>

If **True**, the created storage volume is thinly provisioned.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*CreatedStorageVolume* \[out, optional\]
</dt> <dd>

Reference to the created [**MSFT\_SMStorageVolume**](msft-smstoragevolume.md).

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

**In Use** (6)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Cannot modify volume instance** (40304)
</dt> <dt>

**StorageService: Volume creation capability not supported** (40308)
</dt> <dt>

**StorageService: Cannot find pool** (40315)
</dt> <dt>

**StorageService: Pool does not support creation of thinly provisioned StorageVolumes** (40319)
</dt> <dt>

**StorageService: Size and UseMaximumSize input parameters must be mutually exclusive** (40320)
</dt> <dt>

**StorageService: Size cannot be zero** (40321)
</dt> <dt>

**StorageService: Pool is Primordial** (40600)
</dt> <dt>

**StorageService: Pool Usage is restricted or reserved** (40601)
</dt> <dt>

**StorageService: Goal Paramters within range - failed to create storage settings on provider** (40602)
</dt> <dt>

**StorageService: Goal Paramteres within range - failed to modify storage settings on provider** (40603)
</dt> <dt>

**StorageService: NoSinglePointOfFailure desired value is not supported on provider** (40604)
</dt> <dt>

**StorageService: Invalid Paramter - PackageRedundancyGoal out of range** (40605)
</dt> <dt>

**StorageService: Invalid Paramter - DataRedundancyGoal out of range** (40606)
</dt> <dt>

**StorageService: Invalid Parameter - ParityLayout out of range** (40607)
</dt> <dt>

**StorageService: Failed - Calling GetSupportedParityLayouts on provider** (40608)
</dt> <dt>

**StorageService: Unable to find a Storage Pool to create the Storage Volume** (40609)
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMPool**](msft-smpool.md)
</dt> </dl>

 

 





