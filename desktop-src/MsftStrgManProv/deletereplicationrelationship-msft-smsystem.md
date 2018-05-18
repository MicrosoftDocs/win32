---
title: DeleteReplicationRelationship method of the MSFT\_SMSystem class
description: Deletes a replication relationship between two replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd546a404-4305-40e8-8fa7-098efa41448d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeleteReplicationRelationship method", "DeleteReplicationRelationship method, MSFT_SMSystem class", "MSFT_SMSystem class, DeleteReplicationRelationship method"]
topic_type:
- apiref
api_name:
- MSFT_SMSystem.DeleteReplicationRelationship
api_location:
- StorageService.dll
api_type:
- COM
---

# DeleteReplicationRelationship method of the MSFT\_SMSystem class

Deletes a replication relationship between two replication groups.

## Syntax


```mof
UInt32 DeleteReplicationRelationship(
  [in]            MSFT_SMReplicationGroup REF SourceReplicationGroup,
  [in]            MSFT_SMReplicaPeer      REF TargetGroupReplicaPeer,
  [out]           MSFT_SMJob              REF Job,
  [out, optional] MSFT_SMExtendedStatus       ExtendedStatus,
  [in, optional]  String                      username,
  [in, optional]  String                      password
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroup* \[in\]
</dt> <dd>

A [**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md) object that specifies the source replication group.

</dd> <dt>

*TargetGroupReplicaPeer* \[in\]
</dt> <dd>

A [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that specifies the target replication group.

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

 

 





