---
title: ClusCryptoKeys.AddItem method
description: Adds a crypto key to a ClusCryptoKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4f830e93-fa0a-4dbe-9544-9065cb2b4e8d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddItem method Failover Cluster
- AddItem method Failover Cluster , ClusCryptoKeys class
- ClusCryptoKeys class Failover Cluster , AddItem method
topic_type:
- apiref
api_name:
- ClusCryptoKeys.AddItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusCryptoKeys.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a crypto key to a [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection.

## Syntax


```VB
ClusCryptoKeys.AddItem( _
  ByVal strName _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

String identifying the cryptographic service provider (CSP) key container to be checkpointed. The CSP key container must first be created with the [Cryptography API](https://msdn.microsoft.com/library/windows/desktop/aa380256), and the keys in the container must be exportable. The string must specify the CSP provider type, provider name, and key container name using the following syntax.

*Type*\\*Name*\\*Key*

Note that the values must be separated by a '\\'. The provider type should specify the decimal value of the type, not the constant that represents the value. For example, instead of "PROV\_RSA\_FULL" use "1". The provider name is optional, and if it is omitted, the default CSP provider name associated with the specified provider type will be used.

</dd> </dl>

## Return value

A string that receives the added key.

## Remarks

For more information on the following points, see the [Cryptography Reference](https://msdn.microsoft.com/library/windows/desktop/aa380256).

-   A key container is given a name when it is created using [**CryptAcquireContext**](https://msdn.microsoft.com/library/windows/desktop/aa379886) with *dwFlags* set to **CRYPT\_NEWKEYSET**.
-   Once a key container has been created, the key pairs for that key container must be created using [**CryptGenKey**](https://msdn.microsoft.com/library/windows/desktop/aa379941) with the *dwFlags* parameter set to **CRYPT\_EXPORTABLE**. Note that some CSPs do not allow key exports from their key containers. If a key is not exportable then the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) call will fail with an **NTE\_BAD\_KEY** error.

For more information on checkpoints, see [Checkpointing](checkpointing.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusCryptoKeys is defined as F2E6072C-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusCryptoKeys**](cluscryptokeys-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> </dl>

 

 





