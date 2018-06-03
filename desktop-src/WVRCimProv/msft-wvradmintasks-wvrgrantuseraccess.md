---
title: WvrGrantUserAccess method of the MSFT\_WvrAdminTasks class
description: Performs a CIM call to grant the user permissions to manage Storage Replica.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2153a49c-e392-43ed-9fa1-1da3a70c2161
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrGrantUserAccess method
- WvrGrantUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrGrantUserAccess method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrGrantUserAccess method of the MSFT\_WvrAdminTasks class

Performs a CIM call to grant the user permissions to manage Storage Replica.

## Syntax


```mof
uint32 WvrGrantUserAccess(
  [in] string  UserName,
  [in] boolean IgnoreErrors
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The name of the user to grant permissions to.

</dd> <dt>

*IgnoreErrors* \[in\]
</dt> <dd>

TBD

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

 

 





