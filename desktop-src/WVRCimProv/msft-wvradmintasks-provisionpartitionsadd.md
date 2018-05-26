---
title: ProvisionPartitionsAdd method of the MSFT\_WvrAdminTasks class
description: Adds partition IDs to the partition database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a6f865b8-de18-4542-af50-99dce6b04626
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ProvisionPartitionsAdd method
- ProvisionPartitionsAdd method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, ProvisionPartitionsAdd method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.ProvisionPartitionsAdd
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProvisionPartitionsAdd method of the MSFT\_WvrAdminTasks class

Adds partition IDs to the partition database.

## Syntax


```mof
uint32 ProvisionPartitionsAdd(
  [in] string PartitionIds[]
);
```



## Parameters

<dl> <dt>

*PartitionIds* \[in\]
</dt> <dd>

Identifies the partitions to add to the database.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





