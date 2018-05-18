---
title: ClusResGroupResources.CreateItem method
description: Creates a resource in the cluster and adds it to the ClusResGroupResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '609e3016-b14d-4a64-b86b-15796444a9d9'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CreateItem method Failover Cluster", "CreateItem method Failover Cluster , ClusResGroupResources class", "ClusResGroupResources class Failover Cluster , CreateItem method"]
topic_type:
- apiref
api_name:
- ClusResGroupResources.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroupResources.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [resource](resources.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly) and adds it to the [**ClusResGroupResources**](clusresgroupresources-collection.md) collection.

## Syntax


```VB
ClusResGroupResources.CreateItem( _
  ByVal ResourceName, _
  ByVal ResourceType, _
  ByVal Flag _
)
```



## Parameters

<dl> <dt>

*ResourceName* 
</dt> <dd>

**String** containing the name of the resource to add.

</dd> <dt>

*ResourceType* 
</dt> <dd>

**String** containing the type the resource to add.

</dd> <dt>

*Flag* 
</dt> <dd>

**Long** indicating how to create the resource. *Flag* can be set to one of the following values enumerated from the [**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](cluster-resource-create-flags.md) enumeration.

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

Object that receives [**ClusResource**](clusresource-object.md) object that represents the newly added resource.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusResGroupResources is defined as F2E606EA-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupResources**](clusresgroupresources-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





