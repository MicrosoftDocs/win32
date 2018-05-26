---
title: QueryReplicationPartners method of the MSFT\_WvrAdminTasks class
description: Returns the partners of a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3d482d17-30d2-4d08-9ba9-cbd9dc429fcc
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- QueryReplicationPartners method
- QueryReplicationPartners method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, QueryReplicationPartners method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# QueryReplicationPartners method of the MSFT\_WvrAdminTasks class

Returns the partners of a replication group.

## Syntax


```mof
uint32 QueryReplicationPartners(
  [in]  string  ReplicationGroupName,
  [in]  boolean ContainSourceGroup,
  [out] string  PartnerGroupNames[],
  [out] string  PartnerComputerNames[],
  [out] string  PartnershipIds[],
  [out] string  OwnerNode,
  [out] boolean IsStretch
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

Identifies the replication group.

</dd> <dt>

*ContainSourceGroup* \[in\]
</dt> <dd>

**true** to contain the source group.

</dd> <dt>

*PartnerGroupNames* \[out\]
</dt> <dd>

The names of replication groups in a partner relationship with the group specified in the *ReplicationGroupName* parameter.

</dd> <dt>

*PartnerComputerNames* \[out\]
</dt> <dd>

The FQDN or NetBIOS names of the computers related to the returned replication groups.

</dd> <dt>

*PartnershipIds* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*OwnerNode* \[out\]
</dt> <dd>

TBD.

</dd> <dt>

*IsStretch* \[out\]
</dt> <dd>

Whether the partnership is a stretch partnership.

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
</dt> <dt>

[**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md)
</dt> </dl>

 

 





