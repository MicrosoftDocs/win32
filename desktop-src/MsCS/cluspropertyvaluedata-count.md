---
title: ClusPropertyValueData.Count property
description: Number of data values in the ClusPropertyValueData collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53f2da9f-d72d-4e1b-a7c0-d74ebf1c7418
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusPropertyValueData collection
- ClusPropertyValueData collection Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusPropertyValueData.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPropertyValueData.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of [*data values*](d-gly.md#-wolf-data-value-gly) in the [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusPropertyValueData.Count
```



## Property value

**Long** indicating the number of data values in the collection.

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
</dt> </dl>

 

 





