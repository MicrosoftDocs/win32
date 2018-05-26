---
title: ClusRegistryKeys.AddItem method
description: Adds a registry key to a ClusRegistryKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8b28b848-ab26-4422-9e0e-a47613d7aa63
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddItem method Failover Cluster
- AddItem method Failover Cluster , ClusRegistryKeys class
- ClusRegistryKeys class Failover Cluster , AddItem method
topic_type:
- apiref
api_name:
- ClusRegistryKeys.AddItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusRegistryKeys.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a registry key to a [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection.

## Syntax


```VB
ClusRegistryKeys.AddItem( _
  ByVal strName _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

String identifying the new key.

</dd> </dl>

## Return value

A string that receives the added key.

## Remarks

For more information on checkpoints, see [Checkpointing](checkpointing.md).

## Examples

Use the **AddItem** method to add a registry key to a resource's list of checkpointed registry keys.


```VB
Public Function AddKey(ByRef objRes as ClusResource, _
                       ByVal strKey as String)

  Dim colRegKeys as ClusRegistryKeys
  Set colRegKeys = objRes.RegistryKeys
  colRegKeys.AddItem( strKey )
  Set colRegKeys = Nothing

End Function
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRegistryKeys is defined as F2E6072A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusRegistryKeys**](clusregistrykeys-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> </dl>

 

 





