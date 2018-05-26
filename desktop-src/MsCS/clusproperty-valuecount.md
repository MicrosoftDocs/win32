---
title: ClusProperty.ValueCount property
description: Number of property values associated with a cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 894b4ce9-422e-481f-81a5-8cccae3140a6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ValueCount property Failover Cluster
- ValueCount property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , ValueCount property
topic_type:
- apiref
api_name:
- ClusProperty.ValueCount
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusProperty.ValueCount property

\[The **Format** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of [*property values*](p-gly.md#-wolf-property-value-gly) associated with a [*cluster object*](c-gly.md#-wolf-cluster-object-gly) property.

This property is read-only.

## Syntax


```VB
ClusProperty.ValueCount As Long
```



## Property value

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

[**ClusProperty.Value**](clusproperty-value.md)
</dt> <dt>

[**ClusProperty.Values**](clusproperty-values.md)
</dt> </dl>

 

 





