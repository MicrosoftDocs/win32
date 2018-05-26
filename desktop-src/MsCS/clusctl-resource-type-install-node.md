---
title: CLUSCTL\_RESOURCE\_TYPE\_INSTALL\_NODE control code
description: Internal. Indicates that a new node has been added to the cluster. Resource DLLs receive this control code through the ResourceTypeControl entry point function, which is called once for every resource type supported by the DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7239d38b-10e0-41f0-9024-4db3479bf0e5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_INSTALL_NODE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_INSTALL_NODE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_TYPE\_INSTALL\_NODE control code

[Internal](internal-control-codes.md). Indicates that a new [node](nodes.md) has been added to the [*cluster*](c-gly.md#-wolf-cluster-gly). [Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point function, which is called once for every resource type supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_INSTALL\_NODE as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                             |
|----------------|--------------|---------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit       | 20           | Internal (0x1)<br/>                         |
| Operation code | 0 23         | **CLCTL\_INSTALL\_NODE** (0x50000a)<br/>    |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>          |



 

### Resource DLL Support

Optional. Support the CLUSCTL\_RESOURCE\_TYPE\_INSTALL\_NODE control code if you have any tasks that must be performed when a new node is added to a cluster. The Resource Monitor provides no default processing.

For more information on the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)
</dt> <dt>

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master)
</dt> </dl>

 

 





