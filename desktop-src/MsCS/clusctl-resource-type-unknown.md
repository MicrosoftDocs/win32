---
title: CLUSCTL\_RESOURCE\_TYPE\_UNKNOWN control code
description: Verifies that control codes are being processed on the node where execution of the control is directed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec23ea78-8cd5-4366-a65d-98eb46c90362
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_UNKNOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_UNKNOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_UNKNOWN control code

This [control code](about-control-codes.md) verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed. Applications use this control code as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) parameter.


```C++
ClusterResourceTypeControl( 
  hCluster,                                          // cluster handle
  lpszResTypeName,                                   // resource type name
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_TYPE_UNKNOWN,                     // this control code
  NULL,                                              // input buffer: (not used)
  0,                                                 // input buffer size (not used)
  NULL,                                              // output buffer: (not used)
  0,                                                 // output buffer size (not used)
  NULL );                                            // actual size of resulting data (not used)
```



## Parameters

For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) or [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine). This control code has no parameters associated with it.

<dl></dl>

## Return value

When an application uses CLUSCTL\_RESOURCE\_TYPE\_UNKNOWN as a parameter for [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol), **ClusterResourceTypeControl** always returns **ERROR\_SUCCESS**.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_UNKNOWN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                             |
|----------------|--------------|---------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit       | 20           | External (0x0)<br/>                         |
| Operation code | 0 23         | **CLCTL\_UNKNOWN** (0x0)<br/>               |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

### Resource DLL Support

Conditional. If your DLL supports any other resource type control codes for the indicated resource type, return **ERROR\_SUCCESS**. Otherwise, return **ERROR\_INVALID\_FUNCTION**.

For more information on the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 





