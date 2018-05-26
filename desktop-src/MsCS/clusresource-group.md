---
title: ClusResource.Group property
description: group to which a resource belongs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8fea7c20-57bc-4037-bd1e-4c0c2915a5ce
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Group property Failover Cluster
- Group property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Group property
topic_type:
- apiref
api_name:
- ClusResource.Group
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.Group property

\[The [**MaintenanceMode**](clusresource-maintenancemode.md) property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [group](groups.md) to which a [resource](resources.md) belongs.

This property is read-only.

## Syntax


```VB
ClusResource.Group
```



## Property value

A [**ClusResGroup**](clusresgroup-object.md) object that receives the group containing the resource.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





