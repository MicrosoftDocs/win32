---
title: DllUnregisterCluAdminExtension callback function
description: Cancels the registration of a Failover Cluster Administrator \ 32; extension DLL for resources with the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e139896-f9b3-4b17-a8da-9416f70d2565
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DllUnregisterCluAdminExtension callback function Failover Cluster
topic_type:
- apiref
api_name:
- DllUnregisterCluAdminExtension
api_type:
- UserDefined
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DllUnregisterCluAdminExtension callback function

Cancels the registration of a [Failover Cluster Administrator](cluster-administrator.md) extension DLL for [resources](resources.md) with the [*cluster*](https://www.bing.com/search?q=*cluster*) by removing information from the [cluster database](cluster-database.md).

## Syntax


```C++
HRESULT STDAPICALLTYPE DllUnregisterCluAdminExtension(
  _In_ HCLUSTER hCluster
);
```



## Parameters

<dl> <dt>

*hCluster* \[in\]
</dt> <dd>

Handle to the cluster to modify in the cluster database.

</dd> </dl>

## Return value

If **DllUnregisterCluAdminExtension** is not successful, it returns one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**NOERROR**
</dt> <dd>

0

Registration for the Failover Cluster Administrator extension DLL was successfully removed.

</dd> </dl>

## Remarks

You must implement this function in your extension DLL. Remove the **CLSID** of your extension from the [**AdminExtensions**](groups-adminextensions.md) property of each [*cluster object*](https://www.bing.com/search?q=*cluster object*) extended by your DLL.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



 

 





