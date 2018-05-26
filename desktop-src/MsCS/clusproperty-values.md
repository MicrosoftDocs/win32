---
title: ClusProperty.Values property
description: Retrieves a ClusPropertyValues collection containing all of the property values associated with a multi-value cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53cff9ea-15e4-4408-8e25-23219b8cfe76
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Values property Failover Cluster
- Values property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , Values property
topic_type:
- apiref
api_name:
- ClusProperty.Values
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusProperty.Values property

\[The **Values** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection containing all of the [*property values*](p-gly.md#-wolf-property-value-gly) associated with a multi-value [cluster object property](cluster-object-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperty.Values
```



## Property value

A [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection to receive the property values.

## Remarks

For detailed information about the properties associated with [cluster objects](cluster-objects.md), see [Cluster Object Properties](cluster-object-properties.md).

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

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusProperty.ValueCount**](clusproperty-valuecount.md)
</dt> <dt>

[**ClusProperty.Value**](clusproperty-value.md)
</dt> </dl>

 

 





