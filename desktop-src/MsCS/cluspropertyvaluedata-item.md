---
title: ClusPropertyValueData.Item property
description: Single data value from a ClusPropertyValueData collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'adc7bb98-9d39-48e9-a7d5-f31b168972f4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Item property Failover Cluster", "Item property Failover Cluster , ClusPropertyValueData collection", "ClusPropertyValueData collection Failover Cluster , Item property"]
topic_type:
- apiref
api_name:
- ClusPropertyValueData.Item
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPropertyValueData.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [*data value*](d-gly.md#-wolf-data-value-gly) from a [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusPropertyValueData.Item( _
  ByVal varIndex _
)
```



## Property value

A **Variant** that receives the specified data value.

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
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusPropertyValueData.Count**](cluspropertyvaluedata-count.md)
</dt> </dl>

 

 





