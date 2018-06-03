---
title: ClusResource.RegistryKeys property
description: Returns a ClusRegistryKeys collection containing the checkpointed registry keys for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18bb4cfb-cd96-4f43-9cf6-ab06c22d0abf
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RegistryKeys property Failover Cluster
- RegistryKeys property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , RegistryKeys property
topic_type:
- apiref
api_name:
- ClusResource.RegistryKeys
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.RegistryKeys property

\[The **RegistryKeys** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection containing the checkpointed registry keys for the resource.

This property is read-only.

## Syntax


```VB
ClusResource.RegistryKeys
```



## Property value

A [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection that receives the checkpointed keys.

## Remarks

Use the collection obtained from the **RegistryKeys** property to add, remove, and list a resource's checkpointed keys.

For more information, see [Checkpointing](checkpointing.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusRegistryKeys**](clusregistrykeys-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResource.CryptoKeys**](clusresource-cryptokeys.md)
</dt> </dl>

 

 





