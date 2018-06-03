---
title: SmapiAddMember method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5e6dc9c-d347-4443-8afb-cd6d0eac744d
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SmapiAddMember method
- SmapiAddMember method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SmapiAddMember method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SmapiAddMember method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 SmapiAddMember(
  [in] string ReplicationGroupName,
  [in] string VolumeNames[],
  [in] string PartitionObjectIds[]
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*VolumeNames* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PartitionObjectIds* \[in\]
</dt> <dd>

TBD

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

 

 





