---
title: ClusResources.CreateItem method
description: Creates a resource and adds it to a ClusResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3ff2d33b-08aa-445b-930e-7fbe589f6269'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CreateItem method Failover Cluster", "CreateItem method Failover Cluster , ClusResources collection", "ClusResources collection Failover Cluster , CreateItem method"]
topic_type:
- apiref
api_name:
- ClusResources.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResources.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [resource](resources.md) and adds it to a [**ClusResources**](clusresources-collection.md) collection.

## Syntax


```VB
ClusResources.CreateItem( _
  ByVal strResourceName, _
  ByVal strResourceType, _
  ByVal strGroupName, _
  ByVal lFlag _
)
```



## Parameters

<dl> <dt>

*strResourceName* 
</dt> <dd>

**String** containing the name of the resource to create.

</dd> <dt>

*strResourceType* 
</dt> <dd>

**String** specifying the type of resource to create.

</dd> <dt>

*strGroupName* 
</dt> <dd>

**String** containing the name of the group to which the new resource will belong.

</dd> <dt>

*lFlag* 
</dt> <dd>

Value indicating how to create the resource. *lFlag* can be set to one of these values enumerated from the [**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](cluster-resource-create-flags.md) enumeration.

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

Object that receives contains the new [**ClusResource**](clusresource-object.md) object representing the new resource.

## Remarks

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResources is defined as F2E6070C-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> <dt>

[**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](cluster-resource-create-flags.md)
</dt> </dl>

 

 





