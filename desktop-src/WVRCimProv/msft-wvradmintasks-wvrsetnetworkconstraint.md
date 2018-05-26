---
title: WvrSetNetworkConstraint method of the MSFT\_WvrAdminTasks class
description: Performs a CIM call to set a new Network Constraint for a partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a50d0173-e4e8-4f00-b81c-b1dc0f4cf3cf
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrSetNetworkConstraint method
- WvrSetNetworkConstraint method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrSetNetworkConstraint method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrSetNetworkConstraint
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrSetNetworkConstraint method of the MSFT\_WvrAdminTasks class

Performs a CIM call to set a new Network Constraint for a partnership.

## Syntax


```mof
uint32 WvrSetNetworkConstraint(
  [in] string ReplicationGroupName,
  [in] string PartnerReplicationGroupName,
  [in] string NWInterfaceIndex[]
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

</dd> <dt>

*NWInterfaceIndex* \[in\]
</dt> <dd>

The NW interface index.

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

 

 





