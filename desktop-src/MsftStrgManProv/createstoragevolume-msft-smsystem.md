---
title: CreateStorageVolume method of the MSFT\_SMSystem class
description: Start a job to create a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a6c7773f-3589-42f2-bb1e-b59d34afc9ef'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateStorageVolume method", "CreateStorageVolume method, MSFT_SMSystem class", "MSFT_SMSystem class, CreateStorageVolume method"]
topic_type:
- apiref
api_name:
- MSFT_SMSystem.CreateStorageVolume
api_location:
- StorageService.dll
api_type:
- COM
---

# CreateStorageVolume method of the MSFT\_SMSystem class

Start a job to create a storage volume.

## Syntax


```mof
uint32 CreateStorageVolume(
  [in, optional]  string                   ElementName,
  [in, out]       uint64                   Size,
  [in, optional]  boolean                  NoSinglePointOfFailure,
  [in, optional]  uint16                   PackageRedundancyGoal,
  [in, optional]  uint16                   DataRedundancyGoal,
  [in, optional]  uint16                   ParityLayout,
  [in, optional]  boolean                  ThinlyProvisioned,
  [in, optional]  String                   username,
  [in, optional]  String                   password,
  [out, optional] MSFT_SMStorageVolume REF CreatedStorageVolume,
  [out]           MSFT_SMJob           REF Job,
  [out, optional] MSFT_SMExtendedStatus    ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ElementName* \[in, optional\]
</dt> <dd>

End-user relevant name for the storage volume. If **NULL**, then a system supplied name is used.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

As an input parameter, the desired size. As an output parameter, the size achieved.

</dd> <dt>

*NoSinglePointOfFailure* \[in, optional\]
</dt> <dd>

Whether to specify no single point of failure.

**True** specifies no single point of failure; **False** specifies a single point of failure.

</dd> <dt>

*PackageRedundancyGoal* \[in, optional\]
</dt> <dd>

The desired number of redundant packages to be used.

Range: 0 = *value*

</dd> <dt>

*DataRedundancyGoal* \[in, optional\]
</dt> <dd>

The desired number of complete copies of data to maintain.

Range: 1 = *value*

</dd> <dt>

*ParityLayout* \[in, optional\]
</dt> <dd>

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

A reference to the created [**MSFT\_SMStorageVolume**](msft-smstoragevolume.md) instance.

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

**Success**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unspecified Error**
</dt> <dd>

2

</dd> <dt>

**Timeout**
</dt> <dd>

3

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**In Use**
</dt> <dd>

6

**Windows Server 2012 R2 and Windows Server 2012:** This value is unavailable prior to Windows Server 2016.

</dd> <dt>

**Method Parameters Checked - Job Started**
</dt> <dd>

4096

</dd> <dt>

**Size Not Supported**
</dt> <dd>

4097

</dd> <dt>

**StorageService: Method invocation failed**
</dt> <dd>

40300

</dd> <dt>

**StorageService: Cannot modify volume instance**
</dt> <dd>

40304

</dd> <dt>

**StorageService: Volume creation capability not supported**
</dt> <dd>

40308

</dd> <dt>

**StorageService: Cannot find pool**
</dt> <dd>

40315

</dd> <dt>

**StorageService: Pool does not support creation of thinly provisioned StorageVolumes**
</dt> <dd>

40319

</dd> <dt>

**StorageService: Size cannot be zero**
</dt> <dd>

40321

</dd> <dt>

**StorageService: Pool is Primordial**
</dt> <dd>

40600

</dd> <dt>

**StorageService: Pool Usage is restricted or reserved**
</dt> <dd>

40601

</dd> <dt>

**StorageService: Goal Paramters within range - failed to create storage settings on provider**
</dt> <dd>

40602

</dd> <dt>

**StorageService: Goal Paramteres within range - failed to modify storage settings on provider**
</dt> <dd>

40603

</dd> <dt>

**StorageService: NoSinglePointOfFailure desired value is not supported on provider**
</dt> <dd>

40604

</dd> <dt>

**StorageService: Invalid Paramter - PackageRedundancyGoal out of range**
</dt> <dd>

40605

</dd> <dt>

**StorageService: Invalid Paramter - DataRedundancyGoal out of range**
</dt> <dd>

40606

</dd> <dt>

**StorageService: Invalid Parameter - ParityLayout out of range**
</dt> <dd>

40607

</dd> <dt>

**StorageService: Failed - Calling GetSupportedParityLayouts on provider**
</dt> <dd>

40608

</dd> <dt>

**StorageService: Unable to find a Storage Pool to create the Storage VolumeStorageService CIM Error: Failed**
</dt> <dd>

40609

</dd> <dt>

**StorageService CIM Error: Access denied**
</dt> <dd>

43001

</dd> <dt>

**StorageService CIM Error: Invalid namespace**
</dt> <dd>

43002

</dd> <dt>

**StorageService CIM Error: Invalid parameter**
</dt> <dd>

43003

</dd> <dt>

**StorageService CIM Error: Invalid class**
</dt> <dd>

43004

</dd> <dt>

**StorageService CIM Error: Not found**
</dt> <dd>

43005

</dd> <dt>

**StorageService CIM Error: Not supported**
</dt> <dd>

43006

</dd> <dt>

**StorageService CIM Error: Class has children**
</dt> <dd>

43007

</dd> <dt>

**StorageService CIM Error: Class has instances**
</dt> <dd>

43008

</dd> <dt>

**StorageService CIM Error: Invalid superclass**
</dt> <dd>

43009

</dd> <dt>

**StorageService CIM Error: Already exists**
</dt> <dd>

43010

</dd> <dt>

**StorageService CIM Error: No such property**
</dt> <dd>

43011

</dd> <dt>

**StorageService CIM Error: Type mismatch**
</dt> <dd>

43012

</dd> <dt>

**StorageService CIM Error: Query language not supported**
</dt> <dd>

43013

</dd> <dt>

**StorageService CIM Error: Invalid query**
</dt> <dd>

43014

</dd> <dt>

**StorageService CIM Error: Method not available**
</dt> <dd>

43015

</dd> <dt>

**StorageService CIM Error: Method not found**
</dt> <dd>

43016

</dd> <dt>

**StorageService CIM Error: Unexpected response**
</dt> <dd>

43017

</dd> <dt>

**StorageService CIM Error: Invalid response destination**
</dt> <dd>

43018

</dd> <dt>

**StorageService CIM Error: Namespace not empty**
</dt> <dd>

43019

</dd> <dt>

**StorageService CIM Error: Invalid enumeration context**
</dt> <dd>

43020

</dd> <dt>

**StorageService CIM Error: Invalid operation timeout**
</dt> <dd>

43021

</dd> <dt>

**StorageService CIM Error: Pull has been abandoned**
</dt> <dd>

43022

</dd> <dt>

**StorageService CIM Error: Pull cannot be abandoned**
</dt> <dd>

43023

</dd> <dt>

**StorageService CIM Error: Filtered enumeration not supported**
</dt> <dd>

43024

</dd> <dt>

**StorageService CIM Error: Continuation on error not supported**
</dt> <dd>

43025

</dd> <dt>

**StorageService CIM Error: Server limits exceeded**
</dt> <dd>

43026

</dd> <dt>

**StorageService CIM Error: Server is shutting down**
</dt> <dd>

43027

</dd> <dt>

**StorageService CIM Error: Query feature not supported**
</dt> <dd>

43028

</dd> <dt>

**StorageService: Generic Failure**
</dt> <dd>

43029

</dd> <dt>

**StorageService: Invalid connection credentials**
</dt> <dd>

51000

</dd> <dt>

**StorageService: SSL connection failure**
</dt> <dd>

51005

</dd> <dt>


</dt> <dd>

51010

</dd> </dl>

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

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





