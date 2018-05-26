---
title: ClusProperty.Name property
description: Name of a cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b2d2f8b2-5bfe-4ed9-a746-79490806d85e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name property Failover Cluster
- Name property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , Name property
topic_type:
- apiref
api_name:
- ClusProperty.Name
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusProperty.Name property

\[The **Name** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the name of a [cluster object property](cluster-object-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperty.Name
```



## Property value

**String** that receives the name of the cluster object property.

## Remarks

The **Name** returned depends on the specific [**ClusProperty**](clusproperty-object.md) object and the associated [**cluster object**](cluster-object.md). For detailed information about the properties associated with cluster objects, see [Cluster Object Properties](cluster-object-properties.md).

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
</dt> </dl>

 

 





