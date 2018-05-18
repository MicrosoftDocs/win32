---
title: CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE control code
description: Updates the VmSwitchPorts and VmPhysicalDisks properties of the Virtual Machine configuration resource instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '091b585f-7721-4c6e-b779-98e78b9cb4eb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_VM_CONFIG_UPDATE control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_VM_CONFIG_UPDATE
api_type:
- NA
---

# CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE control code

The CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE [control code](about-control-codes.md)updates the [**VmSwitchPorts**](virtual-machine-configurations-vmswitchports.md) and [**VmPhysicalDisks**](virtual-machine-configurations-vmphysicaldisks.md) properties of the Virtual Machine configuration resource instances. Applications use this control code as a parameter to [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.


```C++
ClusterResourceControl( hResource,                 // resource handle
                        lpszResTypeName,           // resource type name
                        hHostNode,                 // optional host node
                        CLUSCTL_RESOURCE_VM_CONFIG_UPDATE,
                        NULL,                      // lpInBuffer: not used
                        0,                         // cbInBufferSize: not used
                        NULL,                      // lpOutBuffer: not used
                        0,                         // cbOutBufferSize: not used
                        NULL );                    // lpcbBytesReturned: not used
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [*ResourceControl*](resourcecontrol.md).

<dl></dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE (0x01600004) are defined as follows.



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



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[*ResourceControl*](resourcecontrol.md)
</dt> </dl>

 

 





