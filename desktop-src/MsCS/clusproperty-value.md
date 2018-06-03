---
title: ClusProperty.Value property
description: Locally stored copy of the property value of a cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 415458fc-0902-421f-ac00-ee46e24dc8ee
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Value property Failover Cluster
- Value property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , Value property
topic_type:
- apiref
api_name:
- ClusProperty.Value
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperty.Value property

\[The **Value** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets or retrieves the locally stored copy of the [*property value*](https://www.bing.com/search?q=*property value*) of a [cluster object property](cluster-object-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperty.Value
```



## Property value

## Remarks

A [**ClusProperty**](clusproperty-object.md) object operates on a local copy of cluster property data. Changes made to the local copy of the data do not take effect in the [*cluster*](https://www.bing.com/search?q=*cluster*) until the parent [**ClusProperties**](clusproperties-collection.md) collection invokes the [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) method. Any change to the local copy of the property value causes [**ClusProperties.Modified**](clusproperties-modified.md) to return **VARIANT\_TRUE**.

For detailed information about the properties associated with [cluster objects](cluster-objects.md), see [Cluster Object Properties](cluster-object-properties.md).

For cluster object properties that contain multiple values, use [**ClusProperty.ValueCount**](clusproperty-valuecount.md) to find the number of [*property values*](https://www.bing.com/search?q=*property values*), and [**ClusProperty.Values**](clusproperty-values.md) to obtain a [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection containing the property values.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperty is defined as F2E606FE-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusProperties.Modified**](clusproperties-modified.md)
</dt> <dt>

[**ClusProperties.SaveChanges**](clusproperties-savechanges.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusProperty.ValueCount**](clusproperty-valuecount.md)
</dt> <dt>

[**ClusProperty.Values**](clusproperty-values.md)
</dt> <dt>

[**ClusPropertyValues**](cluspropertyvalues-collection.md)
</dt> </dl>

 

 





