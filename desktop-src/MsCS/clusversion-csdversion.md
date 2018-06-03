---
title: ClusVersion.CSDVersion property
description: Returns the number of the latest service pack installed on the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a7f32e65-98d6-4d69-a796-c0b4bcfe8316
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CSDVersion property Failover Cluster
- CSDVersion property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , CSDVersion property
topic_type:
- apiref
api_name:
- ClusVersion.CSDVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusVersion.CSDVersion property

\[The **CSDVersion** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of the latest service pack installed on the local [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusVersion.CSDVersion
```



## Property value

String that receives the build number.

## Remarks

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the [*cluster*](https://www.bing.com/search?q=*cluster*) when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusVersion is defined as F2E60716-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusVersion**](clusversion-object.md)
</dt> <dt>

[**ClusVersion.MajorVersion**](clusversion-majorversion.md)
</dt> <dt>

[**ClusVersion.MinorVersion**](clusversion-minorversion.md)
</dt> </dl>

 

 





