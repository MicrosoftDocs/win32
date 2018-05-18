---
title: CreateReplicationGroup method of the MSFT\_SMSystem class
description: Creates a replication group on a storage subsystem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a08bdf88-bc25-4879-bd4c-96def5b01e8c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateReplicationGroup method", "CreateReplicationGroup method, MSFT_SMSystem class", "MSFT_SMSystem class, CreateReplicationGroup method"]
topic_type:
- apiref
api_name:
- MSFT_SMSystem.CreateReplicationGroup
api_location:
- StorageService.dll
api_type:
- COM
---

# CreateReplicationGroup method of the MSFT\_SMSystem class

Creates a replication group on a storage subsystem.

## Syntax


```mof
UInt32 CreateReplicationGroup(
  [in]            String                     FriendlyName,
  [in]            MSFT_SMStorageObject   REF StorageElements[],
  [in]            MSFT_SMReplicationSettings ReplicationSettings,
  [out]           MSFT_SMReplicationGroup    CreatedReplicationGroup,
  [out]           MSFT_SMJob             REF Job,
  [out, optional] MSFT_SMExtendedStatus      ExtendedStatus,
  [in, optional]  String                     username,
  [in, optional]  String                     password
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The user friendly name of the replication group.

</dd> <dt>

*StorageElements* \[in\]
</dt> <dd>

An array that contains the storage objects to replicate. The order of these array elements determines the consistency order of the replicas.

</dd> <dt>

*ReplicationSettings* \[in\]
</dt> <dd>

A [**MSFT\_SMReplicationSettings**](msft-smreplicationsettings.md) object that specifies the settings to apply to the source replication group.

</dd> <dt>

*CreatedReplicationGroup* \[out\]
</dt> <dd>

When this method returns, this parameter contains the [**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md) object that represents the new replication group.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**MSFT\_SMJob**](msft-smjob.md) object that specifies a reference to a job if this method returns "Method Parameters Checked - Job Started". If this operation performs synchronously, this parameter is set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

A [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that specifies detailed status information about the result of this operation.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> </dl>

## Return value

The possible return values are:

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

**Object Not Found** (8)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





