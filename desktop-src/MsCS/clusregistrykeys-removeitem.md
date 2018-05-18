---
title: ClusRegistryKeys.RemoveItem method
description: Deletes a registry key from a ClusRegistryKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '32b2eef7-40b1-4bfe-9f28-43831006d4cb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RemoveItem method Failover Cluster", "RemoveItem method Failover Cluster , ClusRegistryKeys class", "ClusRegistryKeys class Failover Cluster , RemoveItem method"]
topic_type:
- apiref
api_name:
- ClusRegistryKeys.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusRegistryKeys.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a registry key from a [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection.

## Syntax


```VB
ClusRegistryKeys.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** specifying the key to remove by name or by numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Use the **RemoveItem** method to remove a registry key from a resource's list of checkpointed registry keys.

For more information on checkpoints, see [Checkpointing](checkpointing.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRegistryKeys is defined as F2E6072A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusRegistryKeys**](clusregistrykeys-collection.md)
</dt> </dl>

 

 





