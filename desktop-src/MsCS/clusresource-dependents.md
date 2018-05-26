---
title: ClusResource.Dependents property
description: dependents of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88206f61-9e90-4335-8a34-fc0e6d1ca208
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Dependents property Failover Cluster
- Dependents property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Dependents property
topic_type:
- apiref
api_name:
- ClusResource.Dependents
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.Dependents property

\[The **Dependents** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the [dependents](resource-dependencies.md) of a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.Dependents
```



## Property value

On a successful return, this value contains a [**ClusResDependents**](clusresdependents-collection.md) collection.

## Requirements



|                                     |                                                                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                                                                           |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                                                                                 |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                                                                               |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                                                                               |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                                                                               |
| IID<br/>                      | CLSID\_ClusResource is defined as f2e60709-2631-11d1-89f1-00a0c90d061e<br/> IID\_ISClusResource is defined as f2e6070a-2631-11d1-89f1-00a0c90d061e<br/> |



## See also

<dl> <dt>

[Resource Dependencies](resource-dependencies.md)
</dt> <dt>

[**ClusResDependents**](clusresdependents-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> </dl>

 

 





