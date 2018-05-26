---
title: ClusResource.Type property
description: Returns a ClusResType object representing the resource type of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1393df7b-7ec7-4034-8018-d7f5b7cef3e8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Type property Failover Cluster
- Type property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Type property
topic_type:
- apiref
api_name:
- ClusResource.Type
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.Type property

\[The **Type** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResType**](clusrestype-object.md) object representing the [resource type](resource-types.md) of the [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.Type
```



## Property value

A [**ClusResType**](clusrestype-object.md) object that receives the resource type of the resource.

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

[**ClusResource.TypeName**](clusresource-typename.md)
</dt> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> </dl>

 

 





