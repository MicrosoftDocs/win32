---
title: ClusVersion.Name property
description: Returns the name of the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4825ddd9-6293-4a23-83b0-b8c466b3362c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name property Failover Cluster
- Name property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , Name property
topic_type:
- apiref
api_name:
- ClusVersion.Name
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusVersion.Name property

\[The **Name** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the name of the [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
ClusVersion.Name
```



## Property value

**String** that receives the name.

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

[**ClusVersion.MajorVersion**](clusversion-majorversion.md)
</dt> <dt>

[**ClusVersion.MinorVersion**](clusversion-minorversion.md)
</dt> </dl>

 

 





