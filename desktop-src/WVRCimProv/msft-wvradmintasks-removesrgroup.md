---
title: RemoveSrGroup method of the MSFT\_WvrAdminTasks class
description: Removes a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76591296-9bd3-4a92-9452-ea32628fe527
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveSrGroup method
- RemoveSrGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, RemoveSrGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.RemoveSrGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveSrGroup method of the MSFT\_WvrAdminTasks class

Removes a replication group.

## Syntax


```mof
uint32 RemoveSrGroup(
  [in] string ComputerName,
  [in] string Name
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the replication group to remove.

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

 

 





