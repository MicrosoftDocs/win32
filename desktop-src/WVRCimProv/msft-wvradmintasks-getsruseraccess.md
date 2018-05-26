---
title: GetSrUserAccess method of the MSFT\_WvrAdminTasks class
description: Returns users that have all capabilities required for them to manage Storage Replica on a given computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6ee30cbc-2a77-48ef-89a3-eda450e9ff6d
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSrUserAccess method
- GetSrUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, GetSrUserAccess method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.GetSrUserAccess
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSrUserAccess method of the MSFT\_WvrAdminTasks class

Returns users that have all capabilities required for them to manage Storage Replica on a given computer.

## Syntax


```mof
uint32 GetSrUserAccess(
  [in]  string       ComputerName,
  [out] MSFT_WvrUser Output[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer on which to report.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

On success, returns a collection of [**MSFT\_WvrUser**](msft-wvruser.md) describing the list of users.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





