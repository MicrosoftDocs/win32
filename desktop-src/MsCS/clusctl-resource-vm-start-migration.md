---
title: CLUSCTL\_RESOURCE\_VM\_START\_MIGRATION control code
description: Initiates the live migration of a VM from one node of a cluster to another node of the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ba2111c7-ed50-475c-a301-5c63d0350a8e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_VM_START_MIGRATION control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_VM_START_MIGRATION
api_type:
- NA
---

# CLUSCTL\_RESOURCE\_VM\_START\_MIGRATION control code

Initiates the live migration of a virtual machine (VM) from one node of a cluster to another node of the cluster. The VM must be in the Online (Enabled) state ([**VmState**](virtual-machines-vmstate.md) property is 2) to start a live migration and the resource control must be called on the node that currently hosts the VM. Applications use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.


```C++
ClusterResourceControl( hResource,       // resource handle
                        hHostNode,       // optional node handle
                        CLUSCTL_RESOURCE_VM_START_MIGRATION, 
                        lpInBuffer,      // input buffer: Name of destination node
                        cbInBufferSize,  // input buffer size (bytes)
                        NULL,            // output buffer (not used)
                        0,               // output buffer size (not used)
                        NULL );          // returned data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to an input buffer containing a null-terminated Unicode string containing the name of the destination node for the live migration.

</dd> <dt>

*cbInBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the input buffer.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The migration was successfully started.

</dd> <dt>

**ERROR\_INVALID\_STATE**
</dt> <dd>

5023 (0x139F)

The VM is not in the **Online** (2) state on the source node.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The migration failed to start.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_VM\_START\_MIGRATION (0x01600004) are defined as follows.



| Component                 | Bit location     | Value                                       |
|---------------------------|------------------|---------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit<br/>       | 21<br/>    | **CLCTL\_USER\_BASE** (0x200000)<br/> |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                   |
| Operation code<br/> | 0–23<br/>  | (0x4)<br/>                            |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_ANY** (0x0)<br/>      |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[*ResourceControl*](resourcecontrol.md)
</dt> <dt>

[**VmState**](virtual-machines-vmstate.md)
</dt> </dl>

 

 





