---
title: AddTargetPorts method of the MSFT\_SMStorageGroup class
description: Adds target ports to a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aff3c334-3e20-4253-92f6-78f217cf4414'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddTargetPorts method", "AddTargetPorts method, MSFT_SMStorageGroup class", "MSFT_SMStorageGroup class, AddTargetPorts method"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroup.AddTargetPorts
api_location:
- StorageService.dll
api_type:
- COM
---

# AddTargetPorts method of the MSFT\_SMStorageGroup class

Adds target ports to a storage group.

## Syntax


```mof
Uint32 AddTargetPorts(
  [in]            String                TargetPortIDs[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

The IDs of target ports to add.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate with the SMI-S provider. If this value is not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The username used to authenticate with the SMI-S provider. If this value is not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

**Windows Server 2012:** This parameter is not supported.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid target port ID** (4099)
</dt> <dt>

**Invalid permission** (4100)
</dt> <dt>

**Target/initiator combination already exposed** (4101)
</dt> <dt>

**StorageService: Error TargetPortID Required** (40010)
</dt> <dt>

**StorageService: Not Unique InitiatorID and TargetPortID Combination** (40040)
</dt> <dt>

**StorageService: Unable to get MaskingGroup from job** (40061)
</dt> <dt>

**StorageService: Error Unable to add TargetPort, PortsPerView is set to OnePort** (40070)
</dt> <dt>

**StorageService: Error Unable to add TargetPort, PortsPerView is set to Unknown** (40080)
</dt> <dt>

**StorageService: Provider does not support masking and mapping operations** (40107)
</dt> <dt>

**StorageService: More than one MaskingGroup of the same type are associated with the SPC on the Provider** (40111)
</dt> <dt>

**StorageService: Unable to Find the TargetPort Object on the provider** (40119)
</dt> <dt>

**StorageService: Operation is not supported for a provider that implements GroupMaskingAndMapping Profile** (40300)
</dt> <dt>

**StorageService: Method invocation failed** (41000)
</dt> <dt>

**StorageService: Error: Provider job completed with errors** (43001)
</dt> <dt>

**StorageService CIM Error: Failed** (43002)
</dt> <dt>

**StorageService CIM Error: Access denied** (43003)
</dt> <dt>

**StorageService CIM Error: Invalid namespace** (43004)
</dt> <dt>

**StorageService CIM Error: Invalid parameter** (43005)
</dt> <dt>

**StorageService CIM Error: Invalid class** (43006)
</dt> <dt>

**StorageService CIM Error: Not found** (43007)
</dt> <dt>

**StorageService CIM Error: Not supported** (43008)
</dt> <dt>

**StorageService CIM Error: Class has children** (43009)
</dt> <dt>

**StorageService CIM Error: Class has instances** (43010)
</dt> <dt>

**StorageService CIM Error: Invalid superclass** (43011)
</dt> <dt>

**StorageService CIM Error: Already exists** (43012)
</dt> <dt>

**StorageService CIM Error: No such property** (43013)
</dt> <dt>

**StorageService CIM Error: Type mismatch** (43014)
</dt> <dt>

**StorageService CIM Error: Query language not supported** (43015)
</dt> <dt>

**StorageService CIM Error: Invalid query** (43016)
</dt> <dt>

**StorageService CIM Error: Method not available** (43017)
</dt> <dt>

**StorageService CIM Error: Method not found** (43018)
</dt> <dt>

**StorageService CIM Error: Unexpected response** (43019)
</dt> <dt>

**StorageService CIM Error: Invalid response destination** (43020)
</dt> <dt>

**StorageService CIM Error: Namespace not empty** (43021)
</dt> <dt>

**StorageService CIM Error: Invalid enumeration context** (43022)
</dt> <dt>

**StorageService CIM Error: Invalid operation timeout** (43023)
</dt> <dt>

**StorageService CIM Error: Pull has been abandoned** (43024)
</dt> <dt>

**StorageService CIM Error: Pull cannot be abandoned** (43025)
</dt> <dt>

**StorageService CIM Error: Filtered enumeration not supported** (43026)
</dt> <dt>

**StorageService CIM Error: Continuation on error not supported** (43027)
</dt> <dt>

**StorageService CIM Error: Server limits exceeded** (43028)
</dt> <dt>

**StorageService CIM Error: Server is shutting down** (43029)
</dt> <dt>

**StorageService CIM Error: Query feature not supported** (51000)
</dt> <dt>

**StorageService: Generic Failure** (51005)
</dt> <dt>

**StorageService: Invalid connection credentials** (51010)
</dt> <dt>

**StorageService: SSL connection failure** (51011)
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

[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)
</dt> </dl>

 

 





