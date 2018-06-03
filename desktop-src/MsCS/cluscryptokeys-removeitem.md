---
title: ClusCryptoKeys.RemoveItem method
description: Deletes a crypto key from a ClusCryptoKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ffaf36c7-86d2-4368-8c8f-f0b58a38fceb
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveItem method Failover Cluster
- RemoveItem method Failover Cluster , ClusCryptoKeys class
- ClusCryptoKeys class Failover Cluster , RemoveItem method
topic_type:
- apiref
api_name:
- ClusCryptoKeys.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusCryptoKeys.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a crypto key from a [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection.

## Syntax


```VB
ClusCryptoKeys.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** specifying the object to remove by name or by numeric index.

</dd> </dl>

## Return value

This method does not return a value.

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
</dt> </dl>

 

 





