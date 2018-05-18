---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMAP\_DRIVELETTER control code
description: Modifies the drive letter of a disk on the designated node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '31e45eef-d687-41c3-a0ac-ddd3877fc652'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STORAGE_REMAP_DRIVELETTER control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_REMAP_DRIVELETTER
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMAP\_DRIVELETTER control code

Modifies the drive letter of a disk on the designated node. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( hResource,                                     // resource handle
                            lpszResTypeName,                               // resource type name
                            hHostNode,                                     // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_IS_CLUSTERABLE,  // this control code
                            lpInBuffer,                                    // input buffer: drive letter bitmasks
                            cbInBufferSize,                                // input buffer size (bytes)
                            lpOutBuffer,                                   // output buffer (not used)
                            cbOutBufferSize,                               // allocated buffer size (not used)
                            lpcbBytesReturned );                           // actual size of resulting data (not used)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Contains bitmasks for the current and new drive letters. This parameter is modeled according to the [**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](clus-storage-remap-driveletter.md) structure.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The parameter is incorrect. This value can be returned if the input buffer pointed to by *lpInBuffer* was not large enough to hold the data resulting from the operation. This value can also be returned if **CurrentDriveLetterMask**, one of the members of the [**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](clus-storage-remap-driveletter.md) structure, is zero.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMAP\_DRIVELETTER (0x02000201) as follows.



| Component      | Bit location | Value                                          |
|----------------|--------------|------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)         |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                 |
| Type bit       | 20           | External (0x0)                                 |
| Operation code | 0–23         | **CLCTL\_STORAGE\_REMAP\_DRIVELETTER** (0x201) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)                   |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](clus-storage-remap-driveletter.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





