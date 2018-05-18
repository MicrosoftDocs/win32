---
title: ClusPropertyValues.CreateItem method
description: Creates a property value and adds it to the ClusPropertyValues collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b7175a46-3e0c-4d71-b435-589a145a56f3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CreateItem method Failover Cluster", "CreateItem method Failover Cluster , ClusPropertyValues collection", "ClusPropertyValues collection Failover Cluster , CreateItem method"]
topic_type:
- apiref
api_name:
- ClusPropertyValues.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPropertyValues.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [*property value*](p-gly.md#-wolf-property-value-gly) and adds it to the [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection.

## Syntax


```VB
ClusPropertyValues.CreateItem( _
  ByVal strName, _
  ByVal varValue _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

A **String** containing the name of the property to which this value applies.

</dd> <dt>

*varValue* 
</dt> <dd>

A **Variant** specifying the new property value.

</dd> </dl>

## Return value

A [**ClusPropertyValue**](cluspropertyvalue-object.md) object that receives the new property value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>               |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>   |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>   |
| IID<br/>                      | IID\_ISClusPropertyValues is defined as F2E6071C-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValues**](cluspropertyvalues-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> </dl>

 

 





