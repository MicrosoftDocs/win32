---
title: SuspendGroup method of the MSFT\_WvrAdminTasks class
description: Pauses replication for a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1b120bc-30f3-42a2-a857-5e5dbe60be50
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SuspendGroup method
- SuspendGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SuspendGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SuspendGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SuspendGroup method of the MSFT\_WvrAdminTasks class

Pauses replication for a replication group.

## Syntax


```mof
uint32 SuspendGroup(
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

The name of the replication group to suspend.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| Header<br/>                   | <dl> <dt>Qmgr.h</dt> </dl>         |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





