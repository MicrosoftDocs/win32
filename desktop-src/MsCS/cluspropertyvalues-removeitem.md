---
title: ClusPropertyValues.RemoveItem method
description: Deletes a property value from a ClusPropertyValues collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86184297-c7e1-41da-b760-fbda1ae949ae
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveItem method Failover Cluster
- RemoveItem method Failover Cluster , ClusPropertyValues collection
- ClusPropertyValues collection Failover Cluster , RemoveItem method
topic_type:
- apiref
api_name:
- ClusPropertyValues.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPropertyValues.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [*property value*](p-gly.md#-wolf-property-value-gly) from a [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection.

## Syntax


```VB
ClusPropertyValues.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** specifying the property value to remove by name or by numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>               |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>   |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>   |
| IID<br/>                      | IID\_ISClusPropertyValues is defined as F2E6071C-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValues**](cluspropertyvalues-collection.md)
</dt> </dl>

 

 





