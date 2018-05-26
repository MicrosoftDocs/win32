---
title: PairRemoteSubsystem method of the MSFT\_WvrAdminTasks class
description: Pairing two computers or clusters for replication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 856C8B20-9BEF-47B4-80A7-4DE52C0848CA
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PairRemoteSubsystem method
- PairRemoteSubsystem method, MSFT_WvrAdminTasks interface
- MSFT_WvrAdminTasks interface, PairRemoteSubsystem method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.PairRemoteSubsystem
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PairRemoteSubsystem method of the MSFT\_WvrAdminTasks class

Pairing two computers or clusters for replication.

## Syntax


```mof
uint32 PairRemoteSubsystem(
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

 

 





