---
title: ClusResDependencies.CreateItem method
description: Creates a resource in the cluster and adds it to the dependency collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aaaf80c4-216e-4aaa-a674-3f24e0bfce7e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreateItem method Failover Cluster
- CreateItem method Failover Cluster , ClusResDependencies class
- ClusResDependencies class Failover Cluster , CreateItem method
topic_type:
- apiref
api_name:
- ClusResDependencies.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResDependencies.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [resource](resources.md) in the [*cluster*](https://www.bing.com/search?q=*cluster*) and adds it to the [*dependency*](https://www.bing.com/search?q=*dependency*) collection.

## Syntax


```VB
ClusResDependencies.CreateItem( _
  ByVal ResourceName, _
  ByVal ResourceType, _
  ByVal GroupName, _
  ByVal Flag _
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

*Flag* 
</dt> <dd>

Value indicating how to create the resource. *Flag* can be set to one of the following values enumerated from the [**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_create_flags) enumeration.

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

Resources added to a [**ClusResDependencies**](clusresdependencies-collection.md) collection become [dependencies](resource-dependencies.md) of the resource from which the collection was obtained.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>      |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>    |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>    |
| IID<br/>                      | IID\_ISClusResDependencies is defined as F2E60704-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependencies**](clusresdependencies-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





