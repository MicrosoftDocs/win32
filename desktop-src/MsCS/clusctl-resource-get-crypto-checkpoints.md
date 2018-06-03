---
title: CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS control code
description: Retrieves a list of all the cryptographic key checkpoints set for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a5f6d42-a456-439e-85b6-622fff99dc8f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_CRYPTO_CHECKPOINTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_CRYPTO_CHECKPOINTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS control code

Retrieves a list of all the cryptographic key [checkpoints](checkpointing.md) set for a [resource](resources.md).


```C++
ClusterResourceControl( 
  hResource,                               // resource handle
  hHostNode,                               // optional host node
  CLUSCTL_RESOURCE_GET_CRYPTO_CHECKPOINTS, // control code
  NULL,                                    // lpInBuffer (not used)
  0,                                       // nInBufferSize (not used)
  lpOutBuffer,                             // output buffer: array of strings
  cbOutBufferSize,                         // allocated buffer size (bytes)
  lpcbBytesReturned );                     // size of resulting data (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpOutBuffer* \[in, out\]
</dt> <dd>

On a successful return, points to an array of null-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains a cryptographic service provider (CSP) type, provider name, and key container name in the following format:

Type\\Name\\Key

Note the values are separated by a '\\'. The provider type specifies the decimal value of the type, not the constant that represents the value. For example, "1" instead of "PROV\_RSA\_FULL". The provider name may be omitted, indicating that the default CSP name associated with the specified provider type should be used.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values:

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

If the *lpOutBuffer* parameter is **NULL** and the *cbOutBufferSize* parameter is zero, then **ERROR\_SUCCESS** may be returned, not **ERROR\_MORE\_DATA**.

For more information on the CryptoAPI, see the [Cryptography Reference](https://msdn.microsoft.com/library/windows/desktop/aa380256).

For more information on cluster programming, refer to the following sections:

-   For information on working with control codes, see [Using Control Codes](using-control-codes.md).
-   For information on cluster registry [checkpointing](checkpointing.md), see [Cluster Database](cluster-database.md).
-   [Cluster-aware applications](cluster-aware-applications.md) need to be compiled and linked using ClusAPI.h, ClusAPI.lib, Resource.h, and ResUtils.lib. For an example of cluster-related compiler directives, see [ClusDocEx.h](clusdocex-h.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0 23         | **CLCTL\_GET\_CRYPTO\_CHECKPOINTS** (0xb5)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>               |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

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

[CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT](clusctl-resource-delete-crypto-checkpoint.md)
</dt> </dl>

 

 





