---
title: ClusPropertyValue.Data property
description: ClusPropertyValueData collection containing all of the data values associated with a property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5305541c-ad28-4bdc-92e6-519ba5ab21d5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Data property Failover Cluster
- Data property Failover Cluster , ClusPropertyValue object
- ClusPropertyValue object Failover Cluster , Data property
topic_type:
- apiref
api_name:
- ClusPropertyValue.Data
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPropertyValue.Data property

\[The **Data** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection containing all of the [*data values*](d-gly.md#-wolf-data-value-gly) associated with a [*property value*](p-gly.md#-wolf-property-value-gly).

This property is read-only.

## Syntax


```VB
ClusPropertyValue.Data As ClusPropertyValueData
```



## Property value

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusPropertyValue is defined as F2E6071A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValue**](cluspropertyvalue-object.md)
</dt> <dt>

[**ClusPropertyValue.DataCount**](cluspropertyvalue-datacount.md)
</dt> <dt>

[**ClusPropertyValue.Value**](cluspropertyvalue-value.md)
</dt> </dl>

 

 





