---
title: ClusResource.CoreFlag property
description: Returns CLUS\_FLAGS flags associated with the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e39aa2a-e24c-4d15-9fa9-dec3ecb472ea
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CoreFlag property Failover Cluster
- CoreFlag property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , CoreFlag property
topic_type:
- apiref
api_name:
- ClusResource.CoreFlag
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.CoreFlag property

\[The **CoreFlag** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns [**CLUS\_FLAGS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_flags) flags associated with the [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.CoreFlag
```



## Property value

The **CLUS\_FLAG\_CORE** flag of the [**CLUS\_FLAGS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_flags) enumeration indicates that the resource is a [core resource](core-resources.md) essential to the cluster and cannot be deleted. Included in this group of essential resources are the cluster [IP Address](ip-address.md), the cluster [Network Name](network-name.md), and the [quorum resource](quorum-resource.md).

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

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**CLUS\_FLAGS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_flags)
</dt> </dl>

 

 





