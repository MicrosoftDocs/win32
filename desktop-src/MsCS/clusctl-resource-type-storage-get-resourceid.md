---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_RESOURCEID control code
description: Retrieves the resource ID string for a storage resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47EE15C6-E92D-4FEE-B2A2-5C94875B7D96'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STORAGE_GET_RESOURCEID control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_GET_RESOURCEID
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_RESOURCEID control code

Retrieves the resource ID string for a storage resource. Applications use this control code as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( hCluster,                                     // cluster handle
                            lpszResTypeName,                              // resource type name
                            hHostNode,                                    // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_GET_RESOURCEID, // this control code
                            lpInBuffer,                                   // input buffer: null-terminated path
                            cbInBufferSize,                               // input buffer size
                            lpOutBuffer,                                  // output buffer: resource ID string
                            cbOutBufferSize,                              // allocated buffer size
                            lpcbBytesReturned );                          // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

A null-terminated string representing a path that belongs to a storage resource.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

A returned string representing the resource ID for that storage resource. The resource ID string contains a resource GUID that can be used in an [**OpenClusterResource**](openclusterresource.md) function call to open the resource.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**ERROR\_RESOURCE\_NOT\_FOUND**
</dt> <dd>

The specified path does not belong to storage resources of that type on the specified node.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_RESOURCEID (0x0200022d) as follows.



| Component      | Bit location | Value                                                          |
|----------------|--------------|----------------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)                         |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                                    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                                     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                                 |
| Type bit       | 20           | External (0x0)                                                 |
| Operation code | 0–23         | [**CLCTL\_STORAGE\_GET\_RESOURCEID**](clctl-codes.md) (0x22d) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)                                   |



 

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

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**OpenClusterResource**](openclusterresource.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





