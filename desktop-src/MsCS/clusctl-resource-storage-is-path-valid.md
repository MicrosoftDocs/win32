---
title: CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID control code
description: Verifies that a specified path exists on a storage class resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0a8c69e1-4f7b-4518-a3eb-ffbf31fa749b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_IS_PATH_VALID control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_IS_PATH_VALID
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID control code

Verifies that a specified path exists on a [*storage class resource*](https://www.bing.com/search?q=*storage class resource*). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) function.


```C++
ClusterResourceControl( hResource,                              // resource handle
                        hHostNode,                              // optional host node
                        CLUSCTL_RESOURCE_STORAGE_IS_PATH_VALID, // this control code
                        lpInBuffer                              // input buffer
                        cbInBufferSize,                         // input buffer size (bytes)
                        NULL,                                   // output buffer (not used)
                        0,                                      // output buffer size (not used)
                        NULL );                                 // actual size of result (not used)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) or [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a null-terminated Unicode string specifying the path to validate.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The specified path is valid for the storage class resource identified by *hResource*.

</dd> <dt>

**ERROR\_FILE\_NOT\_FOUND**
</dt> <dd>

2

The specified path is not valid and refers to an offline storage class resource different from the storage class resource identified by the *hResource* parameter.

</dd> <dt>

**ERROR\_PATH\_NOT\_FOUND**
</dt> <dd>

3

The specified path does not exist on the storage class resource identified by *hResource*.

</dd> <dt>

**ERROR\_BAD\_PATHNAME**
</dt> <dd>

161 (0xA1)

The specified path is not valid and cannot exist on the storage class resource identified by *hResource*.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

Implementations of [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) can return one of the previous values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                  |
|---------------------------|------------------|--------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>            |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                 |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                  |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>              |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                              |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_IS\_PATH\_VALID** (0x199)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                |



 

### Resource DLL Support

Conditional. If your [resource DLL](resource-dlls.md) handles storage class resources, you must support the CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID control code. Keep in mind that this control code is a "yes-or-no" question, so try to return only **ERROR\_SUCCESS**, **ERROR\_PATH\_NOT\_FOUND**, **ERROR\_BAD\_PATHNAME**, or other values that unambiguously indicate whether the path is valid.

The [Resource Monitor](resource-monitor.md) does not provide default handling.

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

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





