---
title: ClusCryptoKeys.Item property
description: Single crypto key from a ClusCryptoKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f76aa7e4-1f4c-48dd-b8c1-1210f141f0cd
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusCryptoKeys class
- ClusCryptoKeys class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusCryptoKeys.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusCryptoKeys.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single crypto key from a [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusCryptoKeys.Item( _
  ByVal varIndex _
)
```



## Property value

A string that receives the specified key.

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
</dt> <dt>

[**ClusCryptoKeys.Count**](cluscryptokeys-count.md)
</dt> </dl>

 

 





