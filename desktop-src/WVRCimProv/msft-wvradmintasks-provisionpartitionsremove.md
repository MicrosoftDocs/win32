---
title: ProvisionPartitionsRemove method of the MSFT\_WvrAdminTasks class
description: Removes partition IDs from the partition database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ffcacc2f-dfd8-490a-9f89-d98782b82f02'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ProvisionPartitionsRemove method", "ProvisionPartitionsRemove method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, ProvisionPartitionsRemove method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.ProvisionPartitionsRemove
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# ProvisionPartitionsRemove method of the MSFT\_WvrAdminTasks class

Removes partition IDs from the partition database.

## Syntax


```mof
uint32 ProvisionPartitionsRemove(
  [in] string PartitionIds[]
);
```



## Parameters

<dl> <dt>

*PartitionIds* \[in\]
</dt> <dd>

Identifies the partitions to remove from the database.

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

 

 





