---
title: ClusVersion.MajorVersion property
description: Returns the integer portion of the version number for the operating system installed on the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4d81e0a-4f65-470b-9215-f1b91e582646
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MajorVersion property Failover Cluster
- MajorVersion property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , MajorVersion property
topic_type:
- apiref
api_name:
- ClusVersion.MajorVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusVersion.MajorVersion property

\[The **MajorVersion** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the integer portion of the version number for the operating system installed on the local [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusVersion.MajorVersion
```



## Property value

**Long** that receives the [*major version*](https://www.bing.com/search?q=*major version*).

## Remarks

The **MajorVersion** and [**ClusVersion.MinorVersion**](clusversion-minorversion.md) properties together form a complete Windows [*version number*](https://www.bing.com/search?q=*version number*).


```VB
Version = X.Y
MajorVersion = X
MinorVersion = Y
```



All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the [*cluster*](https://www.bing.com/search?q=*cluster*) when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

## Examples

See [**ClusVersion**](clusversion-object.md) for an example.

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

[**ClusVersion.CSDVersion**](clusversion-csdversion.md)
</dt> <dt>

[**ClusVersion.MinorVersion**](clusversion-minorversion.md)
</dt> </dl>

 

 





