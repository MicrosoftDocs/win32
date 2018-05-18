---
title: ClusProperties.CreateItem method
description: Creates a ClusProperty object and adds it to the ClusProperties collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8df57999-5866-4005-9825-fefb827c876d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CreateItem method Failover Cluster", "CreateItem method Failover Cluster , ClusProperties collection", "ClusProperties collection Failover Cluster , CreateItem method"]
topic_type:
- apiref
api_name:
- ClusProperties.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperties.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [**ClusProperty**](clusproperty-object.md) object and adds it to the [**ClusProperties**](clusproperties-collection.md) collection.

## Syntax


```VB
ClusProperties.CreateItem( _
  ByVal strName, _
  ByVal varValue _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

String. The name of the new property.

</dd> <dt>

*varValue* 
</dt> <dd>

A **Variant** specifying the initial value of the new property.

</dd> </dl>

## Return value

A [**ClusProperty**](clusproperty-object.md) object that receives the added property.

## Remarks

The **CreateItem** method causes a modification to the collection. For more information, see [**ClusProperties.Modified**](clusproperties-modified.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> </dl>

 

 





