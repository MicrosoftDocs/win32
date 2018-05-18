---
title: ClusProperties.SaveChanges method
description: Updates the cluster database with the property data currently stored in the ClusProperties collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2792025f-c434-47e0-a5e8-06a992e3a8d2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["SaveChanges method Failover Cluster", "SaveChanges method Failover Cluster , ClusProperties collection", "ClusProperties collection Failover Cluster , SaveChanges method"]
topic_type:
- apiref
api_name:
- ClusProperties.SaveChanges
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperties.SaveChanges method

\[The **SaveChanges** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Updates the [cluster database](cluster-database.md) with the property data currently stored in the [**ClusProperties**](clusproperties-collection.md) collection.

## Syntax


```VB
ClusProperties.SaveChanges()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

A [**ClusProperties**](clusproperties-collection.md) collection contains a local copy of property data. Changes to the data do not take effect in the [*cluster*](c-gly.md#-wolf-cluster-gly) until **ClusProperties.SaveChanges** is called.

If the properties are successfully saved, **ClusProperties.SaveChanges** calls the [**ClusProperties.Refresh**](clusproperties-refresh.md) method.

The **ClusProperties.SaveChanges** method will fail if the properties in the collection are read-only.

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
</dt> </dl>

 

 





