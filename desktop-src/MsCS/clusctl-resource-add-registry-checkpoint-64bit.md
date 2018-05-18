---
title: CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT control code
description: Adds a registry tree using the 64-bit view of the registry to the list of registry trees that are replicated for a resource. Applications use this control code as a parameter in the ClusterResourceControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2ac6a478-7a14-4f2b-bbfb-3bbc98e97ef0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_ADD_REGISTRY_CHECKPOINT_64BIT control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_ADD_REGISTRY_CHECKPOINT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT control code

Adds a registry tree using the 64-bit view of the registry to the list of registry trees that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter in the [**ClusterResourceControl**](clusterresourcecontrol.md) function.


```C++
ClusterResourceControl( 
  hResource,                                      // resource handle
  hHostNode,                                      // optional host node
  CLUSCTL_RESOURCE_ADD_REGISTRY_CHECKPOINT_64BIT, // this control code
  lpInBuffer,                                     // input buffer: string
  cbInBufferSize,                                 // input buffer size (bytes)
  NULL,                                           // not used
  0,                                              // not used
  NULL );                                         // not used
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the registry key name in the 64-bit view of the registry at the root of the subtree that should be replicated for the resource. This is a key name that is relative to **HKEY\_LOCAL\_MACHINE**, such as **Software\\Microsoft**\\*My Application*. Do not use a leading backslash (\) in the relative path or the call will fail.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful.

</dd> <dt>

**ERROR\_ALREADY\_EXISTS**
</dt> <dd>

The specified key is already being checkpointed.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                             |
|----------------|--------------|-------------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                       |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                            |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                         |
| Type bit       | 20           | External (0x0)<br/>                                         |
| Operation code | 0–23         | **CLCTL\_ADD\_REGISTRY\_CHECKPOINT\_64BIT** (0x4000be)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                          |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_32BIT](clusctl-resource-add-registry-checkpoint-32bit.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_DELETE\_REGISTRY\_CHECKPOINT](clusctl-resource-delete-registry-checkpoint.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-get-registry-checkpoints.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





