---
title: RemoveInitiators method of the MSFT\_SMStorageGroup class
description: Removes the specified initiators from the storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7855165-5aa1-4cdb-86fc-64b4e3d74a07
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveInitiators method
- RemoveInitiators method, MSFT_SMStorageGroup class
- MSFT_SMStorageGroup class, RemoveInitiators method
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroup.RemoveInitiators
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveInitiators method of the MSFT\_SMStorageGroup class

Removes the specified initiators from the storage group.

## Syntax


```mof
Uint32 RemoveInitiators(
  [in]            String                InitiatorPortIDs[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*InitiatorPortIDs* \[in\]
</dt> <dd>

The IDs of initiator ports.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate with the SMI-S provider. If this value is not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate with the SMI-S provider. If this value is not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

**Windows Server 2012:** This parameter is not supported.

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

**Invalid initiator port ID** (4098)
</dt> <dt>

**Target/initiator combination not exposed** (4100)
</dt> <dt>

**StorageService: Error InitiatorID(s) Required** (40005)
</dt> <dt>

**StorageService: Unable to find associated MaskingGroup** (40107)
</dt> <dt>

**StorageService: Provider does not support masking and mapping operations** (40111)
</dt> <dt>

**StorageService: More than one MaskingGroup of the same type are associated with the SPC on the Provider** (40112)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Error: Provider job completed with errors** (41000)
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

[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)
</dt> </dl>

 

 





