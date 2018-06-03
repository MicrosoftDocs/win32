---
title: ClusVersion.VendorId property
description: Returns vendor information about the Cluster service installed on the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7d4b2cd-bb61-429a-970a-4e69113d42a8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VendorId property Failover Cluster
- VendorId property Failover Cluster , ClusVersion object
- ClusVersion object Failover Cluster , VendorId property
topic_type:
- apiref
api_name:
- ClusVersion.VendorId
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusVersion.VendorId property

\[The **VendorId** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns vendor information about the [*Cluster service*](https://www.bing.com/search?q=*Cluster service*) installed on the local [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusVersion.VendorId As String
```



## Property value

**String** that receives the vendor information.

## Remarks

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
</dt> </dl>

 

 





