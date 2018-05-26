---
title: GetSrAccess method of the MSFT\_WvrAdminTasks class
description: Returns a list of clusters paired with the specified cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ee52e11-b710-437c-869a-2b985c666b09
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSrAccess method
- GetSrAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, GetSrAccess method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.GetSrAccess
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSrAccess method of the MSFT\_WvrAdminTasks class

Returns a list of clusters paired with the specified cluster.

## Syntax


```mof
uint32 GetSrAccess(
  [in]  string                ComputerName,
  [in]  string                Cluster,
  [out] MSFT_WvrPairedCluster Output[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer on which to report.

</dd> <dt>

*Cluster* \[in\]
</dt> <dd>

Cluster name.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

On success, returns a collection of [**MSFT\_WvrUser**](msft-wvruser.md) describing the paired clusters.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





