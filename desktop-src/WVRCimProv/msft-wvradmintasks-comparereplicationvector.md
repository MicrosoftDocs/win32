---
title: CompareReplicationVector method of the MSFT\_WvrAdminTasks class
description: Determines whether a destination replication group can connect to a source replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c5032be1-ddb5-4862-84e3-f18537279f3e
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CompareReplicationVector method
- CompareReplicationVector method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, CompareReplicationVector method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.CompareReplicationVector
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CompareReplicationVector method of the MSFT\_WvrAdminTasks class

Determines whether a destination replication group can connect to a source replication group.

## Syntax


```mof
uint32 CompareReplicationVector(
  [in] string  ReplicationVector,
  [in] string  ReplicationGroupName,
  [in] boolean IsNewPartner
);
```



## Parameters

<dl> <dt>

*ReplicationVector* \[in\]
</dt> <dd>

Attributes, such as partition size, physical disk sector size, log size, and version.

</dd> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the secondary replication group.

</dd> <dt>

*IsNewPartner* \[in\]
</dt> <dd>

Returns **true** if the secondary group can connect to the primary group; otherwise **false**.

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

 

 





