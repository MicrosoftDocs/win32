---
title: CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT control code
description: Adds a cryptographic key container to the list of keys that are replicated for a resource. Applications use this control code as a ClusterResourceControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1bfc313e-aa3a-4249-8e47-f30438cd46e9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_ADD_CRYPTO_CHECKPOINT control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_ADD_CRYPTO_CHECKPOINT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT control code

Adds a cryptographic key container to the list of keys that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) parameter.


```C++
ClusterResourceControl( 
  hResource,                              // resource handle
  hHostNode,                              // optional host node
  CLUSCTL_RESOURCE_ADD_CRYPTO_CHECKPOINT, // this control code
  lpInBuffer,                             // input buffer: string
  cbInBufferSize,                         // input buffer size (bytes)
  NULL,                                   // not used
  0,                                      // not used
  NULL );                                 // not used
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the Cryptographic Service Provider (CSP) key container to be replicated. The CSP key container must first be created with the [Cryptography API](https://msdn.microsoft.com/library/windows/desktop/aa380256) and the keys in the container must be exportable. The string must specify the CSP provider type, provider name, and key container name using the following syntax:

Type\\Name\\Key

Note that the values must be separated by a '\\'. The provider type should specify the decimal value of the type, not the constant that represents the value. For example, instead of "PROV\_RSA\_FULL" use "1". The provider name is optional, if omitted, the default CSP provider name associated with the specified provider type will be used.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful.

</dd> <dt>

**NTE\_BAD\_KEY**
</dt> <dd>

The keys in the specified container are not exportable. For more information, see [**CryptGenKey**](https://msdn.microsoft.com/library/windows/desktop/aa379941).

</dd> <dt>

**NTE\_BAD\_KEYSET**
</dt> <dd>

The specified key container does not exist. For more information, see [**CryptAcquireContext**](https://msdn.microsoft.com/library/windows/desktop/aa379886).

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

Only exportable, machine-level keysets can be used for cluster crypto checkpoints.

For more information on the following points, see the [Cryptography\_Reference](https://msdn.microsoft.com/library/windows/desktop/aa380256).

-   A key container is given a name when it is created using [**CryptAcquireContext**](https://msdn.microsoft.com/library/windows/desktop/aa379886) with *dwFlags* set to **CRYPT\_NEWKEYSET**.
-   Once a key container has been created, the key pairs for that key container must be created using [**CryptGenKey**](https://msdn.microsoft.com/library/windows/desktop/aa379941) with the *dwFlags* parameter set to **CRYPT\_EXPORTABLE**. Note that some CSPs do not allow key exports from their key containers. If a key is not exportable then the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) call will fail with an **NTE\_BAD\_KEY** error.
-   C programs that create key sets need to be compiled and linked by using WinCrypt.h and AdvApi32.lib.

For more information on cluster programming, refer to the following sections:

-   For information on working with control codes, see [Using Control Codes](using-control-codes.md).
-   For information on cluster registry [checkpointing](checkpointing.md), see [Cluster Database](cluster-database.md).
-   [Cluster-aware applications](cluster-aware-applications.md) need to be compiled and linked using ClusAPI.h, ClusAPI.lib, Resource.h, and ResUtils.lib. For an example of cluster-related compiler directives, see [ClusDocEx.h](clusdocex-h.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                    |
|----------------|--------------|----------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                        |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit       | 20           | External (0x0)<br/>                                |
| Operation code | 0 23         | **CLCTL\_ADD\_CRYPTO\_CHECKPOINT** (0x4000ae)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                 |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Examples


```C++
//
// The following line creates a string used to checkpoint a
// key container with the following attributes:
//     provider type  = 1 (PROV_RSA_FULL)
//     provider name  = Microsoft Base Provider
//     container name = MyKey 
// Note the use of double backslashes "\\".
// 
WCHAR szCryptoCheckpoint[] = L"1\\Microsoft Base Cryptographic Provider v1.0\\MyKey";

//
// The following line creates a string used to checkpoint a
// key container with the following attributes:
//     provider type  = 1 (PROV_RSA_FULL)
//     provider name  = not specified; default will be used
//     container name = MyKey 
// Note the use of double backslashes "\\".
// 
WCHAR szCryptoCheckpoint[] = L"1\\\\MyKey";

DWORD dwResult = ClusterResourceControl(
                     hRes,
                     NULL,
                     CLUSCTL_RESOURCE_ADD_CRYPTO_CHECKPOINT
                     (LPVOID) szCryptoCheckpoint
                     ( lstrlenW( szCryptoCheckpoint ) + 1 ) * sizeof( WCHAR ),
                     NULL,
                     0,
                     NULL );

if( dwResult != ERROR_SUCCESS )
{
    // Handle error.
}
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT](clusctl-resource-delete-crypto-checkpoint.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-get-crypto-checkpoints.md)
</dt> </dl>

 

 





