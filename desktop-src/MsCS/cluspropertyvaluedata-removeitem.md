---
title: ClusPropertyValueData.RemoveItem method
description: Deletes a data value from a ClusPropertyValueData collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '44cabe30-13ec-4303-9534-ab76e3c951ac'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RemoveItem method Failover Cluster", "RemoveItem method Failover Cluster , ClusPropertyValueData collection", "ClusPropertyValueData collection Failover Cluster , RemoveItem method"]
topic_type:
- apiref
api_name:
- ClusPropertyValueData.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPropertyValueData.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [*data value*](d-gly.md#-wolf-data-value-gly) from a [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection.

## Syntax


```VB
ClusPropertyValueData.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** specifying the data value to remove by numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusPropertyValueData is defined as F2E6071E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValueData**](cluspropertyvaluedata-collection.md)
</dt> </dl>

 

 





