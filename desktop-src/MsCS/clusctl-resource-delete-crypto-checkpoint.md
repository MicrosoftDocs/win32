---
title: CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT control code
description: Removes a cryptographic key container from the list of keys that are being replicated for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7af5d70-b76c-4102-ae48-2354168deb27
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_DELETE_CRYPTO_CHECKPOINT control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_DELETE_CRYPTO_CHECKPOINT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT control code

Removes a cryptographic key container from the list of keys that are being replicated for a resource.


```C++
ClusterResourceControl( 
  hResource,                                 // resource handle
  hHostNode,                                 // optional node handle
  CLUSCTL_RESOURCE_DELETE_CRYPTO_CHECKPOINT, // this control code
  lpInBuffer,                                // input buffer: string
  cbInBufferSize,                            // input buffer size (bytes)
  NULL,                                      // not used
  0,                                         // not used
  NULL );                                    // not used
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the cryptographic service provider type, provider name, and key container name of a key that was previously checkpointed with the [CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md) control code.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

For more information on the CryptoAPI, see the [Cryptography\_Reference](https://msdn.microsoft.com/library/windows/desktop/aa380256).

For more information on cluster programming, refer to the following sections:

-   For information on working with control codes, see [Using Control Codes](using-control-codes.md).
-   For information on cluster registry [checkpointing](checkpointing.md), see [Cluster Database](cluster-database.md).
-   [Cluster-aware applications](cluster-aware-applications.md) need to be compiled and linked using ClusAPI.h, ClusAPI.lib, Resource.h, and ResUtils.lib. For an example of cluster-related compiler directives, see [ClusDocEx.h](clusdocex-h.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                       |
|----------------|--------------|-------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                 |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit       | 20           | External (0x0)<br/>                                   |
| Operation code | 0 23         | **CLCTL\_DELETE\_CRYPTO\_CHECKPOINT** (0x4000b2)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                    |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

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
</dt> <dt>

[CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-get-crypto-checkpoints.md)
</dt> </dl>

 

 





