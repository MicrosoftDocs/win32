---
title: WvrRemoveNetworkConstraint method of the MSFT\_WvrAdminTasks class
description: Performs a CIM call to remove a Network Constraint from a partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5dffbcea-884f-4248-a477-5ec34cec0a4f
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrRemoveNetworkConstraint method
- WvrRemoveNetworkConstraint method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrRemoveNetworkConstraint method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrRemoveNetworkConstraint
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrRemoveNetworkConstraint method of the MSFT\_WvrAdminTasks class

Performs a CIM call to remove a Network Constraint from a partnership.

## Syntax


```mof
uint32 WvrRemoveNetworkConstraint(
  [in] string ReplicationGroupName,
  [in] string PartnerReplicationGroupName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The replication group name.

</dd> <dt>

*PartnerReplicationGroupName* \[in\]
</dt> <dd>

The partner replication group name.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





