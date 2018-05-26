---
title: UnpairRemoteSubsystem method of the MSFT\_WvrAdminTasks class
description: Unpairing two computers or clusters from replication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66EE6D58-9146-4677-BF5C-49C53EE6A35E
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UnpairRemoteSubsystem method
- UnpairRemoteSubsystem method, MSFT_WvrAdminTasks interface
- MSFT_WvrAdminTasks interface, UnpairRemoteSubsystem method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.UnpairRemoteSubsystem
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UnpairRemoteSubsystem method of the MSFT\_WvrAdminTasks class

Unpairing two computers or clusters from replication.

## Syntax


```mof
uint32 UnpairRemoteSubsystem(
  [in] string ComputerName
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

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

 

 





