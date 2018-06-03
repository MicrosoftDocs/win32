---
title: ClusProperties.Refresh method
description: Reads the cluster database and updates the data in the ClusProperties collection to reflect the current cluster data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 900c9401-e8f4-423a-80df-598f5edb2935
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Refresh method Failover Cluster
- Refresh method Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , Refresh method
topic_type:
- apiref
api_name:
- ClusProperties.Refresh
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperties.Refresh method

\[The **Refresh** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Reads the [cluster database](cluster-database.md) and updates the data in the [**ClusProperties**](clusproperties-collection.md) collection to reflect the current [*cluster*](https://www.bing.com/search?q=*cluster*) data.

## Syntax


```VB
ClusProperties.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

A [**ClusProperties**](clusproperties-collection.md) collection contains a local copy of property data. The **Refresh** method updates the local copy with the current property data from the cluster. Any unsaved changes in the collection will be overwritten.

The **Refresh** method causes the [**ClusProperties.Modified**](clusproperties-modified.md) property to return **VARIANT\_FALSE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





