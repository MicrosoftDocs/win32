---
title: CLUSCTL\_RESOURCE\_VM\_CANCEL\_MIGRATION control code
description: Cancels an ongoing Live Migration of a VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f8fcebd9-2221-4a46-9398-13e4c7c0fc50'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_VM_CANCEL_MIGRATION control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_VM_CANCEL_MIGRATION
api_type:
- NA
---

# CLUSCTL\_RESOURCE\_VM\_CANCEL\_MIGRATION control code

Cancels an ongoing live migration of a virtual machine (VM). The migration can be canceled only if the migration is in the "Setup" ([**MigrationState**](virtual-machines-migrationstate.md) is 1) or "Data Transfer" (**MigrationState** is 2) states and the resource control is called on the source node of the live migration. Applications use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.


```C++
ClusterResourceControl( hResource,           // resource handle
                        hHostNode,           // optional node handle
                        CLUSCTL_RESOURCE_VM_CANCEL_MIGRATION, 
                        NULL,                // input buffer (not used)
                        0,                   // input buffer size (not used)
                        NULL,                // output buffer (not used)
                        0,                   // output buffer size (not used)
                        NULL );              // resulting data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl></dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The migration was successfully canceled.

</dd> <dt>

**ERROR\_INVALID\_STATE**
</dt> <dd>

5023 (0x139F)

The VM is not in the "Setup" ([**MigrationState**](virtual-machines-migrationstate.md) is 1) or "Data Transfer" (**MigrationState** is 2) state on the source node.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_VM\_CANCEL\_MIGRATION (0x01600008) are defined as follows.



| Component                 | Bit location     | Value                                       |
|---------------------------|------------------|---------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit<br/>       | 21<br/>    | **CLCTL\_USER\_BASE** (0x200000)<br/> |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                   |
| Operation code<br/> | 0–23<br/>  | (0x8)<br/>                            |
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

[**MigrationState**](virtual-machines-migrationstate.md)
</dt> </dl>

 

 





