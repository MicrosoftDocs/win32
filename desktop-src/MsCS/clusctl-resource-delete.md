---
title: CLUSCTL\_RESOURCE\_DELETE control code
description: Internal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00dfa8d6-2ba0-499e-b510-d4df4d2d748f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_DELETE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_DELETE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_DELETE control code

Internal. Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [resource](resources.md) it is managing is about to be deleted from the [*cluster*](https://www.bing.com/search?q=*cluster*). Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_DELETE as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                       |
|----------------|--------------|---------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit       | 20           | Internal (0x1)<br/>                   |
| Operation code | 0 23         | **CLCTL\_DELETE** (0x500006)<br/>     |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>    |



 

### Resource DLL Support

Optional. Supporting the CLUSCTL\_RESOURCE\_DELETE control code allows you to perform any cleanup tasks that may be necessary before the deletion occurs, such as removing temporary files. Note that the [Cluster service](cluster-service.md) allows only offline resources to be deleted. Thus your resource DLL will receive this control code only for resources that are already offline. The [Resource Monitor](resource-monitor.md) does not provide any default processing.

By default, the CLUSCTL\_RESOURCE\_DELETE control code is sent only to the resource DLL on the [node](nodes.md) that currently owns the resource. For information about ensuring that the control code is sent to every node in the cluster, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md).

Note that when your resource DLL receives this notification, the deletion is inevitable. Your DLL cannot prevent any of its resources from being deleted.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**DeleteClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





