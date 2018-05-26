---
title: GetServerClusterName method of the MSFT\_ServerManagerTasks class
description: Retrieves the access names and name of all the nodes in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2fa02e1c-6f00-4eb1-8a41-9c900083f3e2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetServerClusterName method
- GetServerClusterName method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetServerClusterName method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerClusterName
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetServerClusterName method of the MSFT\_ServerManagerTasks class

Retrieves the access names and name of all the nodes in the cluster.

## Syntax


```mof
uint32 GetServerClusterName(
  [out] string cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The list of cluster names.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> </dl>

 

 





