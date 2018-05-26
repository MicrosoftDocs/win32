---
title: ClusResTypes.CreateItem method
description: Creates a new resource type in the cluster and adds it to a ClusResTypes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7fc79b1-1803-4060-bf1f-39a253bccab6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreateItem method Failover Cluster
- CreateItem method Failover Cluster , ClusResTypes collection
- ClusResTypes collection Failover Cluster , CreateItem method
topic_type:
- apiref
api_name:
- ClusResTypes.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResTypes.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new [resource type](resource-types.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly) and adds it to a [**ClusResTypes**](clusrestypes-collection.md) collection.

## Syntax


```VB
ClusResTypes.CreateItem( _
  ByVal strResTypeName, _
  ByVal strDisplayName, _
  ByVal strResTypeDll, _
  ByVal lLooksAlivePollInterval, _
  ByVal lIsAlivePollInterval _
)
```



## Parameters

<dl> <dt>

*strResTypeName* 
</dt> <dd>

String containing the name of the new resource type.

</dd> <dt>

*strDisplayName* 
</dt> <dd>

String containing the display name of the new resource type.

</dd> <dt>

*strResTypeDll* 
</dt> <dd>

String containing the file name of the library containing the new resource type.

</dd> <dt>

*lLooksAlivePollInterval* 
</dt> <dd>

Length of time in milliseconds that should occur between calls to the new resource type's [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) entry point function.

</dd> <dt>

*lIsAlivePollInterval* 
</dt> <dd>

Length of time in milliseconds that should occur between calls to the new resource type's [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) entry point function.

</dd> </dl>

## Return value

A [**ClusResType**](clusrestype-object.md) object that receives the newly added resource type.

## Remarks

The new resource type must be supported by a [resource DLL](resource-dlls.md). For more information, see [Creating a Custom Resource Type](creating-resource-types.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResTypes is defined as F2E60712-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> <dt>

[**ClusResTypes**](clusrestypes-collection.md)
</dt> <dt>

[**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master)
</dt> <dt>

[**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master)
</dt> </dl>

 

 





