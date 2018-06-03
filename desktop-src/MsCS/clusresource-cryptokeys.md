---
title: ClusResource.CryptoKeys property
description: ClusCryptoKeys collection containing the checkpointed crypto keys for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14f75dc0-6d6e-4b70-9481-d00132f2b87b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CryptoKeys property Failover Cluster
- CryptoKeys property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , CryptoKeys property
topic_type:
- apiref
api_name:
- ClusResource.CryptoKeys
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.CryptoKeys property

\[The **CryptoKeys** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection containing the checkpointed crypto keys for the resource.

This property is read-only.

## Syntax


```VB
ClusResource.CryptoKeys
```



## Property value

A [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection that receives the checkpointed keys.

## Remarks

Use the collection obtained from the **CryptoKeys** property to add, remove, and list a resource's checkpointed crypto keys.

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

[**ClusCryptoKeys**](cluscryptokeys-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





