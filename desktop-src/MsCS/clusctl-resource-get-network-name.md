---
title: CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME control code
description: Retrieves the name private property of a Network Name resource. This control code is unsupported by the other default resource types. Applications can use this control code as a parameter to the ClusterResourceControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 84cdb373-c1c8-433c-8aec-a69e9268f908
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_NETWORK_NAME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_NETWORK_NAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME control code

Retrieves the name [private property](private-properties.md) of a [Network Name](network-name.md) [resource](resources.md). This [control code](about-control-codes.md) is unsupported by the other default [resource types](resource-types.md). Applications can use this control code as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( 
  hResource,                         // resource handle
  hHostNode,                         // optional host node
  CLUSCTL_RESOURCE_GET_NETWORK_NAME, // this control code
  NULL,                              // input buffer (not used)
  0,                                 // input buffer size (not used)
  lpOutBuffer,                       // output buffer: string
  cbOutBufferSize,                   // allocated buffer size (bytes)
  lpcbBytesReturned );               // actual size of resulting data (bytes)
```



## Parameters

The following parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a null-terminated Unicode string containing the name of the resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                            |
|----------------|--------------|--------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>      |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>           |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>        |
| Type bit       | 20           | External (0x0)<br/>                        |
| Operation code | 0 23         | **CLCTL\_GET\_NETWORK\_NAME** (0x169)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>          |



 

### Resource DLL Support

Do not support this control code in your resource DLL. Return **ERROR\_INVALID\_FUNCTION**.

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> </dl>

 

 





