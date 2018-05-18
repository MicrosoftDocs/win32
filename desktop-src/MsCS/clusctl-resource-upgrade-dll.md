---
title: CLUSCTL\_RESOURCE\_UPGRADE\_DLL control code
description: Allows a setup application to upgrade a resource DLL without stopping the Cluster service. Applications use this control code as a ClusterResourceControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '685b0df3-7fc1-4516-933d-fed8934efec0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_UPGRADE_DLL control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_UPGRADE_DLL
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_UPGRADE\_DLL control code

Allows a setup application to upgrade a [resource DLL](resource-dlls.md) without stopping the [Cluster service](cluster-service.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.


```C++
ClusterResourceControl( 
           hResource,                    // resource handle
           hHostNode,                    // host node
           CLUSCTL_RESOURCE_UPGRADE_DLL, // this control code
           lpInBuffer,                   // full path of DLL
           cbInBufferSize,               // allocated buffer size (bytes)
           NULL,                         // not used
           0,                            // not used
           NULL );                       // not used
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*hResource* 
</dt> <dd>

Handle to any [resource](resources.md) supported by the DLL to be upgraded.

</dd> <dt>

*hHostNode* 
</dt> <dd>

Handle to the [node](nodes.md) currently hosting *hResource*. This node is called the upgrading node.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Null-terminated Unicode string specifying the path and filename of the resource DLL to upgrade.

</dd> <dt>

*cbInBufferSize* 
</dt> <dd>

Specifies the byte size of the input buffer.

</dd> </dl>

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_UPGRADE\_DLL as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                   |
|----------------|--------------|---------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>             |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                  |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                   |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>               |
| Type bit       | 20           | External (0x0)<br/>                               |
| Operation code | 0–23         | **CLCTL\_RESOURCE\_UPGRADE\_DLL** (0x4000ba)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                 |



 

### Resource DLL Support

Do not support or use this control code in your resource DLL.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





