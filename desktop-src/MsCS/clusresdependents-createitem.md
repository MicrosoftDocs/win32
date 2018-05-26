---
title: ClusResDependents.CreateItem method
description: Creates a resource in the cluster and adds it to the ClusResDependents collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e696bee0-7ca4-47ec-a29a-b13e445a72de
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreateItem method Failover Cluster
- CreateItem method Failover Cluster , ClusResDependents class
- ClusResDependents class Failover Cluster , CreateItem method
topic_type:
- apiref
api_name:
- ClusResDependents.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResDependents.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [resource](resources.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly) and adds it to the [**ClusResDependents**](clusresdependents-collection.md) collection.

## Syntax


```VB
ClusResDependents.CreateItem( _
  ByVal ResourceName, _
  ByVal ResourceType, _
  ByVal GroupName, _
  ByVal dwFlags _
)
```



## Parameters

<dl> <dt>

*ResourceName* 
</dt> <dd>

**String** containing the name of the resource to create.

</dd> <dt>

*ResourceType* 
</dt> <dd>

**String** specifying the type of the resource to create.

</dd> <dt>

*GroupName* 
</dt> <dd>

**String** containing the name of the [group](groups.md) to which the new resource will belong.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Value indicating how to create the resource. *Flag* can be set to one of the following values enumerated from the [**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_create_flags?branch=master) enumeration.

<dt>

<span id="CLUSTER_RESOURCE_DEFAULT_MONITOR"></span><span id="cluster_resource_default_monitor"></span>

<span id="CLUSTER_RESOURCE_DEFAULT_MONITOR"></span><span id="cluster_resource_default_monitor"></span>****CLUSTER\_RESOURCE\_DEFAULT\_MONITOR**** (0)


</dt> <dd>

The [Cluster service](cluster-service.md) determines the [Resource Monitor](resource-monitor.md) to which the new resource will be assigned.

</dd> <dt>

<span id="CLUSTER_RESOURCE_SEPARATE_MONITOR"></span><span id="cluster_resource_separate_monitor"></span>

<span id="CLUSTER_RESOURCE_SEPARATE_MONITOR"></span><span id="cluster_resource_separate_monitor"></span>****CLUSTER\_RESOURCE\_SEPARATE\_MONITOR**** (1)


</dt> <dd>

Causes the Cluster service to create a separate Resource Monitor dedicated exclusively to the new resource.

</dd> </dl> </dd> </dl>

## Return value

A [**ClusResource**](clusresource-object.md) object that receives the new resource.

## Remarks

Resources added to a [**ClusResDependents**](clusresdependents-collection.md) collection become [dependents](resource-dependencies.md) of the resource from which the collection was obtained.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusResDependents is defined as F2E6072E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependents**](clusresdependents-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





