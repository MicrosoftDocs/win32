---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES control code
description: Retrieves a list of all required dependencies for a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 01a1b0bc-e831-4535-b782-2a24bd6adf22
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_GET_REQUIRED_DEPENDENCIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_REQUIRED_DEPENDENCIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES control code

Retrieves a list of all required [dependencies](resource-dependencies.md) for a [resource type](resource-types.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) parameter.


```C++
ClusterResourceTypeControl( 
  hCluster,                                          // cluster handle
  lpszResTypeName,                                   // resource type name
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_TYPE_GET_REQUIRED_DEPENDENCIES,   // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: value list
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) or [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) containing a [**CLUSPROP\_REQUIRED\_DEPENDENCY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_required_dependency?branch=master) union for each dependency.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

For examples of using CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES, see [Creating a Value List](creating-value-lists.md) and [Parsing a Value List](parsing-a-value-list.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                    |
|----------------|--------------|----------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>        |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit       | 20           | External (0x0)<br/>                                |
| Operation code | 0 23         | **CLCTL\_GET\_REQUIRED\_DEPENDENCIES** (0x11)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                  |



 

### Resource DLL Support

Conditional. If your resource type has required [dependencies](resource-dependencies.md), support the CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES control code in your implementation of [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master). Return a [value list](value-lists.md) containing one [**CLUSPROP\_REQUIRED\_DEPENDENCY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_required_dependency?branch=master) union for each resource on which resources of this type are required to depend. Remember to terminate the list with **CLUSPROP\_SYNTAX\_ENDMARK**.

For example, if your resource type has required dependencies on a storage class device and a [Network Name](network-name.md) resource type, [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) should return a value list with three entries:

-   A [**CLUSPROP\_REQUIRED\_DEPENDENCY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_required_dependency?branch=master) union with the **ResClass** member set to **CLUS\_RESCLASS\_STORAGE**.
-   A [**CLUSPROP\_REQUIRED\_DEPENDENCY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_required_dependency?branch=master) union with the **ResTypeName** member set to "Network Name".
-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure with the Syntax member set to **CLUSPROP\_SYNTAX\_ENDMARK**.

(For an example, see [Creating a Value List](creating-value-lists.md).) The [Resource Monitor](resource-monitor.md) provides no default processing.

For more information on the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

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

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master)
</dt> <dt>

[**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md)
</dt> </dl>

 

 





