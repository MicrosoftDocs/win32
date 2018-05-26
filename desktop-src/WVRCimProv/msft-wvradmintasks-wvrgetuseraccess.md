---
title: WvrGetUserAccess method of the MSFT\_WvrAdminTasks class
description: Performs a CIM call to obtain list of users that have permissions to manage Storage Replica.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32bda217-ddfa-4450-b04f-c9a7fb1cdcec
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrGetUserAccess method
- WvrGetUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrGetUserAccess method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrGetUserAccess
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrGetUserAccess method of the MSFT\_WvrAdminTasks class

Performs a CIM call to obtain list of users that have permissions to manage Storage Replica.

## Syntax


```mof
uint32 WvrGetUserAccess(
  [out] MSFT_WvrUser Output[]
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

On success, contains a collection of [**MSFT\_WvrUser**](msft-wvruser.md) objects that have the appropriate permissions.

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

 

 





