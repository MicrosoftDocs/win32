---
title: VerifyReplicablePartition method of the MSFT\_WvrAdminTasks class
description: Determines whether a partition can be replicated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0815725f-9fbc-4761-b8db-fb2cc70f2bf3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VerifyReplicablePartition method", "VerifyReplicablePartition method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, VerifyReplicablePartition method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.VerifyReplicablePartition
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# VerifyReplicablePartition method of the MSFT\_WvrAdminTasks class

Determines whether a partition can be replicated.

## Syntax


```mof
uint32 VerifyReplicablePartition(
  [in] string PartitionId
);
```



## Parameters

<dl> <dt>

*PartitionId* \[in\]
</dt> <dd>

Identifies the partition to verify.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





