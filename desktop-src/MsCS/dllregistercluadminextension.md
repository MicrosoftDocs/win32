---
title: DllRegisterCluAdminExtension callback function
description: Registers a Failover Cluster Administrator extension DLL for resources with the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17e390a2-5a9d-4763-9c8b-0eb9af78cd26
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DllRegisterCluAdminExtension callback function Failover Cluster
topic_type:
- apiref
api_name:
- DllRegisterCluAdminExtension
api_type:
- UserDefined
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DllRegisterCluAdminExtension callback function

Registers a [Failover Cluster Administrator](cluster-administrator.md) extension DLL for [resources](resources.md) with the [*cluster*](https://www.bing.com/search?q=*cluster*) by adding information to the [cluster database](cluster-database.md).

## Syntax


```C++
HRESULT STDAPICALLTYPE DllRegisterCluAdminExtension(
  _In_ HCLUSTER hCluster
);
```



## Parameters

<dl> <dt>

*hCluster* \[in\]
</dt> <dd>

Handle to the failover cluster to modify in the cluster database.

</dd> </dl>

## Return value

If **DllRegisterCluAdminExtension** is not successful, it can return one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**NOERROR**
</dt> <dd>

0

The Failover Cluster Administrator extension DLL was successfully registered.

</dd> </dl>

## Remarks

You must implement this function in your extension DLL. For each [*cluster object*](https://www.bing.com/search?q=*cluster object*) that you extend in the DLL, append the **CLSID** of the extension to the object's [**AdminExtensions**](groups-adminextensions.md) property. For example, if your extension DLL extends a [group](groups.md), you would add the **CLSID** of the extension to the **AdminExtensions** property of the group.

Note that the [**AdminExtensions**](groups-adminextensions.md) property is a **REG\_MULTI\_SZ** value. There may already be extensions defined for the object. Your implementation should not overwrite existing **CLSID**s or create duplicate entries in the **AdminExtensions** properties.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



 

 





