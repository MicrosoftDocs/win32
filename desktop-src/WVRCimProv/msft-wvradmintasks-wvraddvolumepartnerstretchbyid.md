---
title: WvrAddVolumePartnerStretchById method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0015ce7b-e693-426e-810f-d167c28fc891
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrAddVolumePartnerStretchById method
- WvrAddVolumePartnerStretchById method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrAddVolumePartnerStretchById method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrAddVolumePartnerStretchById method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 WvrAddVolumePartnerStretchById(
  [in] string SourceReplicationGroupName,
  [in] string TargetReplicationGroupName,
  [in] string ReplicaSetId[]
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*TargetReplicationGroupName* \[in\]
</dt> <dd>

The name of the target replication group.

</dd> <dt>

*ReplicaSetId* \[in\]
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

 

 





