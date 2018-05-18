---
title: WvrAddReplica method of the MSFT\_WvrAdminTasks class
description: Adds a volume to an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '41853aa4-474f-49b5-8cb9-1b0d286ec06b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WvrAddReplica method", "WvrAddReplica method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, WvrAddReplica method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrAddReplica
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# WvrAddReplica method of the MSFT\_WvrAdminTasks class

Adds a volume to an existing replication group.

## Syntax


```mof
uint32 WvrAddReplica(
  [in] string ReplicationGroupName,
  [in] string VolumeName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*VolumeName* \[in\]
</dt> <dd>

The name of the volume to add.

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

 

 





