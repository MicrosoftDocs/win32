---
title: ClusPropertyValueData.CreateItem method
description: Creates a data value and adds it to to a ClusPropertyValueData collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 75bd2145-aed5-4a8f-b1da-e8fdcb0a537a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreateItem method Failover Cluster
- CreateItem method Failover Cluster , ClusPropertyValueData collection
- ClusPropertyValueData collection Failover Cluster , CreateItem method
topic_type:
- apiref
api_name:
- ClusPropertyValueData.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusPropertyValueData.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [*data value*](https://www.bing.com/search?q=*data value*) and adds it to to a [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection.

## Syntax


```VB
ClusPropertyValueData.CreateItem( _
  ByVal varValue _
)
```



## Parameters

<dl> <dt>

*varValue* 
</dt> <dd>

A **Variant** specifying the new data value.

</dd> </dl>

## Return value

A **Variant** that receives the new data value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
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
</dt> </dl>

 

 





