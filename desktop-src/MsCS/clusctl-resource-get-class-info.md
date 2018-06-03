---
title: CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO control code
description: Retrieves the class and subclass of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c4f8809-d6eb-43e1-a09e-cfe3770a1fd4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_CLASS_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_CLASS_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO control code

Retrieves the class and subclass of a [resource](resources.md). A resource class identifies resources of similar capability. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) function.

A resource DLL receives the CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO control code when an application requests the resource class of a resource.


```C++
ClusterResourceControl( hResource,                       // resource handle
                        hHostNode,                       // optional host node
                        CLUSCTL_RESOURCE_GET_CLASS_INFO, // this control code
                        NULL,                            // input buffer (not used)
                        0,                               // input buffer size (not used)
                        lpOutBuffer,                     // output buffer: CLUS_RESOURCE_CLASS_INFO structure
                        cbOutBufferSize,                 // allocated buffer size (bytes)
                        lpcbBytesReturned );             // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) or [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [**CLUS\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_resource_class_info) structure containing resource class information for the resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

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

Implementations of [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Invalid function. Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO as follows.



| Component                 | Bit location     | Value                                        |
|---------------------------|------------------|----------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>  |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL**<br/>             |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY**<br/>              |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE**<br/>          |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                    |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_CLASS\_INFO** (0xd)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ**<br/>            |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Optional. If you do not support it, return **ERROR\_INVALID\_FUNCTION** to let the Resource Monitor provide default handling. The Resource Monitor will specify **CLUS\_RESCLASS\_UNKNOWN** as the class and zero as the subclass.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dt>

[**CLUS\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_resource_class_info)
</dt> <dt>

[**CLUS\_RESSUBCLASS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_ressubclass)
</dt> <dt>

[**CLUS\_RESSUBCLASS\_NETWORK**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_ressubclass_network)
</dt> <dt>

[**CLUS\_RESSUBCLASS\_STORAGE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_ressubclass_storage)
</dt> </dl>

 

 





