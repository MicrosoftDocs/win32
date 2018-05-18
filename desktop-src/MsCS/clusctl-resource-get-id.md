---
title: CLUSCTL\_RESOURCE\_GET\_ID control code
description: Retrieves the cluster database subkey identifier for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ca92df70-1d38-4442-9ec2-e7f94e096b0c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_ID control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_ID
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_ID control code

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_GET_ID,                           // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: string (GUID)
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a null-terminated Unicode string containing the **GUID** that identifies the resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The **GUID** string returned in *lpOutBuffer* resides in the cluster database under **HKEY\_LOCAL\_MACHINE\\Cluster\\Resources**.

Do not use the CLUSCTL\_RESOURCE\_GET\_ID control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_ID as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                       |
|----------------|--------------|---------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>       |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit       | 20           | External (0x0)<br/>                   |
| Operation code | 0–23         | **CLCTL\_GET\_ID** (0x39)<br/>        |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>     |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_GET\_ID control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





