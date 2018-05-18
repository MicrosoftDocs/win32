---
title: WvrClearOrphanedPartitionDbRecord method of the MSFT\_WvrAdminTasks class
description: Removes orphaned Storage Replica metadata from the Storage Replica partition database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '61e5bb63-a735-49bb-9dae-8a888d801417'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WvrClearOrphanedPartitionDbRecord method", "WvrClearOrphanedPartitionDbRecord method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, WvrClearOrphanedPartitionDbRecord method"]
---

# WvrClearOrphanedPartitionDbRecord method of the MSFT\_WvrAdminTasks class

Removes orphaned Storage Replica metadata from the Storage Replica partition database.

## Syntax


```mof
uint32 WvrClearOrphanedPartitionDbRecord(
  [in]  MSFT_WvrPartitionDbRecord OrphanedDbRecord,
  [out] boolean                   RebootRequired
);
```



## Parameters

<dl> <dt>

*OrphanedDbRecord* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*RebootRequired* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





